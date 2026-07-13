# 📊 Cẩm Nang Chỉ Báo Kỹ Thuật & Cấu Trúc Sóng

Phân tích kỹ thuật (TA) giúp nhà đầu tư xác định xu hướng dòng tiền ngắn/trung hạn và tối ưu hóa thời điểm mua/bán cổ phiếu.

---

## 1. Nến Nhật & Hành Động Giá (Price Action)

Dựa trên tài liệu **Japanese Candlestick Charting Techniques** của Steve Nison:
*   Mỗi cây nến Nhật mô tả cuộc chiến giữa bên Mua (Bò) và bên Bán (Gấu) trong một khung thời gian cụ thể (Open, High, Low, Close).
*   **Các mô hình nến đảo chiều tin cậy**:
    *   **Nến Búa (Hammer / Pinbar)**: Cho thấy lực cầu hấp thụ mạnh mẽ ở vùng giá thấp, thường xuất hiện ở đáy xu hướng giảm.
    *   **Nến Nhấn Chìm Tăng (Bullish Engulfing)**: Thể hiện lực mua áp đảo hoàn toàn lực bán, kích hoạt xu hướng tăng mới.
    *   **Nến Sao Mai (Morning Star)**: Mô hình 3 nến báo hiệu đảo chiều từ giảm sang tăng mạnh mẽ.

---

## 2. Chỉ Báo RSI (Relative Strength Index)

Dựa trên tài liệu **How to Use the RSI** của John Hayden:
*   RSI là chỉ báo dao động đo lường tốc độ và sự thay đổi của biến động giá (từ 0 đến 100).
*   **Vùng Quá mua (Overbought) / Quá bán (Oversold)**:
    *   RSI > 70: Thị trường đang quá hưng phấn $\rightarrow$ Cảnh báo rủi ro điều chỉnh (vùng phân phối ngắn hạn).
    *   RSI < 30: Thị trường đang quá hoảng loạn $\rightarrow$ Cơ hội tìm điểm mua tích sản chiết khấu sâu.
*   **Hiện tượng Phân kỳ (Divergence)**:
    *   *Phân kỳ dương (Bullish Divergence)*: Giá tạo đáy sau thấp hơn đáy trước, nhưng RSI tạo đáy sau cao hơn đáy trước $\rightarrow$ Tín hiệu đảo chiều tăng giá mạnh mẽ.

---

## 3. Dải Băng Bollinger Bands

Dựa trên tài liệu **Charting Made Easy** của John J. Murphy:
*   Bollinger Bands gồm một đường trung bình động (MA20) ở giữa và hai dải băng (trên và dưới) đo lường độ lệch chuẩn của biến động giá.
*   **Quy luật vận động**:
    *   **Nút thắt cổ chai (Squeeze)**: Khi dải băng trên và dưới co thắt hẹp lại cực độ, nó báo hiệu thị trường sắp có một biến động giá cực mạnh (bùng nổ tăng hoặc sập giảm).
    *   **Bám biên**: Giá bám sát dải băng trên thể hiện xu hướng tăng cực mạnh (Markup); giá bám sát dải băng dưới thể hiện xu hướng giảm mạnh (Markdown).

---

## 4. Lý Thuyết Sóng Elliott (Elliott Wave Theory)

Dựa trên tác phẩm kinh điển **Mastering Elliott Wave** của Glenn Neely:
*   Thị trường vận động theo cấu trúc sóng tuần hoàn gồm **5 sóng đẩy** (Impulse Waves - hướng theo xu hướng chính) và **3 sóng điều chỉnh** (Corrective Waves - ngược xu hướng chính).

```
        3
       /\
      /  \        5
    1/    \4     /\
    /\     \    /  \      A
   /  \2    \  /    \    /\
  /    \     \/      \  /  \C
 /      \             \/    \
/        \                   \B
```

*   **Quy tắc cốt lõi**:
    *   Sóng 2 không được hiệu chỉnh vượt quá điểm khởi nguồn của Sóng 1.
    *   Sóng 3 thường là sóng dài nhất và mạnh nhất, không bao giờ là sóng ngắn nhất trong 3 sóng đẩy (1, 3, 5).
    *   Sóng 4 không được đi vào vùng giá của đỉnh Sóng 1.
*   **Ứng dụng**: Xác định vị thế của thị trường chung để tránh mua đuổi ở đỉnh Sóng 5 (gần vùng phân phối) và chủ động gom mua tích sản ở vùng Sóng C điều chỉnh hoàn tất.
