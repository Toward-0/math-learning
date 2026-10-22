# math-learning · 数学学习档案

目标：面对一道题，能说明条件、选择方法、写出成立的推理，并在之后独立重做或迁移。

## 每次从这里继续

打开 [下一次学习](reviews/review-queue.md#当前任务)，先尝试当前题，再根据具体困难查笔记。一次只处理一个主要障碍，结束时留下可接续的断点。

| 需要什么 | 入口 |
| --- | --- |
| 学到哪里、哪些结论已有证据 | [当前状态](progress.md) |
| 当前题与后续选择 | [下一次学习](reviews/review-queue.md#当前任务) |
| 原题、原答、原稿及订正 | [代表题](practice/representative-problems.md) · [早期手写原稿](practice/handwritten-2026-10-14.md) |
| 反复出现的错误及修正 | [错因台账](mistakes/mistake-log.md) |
| 阶段历史 | [学习回顾](history/2026-09-to-10.md) |

## 按需查阅概念

[函数与极限](notes/01-functions-and-limits.md) · [等价无穷小](notes/02-equivalent-infinitesimals.md) · [导数](notes/03-derivatives.md) · [导数应用](notes/04-derivative-applications.md) · [中值定理](notes/05-mean-value-theorems.md) · [洛必达与综合极限](notes/06-lhopital-and-composite-limits.md) · [泰勒与小 o / 大 O](notes/07-taylor-and-asymptotic-notation.md)

讲义属于教学整理 [C]。原稿、是否使用提示、解答是否正确和独立复测结果分别记录；看懂讲义或自动检查通过，不自动改变掌握状态。

## 每次只记录必要变化

用 [简短交接模板](templates/session-handoff.md) 留下本次题目、本人尝试、关键错误和下一断点，由维护助手选择文件。完整解答只存一份，其他位置链接；没有新证据时无需更新全仓库。默认不安排固定复习日期。

维护按 [AGENTS.md](AGENTS.md) 执行。

## 检查仓库

Python 3.10 或以上，无第三方依赖：

```bash
python scripts/check_repo.py
```

检查 UTF-8、本地链接、图片路径、Markdown 章节锚点及独立公式分隔符；不验证数学推导或学习程度。原始图片按接收批次保存在 `assets/handwritten/` 与 `assets/original-work/`，数学公式使用 `$...$` 和 `$$...$$`。
