# MGA-Designer

**Medical Graphical Abstract Designer** · English | [简体中文](docs/README.zh-CN.md)

Turn a medical manuscript into a graphical abstract you can **open and edit in Adobe Illustrator**. MGA-Designer finds published examples that match your study design. You review the layout, the evidence behind each arrow and the proposed omissions before the skill draws the figure. It uses Illustrator's native shapes, paths and text, then checks the export against the journal's requirements.

[Download the skill](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest) · [Explore the example](docs/demo.md) · [Feedback](https://github.com/hujizhou35-cmd/MGA-Designer/issues)

[![At the plaque shoulder. An arterial cutaway, a magnified endothelial surface, paired tissue profiling and six donor-level comparisons under flow.](docs/media/demo.png)](docs/demo.md)

**At the plaque shoulder.** This entirely fictional study uses eight plaque specimens to illustrate where an endothelial *VCAM1* signal appears. A separate flow-chamber experiment follows six endothelial-cell donors. Each line on the count plot joins the same donor's two conditions. [Inspect the design decisions and synthetic counts](docs/demo.md) · [Download the Illustrator file](docs/media/plaque-atlas.ai?raw=true)

<details>
<summary>Inspect an editable detail</summary>

![Detail from the editable Illustrator artwork](docs/media/editable-detail.png)

</details>

**Tested drawing setup.** On Windows with Illustrator 2023 (27.5.0) and Node.js 24.16.0, the unmodified MCP server 1.10.3 drew a native path and live text on a named layer, saved and reopened the AI file, and exported PNG, SVG and PDF. [Illustrator MCP server](https://github.com/ie3jp/illustrator-mcp-server)

## Choose one download

| File | How to use it |
| --- | --- |
| [Portable SKILL.md](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest/download/SKILL.md) | Give this single file to an assistant that reads Markdown instructions. It includes the reference guides. |
| [Codex skill](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest/download/mga-designer.skill) | Extract this ZIP-format archive into `.agents/skills/mga-designer/` in your project. Rename the downloaded copy to `.zip` first if your extractor requires it. Verify that `SKILL.md` is directly inside the folder. Open a new Codex chat in the project. |
| [Codex plugin](https://github.com/hujizhou35-cmd/MGA-Designer/releases/latest/download/mga-designer-plugin.zip) | Extract the archive into a folder you will keep. Open a terminal there and run the commands below. |

```sh
codex plugin marketplace add .
codex plugin add mga-designer@mga-designer-local
```

For drawing, you need a local, licensed copy of Adobe Illustrator, a compatible desktop host with MCP tools, and the [Illustrator MCP server](https://github.com/ie3jp/illustrator-mcp-server). The skill guides setup and tests a disposable Illustrator document before working on your figure. Internet access is needed to inspect journal requirements and reference figures. With only a Markdown reader, you can still work through the design and approval steps.

## Try it on your manuscript

Attach the manuscript and any results tables it relies on. Name the target journal if you have one. Try this prompt in English or Chinese.

> Use MGA-Designer to plan a graphical abstract for my manuscript. Show me a published example that matches my study design. Explain your choice of layout and what you would leave out. Wait for my approval before drawing.

1. **Check the drawing setup.** Find or install the Illustrator MCP server. Confirm that it can draw, save and reopen objects in a disposable document.
2. **Read the study.** Identify the research question, population or material, methods, main result and conclusion. Match each proposed claim to its source in the manuscript.
3. **Learn from comparable papers.** Inspect graphical abstracts the assistant can actually view. Record the source and explain which reading order or grouping works for this study.
4. **Review the design.** The author sees the content and structure, a separate explanation of the visual form, and a separate list of omissions with reasons. A missing result or uncertain relationship goes back to the author.
5. **Draw, inspect and deliver.** After approval, draw the objects in Illustrator. Reopen the editable source, inspect the export at its intended size, and check the wording, numbers, arrows, clipping and legibility. Deliver the editable master, a preview and the exports supported by the target journal's instructions, with any unresolved checks identified.

## How the study changes the picture

| Study design | A decision the author reviews |
| --- | --- |
| Thematic, comparative or historical review | Should readers follow a set of themes, compare alternatives side by side or trace changes over time? |
| Systematic review or meta-analysis | Which pooled result or synthesis answers the review question, and which uncertainty needs to stay visible? |
| Clinical observational, two- or multi-cohort, or prediction study | Show an association, distinguish the role of each cohort, or separate model development from evaluation. |
| Public omics, omics with experiments, or basic experimental study | Distinguish a computational signal from what was tested experimentally. Give the central comparison and its readout enough space. |
| Bibliometric study | Show what the literature map reveals. A publication trend describes the research field. |

Each route guides the reference search and layout choice. A review may use a radial composition when the themes share a center. A study with parallel analyses may need separate lanes. The manuscript determines which relationships the arrows can support.

## Feedback

Tell us which step was difficult, what you expected and what happened. A small fictional example helps us reproduce an issue. [Open an issue](https://github.com/hujizhou35-cmd/MGA-Designer/issues/new)

MGA-Designer is released under the [MIT License](LICENSE). Adobe Illustrator and the [Illustrator MCP server](https://github.com/ie3jp/illustrator-mcp-server) are separate dependencies.
