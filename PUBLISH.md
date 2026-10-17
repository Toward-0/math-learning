# 将这个数学仓库首次发布到 GitHub

[返回首页](README.md)

仓库已经发布。日常学习后的同步请按 [README 中的流程](README.md#每次学习后怎样同步) 和 [课后交接模板](templates/session-handoff.md) 操作。下文保留首次建库的历史参考，仅用于重新建库时查阅。

## 1. 在 GitHub 建立空仓库

登录自己的 GitHub 账号，打开 https://github.com/new 。

- Repository name：`math-learning`
- Description：`My university math learning notes, verified practice and spaced reviews`
- Public 或 Private：自行选择；Public 表示任何人可以看见学习记录。
- **不要勾选** Initialize with README、Add .gitignore、Choose a license（下载包已经包含 README、.gitignore）。

创建后请在 GitHub 页面确认仓库地址是 `https://github.com/Toward-0/math-learning`。

## 2. 在 Windows 解压

把 `math-learning-ready.zip` 解压到例如 `D:\projects\`，最终文件夹应为：

```text
D:\projects\math-learning\README.md
D:\projects\math-learning\progress.md
D:\projects\math-learning\notes\
D:\projects\math-learning\.github\workflows\check.yml
```

`.github` 和 `.gitignore` 是重要文件，不能删掉。不要把 ZIP 文件本身直接上传到 GitHub 当作学习资料。

## 3. PowerShell 发布

打开 PowerShell，依次运行：

```powershell
cd "D:\projects\math-learning"
git init -b main
git add .
git commit -m "Initial math learning archive"
git remote add origin https://github.com/Toward-0/math-learning.git
git push -u origin main
```

前提是已安装 Git，且已经完成 GitHub 认证。若要求浏览器登录，通过 Git Credential Manager 进行正常授权；不要在聊天中粘贴任何访问令牌。

如果 `git commit` 提示作者身份缺失，可按提示设置自己的 `git config user.name` / `git config user.email` 后重新提交。若 `git push` 提示网络或认证失败，不要反复重置本地仓库，保留具体报错再排查。

## 4. 发布后验证

- 打开 `https://github.com/Toward-0/math-learning`，确认主页 README 正确显示中文与数学公式。
- 点击 `notes/`，确认知识笔记和 `progress.md` 都存在。
- 点击 GitHub 的 **Actions** 页面，等待 `Validate math learning repository` 工作流完成；它仅检查文件和链接，并不检验数学结论。

## 5. 以后怎样维护

每次数学学习后只修改必要的文件：

1. 新知识的简短笔记（如确有新内容）。
2. `practice/` 中的代表性真实作答，以及 `mistakes/` 里的关键错因。
3. `reviews/review-queue.md` 的闭卷复测结果。
4. 确有新证据时更新 `progress.md`。

每次完成本地修改后：

```powershell
git add .
git commit -m "Record math study progress"
git push
```

如果需要 ChatGPT 帮助继续学习，可以提供公开仓库链接，要求先读取 `AGENTS.md`、`progress.md` 和 `reviews/review-queue.md`，再依据实际作答更新。**ChatGPT 的聊天记录不会自动同步到 GitHub。**
