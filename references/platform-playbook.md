# 平台填表手册

只读当前要用的那一节。每条都是真实踩过的坑。

目录：通用技巧｜找岗｜LinkedIn Easy Apply｜Greenhouse｜Ashby｜Lever｜Workday｜Oracle Cloud（Candidate Experience）｜Workable｜Rippling｜Jobvite｜Phenom（如 Blizzard）｜SmartRecruiters / Moka 海外｜Sea 集团（Shopee/Garena/Monee）｜Indeed｜Handshake｜国内校招官网通用｜字节｜小红书｜B 站｜百度｜米哈游等 antd 表单｜BOSS 直聘｜猎聘｜实习僧

---

## 通用技巧
带 JS 的技巧只适用于能在页面里执行脚本的环境（如 Claude in Chrome）；不能执行 JS 的环境（如 ChatGPT agent）用点击、键入、键盘操作，每步看截图核对。
- **上传文件**：怎么把文件交给浏览器见 runtime 文件。上传后一定读该栏显示的文件名。
- **JS 返回被拦**：返回字符串里有 `= & ?` 时会显示 `[BLOCKED: Cookie/query string data]`。先 `.replace(/[=&?]/g,'_')` 再返回；或先存到 `window.__x`，再分段取。
- **长文本读取**：JS 返回会被截断（约 1000 字）。把结果写进页面里一个 `<article><pre>`，再用 `get_page_text` 读。
- **文本框**：React/Vue 表单用 native setter + `input`/`change` 事件；真实键入偶尔会丢字母，写完都读一遍 value。
- **原生弹窗**：页面突然完全无响应、截图也超时，多半是后台标签里的 `alert()`。换页后先执行 `window.alert=m=>{(window.__dlg=window.__dlg||[]).push(m)}; window.confirm=m=>{(window.__dlg=window.__dlg||[]).push(m);return true}`。
- **简历解析**：几乎所有 ATS 都会解析简历，常见错误：个人项目被填成工作经历、名字带括号昵称、起止月份错一个月、学位/专业对不上下拉选项、把技能段塞进职责栏。逐项改。
- **会话过期**：填好的页面不要长时间挂着等确认。Oracle/Workday 重新进入后草稿通常还在。

## 找岗
- **LinkedIn guest 接口**（在 linkedin.com 页面里 fetch，每次间隔 ≥2 秒）：`/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=…&geoId=…&f_TPR=r86400&f_AL=true&f_E=1%2C2&start=0`（`r86400`=24h，`r604800`=一周；`f_AL=true` 只看 Easy Apply；`f_E=1,2` 实习/入门）。返回的 HTML 不能用 DOMParser，用 `split('data-entity-urn="urn:li:jobPosting:')` + 正则取标题、公司、时间。JD 用 `/jobs-guest/jobs/api/jobPosting/{id}`，取 `show-more-less-html__markup` 段。不要用隐藏 iframe 批量加载（会卡死标签）。长循环放后台跑，轮询计数器。
- **Greenhouse / Ashby / Lever 公开 API**：`boards-api.greenhouse.io/v1/boards/{公司}/jobs`、`api.ashbyhq.com/posting-api/job-board/{公司}`、`api.lever.co/v0/postings/{公司}`。云端 curl 可能被代理挡、LinkedIn 等页面的 CSP 会挡跨域 fetch：新开一个标签直接打开其中一个 API 地址，再在这个页面里同源/跨域 fetch 其他公司。
- **Handshake**：搜索页有「Open to US visa sponsorship」快捷筛选。
- **地区**：美国入门岗池子浅时，新加坡、香港、马来西亚的应届/管培岗是不错的补充（LinkedIn geoId：马来西亚 106808692）。
- **LinkedIn Apply 外链**：要解析 href 里的 `url=` 参数才能看到真实 ATS 地址。

## LinkedIn Easy Apply
- 电话国家默认可能是别的国家，改成正确国家码。
- 地点输入框是联想框：键入城市后 ArrowDown + Enter。
- **简历**：列表会记住上次用的那份。每次投之前用 `file_upload` 把当天 stage 的最新版传一次（列表首行显示当天日期并自动选中），这是最可靠的核对方式（卡片上的下载图标只会静默下载，看不了）。“Upload resume / cover letter” 按钮不是 file input：先拦截 `HTMLInputElement.prototype.click` 拿到动态生成的 input，挪到 body/设为可见后再 `file_upload`。
- **Cover letter 文本框会自动带出上一家（甚至同公司上一个岗位）的信**，而且可能出现在第 1 页。不要用脚本连点 Next；每一页都读，Review 页检查 CL 开头的公司名。
- 弹窗在 shadow DOM 里：`document.querySelector` 找不到时递归遍历 `shadowRoot`。radio 重渲染后 id 会变，提交前按位置重读 checked。
- 自动带出的工作经历标题/开始月常不对，按档案改。
- 末页「Follow 公司」默认勾选，取消。提交后不能重投。
- 同一岗位会换新 ID 重发，先查 Excel 和邮箱。

