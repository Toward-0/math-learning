# 数学练习与手写原稿

[返回首页](../README.md) · [当前状态](../progress.md) · [知识笔记](../notes/)

2026-10-14 Codex 收到本人提供的《数学实际作答.docx》，按文档顺序提取 26 张 JPEG，原图内容不作修改 [A]。图号不是题号或日期。数学作答和原始错误由本人完成，以下摘要由 Codex 按原稿整理；另行补充的核对、参考解释标为 [C]，集中维护在 `notes/`。看不见的题干不补写。

本批共用记录：实际作答日期：未记录；是否使用提示：未记录；实际复测日期和结果：尚未记录。作者身份已经明确；缺少这些记录不等于没有复习或不会。后续在对应题目下简记“完整题目或原稿位置｜本人原答及关键错误｜提示情况｜验证结果｜实际复测日期和结果”，仅填写真实发生的内容。本次参考推导核对 [C] 不作为本人复测。

## 原有代表题与证据

旧题编号保留，避免已有引用失效。[B] 为先前概要；只有能匹配的原图或片段增加 [A] 证据。

| 编号 | 原有题目 | 已有作答证据 |
| --- | --- | --- |
| P01 | `lim(x→2)(x²−4)/(x−2)` | [B] 原答 4；本批未找到同题原图，图18、19只是同类题 |
| P02 | `lim(x→0)sin(3x)/x` | [B] 原答 3；本批未找到原图 |
| P03 | `[(x²+1)/(x+1)]'` | [A] [图06](../assets/handwritten/06.jpeg) 有商法则步骤，结果为 `(x²+2x−1)/(x+1)²` |
| P04 | `x³−6x²+9x` 的单调区间与极值 | [B] 递增 `(-∞,1),(3,+∞)`、递减 `(1,3)`，极大点 1、极小点 3；图22第二题导数不同，不充当此题证据 |
| P05 | `x⁴−6x²` 的拐点 | [B] 曾正确判断 ±1 处二阶导变号；[A] [图11](../assets/handwritten/11.jpeg) 补充对应导数和取点计算，完整原题及最终坐标未写出 |
| P06 | `x²` 在 `[1,3]` 的中值点 | [B] 原记 `c=2`；[A] [图15](../assets/handwritten/15.jpeg) 为该题构造过程。[图22](../assets/handwritten/22.jpeg) 第四题数值相符，但题干不全 |
| P07 | `lim(x→0)(e^(2x)−1)/x` | [A] [图23](../assets/handwritten/23.jpeg) 左题，有步骤，原答 2 |
| P08 | `lim(x→0)(x−sin x)/x³` | [A] 同一[图23](../assets/handwritten/23.jpeg)右题，有步骤，原答 `1/6` |
| P09 | `lim(x→0+)x² ln x` | [A] [图24](../assets/handwritten/24.jpeg) 原答 0，但中间漏系数；原 M07 合并至本题 |
| P10 | `lim(x→0)(sin x/x)^(1/x²)` | [A] [图26](../assets/handwritten/26.jpeg) 有错误推导，原答 1；原 M06 合并至本题 |
| P11 | `lim(x→0)(1−cos x)/x²` | [B] 曾误答 −1；正确值见[等价无穷小讲义](../notes/02-equivalent-infinitesimals.md)。无对应原图 |
| P12 | `lim(x→0)x/(1−cos x)` | [B] 曾误答 0；左右趋向不同，见[左右极限讲义](../notes/01-functions-and-limits.md)。图20缺题干，不绑定本题 |

原 M02 的两个错答已保留在 P11、P12。P04/P05 的参考解释集中在[导数应用](../notes/04-derivative-applications.md)；P07～P10 的参考推导集中在[综合极限](../notes/06-lhopital-and-composite-limits.md)。参考推导不代表本人曾写出相同步骤。

## 手写作答

展开各项可直接查看原稿。一张图片包含多题时仍只保存一个图片文件。

<details>
<summary>图01 差商与导数定义</summary>

原稿将 `((3+h)²−9)/h` 化为 `6+h`，取 `h→0` 得 `f'(3)=6`，保留末行涂改。图中未单独写出完整原题。

![图01 差商与导数定义](../assets/handwritten/01.jpeg)

</details>

<details>
<summary>图02 切线</summary>

原稿写出点 `(2,4)`、`f'(2)=4`，从 `y−4=4(x−2)` 得 `y=4x−4`。完整题干未拍到。

![图02 切线](../assets/handwritten/02.jpeg)

</details>

<details>
<summary>图03 三个导数答案</summary>

原稿依次写 `4x³`、`7x⁶`、`6x`；缺少原函数，不反推题目，也不据此逐题判断对错。

![图03 三个导数答案](../assets/handwritten/03.jpeg)

</details>

<details>
<summary>图04 导数代值</summary>

原稿写 `f'(x)=6x+5`、`f'(2)=17`；原函数和完整题干未拍到。

![图04 导数代值](../assets/handwritten/04.jpeg)

</details>

<details>
<summary>图05 乘积求导</summary>

