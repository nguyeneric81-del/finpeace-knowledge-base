# 🌐 Tổng Quan Kiến Trúc Blockchain

Tài liệu này cung cấp nền tảng kiến thức cốt lõi về cấu trúc, phân loại, cơ chế đồng thuận và mô hình giao dịch của công nghệ Blockchain, phục vụ cho việc nghiên cứu và ứng dụng Fintech tại FinPeace.

---

## 1. Blockchain là gì?

**Blockchain** là một sổ cái kỹ thuật số phi tập trung, phân tán và bất biến (incorruptible), được sử dụng để ghi lại các giao dịch trên nhiều máy tính (nút) sao cho các bản ghi không thể bị thay đổi một cách hồi tố nếu không có sự thay đổi của tất cả các khối tiếp theo và sự đồng thuận của mạng lưới.

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│    Block 1    │     │    Block 2    │     │    Block 3    │
│ ├─ PrevHash   │◄────┼─ PrevHash   │◄────┼─ PrevHash   │
│ ├─ Timestamp  │     │ ├─ Timestamp  │     │ ├─ Timestamp  │
│ ├─ TX Data    │     │ ├─ TX Data    │     │ ├─ TX Data    │
│ └─ Hash (SHA) │     │ └─ Hash (SHA) │     │ └─ Hash (SHA) │
└───────────────┘     └───────────────┘     └───────────────┘
```

### 🔑 Các thành phần cốt lõi của một Khối (Block)
*   **Version**: Phiên bản của giao thức blockchain.
*   **Previous Hash**: Mã băm mật mã học của khối liền trước, tạo nên tính liên kết dạng chuỗi ("chain").
*   **Timestamp**: Nhãn thời gian ghi nhận lúc khối được khai thác/tạo ra.
*   **Merkle Root**: Mã băm gốc của toàn bộ cây Merkle đại diện cho tất cả các giao dịch trong khối đó, giúp xác thực nhanh sự hiện diện của một giao dịch.
*   **Nonce**: Giá trị số ngẫu nhiên được thợ đào thay đổi liên tục để tìm ra mã băm khối hợp lệ (trong cơ chế PoW).

---

## 2. Phân Loại Các Hệ Thống Blockchain

| Tiêu chí | Public Blockchain (Công khai) | Consortium Blockchain (Liên doanh) | Private Blockchain (Tư nhân) |
| :--- | :--- | :--- | :--- |
| **Quyền truy cập đọc**| Công khai toàn bộ | Công khai hoặc giới hạn | Giới hạn nội bộ |
| **Quyền ghi (Đồng thuận)**| Ai cũng có thể tham gia | Chỉ các nút được chọn | Một tổ chức duy nhất |
| **Tốc độ giao dịch**  | Chậm (do phi tập trung cao) | Nhanh | Cực kỳ nhanh |
| **Tính phi tập trung** | Tuyệt đối | Trung bình (nhóm tổ chức) | Thấp (tập trung vào 1 bên) |
| **Ví dụ thực tế**     | Bitcoin, Ethereum, Solana | Hyperledger Fabric, Quorum | Hệ thống chuỗi nội bộ |

---

## 3. Cơ Chế Đồng Thuận (Consensus Mechanisms)

Cơ chế đồng thuận là thuật toán giúp các nút độc lập trong mạng thống nhất về trạng thái duy nhất của sổ cái mà không cần bên trung gian tin cậy.

### ⛏️ Proof of Work (PoW - Bằng chứng công việc)
*   *Nguyên lý*: Thợ đào sử dụng năng lượng phần cứng để giải một bài toán mật mã học phức tạp (tìm nonce để mã băm khối bắt đầu bằng một số lượng số 0 nhất định).
*   *Đặc điểm*: Bảo mật cực kỳ cao, chống tấn công tốt nhưng tiêu tốn năng lượng khổng lồ và tốc độ giao dịch thấp (TPS thấp).
*   *Đại diện*: Bitcoin (BTC), Litecoin (LTC).

### 🪙 Proof of Stake (PoS - Bằng chứng cổ phần)
*   *Nguyên lý*: Người tham gia đặt cọc (stake) một lượng coin của mình vào hệ thống để giành quyền xác thực khối mới. Khả năng được chọn tỷ lệ thuận với lượng coin stake và thời gian stake.
*   *Đặc điểm*: Thân thiện với môi trường, TPS cao hơn, giảm nguy cơ thâu tóm bởi các nhóm đào lớn.
*   *Đại diện*: Ethereum (ETH), Cardano (ADA).

### 🗳️ Delegated Proof of Stake (DPoS - Cổ phần ủy quyền)
*   *Nguyên lý*: Người nắm giữ coin bỏ phiếu bầu ra một danh sách giới hạn các Validator (nhân chứng) đại diện để xác thực giao dịch và tạo khối.
*   *Đặc điểm*: Tốc độ giao dịch siêu nhanh (đạt hàng ngàn đến triệu TPS) nhờ số lượng nút đồng thuận ít, nhưng tính tập trung quyền lực cao hơn.
*   *Đại diện*: EOS, TRON.

### 🛡️ Practical Byzantine Fault Tolerance (PBFT)
*   *Nguyên lý*: Đồng thuận dựa trên tin nhắn trao đổi đa chiều giữa các nút được xác định danh tính trước. Chấp nhận tối đa $F$ nút lỗi/gian lận trong tổng số $3F + 1$ nút.
*   *Đặc điểm*: Blocktime gần như bằng 0, không phân tách chuỗi (no forks), phù hợp hoàn hảo với mạng doanh nghiệp.
*   *Đại diện*: Hyperledger Fabric, Quorum (Istanbul BFT).

---

## 4. Mô Hình Sổ Cái: UTXO vs Account-based

### 💸 Mô hình UTXO (Unspent Transaction Output)
*   *Cách hoạt động*: Giao dịch không trừ trực tiếp số dư tài khoản mà tiêu dùng các "đầu ra chưa chi tiêu" (UTXO) từ giao dịch trước và tạo ra các UTXO mới cho người nhận và phần tiền thừa thối lại cho người gửi. Giống như việc trả tiền bằng tiền mặt giấy.
*   *Ưu điểm*: Tính bảo mật cao, các giao dịch có thể xử lý song song, bảo vệ quyền riêng tư tốt (vì địa chỉ ví thay đổi liên tục).
*   *Đại diện*: Bitcoin, Cardano.

### 💳 Mô hình Account-based (Dựa trên tài khoản)
*   *Cách hoạt động*: Quản lý số dư trực tiếp trên từng tài khoản (ví) giống như hệ thống tài khoản ngân hàng. Giao dịch chỉ đơn giản là trừ số dư tài khoản A và cộng vào tài khoản B.
*   *Ưu điểm*: Cực kỳ trực quan, dễ dàng lập trình và thực thi các Hợp đồng thông minh (Smart Contracts) phức tạp có trạng thái (stateful).
*   *Đại diện*: Ethereum, Binance Smart Chain.