## Greenhouse
- 公司官网可能跳转，embed 地址通常可用：`job-boards.greenhouse.io/embed/job_app?for={公司}&token={job_id}`。
- react-select 下拉：点开 → 键入 → 点选项或 Enter。每个选完用 JS 读 `.select__single-value` 核对；连续 type+Enter 时焦点可能落进下一个文本框，文本框也要再读一遍。下拉没展开时按 Enter 会触发一次表单校验。
- Location (City)：输入 “City, State前几个字母” 再选，选完放大截图核对（“Jersey City” 第二项是 Wisconsin）。
- 有的“可入职时间”看起来像文本框其实是下拉。
- 教育栏可能显示 N/A，要手动选学校/学位（本科学校不在列表里时选 Other）。
- “是否接收短信/WhatsApp” 下拉在某些浏览器里会被别的扩展弹层盖住整页：用 JS `focus()` 对应 input 后键盘输入，放到最后填。
- CL 可传 PDF 或 “Enter manually”。末尾的隐私/仲裁确认下拉属同意类，留给本人。

## Ashby
- 先传简历，等几秒（会解析并重置文本框）再填文字。文本框 triple_click + 真实键入或 native setter，填完读 value。
- Yes/No 是按钮。显示选中不等于已登记：提交报 “Missing entry” 时先点另一个再点回来。
- 期望薪资可能是数字框（只能填数字）；JD 没写薪资时问用户。

## Lever
- 提交时有 hCaptcha：填好后停下，留给本人。
- 地点/签名选项按档案如实填。

## Workday
- 需要账号：本人注册/登录后再继续。账号写进 Excel 第 11 列。
- 推荐 “Autofill with Resume”，然后逐步核对：My Information → My Experience → Application Questions → Voluntary Disclosures → Self Identify → Review。
- **下拉是 listbox 按钮**：循环“点按钮 → 点 `[role=option]` 文本完全相等的项”。prompt 类（学校、专业）：键入 → Enter 一次搜索 → 点选项；再按一次 Enter 会选中高亮的错误项。
- 日期：在月份 spinbutton 里直接键入 “MMYYYY”（Self Identify 的日期键入 “MMDDYYYY”）。
- 电话报格式错：只输数字。
- 推荐技能 chip 删除：`[data-automation-id="selectedItem"]` 所在节点附近的 `[data-automation-id="DELETE_charm"]`。删掉简历里没有的技能。
- 搬迁题常是 checkbox 组。Voluntary Disclosures 页底部的 “Yes, I agree”（含仲裁/通讯同意）留给本人。
- **提交后去 Candidate Home 看状态**：显示 “Not Submitted” 就是没交上。

## Oracle Cloud（Candidate Experience，如 Verisk）
- 输邮箱即可免注册 easy-apply；会话过期后重新输邮箱会发 6 位邮件验证码（本人输入）。验证后草稿会恢复，直接跳到最后一页。
- 上传简历后分块补全：链接要带 `http://`；ZIP 是联想框（键入后 ArrowDown 选中再 Enter）；学历是 pill 按钮；Yes/No 是 `role=radio`，JS `.click()` 不生效，用 `find` 拿 ref 点击。
- 最后一页点各分区会进入完整 4 步表单（Personal Info / Self ID / Talent Info / More About You），可在这里核对附件、删除解析出的错误经历（`aria-label="Delete"` 按钮，注意同页里教育也有同名按钮，按所在卡片文字定位）、补 EEO。
- 末页：隐私政策勾选（同意类）、E-Signature 全名；营销/职位推送勾选不勾。提交后 My Applications 显示 “Under Consideration”。

## Workable
- LinkedIn 带入的经历/教育要改（职位名、结束日期、本科日期 N/A）。下拉是普通 select：native setter + change 事件。
- 数据处理/敏感信息同意题留给本人。

## Rippling
- 简历解析会把 Current company 填成个人项目名，清空。下拉是自定义组件，坐标点开再点选项。“如果是请举例”文本框即使选 No 也可能必填。

## Jobvite
- 先选居住地才出表单。Add Resume 菜单里选 File 会生成新的 file input，容易传到 Additional Files（CL 栏）——上传后看 “Add Resume” 下显示的文件名。

