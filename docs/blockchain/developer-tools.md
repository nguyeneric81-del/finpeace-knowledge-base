# 🛠️ Bản Đồ Công Cụ & Thư Viện Lập Trình Blockchain

Tài liệu này tổng hợp các công cụ phát triển, môi trường kiểm thử, SDK và thư viện lập trình blockchain được phân loại theo ngôn ngữ lập trình và nền tảng, dựa trên bộ tài nguyên **mikeroyal/Blockchain-Guide**.

---

## 1. Môi Trường Phát Triển & Nền Tảng (Platforms & Suite)

### 🧱 Ethereum Suite (EVM Ecosystem)
*   **[Truffle](https://trufflesuite.com/)**: Bộ khung phát triển (development suite), kiểm thử (testing framework) và quản lý asset cho Ethereum DApps.
*   **[Ganache](https://trufflesuite.com/ganache)**: Trình giả lập mạng Ethereum cục bộ (local blockchain emulator) chạy trên máy cá nhân, cho phép triển khai và chạy thử smart contract mà không tốn phí Gas thật.
*   **[Hardhat](https://hardhat.org/)**: Môi trường phát triển Ethereum linh hoạt, hỗ trợ biên dịch, deploy, chạy thử và debug smart contract với tính năng in log (`console.log`) ngay trong Solidity.

### 🏢 Enterprise Blockchain Platforms
*   **[Hyperledger Fabric](https://www.hyperledger.org/projects/fabric)**: Khung blockchain dạng liên minh (permissioned consortium), thiết kế dạng module linh hoạt cho doanh nghiệp, hỗ trợ đa ngôn ngữ để viết hợp đồng thông minh (Chaincode).
*   **[Corda (R3)](https://www.corda.net/)**: Nền tảng sổ cái phân tán được thiết kế riêng cho các giao dịch tài chính ngân hàng, bảo vệ tính riêng tư tuyệt đối của các bên tham gia giao dịch.

---

## 2. Thư Viện Lập Trình Theo Ngôn Ngữ (Language SDKs)

### 🟢 JavaScript / TypeScript
*   **[web3.js](https://github.com/web3/web3.js)**: Thư viện JavaScript chính thức để giao tiếp với các node Ethereum cục bộ hoặc từ xa thông qua các kết nối HTTP, IPC hoặc WebSocket.
*   **[ethers.js](https://github.com/ethers-io/ethers.js/)**: Thư viện JavaScript gọn nhẹ, bảo mật và phổ biến dùng để tương tác với mạng lưới Ethereum, tối ưu hóa cho ví client-side.
*   **[bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)**: Thư viện JavaScript mạnh mẽ chạy trên Node.js và trình duyệt để quản lý địa chỉ ví Bitcoin, ký số và xây dựng giao dịch.

### 🔵 Golang
*   **[go-ethereum (Geth)](https://github.com/ethereum/go-ethereum)**: Bản cài đặt node Ethereum bằng ngôn ngữ Go. Geth cũng cung cấp bộ công cụ CLI và API phong phú để tích hợp hệ thống backend với mạng blockchain.
*   **[btcd](https://github.com/btcsuite/btcd)**: Bản cài đặt node Bitcoin đầy đủ (full node) viết bằng ngôn ngữ Go, cung cấp các thư viện băm, chữ ký số và ví cực kỳ tin cậy.

### 🟡 Python
*   **[web3.py](https://github.com/ethereum/web3.py)**: Thư viện Python tương đương `web3.js` dùng để kết nối và điều khiển các hợp đồng thông minh trên mạng lưới Ethereum.
*   **[pycoin](https://github.com/richardkiss/pycoin)**: Bộ công cụ tiện ích Python toàn diện để tạo khóa (keys), ký giao dịch (signatures) và tương tác với mạng lưới Bitcoin và Altcoins.
*   **[txwatcher](https://github.com/tsileo/txwatcher)**: Tiện ích Python gọn nhẹ giúp giám sát sự thay đổi số dư của các địa chỉ ví Bitcoin thông qua API Websocket và thực thi các webhook callback tự động.

### 🦀 Rust
*   **[ethers-rs](https://github.com/gakonst/ethers-rs)**: Thư viện Rust hiệu năng cao để tương tác với Ethereum, hỗ trợ đầy đủ ví cứng, quản lý bộ nhớ an toàn và kiểm thử tự động.
*   **[rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin)**: Thư viện Rust chuẩn mực để xử lý cấu trúc dữ liệu, khối, giao dịch và địa chỉ ví của mạng lưới Bitcoin.

---

## 3. Tiện Ích & Công Cụ Trực Quan (Utilities & Visualizers)

*   **[BlockShell](https://github.com/daxeel/blockshell)**: Công cụ CLI tối giản giúp các nhà phát triển học hỏi các khái niệm kỹ thuật cốt lõi của blockchain như liên kết khối và cơ chế đào (mining).
*   **[Nigiri CLI](https://github.com/vulpemventures/nigiri/)**: Công cụ dòng lệnh mạnh mẽ giúp lập trình viên nhanh chóng dựng lên một mạng thử nghiệm Bitcoin cục bộ (regtest box) kèm trình khám phá dữ liệu (Esplora) để test ví và API.
*   **[Hal](https://github.com/stevenroose/hal)**: "Con dao pha lê" dòng lệnh Bitcoin viết bằng Rust, dùng để decode/encode các giao dịch, địa chỉ ví, khối dữ liệu trực tiếp trên terminal.
*   **[Bitauth IDE](https://ide.bitauth.com/)**: Môi trường phát triển trực quan trên web để thiết kế, debug và mô phỏng hoạt động của các hợp đồng thông minh Bitcoin (Bitcoin Scripts).
