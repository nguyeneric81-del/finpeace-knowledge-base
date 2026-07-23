import os
import sys
import time
import requests
import concurrent.futures
from dotenv import load_dotenv

# Tải biến môi trường từ file .env ở gốc dự án
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(dotenv_path=os.path.join(ROOT_DIR, ".env"))

# Import lớp CloudflareKimiProvider đã viết trước đó
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cloudflare_llm_provider import CloudflareKimiProvider

class MultiAgentOrchestrator:
    """
    Hệ thống Điều phối Multi-Agent song song cho FinPeace.
    Chạy song song 3 Agent chuyên trách (FA, TA, Macro) và tổng hợp kết quả qua Master Agent.
    """
    def __init__(self):
        self.llm = CloudflareKimiProvider()
        self.supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        
    def _query_supabase(self, endpoint: str, params: dict) -> list:
        """Helper để truy vấn nhanh dữ liệu từ Supabase REST API"""
        if not self.supabase_url or not self.supabase_key:
            return []
        
        url = f"{self.supabase_url}/rest/v1/{endpoint}"
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json"
        }
        try:
            res = requests.get(url, headers=headers, params=params)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            print(f"⚠️ Không thể truy vấn dữ liệu từ {endpoint}: {e}")
            return []

    def get_market_context(self, ticker: str) -> dict:
        """Truy xuất thông tin cơ bản và giá cổ phiếu từ cơ sở dữ liệu"""
        print(f"🔍 [Data Layer] Đang truy xuất dữ liệu cho mã {ticker}...")
        
        # 1. Truy vấn thông tin doanh nghiệp
        company_data = self._query_supabase("companies", {"ticker": f"eq.{ticker}"})
        company = company_data[0] if company_data else {"name": ticker, "industry": "N/A", "exchange": "HOSE"}
        
        # 2. Truy vấn giá cổ phiếu mới nhất
        price_data = self._query_supabase("stock_prices", {
            "ticker": f"eq.{ticker}",
            "order": "date.desc",
            "limit": 1
        })
        price = price_data[0] if price_data else {"price": "N/A", "date": "N/A"}
        
        return {
            "ticker": ticker,
            "name": company.get("name"),
            "industry": company.get("industry"),
            "exchange": company.get("exchange"),
            "price": price.get("price"),
            "price_date": price.get("date")
        }

    # --- ĐỊNH NGHĨA CÁC CHUYÊN GIA (SPECIALIZED AGENTS) ---

    def run_fundamental_agent(self, context: dict) -> str:
        """Agent 1: Phân tích cơ bản (FA) - Warren Buffett / Benjamin Graham Principles"""
        print("🧬 [FA Agent] Bắt đầu phân tích sức khỏe tài chính & định giá...")
        system_instruction = (
            "Bạn là Chuyên gia Phân tích Cơ bản của FinPeace (VVIA Agent).\n"
            "Nhiệm vụ của bạn là đánh giá giá trị nội tại, sức khỏe tài chính, và biên an toàn "
            "của doanh nghiệp dựa trên các quy tắc đầu tư giá trị kinh điển."
        )
        prompt = (
            f"Hãy phân tích cơ bản cho cổ phiếu {context['name']} ({context['ticker']}) "
            f"thuộc ngành {context['industry']}, giao dịch tại sàn {context['exchange']}.\n"
            f"Giá hiện tại tham chiếu: {context['price']} (Ngày {context['price_date']}).\n"
            "Nội dung cần tập trung:\n"
            "- Nhận diện lợi thế cạnh tranh cốt lõi (Economic Moats).\n"
            "- Đánh giá tính an toàn tài chính (nợ vay, dòng tiền).\n"
            "- Đưa ra định giá sơ bộ hoặc khuyến nghị tích sản dài hạn (SIP)."
        )
        return self.llm.generate(prompt, system_instruction=system_instruction)

    def run_technical_agent(self, context: dict) -> str:
        """Agent 2: Phân tích kỹ thuật (TA) - Trend Following / Indicators"""
        print("📈 [TA Agent] Bắt đầu phân tích cấu trúc sóng & chỉ báo kỹ thuật...")
        system_instruction = (
            "Bạn là Chuyên gia Phân tích Kỹ thuật của FinPeace (Trend Analyzer Agent).\n"
            "Nhiệm vụ của bạn là xác định xu hướng giá, các ngưỡng hỗ trợ/kháng cự quan trọng "
            "và tìm kiếm các điểm breakout ngắn-trung hạn."
        )
        prompt = (
            f"Hãy phân tích kỹ thuật cho cổ phiếu {context['ticker']}.\n"
            f"Giá hiện tại tham chiếu: {context['price']} (Ngày {context['price_date']}).\n"
            "Nội dung cần tập trung:\n"
            "- Xác định xu hướng hiện tại (Trend/Sideway) và các mốc hỗ trợ/kháng cự cứng.\n"
            "- Đề xuất Vùng mua (Entry Zone), Cắt lỗ (Stop Loss) và Chốt lời (Take Profit) "
            "đáp ứng tỷ lệ Risk/Reward tối thiểu là 1:3.\n"
            "- Phác thảo kế hoạch giao dịch ngắn hạn."
        )
        return self.llm.generate(prompt, system_instruction=system_instruction)

    def run_macro_agent(self, context: dict) -> str:
        """Agent 3: Phân tích Vĩ mô & Động lực Ngành (Macro / Catalyst)"""
        print("🌐 [Macro Agent] Bắt đầu phân tích tác động vĩ mô & chu kỳ ngành...")
        system_instruction = (
            "Bạn là Chuyên gia Phân tích Vĩ mô và Chu kỳ Ngành của FinPeace.\n"
            "Nhiệm vụ của bạn là đánh giá môi trường lãi suất, chính sách tiền tệ, "
            "xu hướng dòng tiền và các động lực tăng giá (Catalysts) lớn thúc đẩy ngành."
        )
        prompt = (
            f"Hãy phân tích vĩ mô và chất xúc tác cho ngành {context['industry']} "
            f"và mã cổ phiếu {context['ticker']}.\n"
            "Nội dung cần tập trung:\n"
            "- Động lực vĩ mô hiện tại (lãi suất, tỷ giá, đầu tư công) tác động như thế nào đến ngành này.\n"
            "- Catalyst quan trọng thúc đẩy doanh thu/lợi nhuận doanh nghiệp trong 2 quý tới.\n"
            "- Mức độ rủi ro hệ thống của thị trường chung."
        )
        return self.llm.generate(prompt, system_instruction=system_instruction)

    # --- ĐIỀU PHỐI VÀ TỔNG HỢP (MASTER SYNTHESIS) ---

    def synthesize_proposal(self, context: dict, fa_report: str, ta_report: str, macro_report: str) -> str:
        """Master Agent: Tổng hợp báo cáo từ 3 chuyên gia thành Trading Plan thống nhất"""
        print("\n👑 [Master Agent] Bắt đầu tổng hợp và biên soạn báo cáo tích hợp...")
        system_instruction = (
            "Bạn là Wealth Coach Trưởng của FinPeace.\n"
            "Nhiệm vụ của bạn là tổng hợp các báo cáo độc lập từ 3 chuyên gia (Cơ bản, Kỹ thuật, Vĩ mô) "
            "để tạo ra một Bản Đề xuất Đầu tư & Kế hoạch Giao dịch (Investment & Trading Proposal) hoàn chỉnh, "
            "ngắn gọn, thực tế và dễ hiểu cho khách hàng."
        )
        prompt = (
            f"Dưới đây là các báo cáo phân tích cho cổ phiếu {context['name']} ({context['ticker']}):\n\n"
            f"=== 1. PHÂN TÍCH CƠ BẢN (FA) ===\n{fa_report}\n\n"
            f"=== 2. PHÂN TÍCH KỸ THUẬT (TA) ===\n{ta_report}\n\n"
            f"=== 3. PHÂN TÍCH VĨ MÔ & NGÀNH ===\n{macro_report}\n\n"
            f"Hãy biên soạn lại thành một bài đề xuất đầu tư chuẩn hóa theo cấu trúc của FinPeace:\n"
            f"1. Tóm tắt luận điểm đầu tư cốt lõi (Catalysts).\n"
            f"2. Bảng thông số Kế hoạch Giao dịch (Entry Zone, Stop Loss, Take Profit, Tỷ lệ R:R, Quy mô vốn).\n"
            f"3. Đánh giá rủi ro và Kế hoạch phân bổ chi tiết."
        )
        return self.llm.generate(prompt, system_instruction=system_instruction)

    def orchestrate(self, ticker: str):
        """Khởi động luồng chạy song song và xuất kết quả"""
        start_time = time.time()
        context = self.get_market_context(ticker)
        
        print("\n⚡ BẮT ĐẦU CHẠY SONG SONG CÁC AGENT TRÊN THREAD POOL...")
        
        # Chạy song song 3 Agent phân tích độc lập
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            future_fa = executor.submit(self.run_fundamental_agent, context)
            future_ta = executor.submit(self.run_technical_agent, context)
            future_macro = executor.submit(self.run_macro_agent, context)
            
            # Đợi cả 3 tiến trình hoàn thành
            concurrent.futures.wait([future_fa, future_ta, future_macro])
            
            fa_report = future_fa.result()
            ta_report = future_ta.result()
            macro_report = future_macro.result()
            
        print("✅ Tất cả 3 chuyên gia phân tích đã hoàn thành báo cáo.")
        
        # Master Agent tổng hợp
        proposal = self.synthesize_proposal(context, fa_report, ta_report, macro_report)
        
        # Lưu kết quả ra file nháp trong thư mục scratch
        scratch_dir = os.path.join(ROOT_DIR, "scratch")
        os.makedirs(scratch_dir, exist_ok=True)
        output_file = os.path.join(scratch_dir, f"investment_proposal_{ticker.lower()}.md")
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(proposal)
            
        execution_time = time.time() - start_time
        print(f"\n✨ HOÀN THÀNH trong {execution_time:.2f} giây!")
        print(f"💾 Báo cáo đề xuất đầu tư đã được lưu tại: {output_file}")
        
        return proposal, output_file

if __name__ == "__main__":
    ticker = "HPG"
    if len(sys.argv) > 1:
        ticker = sys.argv[1].upper()
        
    orchestrator = MultiAgentOrchestrator()
    proposal, file_path = orchestrator.orchestrate(ticker)
