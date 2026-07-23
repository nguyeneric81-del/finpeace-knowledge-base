# 📜 Hợp Đồng Thông Minh (Smart Contracts) & DeFi

Tài liệu này trình bày về công nghệ Hợp đồng thông minh (Smart Contracts), các tiêu chuẩn token phổ biến trên mạng lưới EVM, quy tắc bảo mật mã nguồn và các ứng dụng thực tế trong không gian Tài chính Phi tập trung (DeFi).

---

## 1. Hợp Đồng Thông Minh (Smart Contract) là gì?

**Hợp đồng thông minh** là một chương trình máy tính tự thực thi (self-executing) được lưu trữ trực tiếp trên mạng lưới blockchain. Nó tự động thực hiện các điều khoản thỏa thuận giữa người mua và người bán khi các điều kiện định trước được đáp ứng, không cần sự can thiệp của bên thứ ba hay pháp luật truyền thống.

```
[Trigger Event] ──→ [Smart Contract Logic] ──→ [State Update on Blockchain]
(Ví dụ: Nhận ETH)     (Nếu ETH = 1.0, gửi NFT)     (Cập nhật chủ sở hữu ví)
```

*   **Solidity**: Ngôn ngữ lập trình hướng đối tượng, phổ biến nhất hiện nay dùng để viết Hợp đồng thông minh trên các blockchain tương thích EVM (Ethereum, BSC, Polygon, Avalanche).

---

## 2. Tiêu Chuẩn Token Phổ Biến (Ethereum Improvement Proposals)

Các tiêu chuẩn ERC (Ethereum Request for Comments) định nghĩa giao diện chuẩn để các token có thể tương tác dễ dàng với ví điện tử, sàn giao dịch và các hợp đồng thông minh khác.

### 🪙 ERC-20 (Fungible Token Standard)
*   *Định nghĩa*: Tiêu chuẩn cho các token có thể thay thế được cho nhau. Mỗi token có giá trị hoàn toàn bằng nhau (giống như các tờ tiền 100.000 VNĐ giấy).
*   *Các hàm chính bắt buộc*:
    *   `totalSupply()`: Tổng lượng cung lưu hành.
    *   `balanceOf(address account)`: Số dư ví của tài khoản.
    *   `transfer(address recipient, uint256 amount)`: Chuyển token sang ví khác.
    *   `approve(address spender, uint256 amount)`: Cấp quyền cho một hợp đồng khác (như DEX) chi tiêu số lượng token của mình.
*   *Ứng dụng*: Stablecoins (USDT, USDC), Token tiện ích (UNI, LINK).

### 🖼️ ERC-721 (Non-Fungible Token Standard - NFT)
*   *Định nghĩa*: Tiêu chuẩn cho các token độc nhất vô nhị, không thể thay thế cho nhau. Mỗi token có mã định danh `tokenId` duy nhất và thuộc tính riêng biệt.
*   *Ứng dụng*: Vé tham dự sự kiện số, chứng nhận sở hữu tác phẩm nghệ thuật, token hóa tài sản đời thực (Bất động sản, chứng chỉ cổ phần).

---

## 3. Bảo Mật Hợp Đồng Thông Minh (Smart Contract Security)

Hợp đồng thông minh một khi đã deploy lên blockchain thì **không thể sửa đổi** (immutable). Mọi lỗ hổng bảo mật đều có thể dẫn đến việc mất mát toàn bộ tài sản trong bể thanh khoản mà không thể khôi phục.

### 🛡️ Các nguyên tắc bảo mật cốt lõi:
1.  **Sử dụng OpenZeppelin Contracts**: Luôn kế thừa từ thư viện chuẩn OpenZeppelin (`@openzeppelin/contracts`) thay vì tự viết lại các hàm quản lý quyền (`Ownable`), lưu trữ toán học an toàn, và tiêu chuẩn token.
2.  **Chống tấn công Reentrancy (Ghi nhận lại)**: Sử dụng Modifier `nonReentrant` của OpenZeppelin để bảo vệ các hàm rút tiền, hoặc áp dụng mẫu thiết kế **Checks-Effects-Interactions** (Kiểm tra điều kiện $\rightarrow$ Cập nhật trạng thái số dư $\rightarrow$ Thực hiện chuyển tiền).
3.  **Hạn chế quyền lực Owner**: Sử dụng ví đa chữ ký (Multi-sig như Gnosis Safe) hoặc cơ chế khóa thời gian (Timelock) cho các hàm quản trị hệ thống quan trọng để tránh rủi ro lộ khóa private key của admin.

---

## 4. Ứng Dụng Trong Tài Chính Phi Tập Trung (DeFi)

Tài chính Phi tập trung (DeFi) sử dụng hợp đồng thông minh để thay thế các trung gian tài chính truyền thống (Ngân hàng, Sàn chứng khoán, Quỹ đầu tư).

*   **Sàn giao dịch phi tập trung (DEX - Decentralized Exchanges)**: Sử dụng mô hình tạo lập thị trường tự động (AMM - Automated Market Makers) như Uniswap, PancakeSwap cho phép người dùng tự do hoán đổi (swap) tài sản mà không cần sổ lệnh (orderbook).
*   **Giao thức Cho vay (Lending Protocols)**: Cho vay thế chấp tài sản số (như Aave, Compound), lãi suất được tự động điều chỉnh theo cung cầu cung cấp bởi thuật toán của smart contract.
*   **Token hóa tài sản thế giới thực (RWA - Real World Assets)**: Chuyển đổi các tài sản truyền thống (vàng, bất động sản, chứng chỉ tiền gửi) thành các token ERC-20/ERC-721 trên blockchain, tạo ra các cơ hội đầu tư tích sản linh hoạt với dòng vốn cực kỳ nhỏ (phù hợp với chiến lược Wealth Planning của FinPeace).