原稿：`y=x³(x²+2x)`；使用 `f'g+fg'`，展开 `3x⁴+6x³+2x⁴+2x³`，得到 `5x⁴+8x³`。本张步骤正确，不能用它抹去历史上的其他乘积符号错误。

![图05 乘积求导](../assets/handwritten/05.jpeg)

</details>

<details>
<summary>图06 商法则 P03</summary>

原稿：`y=(x²+1)/(x+1)`；分子为 `2x(x+1)−(x²+1)`，化简为 `x²+2x−1`，分母展开为 `x²+2x+1`。这张提供了 P03 的实际计算过程。

![图06 商法则 P03](../assets/handwritten/06.jpeg)

</details>

<details>
<summary>图07 链式求导</summary>

原稿：`y=(x²+2x)⁴`，先写 `4(x²+2x)³(2x+2)`，再化为 `8(x+1)(x²+2x)³`。

![图07 链式求导](../assets/handwritten/07.jpeg)

</details>

<details>
<summary>图08 五个导数答案</summary>

原稿有 `−3sin(3x)`、`10x(x²+1)⁴`、`2xe^(x²)`、`2/(2x+1)`、`2x sin x+x² cos x`。没有原函数，只作为答案片段保留。

![图08 五个导数答案](../assets/handwritten/08.jpeg)

</details>

<details>
<summary>图09 驻点与极值</summary>

原稿写 `f'=4x³−12x²`、`f''=12x²−24x`；算出驻点 0、3，判断 3 为极小值点，并用 0 两侧一阶导均为负说明 0 不是极值点。与旧概要中的四次多项式主题相符，但图中完整原函数未拍到；不能据此认定旧混淆已经全部解决。

![图09 驻点与极值](../assets/handwritten/09.jpeg)

</details>

<details>
<summary>图10 曲线弯曲方向的困惑</summary>

原稿写 `f''(−1)=36`、`f''(1)=−12`，对正负对应的弯曲方向提出疑问，并画了草图。原话包括“我感觉我对判断曲线弯曲的定义有点模糊”。这是真实困惑，不改成已经掌握；相关解释见[导数应用讲义](../notes/04-derivative-applications.md)。

![图10 曲线弯曲方向的困惑](../assets/handwritten/10.jpeg)

</details>

<details>
<summary>图11 二阶导符号 P05 的相关片段</summary>

原稿写 `f'=4x³−12x`、`f''=12x²−12`，求出零点 ±1，再计算 `f''(0)=−12`、`f''(±2)=36` 并画图。与 P05 的导数计算吻合；原函数、最终拐点坐标未在本张完整写出。

![图11 二阶导符号 P05 的相关片段](../assets/handwritten/11.jpeg)

</details>

<details>
<summary>图12 中值点计算与几何图</summary>

原稿画割线、切线图，并算 `(f(2)−f(0))/(2−0)=2`、`f'(c)=2c=2`，得到 `c=1`。只按可见区间计算保留，不与 `[1,3]` 的 P06 合成同一题。

![图12 中值点计算与几何图](../assets/handwritten/12.jpeg)

</details>

<details>
<summary>图13 罗尔情境的片段</summary>

图示横坐标 −1、1，原稿写 `f'=2x`、`f'(c)=2c=0`，得 `c=0` 和 `(0,0)`。完整题干未拍到，不能补称原稿已逐条验证定理条件。

![图13 罗尔情境的片段](../assets/handwritten/13.jpeg)

</details>

<details>
<summary>图14 端点相等与中值点</summary>

原稿计算 `f(1)=1−4+3=0`、`f(3)=9−12+3=0`，由 `f'=2x−4` 得 `c=2∈(1,3)`。这与 P06 的 `f=x²` 不同，不因答案都是 2 就合并。

![图14 端点相等与中值点](../assets/handwritten/14.jpeg)

</details>

<details>
<summary>图15 P06 的辅助函数构造</summary>

原稿明确写 `f=x²`、`x∈[1,3]`；令 `g=f−kx`，由 `1−k=9−3k` 求出 `k=4`，验证 `g(1)=g(3)=−3`。本张停在端点相等，没有写出最终 `c`；保留为 P06 的过程片段。

![图15 P06 的辅助函数构造](../assets/handwritten/15.jpeg)

</details>

<details>
<summary>图16 平均斜率与中值点混淆</summary>

原稿：`f=x³`、`x∈[0,2]`，先得到 `3c²=4`，随后写成 `k=c=2√3/3`，并用这个数构造 `g=f−kx`。关键错误是这一行把平均斜率 `k` 与中值点横坐标 `c` 混同，随后辅助函数也受影响；原图保留错误。核对结果 [C]：`k=4`，`c=2√3/3`；辅助函数的端点相等检查及参考修正见[中值定理笔记](../notes/05-mean-value-theorems.md)。这为原 M05 增加了可见证据，不是本人已完成修正或复测的记录。

![图16 平均斜率与中值点混淆](../assets/handwritten/16.jpeg)

</details>

<details>
<summary>图17 另一道辅助函数题</summary>

