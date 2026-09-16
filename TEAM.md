# TEAM — Day04, K4-L3B

**Làm nhóm.** Mỗi người tự viết và commit phần INDIVIDUAL của mình.

## Thông tin bài nộp

- Tên nhóm: T040
- Người đại diện / MSSV: Ngô Lê Thủy Tiên / 2A202602614
- Tên repo: `K4-L3-DAY04-T040-PromptEngineeringToolCalling`
- URL repo, nhánh nộp, commit chốt: https://github.com/tiennl/K4-L3-DAY04-T040-PromptEngineeringToolCalling — nhánh: `main` (PR #1–#4 đã merge từ `chien`/`khoa`/`tien`/`linh-fe` vào `main`; nhánh `tien` hiện trùng `main`)
- Deadline áp dụng và link thông báo đổi hạn nếu có: 12:00 ngày 16/09/2026, Asia/Ho_Chi_Minh

## Thành viên

| Họ và tên | MSSV | GitHub | Vai trò và công việc | File/commit/PR |
|---|---|---|---|---|
| Phùng Trọng Chiến | 2A202602430 | Chienne12 | Prompt & Tool Engineering (v0 → v3) | PR #1 — `artifacts/system_prompt.md` v1 (`69223b9`) + v3 (`f89a89b`), `artifacts/tools.yaml` v2 (`db9c3dc`), `artifacts/version_log.csv` (`2a26ed3`), bản dịch tiếng Việt giữ nguyên logic cải tiến (`8f80228`, `15d628a`, `df46c03`) |
| Nguyễn Hồng Khoa | 2A202602534 | hmster915 | Eval nhóm & An toàn | PR #2 — `data/eval_group.json` 10 case (`3281c21`), `runs/v0-v3_B_group_openai_*.json` (`d7c0416`), `runs/v0_B_base_openai_*.json` (`8cb2ea4`) |
| Nguyễn Khánh Linh | 2A202602409 | klinhnguyen2012 | UI & Transcript | PR #4 — `chat.py` hiện tool trace đầy đủ + `tests/test_chat.py` (`6fa3203`), `transcripts/ticket-cancellation-v0.transcript.json` + `transcripts/ticket-modification-failed-v0.transcript.json` (`0d8491c`) |
| Ngô Lê Thủy Tiên | 2A202602614 | tiennl | Report, tổng hợp, evidence & Bonus mở rộng | PR #3 — `artifacts/REPORT.md` Phần A (`4b4a592`), run baseline v0 OpenRouter (`2272ed8`), `TEAM.md` thông tin nhóm (`64e8a21`); commit trực tiếp — thay evidence Gemini lỗi bằng OpenRouter thật trên nhánh `chien` trước khi merge PR #1 (`caa130b`), run xác minh sau merge (`7c5befd`), cập nhật bảng thành viên (`92f3046`); PR #5 — `artifacts/REPORT.md` Phần B + `TEAM.md` tổng hợp evidence, nhận xét chung, checklist (`e0ab164`, `a8385b2`) |

## Phân công song song (4 người)

### Chung cả nhóm (CP0, làm cùng nhau trước)

