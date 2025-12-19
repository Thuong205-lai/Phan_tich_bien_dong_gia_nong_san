📊 Phân tích biến động giá nông sản 
1. Giới thiệu

Dự án này tập trung vào việc phân tích biến động giá nông sản theo thời gian và xây dựng mô hình dự báo giá trong tương lai dựa trên dữ liệu lịch sử. Thông qua các phương pháp phân tích chuỗi thời gian và mô hình dự báo thống kê, dự án nhằm làm rõ xu hướng, mùa vụ, các biến động bất thường của giá nông sản, đồng thời đánh giá hiệu quả của các mô hình dự báo khác nhau.

Dự án được thực hiện trong khuôn khổ bài tiểu luận môn học, với mục tiêu minh họa khả năng ứng dụng Python và các phương pháp phân tích dữ liệu vào bài toán thực tiễn trong lĩnh vực nông nghiệp.

2. Dữ liệu

Nguồn dữ liệu: Dữ liệu giá nông sản do giảng viên cung cấp.

Tần suất: Theo tháng.

Khoảng thời gian: Từ tháng 01/2018 đến tháng 12/2020.

Các trường chính:

LoaiNongSan: Loại nông sản

Nam, Thang: Thời gian quan sát

Gia: Giá gốc

Gia_clean: Giá sau khi làm sạch và xử lý thiếu

Date: Biến thời gian chuẩn (ngày đầu tháng)

3. Cấu trúc thư mục
project/
- data/
      raw/                # Dữ liệu gốc (Excel)
      processed/          # Dữ liệu đã làm sạch (CSV)

- notebooks/                                                                                                                                                               
      01_data_quality.ipynb                                                                                                                                                
      02_eda.ipynb                                                                                                                                                         
      03_forecasting.ipynb                                                                                                                                                 

- src/
      data_cleaning.py          
      data_quality.py
      config.py           

- reports/
      figures/                  
      tables/                  

- README.md
- requirements.txt

5. Phương pháp nghiên cứu

Dự án được thực hiện theo các bước chính sau:

Làm sạch và tiền xử lý dữ liệu

Chuẩn hóa tên cột và định dạng dữ liệu

Xử lý giá trị thiếu bằng nội suy theo thời gian

Đánh giá chất lượng dữ liệu và phát hiện giá trị bất thường

Phân tích biến động giá

Phân tích xu hướng dài hạn

Phân tích mùa vụ theo chu kỳ năm

Phân tích cú sốc giá dựa trên phần dư của chuỗi thời gian

Xây dựng và đánh giá mô hình dự báo

Mô hình dự báo cơ sở: Naive và Seasonal Naive

Mô hình nâng cao: SARIMA

Đánh giá bằng các chỉ số MAE, RMSE, MAPE

Backtesting và dự báo tương lai

Backtesting theo phương pháp cửa sổ mở rộng

Dự báo giá nông sản cho 12 tháng tiếp theo

Trình bày khoảng tin cậy 95% và phân tích rủi ro

5. Kết quả chính

Giá nông sản trong giai đoạn nghiên cứu có xu hướng tăng ổn định.

Yếu tố mùa vụ tồn tại nhưng ảnh hưởng không mạnh so với xu hướng dài hạn.

Các cú sốc giá xuất hiện với tần suất thấp.

Mô hình SARIMA cho kết quả dự báo chính xác và ổn định hơn so với các mô hình dự báo cơ sở.

Dự báo 12 tháng cho thấy giá tiếp tục xu hướng tăng, với khoảng tin cậy tương đối hẹp.

6. Công nghệ và thư viện sử dụng

Python 3.x

pandas, numpy

matplotlib

statsmodels

7. Hướng phát triển

Mở rộng dữ liệu theo thời gian hoặc tần suất cao hơn (tuần/ngày)

Kết hợp các biến ngoại sinh như thời tiết, chi phí đầu vào, chỉ số kinh tế

Áp dụng các mô hình học máy hoặc mô hình lai để nâng cao độ chính xác dự báo

8. Tác giả
Sinh viên thực hiện: Lại Huyền Thương
Môn học: Lập trình Python cho nông nghiệp
