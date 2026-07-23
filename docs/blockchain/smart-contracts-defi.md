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

---

## 5. Phân Loại Tài Khoản & Cơ Chế Thực Thi Trên Ethereum

Để tương tác với Hợp đồng thông minh và thực thi các giao thức DeFi, mạng lưới Ethereum chia cấu trúc tài khoản thành hai loại chính:

### A. EOA (Externally Owned Account - Tài khoản sở hữu ngoài)
*   *Đặc điểm*: Được tạo ra trực tiếp bởi người dùng (qua ví MetaMask, Ledger, v.v.). 
*   *Quản lý*: Quản lý bằng cặp khóa công khai - bảo mật (Public/Private Key). Người giữ khóa private key có toàn quyền kiểm soát số dư của ví.
*   *Mã nguồn*: Không chứa mã code lập trình (smart contract code).
*   *Hoạt động*: Có thể gửi giao dịch chuyển tiền (ETH) hoặc gửi giao dịch chứa dữ liệu để kích hoạt Hợp đồng thông minh.

### B. CA (Contract Account - Tài khoản hợp đồng)
*   *Đặc điểm*: Được tạo ra khi một hợp đồng thông minh được triển khai thành công lên blockchain.
*   *Địa chỉ*: Sở hữu một địa chỉ ví duy nhất trên chuỗi (Smart Contract Address) để định vị mã nguồn của nó.
*   *Quản lý*: **Không sở hữu khóa bảo mật (Private Key)**. Hoạt động của CA hoàn toàn tuân thủ theo logic lập trình được viết sẵn trong mã Solidity của nó.
*   *Hoạt động*: Chỉ có thể thực thi mã, cập nhật biến trạng thái (state variables), hoặc gọi đến các CA khác khi nhận được một giao dịch kích hoạt từ một tài khoản EOA (hoặc một CA khác).

---

## 6. Phí Giao Dịch (Gas) & Các Giao Thức Phụ Trợ (Swarm, Whisper)

### ⛽ Cơ chế phí giao dịch: Ether và Gas
*   **Ether (ETH)**: Đồng tiền bản vị của Ethereum, dùng để thanh toán phí cho các Validators để duy trì mạng lưới.
*   **Gas**: Đơn vị đo lường năng lượng tính toán cần thiết để thực thi các dòng lệnh trong hợp đồng thông minh. Mỗi dòng lệnh (opcode) trong Solidity tiêu thụ một lượng Gas định trước (ví dụ: phép toán cộng tiêu tốn ít Gas hơn phép toán lưu dữ liệu vào State DB).
*   *Mục đích*: Việc thu phí Gas bắt buộc các nhà phát triển phải viết code tối ưu hiệu năng, ngăn chặn hành vi gửi giao dịch spam hoặc tạo vòng lặp vô hạn (Infinite Loop) làm nghẽn mạng lưới.

### 🌐 Các giao thức phụ trợ trong Web3 Stack
Bên cạnh blockchain Ethereum xử lý các giao dịch tài chính, Web3 Stack tích hợp các giao thức phụ trợ phi tập trung:
*   **Swarm**: Nền tảng lưu trữ và chia sẻ tệp phi tập trung P2P (tương tự IPFS hoặc BitTorrent). Dữ liệu được chia nhỏ, mã hóa và phân tán tại các máy tính chạy nút. Hệ thống sử dụng ETH làm phần thưởng khuyến khích cho các nút lưu trữ dữ liệu hộ người dùng khác.
*   **Whisper**: Giao thức nhắn tin ngang hàng (P2P) được mã hóa an toàn, cho phép các nút truyền tin trực tiếp với nhau mà không tiết lộ danh tính người gửi/người nhận cho các bên thứ ba.
