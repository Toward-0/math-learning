# math-learning · 大学数学学习档案

> 真实作答 → 概念理解 → 错因分析 → 间隔复习 → 重新验证

这是个人大学数学学习仓库。目标不是堆积题目、追求绿色进度条，而是保存**可追溯的学习证据**，帮助发现遗忘、验证理解并持续进步。

## 从这里开始

| 我现在想做什么 | 阅读位置 |
| --- | --- |
| 确认学到哪里、下一步学什么 | [当前进度](progress.md) |
| 复习本周最容易忘的知识 | [复习队列](reviews/review-queue.md) |
| 查阅结构化知识讲义 | [知识笔记](#知识笔记) |
| 回忆真正做过的代表题 | [历史题目与可核实证据](practice/representative-problems.md) |
| 查找概念或计算误区 | [错题与易错点](mistakes/mistake-log.md) |
| 回看此前完整学习主线 | [2026 年 9—10 月学习回顾](history/2026-09-to-10.md) |
| 让 ChatGPT / Codex 协助维护 | [AGENTS.md](AGENTS.md) |
| 第一次上传 GitHub | [发布步骤](PUBLISH.md) |

## 当前定位

截至 **2026-10-17**，学习主线已推进到泰勒多项式构造，正在学习泰勒余项与小 o / 大 O。各模块的掌握记录与当前待答断点统一见 [当前进度](progress.md)。

## 知识笔记

1. [函数、基础极限与左右极限](notes/01-functions-and-limits.md)
2. [重要极限与等价无穷小](notes/02-equivalent-infinitesimals.md)
3. [导数定义与求导法则](notes/03-derivatives.md)
4. [导数应用：单调性、极值、拐点](notes/04-derivative-applications.md)
5. [罗尔和拉格朗日中值定理](notes/05-mean-value-theorems.md)
6. [洛必达法则与综合极限](notes/06-lhopital-and-composite-limits.md)
7. [泰勒多项式、余项与小 o / 大 O](notes/07-taylor-and-asymptotic-notation.md)

笔记是**教学整理**，不是本人从零独立完成的证明。每篇笔记都包含使用条件、反例或常见陷阱、代表例题与复习检查点。

## 每次学习后怎样同步

1. 在学习聊天中按 [课后交接模板](templates/session-handoff.md) 整理本次新增内容，并保留代表题原稿。
2. 将交接记录和原稿交给维护助手，说明“同步到数学仓库”。助手按 [维护规则](AGENTS.md) 读取最新版本、选择必要文件、检查并提交。
3. 同步完成后查看返回的提交链接；下次从 [当前进度](progress.md) 和 [下一次学习](reviews/review-queue.md) 接续。

每次只需要交接本次新增内容。最后一道题应留下完整题干与作答状态，便于继续学习。默认只保留下一次学习，不额外生成固定日期的复习排期。

## 数学公式与图片

GitHub Markdown 支持常见 LaTeX 数学公式：行内使用 `$...$`，独立公式使用 `$$...$$`。手写原稿保存在现有的 `assets/original-work/`，并在练习记录中附文字转录或说明；**不要用一张图片代替全部错误分析**。

## 可验证性

仓库提供一个不需要第三方依赖的轻量检查程序：

```bash
python scripts/check_repo.py
```

它只验证 Markdown 本地链接是否存在、文件是否为 UTF-8、历史记录与目录是否能被读取；**不会自动判断数学证明是否正确，也不能证明学习者掌握了知识**。GitHub Actions 仅做同样的基础检查。

## 来源说明

来源等级见 [维护规则](AGENTS.md#事实与学习状态)。历史概要保留原标记；四张原稿、转录与订正统一见 [练习证据](practice/representative-problems.md#original-work)。
