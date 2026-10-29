# 在 Claude 里运行

适用：Claude 桌面版 / Cowork / Claude Code，装了 Claude in Chrome 扩展；文件在用户电脑上时通过 Cowork 的“连接文件夹”访问。

## 浏览器（Claude in Chrome）
- 开始先 `tabs_context_mcp`；连了多个 Chrome 时用 `select_browser` 选档案里记的 deviceId（列表显示名会变，按 deviceId 认）。tab group 丢了：先 `select_browser`，再 `tabs_context_mcp(createIfEmpty: true)`。
- 读页面：`get_page_text`、`read_page`、`find`（拿元素 ref）；操作：`computer`（点击、键入、截图、zoom）、`form_input`、`javascript_tool`。
- 上传：用 `find` 找 `input[type=file]` 的 ref，再 `file_upload`（只认云端 `/mnt/user-data/uploads` 或 `/mnt/user-data/outputs` 下的文件，单次 <10MB）。不要点上传按钮，会弹系统文件框。
- 这是用户自己的 Chrome，已有的登录状态可以直接用；需要本人操作的页面保留标签，用户打开 Chrome 就能接着做。

## 用户电脑上的文件（Cowork 连接文件夹）
- 列目录：`device_list_dir`；在用户电脑上跑命令：`device_bash`（文件夹挂在 `$HOME/mnt/<文件夹名>`）。
- 简历传给浏览器：`device_stage_files` 把 PDF 拷到云端 `/mnt/user-data/uploads/<文件夹名>/…`，再 `file_upload`。
- 生成的 cover letter：在云端 `/mnt/user-data/outputs/` 生成 → `device_commit_files` 写回用户的 Cover Letters 文件夹。
- **Excel 不要来回传**：把 `scripts/tracker_update.py` 和 ops.json commit 到用户文件夹（如「Claude outputs/」），再用 `device_bash` 在用户电脑上运行。用户电脑上要有 openpyxl。

## 定时运行
- 每日投递可以做成定时任务：每次运行是全新会话，所以任务指令里要写“先用 job-apply-pipeline skill，读 profile.md”。
- 定时运行时没人在看：有需要用户处理的事（验证码、同意项、限投候选、面试/笔试）用推送通知；一切正常就不打扰。

## 记笔记
- 会话挂了项目（Project）时，把当天新踩的坑写进项目文档（如 `daily-apply-notes-{日期}.md`），下次运行先读最近一两天的。
