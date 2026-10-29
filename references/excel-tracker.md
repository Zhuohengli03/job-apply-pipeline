# 投递追踪 Excel

## 结构
一个工作簿，按渠道分工作表，列结构完全一样（11 列）：

| 列 | 内容 |
|---|---|
| 公司 | 公司名（可加括号说明业务/部门） |
| 平台 | 实际投递渠道，如 LinkedIn Easy Apply / Greenhouse(官网) / Workday（官网，经LinkedIn） / 小红书校招官网 |
| 职位 | 职位全称；校招写志愿序号和方向 |
| 办公（远程/混合/线下） | 含城市、是否需搬迁 |
| 日期 | YYYY-MM-DD |
| 状态 | 见下方状态表 |
| 网址 | 岗位详情页 |
| 备注 | 发布时间或截止日期；匹配点、缺口；页面显示的文件名和核对方式；留给本人的步骤；后续进展追加在后面（用“｜日期：”分隔） |
| 使用简历（文件路径） | 完整路径；未投写“—（未投）” |
| Cover Letter（文件路径） | 完整路径；没有 CL 栏写“无（表单无CL栏）” |
| 投递入口网址 / 登录账号 | `实际提交的页面网址 ｜ 登录方式和账号`（不写密码、证件号、验证码；看不出账号写“账号未知”并问本人） |

工作表：
- 「投递追踪」：公司官网、海外平台（LinkedIn、Greenhouse、Ashby、Lever、Workday、Indeed、Handshake…）、国内校招官网。
- 「BOSS直聘」「猎聘」「实习僧」等：各国内平台。
- 「LinkedIn打招呼」（可选，列结构不同）：社交加好友记录，不是投递，查重时不要当投递。
- 「总览」（可选）：只读公式统计，不要改。

**状态值**：已提交、已投递、进行中、面试中、测评中、Offer、已拒、未提交、待补信息、待验证码、跳过。

## 写入规则
- 写之前先备份到备份文件夹：`求职投递追踪_backup_{日期}_{说明}.xlsx`。
- 用 openpyxl 读整本再保存（保留所有工作表和条件格式），不要新建工作簿覆盖。
- 按工作表名字取（`wb['BOSS直聘']`），不要用 `active`；按表头名字找列，不要写死列号。
- 新行复制同表上一行的样式。
- 写完核对所有工作表都还在。
- 状态更新（拒信、面试、用户补交）去原来那一行改，不要新加行；备注追加“｜MM/DD：…”。

`scripts/tracker_update.py` 已实现以上规则：

```bash
# 新建空表（第一次用）
python3 tracker_update.py init "/path/求职投递追踪.xlsx"

# 追加/更新（ops.json 见脚本顶部说明）
python3 tracker_update.py apply "/path/求职投递追踪.xlsx" ops.json --backup-dir "/path/Claude outputs" --tag followup

# 统计
python3 tracker_update.py stats "/path/求职投递追踪.xlsx"
python3 tracker_update.py search "/path/求职投递追踪.xlsx" 百度 Baidu
```

不同环境怎么运行脚本、怎么把改好的表交还用户，见 `runtime-claude.md` / `runtime-chatgpt.md`。都不能跑 Python 时，给出要追加的整行（11 列，制表符分隔，可直接粘贴进 Excel）和要修改的行（公司+职位+新状态+追加备注）。

## 统计口径（“我投了多少份”）
- 算作已投递的状态：已提交、已投递、已拒、进行中、面试中、测评中、Offer。
- 不算：未提交、待补信息、待验证码、跳过。
- 分开报：
  - 官网/ATS 网申（「投递追踪」里平台不是 LinkedIn Easy Apply 的）
  - LinkedIn Easy Apply（正式申请，但用户可能不想算进“网申”，单列）
  - 招聘平台投递（猎聘、实习僧等真正投了简历的）
  - BOSS 直聘打招呼、LinkedIn 加好友：不算投递
- 顺便报：已拒数量、进行中/面试/测评的公司。
