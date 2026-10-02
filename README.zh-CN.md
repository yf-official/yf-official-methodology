![Methodology：几何、交互、渲染与验证](assets/methodology.svg)

# Methodology · 方法论论文集

[English](README.md) · 简体中文

**记录工具背后的推导与取舍。** 收录 yf-official 项目相关的方法论论文与技术研究：一个设计问题如何转化为几何模型、编辑流程，以及可以检验的结果。

目前收录 **2 篇英文技术稿**，均发布于 **2026 年 10 月 1 日**。中文页面提供导读，PDF 为英文原稿。各篇论文分别说明已有证据、适用范围和待验证事项。

[论文目录](#论文目录) · [阅读路线](#阅读路线) · [共同方法](docs/methodology.zh-CN.md) · [BibTeX 引用](references.bib) · [参与完善](CONTRIBUTING.zh-CN.md)

## 论文目录

| 论文 | 核心问题 | 研究主题 | 阅读入口 |
| --- | --- | --- | --- |
| **DeckStage** | 如何遵循参考图的几何关系，同时保留原始扑克牌设计？ | 射影几何 · 非破坏性渲染 · 折叠包装 | [中文导读](papers/deckstage/README.zh-CN.md) · [英文 PDF](https://github.com/yf-official/yf-official-methodology/releases/download/paper-2026-10-01/DeckStage_Methodology.pdf) |
| **IconLab** | 如何让交互编辑与不同尺寸的导出共享一致的几何含义？ | 仿射变换 · 撤销事务 · 超采样 | [中文导读](papers/iconlab/README.zh-CN.md) · [英文 PDF](https://github.com/yf-official/yf-official-methodology/releases/download/iconlab-paper-2026-10-01/IconLab-methodology.pdf) |

### 01 / DeckStage

**Reference-Constrained Reconstruction of Playing-Card Mockup Scenes: Geometry, Non-Destructive Rendering, and Validation**<br>
参考约束下的扑克牌展示场景重建：几何、非破坏性渲染与验证（中文译名）<br>
Fox Studio · 22 页 · 英文 · 供设计评审的技术稿

扑克牌场景同时涉及实体尺寸、参考透视、物体遮挡和原始图稿。论文从线族重建出发，连接共享平面单应变换、渲染时裁切、局部圆角蒙版、倾斜扇形牌组和牌盒相机模型，再以不可变图稿图集与折叠图描述包装展开与闭合。

**可借鉴的方法：** 先建立场景模型，再处理外观；保留原始素材；让投影、可见性、拖放命中和导出遵循同一套几何关系。

**证据范围：** 给出了尺寸规格的精确检查和受控的射影／仿射合成实验。参考图的独立配准、应用性能和拟议的渲染验收条件仍需进一步验证。

[展开中文导读 →](papers/deckstage/README.zh-CN.md) · [查看发布版本](https://github.com/yf-official/yf-official-methodology/releases/tag/paper-2026-10-01)

### 02 / IconLab

**A Geometry-Consistent Method for Interactive Icon Composition and Multiresolution Export**<br>
交互式图标合成与多分辨率导出的几何一致性方法（中文译名）<br>
yf-official · 8 页 · 英文 · 技术论文

图标编辑器需要把连续手势连接到离散像素输出。论文区分规范设计状态、显示偏好、即时预览、撤销事务和快照导出，形式化描述坐标反射、仿射变换、渐变与采样，并指出原生实现基线中尚未解决的差异。

**可借鉴的方法：** 让预览与导出共享几何语义；编辑时即时反馈；以有意义的操作提交撤销记录；从同一份冻结状态分别渲染各个目标尺寸。

**证据范围：** 给出了合成覆盖率实验和 30,000 次坐标检查，尚未测量原生渲染器的逐像素一致性、交互延迟或审美收益。

[展开中文导读 →](papers/iconlab/README.zh-CN.md) · [项目源码](https://github.com/yf-official/IconLab) · [查看发布版本](https://github.com/yf-official/yf-official-methodology/releases/tag/iconlab-paper-2026-10-01)

## 阅读路线

| 你关心的问题 | 建议先读 | 再连接到 |
| --- | --- | --- |
| 从参考图重建场景 | DeckStage 第 IV–V 节：线族与平面估计 | 第 VIII–IX 节：相机先验与折叠包装 |
| 渲染中保持图稿完整 | DeckStage 第 VI 节：物理裁切与局部蒙版 | IconLab 第 III–IV 节：连续底板、变换与合成 |
| 做好编辑器交互 | IconLab 第 V 节：即时更新与撤销事务 | DeckStage 第 XI 节：直接分配素材与场景状态 |
| 多尺寸、高质量导出 | IconLab 第 VI 节：快照导出与采样 | DeckStage 第 XII 节：输出尺寸与原始素材重渲染 |
| 判断技术结论是否充分 | IconLab 第 VII–VIII 节：合成实验与局限 | DeckStage 第 XIII–XIV 节：证据分类与验证约定 |

想先了解整体思路，可以阅读[共同方法导览](docs/methodology.zh-CN.md)。每篇导读都提供章节地图、已报告的结果和开放问题。

## 阅读、引用与复用

- **阅读：** 导读用于定位问题；公式、图表与完整论证以对应版本的 PDF 为准。
- **引用：** 使用单篇论文的作者、完整标题、年份和发布链接，可直接复制 [references.bib](references.bib)。本仓库没有为论文指定 DOI 或发表期刊／会议。
- **复用：** 按单篇论文确认权利。DeckStage 明确保留所有权利，转载需许可；IconLab 发布页没有声明复用许可。公开可读不等于获得复用授权。
- **扩充：** 按[贡献指南](CONTRIBUTING.zh-CN.md)和[论文导读模板](templates/paper-notes.md)新增条目，元数据统一记录在 [catalog.json](catalog.json)。

## 仓库结构

```text
papers/          双语论文导读、章节地图与证据边界
docs/            跨项目的方法联系
assets/          仓库视觉素材
templates/       新论文的导读模板
catalog.json     结构化出版信息
references.bib   单篇论文的引用条目
scripts/         目录与本地链接检查
```

PDF 保留在带版本的 GitHub Releases 中。导读独立维护，不替代或修改已发布的论文原稿。

## 后续完善方向

- 新项目有可供评审的论文后，再按同样的双语导读与元数据结构收录。
- 作者公开复现脚本和数据后，补充对应链接；当前仓库提供论文与导读。
- 修订稿使用新的发布版本，并记录论证与实验的变化。

发现失效链接、事实错误或需要补充的说明，可以[提交 Issue](https://github.com/yf-official/yf-official-methodology/issues/new/choose)，注明论文、章节及建议修改内容。