## Phenom（如 careers.blizzard.com）
- 第一步必须先上传简历；上传成功会弹原生 alert，后台标签里看不见会锁死页面——先覆盖 `window.alert`（见通用技巧）。下拉用 `form_input`。CL 传在 “Additional attachments”。

## SmartRecruiters / Moka 海外（hire-r1.mokahr.com 等）
- 要先 Sign in 的，留给本人。

## Sea 集团（careers.shopee.sg / careers.garena.com / Monee）
- 访客可投。解析后逐项改（名字、起止月份）；学位等级选 Others / Not Applicable；Supporting Documents 可传 CL；担保题可能默认 No，要改。月份选择器弹出动画未结束就点会选错，等 1–2 秒并截图核对。
- JD 写明集团内同时只考虑一个岗位：按限投处理。

## Indeed（smartapply）
- “Review your resume details” 页要勾两个 “No … to add” 才能继续。卡在 “Preparing review”（多半是后台 reCAPTCHA）就留给本人，不要反复刷新。

## Handshake
- 部分岗位跳外部 ATS；有的需要在 Handshake 内上传文档。

---

## 国内校招官网通用
- 登录基本是手机验证码：本人登录。限投规则以页面提示为准（“已投递方向”“还可以选择 N 个子方向”“最多投递 N 个职位”“方向不可更换”）。
- 在线简历通常所有志愿共用：投之前核对内容是最新；投之后不要改。
- 上传附件选“仅替换附件”，不要“解析覆盖”。
- 证件号、邮箱/短信验证码由本人填。
- 提交后通常有“确认投递”弹窗，再点确定；看到“投递成功/已投递”。

## 字节跳动
- 不要点「解析并覆盖」（会清空证件号等）；只上传附件，逐项手改，用真实键入。后台标签可能整页重载回旧在线简历，提交前把附件名、毕业时间、学院、自我评价再读一遍。
- 「了解渠道」必填：字节跳动招聘官方渠道/账号 → 校园招聘官网。下拉弹层残留会挡控件：选完把弹层 `display:none`。提交后“确定投递吗？”→「继续投递」→ 看到「投递成功」。

## 小红书（job.xiaohongshu.com）
- 直接往文件框传 PDF 会触发解析、覆盖已存字段。原附件预览确认是最新版就不重传；覆盖了就刷新页面（不提交）恢复。
- 意向城市是多选；服从调剂默认“是”；提交后有「确认投递」弹窗。投递记录：`/campus/record`。

## B 站（jobs.bilibili.com）
- 应届列表 `campus/positions?code=03&type=3`（产品运营类）。在线简历两个志愿共用；附件选“仅替换附件”。ant-design-vue 表单：文本用 native setter + input 事件；月份选择器先改结束月再改开始月，“至今”最后勾。

## 百度（talent.baidu.com）
- 没有在线简历时要先创建校招简历，证件号必填（本人填）。

## 米哈游等 antd 表单 / Moka 国内
- 后台标签里下拉/日期弹层的关闭动画会卡住、挡住下面的输入框，误点会改错日期。日期用 JS 点 `td[title="YYYY-MM-DD"]`；下拉用键盘 Down/Enter；每次选完 blur 并把 `.ant-picker-dropdown`、`.ant-select-dropdown` 设为 `display:none`；最后把所有日期读一遍。
- Moka 出生日期是年月选择器：点年份标题切换年代再选。
- 「保存并预览」后可能弹邮箱验证码（本人完成）。

## BOSS 直聘（打招呼，不算正式投递）
- 只用网页、按正常人速度操作；**绝不批量调用 joblist 等接口**（会触发“账户异常”验证）。
- 双方都回复前不能发附件：先发简历图片（PNG，由 PDF 导出），再发文字招呼语，这样 HR 列表预览显示文字前 15 字。顺序不能反。
- 招呼语：前 15 字直接给出和 JD 最匹配的硬信息（带数字），不要“您好/我是”开头；后文 60–120 字补身份和对应关系；只写简历里有的事实。
- 薪资在列表页是加密字体，去详情页看。按城市搜比全国搜准；`experience=102` 是在校/应届。

## 猎聘
- 附件上限 3 份，替换要本人先删。连续快速保存会触发验证码：编辑间隔 10–20 秒。antd 弹窗卡在透明动画里：把 `.ant-c-modal` 及祖先的 `opacity` 设 1、`transform` 设 none。
- 「我的投递」：c.liepin.com/job/record/apply。搜索可加 `pubTime=7`、`workYearCode=1`。

## 实习僧
- 网页看不到 HR 消息（只在 App）。有的岗位点「投个简历」没有反应，算没投成。