原稿明确写 `f=x²`、`x∈[0,4]`，求 `k=4`，令 `g=x²−4x`，验证两端相等，由 `2c−4=0` 得 `c=2`。保留涂改；区间不同于 P06。

![图17 另一道辅助函数题](../assets/handwritten/17.jpeg)

</details>

<details>
<summary>图18 因式分解极限</summary>

原稿：`lim(x→3)(x²−9)/(x−3)`；分解并约去 `x−3`，得 `lim(x→3)(x+3)=6`。与 P01 的趋近点和题目不同，单独保留。

![图18 因式分解极限](../assets/handwritten/18.jpeg)

</details>

<details>
<summary>图19 负趋近点的极限</summary>

原稿：`lim(x→−2)(x²−4)/(x+2)`；分解为 `(x+2)(x−2)`，约分后得到 −4。不是 P01 的同一题。

![图19 负趋近点的极限](../assets/handwritten/19.jpeg)

</details>

<details>
<summary>图20 缺题干的三个答案</summary>

只看到依次写出的 `−∞`、`+∞`、“不存在”。无法确认对应表达式，不能据这些结果认定是 P12 的原答。

![图20 缺题干的三个答案](../assets/handwritten/20.jpeg)

</details>

<details>
<summary>图21 链式求导片段</summary>

可见 `(x²+1)³` 的求导计算，写出 `3(x²+1)²·2x`，得到 `6x(x²+1)²`。左侧裁切，原稿符号与省略保持原样。

![图21 链式求导片段](../assets/handwritten/21.jpeg)

</details>

<details>
<summary>图22 四题混合复习</summary>

本页依次为：①趋近 −2 的分式极限得 −4；②由 `f'=3x²−6x` 的符号判断 0 为极大、2 为极小；③`|x|` 在 `[-1,1]` 因 0 不可导不能用罗尔；④求 `k=(3²−1)/2=4`，由 `g'(c)=2c−4=0` 得 `c=2`。第四题数值与 P06 相符，但本页缺完整题干，不把图片拼接成一次完整答卷；第一题与图19表达式相同，作答时间及是否复测未确认。

![图22 四题混合复习](../assets/handwritten/22.jpeg)

</details>

<details>
<summary>图23 洛必达极限 P07 与 P08</summary>

左题原稿将 `(e^(2x)−1)/x` 求导后得到极限 2；右题依次写 `(1−cos x)/(3x²)`、`sin x/(6x)`，得到 `1/6`。提供了两题的真实计算步骤，但原稿没有逐次写明适用条件。

![图23 洛必达极限 P07 与 P08](../assets/handwritten/23.jpeg)

</details>

<details>
<summary>图24 P09 的漏系数原稿</summary>

原稿将 `x² ln x` 转为 `ln x/(1/x²)`，下一行写为 `−x²`，最后得 0。关键错误位于这一步求导后的中间式。核对结果 [C]：最终答案 0 正确，但中间漏系数；分母导数及正确中间式见[综合极限讲义](../notes/06-lhopital-and-composite-limits.md)。保留原稿，不将参考修正记为本人已复测。

![图24 P09 的漏系数原稿](../assets/handwritten/24.jpeg)

</details>

<details>
<summary>图25 有理化极限</summary>

原稿计算 `lim(x→∞)(√(x²+4x)−x)`；乘共轭后化成 `4/(√(1+4/x)+1)`，得到 2。该变形按 `x→+∞` 理解成立；图中趋向只写了 `∞`。

![图25 有理化极限](../assets/handwritten/25.jpeg)

</details>

<details>
<summary>图26 P10 的错误推导</summary>

原稿设 `y=(sin x/x)^(1/x²)`，正确写出 `ln y=(1/x²)ln(sin x/x)`。第一处不成立的等号是下一行的 `lim(x→0) ln y = −(1/x³)·(x/sin x)`，之后又写为 0，得到原答 `e⁰=1`。核对结果 [C]：错误发生在取对数后的变形；该跳步的具体问题及合法处理集中在[综合极限讲义](../notes/06-lhopital-and-composite-limits.md)，不推测错误动机。本图没有本人正确修正或实际复测过程，保留原答 1。

![图26 P10 的错误推导](../assets/handwritten/26.jpeg)

</details>

## 尚无完整原题的历史错误 [B]

- 原 M01：乘积求导曾把一个应为正的项写成负号，概要记载后续基础练习改善；未保存该次完整原题，不把图05的正确计算冒充那次修正。
- 原 M04：概要记有 `x⁴−4x³` 一类题的驻点、极值、拐点混淆。图09、10补充了相关计算与真实困惑；两者不能证明所有旧错误已纠正。
- 原 M05：平均斜率 `k` 与中值点 `c` 的混淆现有图16证据；其他区间的正确作答分开保留，不能自动视为同题复测。

原 M03 是整理者的常见风险提示，不是本人错误，说明仅保留在[等价替换讲义](../notes/02-equivalent-infinitesimals.md)。关于隔几天遗忘的原 M08 观察保留在[历史回顾](../history/2026-09-to-10.md)。
