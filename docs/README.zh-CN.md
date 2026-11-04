# MGA-Designer

**医学图像摘要设计助手**（Medical Graphical Abstract Designer） · [English](../README.md) | 简体中文

把医学论文画成一张**可以在 Adobe Illustrator 里继续编辑**的图像摘要。MGA-Designer 会先找与你研究设计相近的已发表图像摘要，请你确认读图顺序、每根箭头的证据和准备省略的内容，再用 Illustrator 原生形状、路径和文字逐个绘制图中对象，并按目标期刊要求检查导出文件。

[下载技能](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest) · [查看案例](demo.md) · [反馈问题](https://github.com/hujizhou35-cmd/MGA-Designer/issues)

[![斑块肩部图像摘要。由动脉剖面和内皮局部放大图读到配对组织取材，再读独立流动室中六位供者的配对结果。](media/demo.png)](demo.md)

**斑块肩部。** 这个教学案例完全虚构。组织示意图用八份斑块标本说明内皮 *VCAM1* 信号的位置。独立的体外流动室实验使用另外六位供者的内皮细胞，计数图中每条线连接同一供者在两种条件下的结果。[查看构图取舍与虚构原始计数](demo.md) · [下载 Illustrator 源文件](media/plaque-atlas.ai?raw=true)

<details>
<summary>查看可编辑图稿局部</summary>

![可编辑 Illustrator 图稿的局部细节](media/editable-detail.png)

</details>

**已实测的绘制环境。** 在 Windows、Illustrator 2023（27.5.0）和 Node.js 24.16.0 下，未经修改的 MCP server 1.10.3 成功在命名图层中绘制了原生路径和可编辑文字，保存并重新打开 AI 文件，导出了 PNG、SVG 和 PDF。[Illustrator MCP server 上游项目](https://github.com/ie3jp/illustrator-mcp-server)

## 三个文件选哪一个

| 下载 | 使用方法 |
| --- | --- |
| [单文件 SKILL.md](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest/download/SKILL.md) | 交给能读取 Markdown 指令的助手。所有配套指南都已收在这个文件里。 |
| [Codex 技能包](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest/download/mga-designer.skill) | 将这个 ZIP 格式的压缩包解压到你的项目目录 `.agents/skills/mga-designer/` 下。解压工具无法识别时，可先把下载文件的后缀改成 `.zip`。确认打开该目录就能看到 `SKILL.md`，然后在该项目中新建 Codex 对话。 |
| [Codex 插件包](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest/download/mga-designer-plugin.zip) | 解压到准备保留的文件夹，在该文件夹里打开终端，依次执行下面两条命令。 |

```sh
codex plugin marketplace add .
codex plugin add mga-designer@mga-designer-local
```

实际绘制需要本机已安装并获得授权的 Adobe Illustrator、支持 MCP 工具的桌面助手，以及 [Illustrator MCP server](https://github.com/ie3jp/illustrator-mcp-server)。技能会引导你完成配置，并用临时新文档测试连接。核对期刊规范和查看参考图需要联网。只有 Markdown 阅读功能时，仍可以完成构思和方案确认。

## 用自己的稿件试一次

提供稿件和支撑结果的表格。如果已选好投稿期刊，请附上名称。可以用中文或英文提出请求。

> 用 MGA-Designer 给这篇论文设计图像摘要。先找一张研究设计相近的已发表图像摘要，说清楚为什么这样排版、准备省略哪些内容。等我确认后再画。

1. **检查绘制环境。** 查找或安装 Illustrator MCP server，再用临时新文档实测绘制、保存和重新打开。
2. **读懂研究。** 提取研究问题、研究对象或实验材料、研究方法、主要结果和结论。准备写到图上的每项判断都要能在稿件中找到依据。
3. **看同类论文怎么画。** 打开能实际查看的图像摘要，记下出处，说明其中哪种阅读顺序或分组方式适合这项研究。
4. **让作者看方案。** 分开讲清楚图的结构和内容、为什么选这种形式、准备省略什么以及理由。缺少关键数值或无法判断关系时，先向作者核实。
5. **绘制、检查、交付。** 获得确认后在 Illustrator 中绘制。重新打开可编辑源文件，按实际使用尺寸查看导出图，检查数字、措辞、箭头、裁切和可读性。交付可编辑母版、预览及按目标期刊要求导出的文件，并注明仍需确认的项目。

## 不同研究会怎么画

| 文章类型 | 作者需要确认的构图选择 |
| --- | --- |
| 主题型、对比型或演进型综述 | 是围绕一个主题展开，并列比较几种解释，还是按时间呈现变化？ |
| 系统综述或 Meta 分析 | 哪个汇总结果回答了研究问题？读者还需要看到哪些不确定性？ |
| 临床观察、双队列或多队列、预测模型研究 | 画清观察到的关联、各队列分别回答的问题，或模型开发与评估的区别。 |
| 公共组学数据、组学结合实验、基础实验研究 | 区分数据分析发现的信号与实际验证过的结果，给主要比较和测量结果留出位置。 |
| 文献计量学研究 | 画出文献图谱揭示的领域结构或趋势，并保留这一结论适用的范围。 |

这些分类用于找参考图、决定怎么排。多个主题确实围绕同一中心时，综述可以画成放射状。几项并行分析需要分别解释时，可以分栏。每一根箭头代表什么，要回到稿件中核对。

## 反馈

欢迎说明在哪一步遇到问题、希望得到什么、实际发生了什么。如果能附上一个小型虚构示例，我们更容易复现。[提交 Issue](https://github.com/hujizhou35-cmd/MGA-Designer/issues/new)

MGA-Designer 采用 [MIT 许可证](../LICENSE)。Adobe Illustrator 和 [Illustrator MCP server](https://github.com/ie3jp/illustrator-mcp-server) 是单独安装的依赖。
