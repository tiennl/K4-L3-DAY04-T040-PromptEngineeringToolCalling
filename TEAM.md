# TEAM — Day04, K4-L3B

**Làm nhóm.** Mỗi người tự viết và commit phần INDIVIDUAL của mình.

## Thông tin bài nộp

- Tên nhóm: T040
- Người đại diện / MSSV: Ngô Lê Thủy Tiên / 2A202602614
- Tên repo: `K4-L3-DAY04-T040-PromptEngineeringToolCalling` _(cần xác nhận lại quy tắc — README/SUBMISSION.md yêu cầu HoVaTen-MSSV, chưa rõ mã nhóm T040 có được chấp nhận thay thế không)_
- URL repo, nhánh nộp, commit chốt: https://github.com/tiennl/K4-L3-DAY04-T040-PromptEngineeringToolCalling — nhánh: _(chưa chốt, đang phát triển trên `tien`)_ — commit: _(điền commit chốt cuối buổi)_
- Deadline áp dụng và link thông báo đổi hạn nếu có: 23:59 ngày làm lab, Asia/Ho_Chi_Minh (mặc định theo SUBMISSION.md; cập nhật nếu Keycoach có thông báo khác)

## Thành viên

| Họ và tên | MSSV | GitHub | Vai trò và công việc | File/commit/PR |
|---|---|---|---|---|
| Phùng Trọng Chiến | 2A202602430 | Chienne12 | Prompt & Tool Engineering (v0 → v3) | PR #1 — `artifacts/system_prompt.md`, `artifacts/tools.yaml`, `artifacts/version_log.csv`, `runs/v0-v3_*_openrouter_*.json` |
| Nguyễn Hồng Khoa | 2A202602534 | hmster915 | Eval nhóm & An toàn | PR #2 — `data/eval_group.json`, `runs/v0-v3_*_group_*.json`, `runs/v0_B_base_openai_*.json` |
| Nguyễn Khánh Linh | 2A202602409 | klinhnguyen2012 | UI & Transcript | _(chưa có commit)_ |
| Ngô Lê Thủy Tiên | 2A202602614 | tiennl | Report, tổng hợp & Bonus mở rộng | PR #3 — `starter_v0/artifacts/REPORT.md` (Phần A), `TEAM.md` (thông tin nhóm, checklist phân công) |

## Phân công song song (4 người)

### Chung cả nhóm (CP0, làm cùng nhau trước)

- [ ] Mỗi người clone repo, tự tạo `.venv` riêng, cài `requirements.txt`
- [ ] Mỗi người tự điền `.env` với key provider của mình (không commit)
- [ ] Cả nhóm thống nhất giữ IT Helpdesk hay đổi lĩnh vực; nếu đổi, chốt ngay nhiệm vụ chính/người dùng/tool flow
- [ ] 1 người chạy **v0 chưa sửa gì** và commit run JSON làm mốc chung cho cả nhóm so sánh sau này

### Người 1 — Phùng Trọng Chiến — Prompt & Tool Engineering (v0 → v3)

- [ ] Đọc trace/lỗi từ run v0 baseline, chọn 1 failure rõ (sai tool/sai input/thiếu info/multi-turn/xác nhận-hủy/an toàn dữ liệu)
- [ ] Đặt giả thuyết → sửa `artifacts/system_prompt.md` và/hoặc `artifacts/tools.yaml` → chạy v1
- [ ] Lặp lại cho v2, v3 (mỗi vòng 1 giả thuyết rõ)
- [ ] Ghi mọi lần chạy vào `artifacts/version_log.csv` (thay đổi, lý do, hash, metric trước/sau, đường dẫn run)
- Sở hữu file: `artifacts/system_prompt.md`, `artifacts/tools.yaml`, `artifacts/version_log.csv`

### Người 2 — Nguyễn Hồng Khoa — Eval nhóm & An toàn

- [ ] Viết đúng 10 case vào `data/eval_group.json` (5 một lượt + 5 nhiều lượt), có đầu ra kỳ vọng
- [ ] Chạy case nhóm cùng các version của Người 1 khi có
- [ ] Chạy bộ 12 case an toàn (`eval_adversarial.json`)
- [ ] Phân tích chi tiết ít nhất 3 case an toàn (hành vi thật: hỏi lại, tôn trọng hủy/sửa, giữ dữ liệu nội bộ)
- Sở hữu file: `data/eval_group.json`, phần phân tích safety trong report

### Người 3 — Nguyễn Khánh Linh — UI & Transcript

- [ ] Chạy/chỉnh `chat.py` sao cho UI hiện rõ tool được gọi, input, kết quả/lỗi và version đang chạy
- [ ] Test UI với cả case thường và case đa lượt (thiếu info, sửa/hủy)
- [ ] Lưu transcript của các hội thoại bắt buộc (hỏi lại, xác nhận, hủy)
- [ ] Nhờ 1 người khác chạy thử UI theo đúng hướng dẫn README để xác nhận người ngoài chạy được
- Sở hữu file: `chat.py` (phần UI), thư mục transcript

### Người 4 — Ngô Lê Thủy Tiên — Report, tổng hợp & Bonus mở rộng

- [ ] Theo dõi tiến độ 3 người kia, tổng hợp số liệu trước/sau vào `artifacts/REPORT.md`
- [ ] Viết phần cách chạy, giới hạn còn lại, liên kết evidence (run file, version log, transcript)
- [ ] Nếu làm bonus: thiết kế 1 chức năng mới ngoài luồng cơ bản (data + code tích hợp + case test + demo), xem `RUBRIC.md`
- [ ] Cuối buổi: rà tên repo, checklist `SUBMISSION.md`, đảm bảo không commit `.env`/dữ liệu thật
- Sở hữu file: `artifacts/REPORT.md`, `SUBMISSION.md` checklist

### Đồng bộ tránh xung đột

- Mỗi người làm trên 1 branch riêng, PR nhỏ và thường xuyên
- `version_log.csv` chỉ Người 1 append; người khác gửi thông tin để họ ghi, tránh merge conflict
- Trước khi merge PR sửa `system_prompt.md`/`tools.yaml`, để Người 2 chạy lại eval_group + safety để xác nhận không phá hành vi cũ

### Mốc kiểm tra chéo (theo CHECKPOINTS.md)

| Giờ | Cần xong |
|---|---|
| 18:20 | v0 baseline chạy, `provider_error_cases == 0` |
| 19:05 | v1–v3 xong, có so sánh metric |
| 19:30 | 12 case an toàn + 3 phân tích xong |
| 20:10 | UI hoạt động, 10 case nhóm, transcript đầy đủ |
| 20:25 | Report + TEAM/INDIVIDUAL hoàn thiện — mốc kiểm tra tại lớp |

## Nhận xét chung

- Kết quả và bằng chứng:
- Thay đổi hiệu quả nhất:
- Giới hạn còn lại:
- Cách phân công và tích hợp:

## INDIVIDUAL

Sao chép mục này cho từng thành viên.

### Họ và tên — MSSV

- Phần việc và file/commit/PR:
- Quyết định, khó khăn và cách xử lý:
- Điều đã học:
- AI/công cụ đã dùng và cách kiểm tra:
- Thời điểm đã tự nộp URL repo chung trên VLearn:
