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

---

## 5. Vấn Đề Chi Tiêu Kép (Double Spending) & Nakamoto Consensus

### 💸 Vấn đề Chi Tiêu Kép (Double Spending)
Trong thế giới số, dữ liệu có thể dễ dàng sao chép và gửi đi nhiều nơi cùng lúc (như file hình ảnh hoặc bài hát). Với tiền kỹ thuật số, nếu không có cơ chế ngăn chặn, một người có thể gửi cùng một đồng coin cho hai người khác nhau tại cùng một thời điểm, dẫn đến lạm phát và phá vỡ lòng tin của hệ thống sổ cái.

### 🛡️ Cách Bitcoin Giải Quyết (Nakamoto Consensus)
Bitcoin sử dụng cơ chế đồng thuận Proof of Work (PoW) kết hợp với luật **Chuỗi dài nhất (Longest Chain Rule)** để giải quyết chi tiêu kép:
1.  Mỗi giao dịch được phát lên mạng và chờ thợ đào đóng gói vào khối.
2.  Nếu hai giao dịch mâu thuẫn (chi tiêu kép) được hai thợ đào đóng gói vào hai khối khác nhau tại cùng một thời điểm, chuỗi sẽ bị phân tách tạm thời (fork).
3.  Các thợ đào khác sẽ tiếp tục khai thác khối tiếp theo dựa trên khối mà họ nhận được trước.
4.  Khi một trong hai nhánh có thêm khối mới và trở nên dài hơn nhánh còn lại, toàn bộ mạng lưới sẽ tự động công nhận nhánh dài hơn này là chuỗi hợp lệ duy nhất (**Nakamoto Consensus**). Nhánh ngắn hơn sẽ bị loại bỏ (gọi là *orphan blocks*), và các giao dịch nằm trong đó sẽ được trả về hàng đợi (mempool) để xử lý lại.
5.  **Số lượng Xác nhận (Confirmations)**: Nhà đầu tư thường được khuyến nghị chờ từ 3 đến 6 xác nhận khối (tương đương 30-60 phút trên mạng Bitcoin) để đảm bảo giao dịch của mình đã nằm chắc chắn trong chuỗi dài nhất và không thể bị đảo ngược.

> [!WARNING]
> **Tấn công 51% (51% Attack)**: Nếu một nhóm thợ đào kiểm soát hơn 51% tổng công suất băm (hashrate) của toàn mạng lưới, họ có khả năng tạo ra một chuỗi phụ dài hơn chuỗi công khai một cách bí mật, sau đó phát sóng lên mạng lưới để đảo ngược các giao dịch đã xác nhận nhằm thực hiện chi tiêu kép thành công.

---

## 6. Phân Tích Quy Trình Giao Dịch Trong Private & Consortium Blockchain

Mạng lưới doanh nghiệp yêu cầu quy trình bảo mật danh tính và hiệu năng xử lý hoàn toàn khác biệt so với các mạng lưới công khai:

### A. Phân biệt Quyền hạn (Permissioned Models)
*   **Public Permissioned (Ví dụ: Ripple)**: Bất kỳ ai cũng có thể đọc và gửi giao dịch (gần gũi với công chúng), nhưng quyền xác thực giao dịch và tạo khối chỉ được giao cho một số nút đáng tin cậy đã được phê duyệt trước.
*   **Private Permissioned (Ví dụ: Hyperledger Fabric)**: Mạng lưới hoàn toàn khép kín. Cả quyền đọc, ghi, và tham gia đồng thuận đều được phân quyền chặt chẽ thông qua các chứng chỉ số MSP (Membership Service Provider).

### B. Quy trình xử lý giao dịch trong Hyperledger Fabric (Transaction Flow)
Thay vì phát sóng rộng rãi (broadcast) giao dịch lên mạng như Bitcoin/Ethereum, Hyperledger Fabric sử dụng quy trình 4 bước tối ưu hiệu năng:

```
[Client App] ──1. Gửi đề xuất ──► [Endorsement Peers] (Bảo chứng & mô phỏng)
     ▲                                   │
     │◄─────────2. Ký bảo chứng ─────────┘
     │
     └──3. Gửi giao dịch ───────► [Ordering Service] (Sắp xếp & đóng khối)
                                         │
                                4. Phát khối mới
                                         ▼
                                  [Committer Peers] (Xác thực lại & Commit)
```

1.  **Đề xuất (Proposal)**: Client gửi yêu cầu giao dịch đến các nút **Endorsement Peers** được chỉ định.
2.  **Mô phỏng & Bảo chứng (Simulate & Endorse)**: Các nút này kiểm tra quyền hạn, giả lập giao dịch trên trạng thái sổ cái hiện tại (không ghi đè thật) để xem kết quả đầu ra có chính xác không. Nếu đúng, họ ký số xác nhận (endorsement signature) và gửi lại cho Client.
3.  **Sắp xếp (Ordering)**: Client gom đủ số lượng chữ ký bảo chứng hợp lệ và gửi toàn bộ giao dịch đến **Ordering Service**. Dịch vụ này sắp xếp các giao dịch theo thời gian, đóng gói thành khối mới.
4.  **Xác thực & Ghi nhận (Validation & Commit)**: Ordering Service phát khối mới đến các nút **Committer Peers**. Các nút này chạy bước xác thực cuối cùng (kiểm tra xem có xung đột trạng thái hay không) rồi ghi khối đó vào sổ cái local, cập nhật cơ sở dữ liệu trạng thái (State DB).

### C. Cơ chế chia sẻ dữ liệu Point-to-Point của Corda (R3)
*   *Vấn đề của Blockchain truyền thống*: Tất cả các nút đều phải lưu trữ một bản sao đầy đủ của sổ cái, gây lãng phí dung lượng và làm lộ bí mật kinh doanh giữa các đối thủ cạnh tranh trong cùng mạng lưới.
*   *Giải pháp của Corda*: Dữ liệu giao dịch chỉ được lưu trữ và chia sẻ **Point-to-Point** giữa các bên liên quan trực tiếp đến giao dịch đó. Một bên thứ ba bên ngoài không thể nhìn thấy hay tải về thông tin này.
*   *Đồng thuận hai tầng*:
    1.  *Đồng thuận hiệu lực (Validity Consensus)*: Các bên tham gia trực tiếp tự xác thực nội dung và ký số vào hợp đồng thông minh.
    2.  *Đồng thuận độc nhất (Uniqueness Consensus)*: Sử dụng một nút **Notary** (Công chứng viên) độc lập để kiểm tra xem các tài sản thế chấp trong giao dịch có bị chi tiêu kép (double spent) hay không mà không cần biết chi tiết nội dung giao dịch.

