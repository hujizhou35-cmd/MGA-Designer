# Physical function around a cardiovascular event

**A blind illustration of a published study** · [English home](../README.md) · [简体中文主页](README.zh-CN.md)

Quan Zhou, Zhaoping Wang, Qin Xu, Xue Xia, Meng Gao, Luwen Zhang, Xue Tian, Di He and Anxin Wang studied changes in physical function around the first reported diagnosis of heart disease or stroke. The article appeared in *BMC Public Health* **26**, 2184 (2026). The repository's illustration was made for this educational comparison. [Paper and published graphical abstract](https://doi.org/10.1186/s12889-026-27763-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/42185788/) · [Open full text and supplement](https://pmc.ncbi.nlm.nih.gov/articles/PMC13383399/)

## How to read the independent figure

The study followed **23,307 adults aged 50 or older** without cardiovascular disease (CVD) at baseline. Across ELSA in England, HRS in the United States and CHARLS in China, 4,355 participants reported that a physician had diagnosed heart disease or stroke during follow-up. The cohort counts and event totals come from Table 1.

Frailty was measured through reported difficulties. The seven mobility questions included climbing stairs. The daily-function score combined five activities of daily living (ADL) and five instrumental activities (IADL), including getting dressed and shopping for groceries. Higher scores mean greater difficulty. The two instruments have different ranges, **0–100** for mobility and **0–200** for daily function. The heart and brain identify the conditions included in the study. The staircase and grocery bag illustrate questionnaire items from supplementary Table S1.

| Read from left to right | What is compared | Unit |
| --- | --- | --- |
| Before the event | At baseline, participants who later reported an event compared with those who remained event-free | Difference in score points |
| At diagnosis | The short-term change in level associated with the event in the adjusted longitudinal model | Score points |
| After the event | The change in annual slope relative to the pre-event slope, as defined in the footnotes of Tables 2 and 3 and the model equation | Score points per year |

Each row represents one cohort. The dots or diamonds give the estimates from the CVD rows of Tables 2 and 3. The bars are their 95% confidence intervals. For example, among HRS participants the estimated short-term change was **4.73 mobility points** (95% CI 3.95–5.50) and **5.53 daily-function points** (4.61–6.45). Compare each outcome across time and cohorts while keeping its scoring range in view.

**中文读图说明。** 三个队列合计 23,307 人，入组时均无心血管病，随访期间有 4,355 人报告医生诊断了心脏病或卒中。从左向右看三栏：第一栏比较两组人在入组时的评分；第二栏是模型估计的确诊时短期变化；第三栏是确诊后相对于确诊前，每年的变化速度差了多少。比如，美国 HRS 队列在事件发生时，行动困难评分估计增加 4.73 分（95% 置信区间 3.95–5.50）。分数越高，表示完成活动越困难。

## What went into the design

| Design decision | Reason |
| --- | --- |
| Keep all three cohorts separate, with the same row order in every column. | The paper fits cohort-specific models. A single estimate would imply pooling that the main tables do not report. |
| Use measured points and intervals in three labeled columns. | A baseline difference, a short-term change and a change in annual slope answer different questions. Individual records and full predicted series were not needed to show these reported estimates. |
| Keep the pre-event mobility result in the figure footer. | All three pre-event slope-difference intervals include zero. A baseline gap alone does not establish a faster preceding decline. For daily function, pre-event slope estimates were lower in the eventual-CVD group in ELSA and HRS; the CHARLS interval included zero. |
| Keep the main figure about overall CVD. | The paper also examined heart disease and stroke separately. Estimates and their precision vary by subtype. The detailed angina, heart attack, coronary heart disease and heart failure analyses were available in ELSA and HRS. |
| Leave the adjustment set, subgroup analyses and sensitivity checks in the paper and this note. | The mixed models used repeated scores, person-specific intercepts and slopes, and baseline covariates. The authors examined age, sex and BMI subgroups, alternative inclusion criteria, missing covariates and medication adjustment. These observational estimates do not establish the effect of an intervention. |

**取舍理由。** 三个队列分别建模，所以没有画一个“总体效应”。保留置信区间和事件前的行动能力结果，是为了让读者区分“起点已有差距”和“当时恶化更快”。亚型、分层和敏感性分析放在正文和补充材料中，感兴趣的读者可以继续查看。

Two figures from **other studies** informed the layout. The published graphical abstract of a UK Biobank study places its frailty measurements alongside the cardiac condition under investigation. Here, small illustrations identify the activities behind each score. Its conduction-system anatomy and hazard ratios belong to that study. A *PLOS Medicine* results figure uses a common fall-event marker and repeated outcome rows. Here, the design uses a common event boundary for all three cohorts and reports the coefficients Zhou and colleagues tabulated. [UK Biobank paper and graphical abstract](https://doi.org/10.3389/fcvm.2026.1967667) · [PLOS Medicine, Figure 2](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1005083#pmed-1005083-g002)

## Independent drawing and the published original

The project owner reviewed the independent color sketch, layout and omissions. The original vector illustrations and data marks were then opened through the Illustrator MCP server, organized into seven named layers, saved as AI and exported from Illustrator 2023 (27.5.0). The reopened master has 90 editable text frames. A headline and a data point were selected as native objects. All 18 printed estimates, point positions and 36 interval endpoints in the vector PDF were checked against the publisher’s Tables 2 and 3. The PDF contains no embedded bitmaps. [AI master](media/cvd-frailty.ai?raw=true) · [Vector PDF](media/cvd-frailty.pdf) · [Full-size PNG](media/cvd-frailty.png)

The independent AI, PDF and PNG were frozen in a separate commit before retrieving the publisher’s image. In the original, the event timeline and predicted mobility curve communicate the sequence of change. The independent version devotes more space to the measurements, uncertainty and differences among cohorts. [Independent artwork at the time it was frozen](https://github.com/hujizhou35-cmd/MGA-Designer/commit/2b41589d2804c6061ebeba615195cbce45667db0)

**图像来源与授权。** 左图是本项目独立绘制的教学作品。右图是 Zhou 等人的论文原版，按出版社提供的文件原样展示。原图的许可与技能的 MIT 许可证分开。完整作者名单和论文出处见本页开头。

**Credit for the published image.** “Graphical Abstract” from *Physical function frailty trajectory before and after cardiovascular event among older adults in three multinational cohorts*, © The Author(s) 2026. The publisher-supplied image is shared unchanged for this noncommercial educational comparison. The original is covered by CC BY-NC-ND 4.0 and is excluded from the repository's MIT licence. [Publisher’s original image](https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs12889-026-27763-w/MediaObjects/12889_2026_27763_Figa_HTML.png) · [Article](https://doi.org/10.1186/s12889-026-27763-w) · [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
