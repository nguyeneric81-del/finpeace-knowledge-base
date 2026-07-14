# 🔌 Tích Hợp Cloudflare Workers AI Kimi (LLM Miễn Phí)

Tài liệu này hướng dẫn cách kết nối và sử dụng dịch vụ **Cloudflare Workers AI** với mô hình **Kimi K2.7 Code** (`@cf/moonshotai/kimi-k2.7-code`) làm giải pháp LLM dự phòng miễn phí (tối đa 10.000 Neurons/ngày) cho các ứng dụng chatbot và phân tích tự động của FinPeace.

---

## 1. Cấu Hình Biến Môi Trường (.env)

Tất cả thông tin tài khoản được lưu trữ an toàn tại file `.env` ở thư mục gốc của dự án:

```env
# Cloudflare Workers AI Configuration
CLOUDFLARE_ACCOUNT_ID="your_cloudflare_account_id"
CLOUDFLARE_API_TOKEN="your_cloudflare_api_token"
CF_AI_MODEL="@cf/moonshotai/kimi-k2.7-code"
```

*   **API Token** (`FinPeaceW1`): Được cấu hình đầy đủ quyền `Workers AI: Edit` để thực thi truy vấn mô hình AI.

---

## 2. Cách Sử Dụng File Kết Nối (Connector)

File code kết nối đã được viết sẵn tại: **[cloudflare_llm_provider.py](../tools/cloudflare_llm_provider.py)**.

### 🔹 Cách nhập và gọi từ các chatbot khác:
```python
from tools.cloudflare_llm_provider import CloudflareKimiProvider

# Khởi tạo provider
llm = CloudflareKimiProvider()

# Gửi yêu cầu
prompt = "Hãy giải thích triết lý 'Trả cho bản thân trước' bằng 1 câu ngắn gọn."
response = llm.generate(prompt, system_instruction="Bạn là Wealth Coach FinPeace.")

print(response)
```

---

## 3. Chính Sách Giới Hạn Của Cloudflare Free Tier

*   **Hạn mức miễn phí hàng ngày**: **10,000 Neurons/ngày** (reset mỗi 24 giờ).
*   **Neuron tiêu thụ**:
    *   Mô hình Kimi K2.7 Code tiêu thụ khoảng vài trăm Neurons cho mỗi 1.000 tokens (tùy độ dài Input/Output).
    *   Với hạn mức này, hệ thống chatbot có thể xử lý khoảng **50 - 200 lượt hội thoại/ngày hoàn toàn miễn phí**.
*   **Cơ chế dự phòng (Fallback)**: Thiết kế chatbot ưu tiên gọi Cloudflare Kimi trước. Nếu nhận về mã lỗi `429` (hết hạn mức Neuron trong ngày), hệ thống sẽ tự động chuyển mạch (fallback) sang gọi API có phí của OpenAI (GPT-4o-mini) hoặc Gemini.
