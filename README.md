# Information Retrieval — Search Engine với Apache Spark, OrientDB, TF-IDF & PageRank

> Đồ án cuối kỳ môn **Khai thác Thông tin (Information Retrieval)** — Chương trình Thạc sĩ
> Công nghệ Thông tin, Trường Đại học Công nghệ TP.HCM (HUTECH).

Xây dựng một **công cụ tìm kiếm (search engine) mini**: thu thập (crawl) các trang web /
bài báo, lưu trữ dưới dạng đồ thị trên **OrientDB**, rồi áp dụng **TF-IDF** để xếp hạng
độ liên quan theo truy vấn và **PageRank** để đánh giá độ uy tín của trang dựa trên cấu
trúc liên kết. Phần tính toán nặng được xử lý phân tán bằng **Apache Spark (PySpark)**.

Đề tài tập trung tìm hiểu **Apache Spark / Hadoop**, **OrientDB** (multi-model NoSQL,
graph), và áp dụng hai bài toán kinh điển của Information Retrieval là **TF-IDF** và **PageRank**.

## Kiến trúc hệ thống

```
End user ─► Frontend (React)
                 │
                 ▼
            Flask — Endpoint API
            Core: 1) Crawler  2) TF-IDF  3) PageRank
                 │                         │
       pyorientdb│                         │ PySpark (Python Driver)
                 ▼                         ▼
        OrientDB (Community Edition)   Py4J / JVM ─► Spark Master ─► Worker Nodes
        + File System                                              (Executor / Task)
```

- **Frontend**: giao diện tìm kiếm (React).
- **Backend (Flask)**: expose REST API; lõi xử lý gồm Crawler, TF-IDF, PageRank.
- **Apache Spark (PySpark)**: chạy TF-IDF / PageRank phân tán qua Py4J → Spark Context →
  Master Node → Worker Nodes (Executor/Task).
- **OrientDB Community Edition**: lưu trữ dữ liệu trang web dạng đồ thị (`Website` + `Link`),
  kết nối qua `pyorientdb`; dữ liệu thô lưu kèm trên File System.

## Thành phần kiến thức & công nghệ

| Chủ đề | Nội dung |
|--------|----------|
| **Apache Spark** | Xử lý phân tán in-memory; 5 thành phần: Spark Core, Spark SQL, Spark Streaming, MLlib, GraphX; hỗ trợ Java/Scala/Python/R. Mô hình: Driver (Spark Context) ↔ Cluster Manager → Worker Node (Executor + Cache + Task) |
| **Hadoop** | Lưu trữ phân tán; 4 module: HDFS, YARN, MapReduce, Hadoop Common (minh họa kiến trúc HDFS NameNode/DataNode và luồng MapReduce) |
| **OrientDB** | Multi-model NoSQL viết bằng Java; mô hình graph / document / key-value / object; cú pháp SQL-like; Community & Enterprise Edition |
| **TF-IDF** | Đánh trọng số từ khóa để cải thiện tìm kiếm & truy xuất thông tin |
| **PageRank** | Xếp hạng độ uy tín trang web dựa trên cấu trúc liên kết |

## Mô hình dữ liệu trên OrientDB

Trang web được mô hình hóa thành **đồ thị có hướng** (Property Graph):

- **Vertex (V):** `Website` (mỗi node là một URL / bài báo)
- **Edge (E):** `Link` (liên kết outbound từ trang này sang trang khác)

```sql
-- Lấy một trang và các liên kết của nó trong OrientDB Studio
SELECT FROM Website WHERE id = '4785199'
```

## Các công thức

**TF-IDF** — trọng số của từ `i` trong tài liệu `j`:

```
TF(i,j)  = F(i,j) / max(F(·,j))          # tần suất chuẩn hóa
IDF(i)   = log2( N / DF(i) )             # N: tổng số tài liệu, DF(i): số tài liệu chứa từ i
TF-IDF(i,j) = TF(i,j) × IDF(i)
```

**PageRank** — độ uy tín của trang `A`, hệ số giảm dần `d = 0.85`:

```
PR(A) = (1 - d) + d * Σ ( PR(Tᵢ) / C(Tᵢ) )
```

trong đó `Tᵢ` là các trang trỏ đến `A`, `C(Tᵢ)` là số liên kết outbound của `Tᵢ`.

## Cài đặt & chạy

> Điều chỉnh lại theo cấu trúc thực tế của repo.

### Yêu cầu
- Python 3.x, Java (JVM cho Spark/OrientDB)
- Apache Spark / PySpark
- OrientDB Community Edition (Docker)
- Node.js (cho frontend React)

### Khởi động OrientDB
```bash
docker run -d --name orientdb -p 2424:2424 -p 2480:2480 \
  -e ORIENTDB_ROOT_PASSWORD=root orientdb:2.2.35
# OrientDB Studio: http://localhost:2480
```

### Backend
```bash
pip install flask pyspark pyorientdb beautifulsoup4 requests
python app.py        # khởi động Flask Endpoint API
```

### Frontend
```bash
npm install && npm run dev
```

## Hướng phát triển

- Mở rộng dataset; thu thập được các trang web có độ phức tạp cao hơn.
- Tăng tốc độ / hiệu suất bằng đa luồng hoặc phân tán hóa quá trình xử lý.
- Tích hợp **Spark Connect** để chạy PageRank trên dữ liệu lớn.
- Hoàn thiện giao diện người dùng.

## ⚠️ Lưu ý

Code crawler chỉ phục vụ **mục đích học tập, nghiên cứu**; tôn trọng `robots.txt` và Điều
khoản dịch vụ của trang nguồn. Không commit secrets / dữ liệu nhạy cảm.

## Nhóm thực hiện — Nhóm 7

| Học viên | MSHV |
|----------|------|
| Nguyễn Ngọc Đỉnh | 2440861001 |
| Hà Anh Dũng | 2440861003 |
| Nguyễn Đông Hồ | 2441861016 |
| Nguyễn Minh Chiến | 2441861007 |
| Nguyễn Minh Trung Nghĩa | 2441861021 |
| Phạm Huỳnh Cao Minh | 2441861016 |

GVHD: TS. Phạm Thế Anh Phú
