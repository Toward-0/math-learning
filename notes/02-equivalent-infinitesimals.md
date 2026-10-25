# 02 · 重要极限与等价无穷小

[知识目录](README.md) · [学习记录](../progress.md) · [错题记录](../mistakes/mistake-log.md)

> 类型：整理者讲义 `[C]`。强调适用条件，而不是只背结论。

## 重要极限一

$$
\lim_{x\to0}\frac{\sin x}{x}=1.
$$

于是：

$$
\lim_{x\to0}\frac{\sin(3x)}x
=3\lim_{x\to0}\frac{\sin(3x)}{3x}=3.
$$

**前提：** 三角函数使用弧度制，自变量趋于 0。

## 重要极限二

$$
\lim_{t\to0}(1+t)^{1/t}=e.
$$

其常用扩展是：当 `u(x)→0`、底数在所考察区间为正，并且 `u(x)v(x)→A` 时，

$$
(1+u(x))^{v(x)}\to e^A.
$$

**这不是“看到 1 的无穷次方就答 e”**；需要先算清对数极限（或等价的乘积极限）。旧学习中做过 `e²`、`e^{-6}` 等变形结果。

## 什么叫等价无穷小？

如果 `\alpha(x)→0`、`\beta(x)→0`，并且

$$
\lim_{x\to a}\frac{\alpha(x)}{\beta(x)}=1,
$$

就记作 `\alpha(x)\sim\beta(x)`（当 `x→a` 时）。

常用的 `x→0` 等价式：

$$
\sin x\sim x,\qquad \tan x\sim x,
$$

$$
1-\cos x\sim\frac{x^2}{2},\qquad
\ln(1+x)\sim x,
$$

$$
e^x-1\sim x.
$$

例：

$$
\lim_{x\to0}\frac{1-\cos x}{x^2}=\frac12.
$$

## 同阶、高阶、等价

设两个无穷小 `α,β`，考察比值 `α/β`：

- 趋向非零有限常数：**同阶无穷小**。
- 趋向 1：**等价无穷小**（是同阶的特殊情况）。
- 趋向 0：`α` 相对于 `β` 是**高阶无穷小**。

例：`x²` 相对于 `x` 是高阶，因为 `x²/x→0`。`2x` 和 `x` 同阶却不等价，因为比值趋于 2。

## 为什么加减法不能随意替换？

等价关系控制的是**相对误差**。假设比较函数在所考察的去心邻域内非零，令

$$
\varepsilon(x)=\frac{\alpha(x)}{\beta(x)}-1\to0,
\qquad \alpha(x)=\beta(x)(1+\varepsilon(x)).
$$

这解释了乘除结构中为什么可以替换。例如 $q(x)\ne0$ 且 $\beta(x)/q(x)\to L$（有限），则

$$
\frac{\alpha(x)}{q(x)}
=\frac{\beta(x)}{q(x)}(1+\varepsilon(x))\to L.
$$

减法却可能把主项消掉：

$$
\alpha(x)-\beta(x)=\beta(x)\varepsilon(x).
$$

剩下的恰好是替换时忽略的误差，所以不能直接写成0。用[小 o 记号](07-taylor-and-asymptotic-notation.md#小-o-与大-o-的区别)表示，就是 $\alpha\sim\beta\iff\alpha-\beta=o(\beta)$；它描述误差的相对大小，不表示误差恒为零。

例如：

$$
\sin x - x.
$$

如果直接把 `sin x` 换成 `x`，就得到 `0`，抹掉了本来很重要的更高阶差值。正确做法是分析抵消后剩余的首个非零阶（需要时使用恒等变形、洛必达、或后续的泰勒工具）。

**判断流程：** 先看整体结构 → 判断有无重要抵消 → 说明为何可以替换 → 再计算极限。

指数型的取对数步骤统一见[综合极限](06-lhopital-and-composite-limits.md#logarithmic-limit)。

## 按需自检

1. 为什么 `sin x ~ x` 不能直接证明 `sin x−x` 等于零？
2. 说出 `1−cos x` 的等价无穷小，并算 `(1−cos x)/x²` 的极限。
3. 对 `(1+2x)^{1/x}`，解释极限为什么是 `e²` 而不是 `e`。