- [ ] Mỗi người clone repo, tự tạo `.venv` riêng, cài `requirements.txt`
- [ ] Mỗi người tự điền `.env` với key provider của mình (không commit)
- [x] Cả nhóm thống nhất giữ IT Helpdesk hay đổi lĩnh vực; nếu đổi, chốt ngay nhiệm vụ chính/người dùng/tool flow — giữ IT Helpdesk, không đổi lĩnh vực
- [x] 1 người chạy **v0 chưa sửa gì** và commit run JSON làm mốc chung cho cả nhóm so sánh sau này — `runs/v0_B_base_openrouter_20260915T203947961416.json` (PR #1)

### Người 1 — Phùng Trọng Chiến — Prompt & Tool Engineering (v0 → v3)

- [x] Đọc trace/lỗi từ run v0 baseline, chọn 1 failure rõ (sai tool/sai input/thiếu info/multi-turn/xác nhận-hủy/an toàn dữ liệu)
- [x] Đặt giả thuyết → sửa `artifacts/system_prompt.md` và/hoặc `artifacts/tools.yaml` → chạy v1 (case_accuracy 0.6667 → 0.7667) — commit `69223b9`
- [x] Lặp lại cho v2, v3 (mỗi vòng 1 giả thuyết rõ) — v2: 0.9000 đỉnh (commit `db9c3dc`), v3: 0.8333 regress 4 case (commit `f89a89b`, xem `artifacts/REPORT.md` B2)
- [x] Ghi mọi lần chạy vào `artifacts/version_log.csv` (thay đổi, lý do, hash, metric trước/sau, đường dẫn run) — commit `2a26ed3`
- Sở hữu file: `artifacts/system_prompt.md`, `artifacts/tools.yaml`, `artifacts/version_log.csv`

### Người 2 — Nguyễn Hồng Khoa — Eval nhóm & An toàn

- [x] Viết đúng 10 case vào `data/eval_group.json` (5 một lượt + 5 nhiều lượt), có đầu ra kỳ vọng — commit `3281c21`
- [x] Chạy case nhóm cùng các version của Người 1 khi có — `runs/v0-v3_B_group_openai_*.json`, commit `d7c0416`
- [ ] Chạy bộ 12 case an toàn (`eval_adversarial.json`) — **còn thiếu**, chưa có `runs/*adversarial*.json`
- [ ] Phân tích chi tiết ít nhất 3 case an toàn (hành vi thật: hỏi lại, tôn trọng hủy/sửa, giữ dữ liệu nội bộ) — **còn thiếu**, phụ thuộc mục trên
- Sở hữu file: `data/eval_group.json`, phần phân tích safety trong report

### Người 3 — Nguyễn Khánh Linh — UI & Transcript

- [x] Chạy/chỉnh `chat.py` sao cho UI hiện rõ tool được gọi, input, kết quả/lỗi và version đang chạy — commit `6fa3203` (PR #4)
- [x] Test UI với cả case thường và case đa lượt (thiếu info, sửa/hủy)
- [x] Lưu transcript của các hội thoại bắt buộc (hỏi lại, xác nhận, hủy) — `transcripts/ticket-cancellation-v0.transcript.json`, `transcripts/ticket-modification-failed-v0.transcript.json`, commit `0d8491c`
- [ ] Nhờ 1 người khác chạy thử UI theo đúng hướng dẫn README để xác nhận người ngoài chạy được
- Sở hữu file: `chat.py` (phần UI), thư mục transcript

### Người 4 — Ngô Lê Thủy Tiên — Report, tổng hợp & Bonus mở rộng

- [x] Theo dõi tiến độ 3 người kia, tổng hợp số liệu trước/sau vào `artifacts/REPORT.md` — commit `e0ab164` (PR #5)
- [x] Viết phần cách chạy, giới hạn còn lại, liên kết evidence (run file, version log, transcript) — commit `e0ab164`, `a8385b2`
- [ ] Nếu làm bonus: thiết kế 1 chức năng mới ngoài luồng cơ bản (data + code tích hợp + case test + demo), xem `RUBRIC.md` — chưa làm, xem `artifacts/REPORT.md` B5
- [ ] Cuối buổi: rà tên repo, checklist `SUBMISSION.md`, đảm bảo không commit `.env`/dữ liệu thật — đã xác nhận `.env` không được track; checklist `SUBMISSION.md` còn vài mục mở (xem `artifacts/REPORT.md` C3)
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

- Kết quả và bằng chứng: `case_accuracy` bộ base (30 case) tăng từ 0.6667 (v0) → 0.7667 (v1) → **0.9000 (v2, đỉnh)** → 0.8333 (v3); bộ eval nhóm (10 case) tăng từ 0.60 (v0) → 0.80 (v1–v3, không đổi thêm). Bằng chứng đầy đủ trong `artifacts/version_log.csv`, `runs/v0-v3_*.json` và 2 transcript UI thật (`transcripts/ticket-cancellation-v0.transcript.json`, `transcripts/ticket-modification-failed-v0.transcript.json`) — xem `artifacts/REPORT.md` phần B.
- Thay đổi hiệu quả nhất: v2 (sửa `tools.yaml` — mô tả tool rõ hơn và quy ước argument) cho mức tăng lớn nhất và không có case nào regress so với v1. v1 (sửa `system_prompt.md` lần đầu) là bước nền tảng giúp `multiturn_accuracy` đạt 1.0 ngay từ vòng đầu.
- Giới hạn còn lại: (1) v3 sửa `system_prompt.md` để xử lý multi-turn/parallel call nhưng làm **regress 4 case đã pass ở v2** (H10, H12, H13, H17 — xem `artifacts/REPORT.md` B2), case_accuracy tổng giảm so với v2. (2) 2 case fail ở mọi version chưa từng được sửa: `H19_ambiguous_environment`/`G03_ambiguous_environment` (agent tự chọn enum thay vì hỏi) và `H12`/`M05`/`M09`/`G05` (agent coi việc sửa 1 field ticket là xác nhận ngầm) — bằng chứng thật trong `transcripts/ticket-modification-failed-v0.transcript.json` cho thấy agent tạo ticket có ID thật dù chưa được xác nhận rõ ràng, đây là rủi ro an toàn cần ưu tiên sửa trước. (3) Bộ 12 case an toàn (`data/eval_adversarial.json`) chưa được chạy — chưa có bằng chứng cho phần B4a của report. (4) Chưa làm phần mở rộng/bonus ngoài luồng cơ bản.
- Cách phân công và tích hợp: 4 người làm song song trên nhánh riêng (`chien`, `khoa`, `linh-fe`, `tien`), mỗi người sở hữu file riêng để tránh xung đột (prompt/tool vs eval nhóm vs UI/transcript vs report), merge qua PR #1–#4 vào `main`. `version_log.csv` chỉ Người 1 append theo đúng quy ước đã đặt ra.

## INDIVIDUAL

Sao chép mục này cho từng thành viên.

### Ngô Lê Thủy Tiên — 2A202602614

- Phần việc và file/commit/PR: Report, tổng hợp số liệu từ `version_log.csv` và toàn bộ `runs/*.json`/`transcripts/*.json` của 3 thành viên vào `artifacts/REPORT.md` (điền B1–B7, A1, A4, C1–C3); cập nhật `TEAM.md` (bảng thành viên, checklist phân công, mục này). Trước đó: PR #3 (`artifacts/REPORT.md` phần A, `TEAM.md` thông tin nhóm).
- Quyết định, khó khăn và cách xử lý: Số liệu v0 trong `REPORT.md` cũ (0.70) không khớp `version_log.csv` (0.6667) do khác run file — chọn `version_log.csv` làm nguồn chính vì đó là log chính thức của người sở hữu prompt/tool. Không có run cho `eval_adversarial.json` nên không bịa số liệu cho B4a mà ghi rõ là phần việc còn thiếu thay vì để trống không giải thích.
- Điều đã học: So khớp kết quả case-level qua nhiều version (không chỉ nhìn `case_accuracy` tổng) mới phát hiện được v3 vừa sửa vừa làm regress case cũ đã pass ở v2 — số liệu tổng hợp có thể che giấu trade-off thật.
- AI/công cụ đã dùng và cách kiểm tra: Dùng Claude Code để đọc `runs/*.json`/`transcripts/*.json` bằng script Python, đối chiếu kết quả case-level giữa các version và với `version_log.csv`/`data/eval_*.json` gốc trước khi đưa vào report; mọi số liệu trong `REPORT.md`/`TEAM.md` đều trỏ tới file run/transcript thật để tự kiểm tra lại.
- Thời điểm đã tự nộp URL repo chung trên VLearn: _(điền sau khi nộp)_

### Họ và tên — MSSV

- Phần việc và file/commit/PR:
- Quyết định, khó khăn và cách xử lý:
- Điều đã học:
- AI/công cụ đã dùng và cách kiểm tra:
- Thời điểm đã tự nộp URL repo chung trên VLearn:
