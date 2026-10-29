# job-apply-pipeline

一个求职网申的 Agent Skill，Claude 和 ChatGPT 都能用。AI 按这套流程帮你找岗位、判断匹配度、写 cover letter、用浏览器填申请表并在核对后提交，最后把每一份投递记进 Excel。

这套流程是在几周里每天真实投递跑出来的，累计 200 多份，踩过的坑都写成了规则。skill 里没有任何个人信息：第一次用时，它会根据你的简历帮你建一份自己的 `profile.md`。

## 适合谁

- **在找实习或全职的学生、应届生**，特别是**同时投海外和国内的中国留学生**。海外的公司官网、LinkedIn，国内的校招官网、BOSS直聘，一套流程都能管。
- 投**产品、运营、增长、数据分析、游戏（策划/运营/发行/用研）**等方向。这些方向的经验最多，换成别的方向也能用，在档案里改目标方向就行。
- **需要工作签证担保的人**（如 F-1 OPT）。工作授权和担保问题一律如实回答，岗位明确写了不担保的不会投。
- **想海投但不想乱投的人**。每个岗位都会逐条对照 JD，写一句匹配点、一句缺口，不匹配的不投。
- 每天有 10–20 分钟处理 AI 交回来的事情：验证码、同意条款、登录，以及限投岗位的选择。

不太适合：3 年以上经验的社招（选岗规则按应届和入门岗写的），以及希望完全不看、全自动提交的人（这套规则刻意把一些关键步骤留给你本人）。

## 会在哪些地方投递

| 渠道 | AI 做什么 | 算不算一份投递 |
|---|---|---|
| **公司官网 / 招聘系统**：Greenhouse、Ashby、Lever、Workday、Oracle、Workable、Rippling、Jobvite、Phenom、SmartRecruiters，以及 Shopee、Garena 等官网 | 找岗、判断匹配、写 cover letter、填表、核对附件、提交 | 算（官网网申） |
| **国内校招官网**：字节、网易、阿里、快手、小红书、B站、百度、京东、米哈游、鹰角等 | 填表、核对附件后提交；有投递次数上限的平台，先列出候选岗位由你决定 | 算（官网网申） |
| **LinkedIn 投递**（Easy Apply） | 填表、上传并核对简历和 CL、提交 | 算（单独统计） |
| **Indeed 投递** | 填写 smartapply 并提交 | 算 |
| **Handshake** | 找岗（可筛“接受签证担保”）、投递 | 算 |
| **LinkedIn 打招呼** | 找招聘官、用人经理、校友和同岗位的人，加好友时每人单独写附言；对方通过后发跟进消息 | 不算（单独记录） |
| **BOSS直聘** | 挑对口岗位打招呼：先发简历图片，再发按 JD 写的招呼语；HR 要简历时发附件 | 不算投递（打招呼） |
| **猎聘** | 投附件简历、打招呼 | 投了简历的算 |
| **实习僧** | 投简历 | 投了简历的算 |

你问“我投了多少份”时，AI 会分开报：官网网申、LinkedIn Easy Apply、招聘平台投递三类。BOSS 打招呼和 LinkedIn 加好友不算在内。

## 这些事永远由你本人做

- 注册账号、输入密码、登录
- 所有验证码，包括邮件和短信验证码（就算你把验证码发给 AI，它也不会替你填）
- 同意类勾选：隐私政策、数据处理、背调授权、仲裁协议、条款
- 身份证号、护照号、SSN

遇到这些步骤，AI 会停在那一步并把页面留着，在汇总里告诉你去哪个页面做什么。

## 安装

### Claude
1. 在 Claude 里添加这个 skill：下载本仓库的 zip 上传。能不能自己添加 skill，取决于你的账号或组织设置。
2. 安装 Claude in Chrome 扩展。用 Cowork 的话，把放简历和投递表的文件夹也连接进来。
3. 说“帮我建求职档案”（第一次用时），之后说“开始今天的投递”。

### ChatGPT
- **有 Skills 功能**（需要工作区管理员开启）：把这个文件夹打成 zip 上传为 skill，用法同上。填表时用 agent 模式或 Atlas 浏览器。
- **没有 Skills 功能**：按 `adapters/chatgpt-project-instructions.md` 的说明，把里面那段指令粘进 ChatGPT 的 Project 或自定义 GPT，再上传参考文件和你的简历。

## 第一次使用：建个人档案

1. 把在用的几版简历 PDF 发给 AI，说“帮我建求职档案”。
2. AI 先从简历里读出能读的信息，再分 4 轮问你：
   - 身份与工作授权
   - 求职方向与偏好
   - 表单固定答案
   - 运行设置
3. 确认 AI 给你的摘要后，档案存进你自己的求职文件夹。

也可以照 `references/profile-template.md` 自己填。注意：**`profile.md` 里是你的个人信息，不要上传到 GitHub，也不要分享给别人。**

## 文件说明

| 文件 | 内容 |
|---|---|
| `SKILL.md` | 主流程和硬规则 |
| `references/onboarding.md` | 第一次使用时怎么建档案 |
| `references/profile-template.md` | 个人档案模板 |
| `references/selection-and-matching.md` | 选岗和匹配度判断 |
| `references/platform-playbook.md` | 各招聘网站的填表技巧和踩过的坑 |
| `references/outreach.md` | LinkedIn 打招呼，以及 BOSS直聘、猎聘、实习僧的打招呼 |
| `references/excel-tracker.md` | 投递表格式和统计口径 |
| `references/runtime-claude.md`、`runtime-chatgpt.md` | 在 Claude 和 ChatGPT 里分别怎么操作 |
| `adapters/chatgpt-project-instructions.md` | 没有 Skills 功能时，ChatGPT 用的指令 |
| `scripts/tracker_update.py` | 投递表：新建、追加或更新、统计、搜索（需要 openpyxl） |
| `scripts/cover_letter.py` | 生成 cover letter PDF（需要 reportlab） |

## 注意

- 各招聘网站的页面会改版，`platform-playbook.md` 里的技巧可能过时。遇到新坑，欢迎补充。
- 遵守各平台的使用条款，按正常人的节奏操作，不要批量调用平台接口。
- AI 填的每一份申请都以你本人的名义提交，请定期抽查投递表和申请记录。
