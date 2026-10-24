# math-learning

目标：面对一道题，能说明条件、选择合法方法、写出推理，并在之后独立完成变式。

从[当前任务](progress.md#当前任务)继续：先作答，按暴露的障碍查概念，订正后留下下一断点。

| 需要什么 | 只在这里维护 |
| --- | --- |
| 当前题、能力证据和下一步 | [学习状态](progress.md) |
| 原题、本人原答及必要核查 | [代表题](practice/representative-problems.md) · [手写原稿](practice/handwritten-2026-10-14.md) |
| 错因与实际复测结果 | [错因台账](mistakes/mistake-log.md) |
| 过去的学习与资料接收节点 | [历史记录](history/2026-09-to-10.md) |

## 按概念依赖查阅

[函数与极限](notes/01-functions-and-limits.md) → [等价无穷小](notes/02-equivalent-infinitesimals.md) → [导数](notes/03-derivatives.md) → [导数应用](notes/04-derivative-applications.md) / [中值定理](notes/05-mean-value-theorems.md) → [洛必达与综合极限](notes/06-lhopital-and-composite-limits.md) → [泰勒与余项](notes/07-taylor-and-asymptotic-notation.md)。

这是一条查找前置概念的路线，不是必须重学的清单。笔记保存定义、条件和必要例子；个人状态只在学习状态中更新。

保留内容的标准：能提供真实作答证据、解释一个具体障碍，或支持下一次独立尝试。重复讲解改为链接；不同原稿保留，即使题型相同。维护与记录规则集中见 [AGENTS.md](AGENTS.md)。

## 检查仓库

Python 3.10 或以上，无第三方依赖：

~~~bash
python scripts/check_repo.py
~~~

检查 UTF-8、本地链接、图片路径、Markdown 锚点及公式分隔符；不判断数学推导或掌握程度。公式使用 `$...$` 和 `$$...$$`。
