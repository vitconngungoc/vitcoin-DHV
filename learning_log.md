# NHẬT KÝ TỰ HỌC (LEARNING LOG) - BÀI 01

## 1. GHI LẠI QUÁ TRÌNH (BẮT BUỘC)

### Lỗi 01: Lỗi xác thực quyền truy cập Git (Error 403)
* **Mô tả lỗi**: Khi thực hiện lệnh `git push`, Terminal báo lỗi `fatal: unable to access... The requested URL returned error: 403`. [cite_start]Nguyên nhân là do máy tính đang lưu thông tin tài khoản GitHub cũ không có quyền ghi vào repository mới.
* **Nơi tìm giải pháp**: Tìm kiếm trên StackOverflow và tham khảo tài liệu về Git Credential Manager.
* **Kết quả**: Truy cập vào *Credential Manager* trên Windows, xóa thông tin đăng nhập cũ của GitHub và thực hiện đăng nhập lại bằng đúng tài khoản `vitconngungoc`. [cite_start]Lệnh push đã hoạt động bình thường.

### Lỗi 02: Lỗi không tìm thấy tên cột (KeyError)
* **Mô tả lỗi**: Khi truy cập cột `df_titanic['Pclass']`, hệ thống báo lỗi `KeyError: 'Pclass'`.
* **Nơi tìm giải pháp**: Kiểm tra lại dữ liệu bằng lệnh `df_titanic.info()` và tra cứu tài liệu Seaborn Titanic dataset.
* **Kết quả**: Phát hiện ra khi load dữ liệu trực tiếp từ Seaborn, tên các cột được chuẩn hóa thành chữ thường (`pclass`) thay vì viết hoa chữ cái đầu như file CSV thô. [cite_start]Sau khi sửa lại tên cột, code đã chạy thành công.

### Điều tự học được ngoài bài giảng
* **Chủ đề**: Sử dụng tham số `normalize=True` trong hàm `value_counts()`.
* **Tóm tắt**: Thay vì chỉ đếm số lượng tuyệt đối, việc thêm `normalize=True` sẽ giúp Pandas tự động tính toán tỉ lệ phần trăm của từng nhóm dữ liệu. [cite_start]Điều này giúp việc quan sát tỉ lệ sống sót của các nhóm trở nên nhanh chóng và trực quan hơn mà không cần thực hiện phép tính chia thủ công[cite: 51].

### Tổng kết 3 câu cảm nhận
* [cite_start]**Điều khó nhất**: Việc thiết lập môi trường Python đồng bộ với VS Code và quản lý các commit trên Git để đảm bảo đúng quy trình làm việc chuyên nghiệp[cite: 51].
* [cite_start]**Điều thú vị nhất**: Khám phá ra sức mạnh của dữ liệu khi những con số khô khan có thể phản ánh chính xác các quy tắc xã hội và đạo đức ("phụ nữ và trẻ em trước") trong một thảm họa lịch sử[cite: 51].
* [cite_start]**Câu hỏi chưa có câu trả lời**: Với một cột dữ liệu bị thiếu quá nhiều như `deck` (hơn 77%), liệu có phương pháp toán học nâng cao nào để khôi phục thông tin thay vì chỉ đơn giản là bỏ qua nó không? [cite: 51]

## 2. TÀI NGUYÊN TỰ HỌC (BẮT BUỘC & BONUS)

### Xem video YouTube về Pandas
* [cite_start]**Tên video**: "Pandas Data Science Tutorial" của Keith Galli[cite: 53].
* [cite_start]**Điều học được**: Cách sử dụng hàm `.loc` và `.iloc` để trích xuất dữ liệu dựa trên nhãn hoặc chỉ số dòng một cách linh hoạt, giúp thao tác với DataFrame nhanh hơn rất nhiều so với dùng vòng lặp[cite: 53].

### Hoạt động trên Kaggle (BONUS)
* [cite_start]**Tài khoản**: Đã tạo tài khoản Kaggle thành công[cite: 54].
* [cite_start]**Notebook tham khảo**: "Titanic Data Science Solutions"[cite: 54].
* **2 kỹ thuật mới**: 
    1.  [cite_start]*Feature Engineering*: Tạo ra các cột mới (như `is_alone`) từ các cột sẵn có để tăng độ chính xác cho phân tích[cite: 54].
    2.  [cite_start]*Imputation*: Cách sử dụng trung vị (median) của từng nhóm nhỏ (theo hạng vé hoặc giới tính) để điền vào dữ liệu tuổi bị thiếu thay vì dùng trung vị của toàn bộ tập dữ liệu[cite: 54].

### Theo dõi chuyên gia trên LinkedIn (BONUS)
* [cite_start]**Tên chuyên gia**: Cassie Kozyrkov (Chief Decision Scientist tại Google)[cite: 54].
* [cite_start]**Lý do chọn**: Bà có khả năng giải thích các khái niệm phức tạp về thống kê và khoa học dữ liệu bằng những ví dụ đời thường rất dễ hiểu, giúp sinh viên mới bắt đầu có cái nhìn tổng quan và thực tế hơn về ngành này[cite: 54].