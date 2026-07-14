import os
import requests
from dotenv import load_dotenv

# Tự động load các biến môi trường từ file .env ở thư mục gốc
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env"))

class CloudflareKimiProvider:
    """
    LLM Provider sử dụng Cloudflare Workers AI với mô hình Kimi K2.7 Code miễn phí.
    Dùng làm phương án dự phòng (fallback) tối ưu chi phí cho các Chatbot FinPeace.
    """
    def __init__(self):
        self.account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
        self.api_token = os.getenv("CLOUDFLARE_API_TOKEN")
        self.model = os.getenv("CF_AI_MODEL", "@cf/moonshotai/kimi-k2.7-code")
        self.api_url = f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/ai/run/{self.model}"
        
    def generate(self, prompt: str, system_instruction: str = "") -> str:
        if not self.account_id or not self.api_token:
            return "Lỗi: Chưa cấu hình CLOUDFLARE_ACCOUNT_ID hoặc CLOUDFLARE_API_TOKEN trong file .env!"

        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})
        
        try:
            res = requests.post(self.api_url, headers=headers, json={"messages": messages})
            res.raise_for_status()
            data = res.json()
            
            if data.get("success"):
                # Trích xuất nội dung hội thoại chuẩn cấu trúc OpenAI
                return data["result"]["choices"][0]["message"]["content"]
            else:
                return f"Lỗi Cloudflare AI: {data.get('errors')}"
        except Exception as e:
            return f"Lỗi kết nối: {str(e)}"

# Đoạn code chạy thử nhanh
if __name__ == "__main__":
    provider = CloudflareKimiProvider()
    print("Đang gọi thử Kimi...")
    response = provider.generate("Hãy chào tôi bằng 1 câu truyền cảm hứng đầu tư ngắn gọn.")
    print("Kimi phản hồi:", response)
