# 📐 Chiến Lược Quản Trị Vốn & Quy Mô Vị Thế

Quản trị vốn (Money Management) quyết định sự sống còn của nhà giao dịch ở **Tầng 3 (Tài sản Nâng cao)**. Một hệ thống giao dịch có tỷ lệ thắng cao vẫn có thể phá sản nếu không quản trị quy mô vị thế hợp lý.

---

## 1. Quy Tắc Rủi Ro Tối Đa 2% (2% Rule)

Quy tắc nền tảng giúp bảo vệ vốn tuyệt đối trước chuỗi thua lỗ liên tiếp:

$$\text{Số tiền rủi ro tối đa cho mỗi giao dịch} = \text{Tổng tài sản khả dụng (Net Equity)} \times 2\%$$

*   *Ví dụ*: Tài khoản của bạn có **100 triệu VNĐ**. 2% rủi ro tối đa nghĩa là bạn chỉ cho phép mình lỗ tối đa **2 triệu VNĐ** cho giao dịch này.
*   **Công thức tính số lượng cổ phiếu cần mua**:

$$\text{Số lượng cổ phiếu cần mua} = \frac{\text{Số tiền rủi ro tối đa (2 triệu)}}{\text{Giá mua} - \text{Giá cắt lỗ (Stoploss)}}$$

*   *Ý nghĩa*: Công thức này tự động điều chỉnh quy mô mua dựa trên khoảng cách cắt lỗ. Khoảng cách cắt lỗ càng xa (rủi ro cao) thì số lượng cổ phiếu được mua càng ít; khoảng cách cắt lỗ càng gần thì số lượng cổ phiếu được mua càng nhiều, nhưng tổng rủi ro mất tiền luôn khống chế ở mức 2 triệu VNĐ.

---

## 2. Phương Pháp Định Quy Mô Vị Thế Cố Định (Fixed Fractional)

Dựa trên tài liệu **Mathematics of Money Management** của Ralph Vince và các nghiên cứu của Ryan Jones:
*   Phương pháp này duy trì tỷ lệ rủi ro cố định cho mỗi giao dịch khi tài khoản tăng trưởng hoặc sụt giảm.
*   Khi tài khoản tăng lên **150 triệu VNĐ**, số tiền rủi ro 2% sẽ tự động tăng lên **3 triệu VNĐ** (quy mô giao dịch tăng lên). Khi tài khoản sụt giảm xuống **80 triệu VNĐ**, số tiền rủi ro 2% tự động giảm xuống còn **1,6 triệu VNĐ** (quy mô giao dịch tự co cụm lại để phòng vệ).
*   Cơ chế này giúp tối ưu hóa lãi kép khi chiến thắng và tự động phanh lại khi gặp chuỗi thua lỗ.

---

## 3. Quản Trị Đòn Bẩy (Margin Management)

*   **Không dùng margin cho Tích sản (SIP)**: Tích sản dài hạn đòi hỏi sự bền bỉ qua các chu kỳ giảm điểm mạnh. Sử dụng margin sẽ khiến tài khoản bị call margin cưỡng bức bán tháo trước khi giá phục hồi.
*   **Kỷ luật margin trong Giao dịch xu hướng**:
    *   Chỉ sử dụng margin khi thị trường chung được xác nhận ở xu hướng tăng mạnh mẽ (Uptrend).
    *   Tỷ lệ sử dụng margin không được vượt quá **0.5** (tức là 1 đồng vốn tự có chỉ vay thêm tối đa 0.5 đồng).
    *   Phải có kế hoạch hạ tỷ trọng margin lập tức khi thị trường xuất hiện 3 - 5 ngày phân phối lớn.
