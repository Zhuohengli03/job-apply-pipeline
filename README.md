# job-apply-pipeline 安装与使用

一个求职网申 skill：找岗 → 判断匹配 → 写 cover letter → 用浏览器代理填表 → 核对提交 → 记进 Excel。不含任何个人信息，第一次用时会帮你建自己的 `profile.md`。

## Claude
1. 在 Claude 里添加这个 skill（上传 `.skill` 或 zip；能不能自己加 skill 取决于你的账号/组织设置）。
2. 安装 Claude in Chrome 扩展；用 Cowork 的话，把放简历和投递表的文件夹连接进来。
3. 说“帮我建求职档案”或直接“开始今天的投递”。

## ChatGPT
- **有 Skills 功能**（工作区管理员开启后可用）：把这个文件夹打包成 zip 上传为 skill，用法同上。浏览器操作用 agent 模式或 Atlas 浏览器。
- **没有 Skills 功能**：按 `adapters/chatgpt-project-instructions.md` 的说明，把那段指令粘进 ChatGPT Project 或自定义 GPT，再上传参考文件和简历。

## 文件说明
- `SKILL.md`：主流程和硬规则
- `references/profile-template.md`：个人档案模板（复制后填好，存在自己的求职文件夹）
- `references/selection-and-matching.md`：选岗与匹配度判断
- `references/platform-playbook.md`：LinkedIn、Greenhouse、Ashby、Workday、Oracle、国内校招官网等的填表技巧
- `references/excel-tracker.md`：投递表格式与统计口径
- `references/runtime-claude.md`、`references/runtime-chatgpt.md`：两种环境的具体操作方式
- `scripts/tracker_update.py`：建表、追加/更新、统计、搜索（需要 openpyxl）
- `scripts/cover_letter.py`：生成 cover letter PDF（需要 reportlab）

## 安全边界
密码、验证码（含邮件验证码）、同意条款、证件号永远由你本人操作；工作授权和担保问题如实回答。
