# DeckStage · 论文导读

[English](README.md) · 简体中文 · [返回论文集](../../README.zh-CN.md)

## 出版信息

**Reference-Constrained Reconstruction of Playing-Card Mockup Scenes: Geometry, Non-Destructive Rendering, and Validation**<br>
参考约束下的扑克牌展示场景重建：几何、非破坏性渲染与验证（中文译名）

| 项目 | 信息 |
| --- | --- |
| 作者 | Fox Studio |
| 发布日期 | 2026 年 10 月 1 日 |
| 形式 | 供设计评审的英文技术稿，22 页 |
| 发布版本 | `paper-2026-10-01` |
| 主题 | 射影几何、不可变图稿、扇形牌组、遮挡、相机先验、折叠包装 |

[阅读英文 PDF](https://github.com/yf-official/yf-official-methodology/releases/download/paper-2026-10-01/DeckStage_Methodology.pdf) · [发布说明](https://github.com/yf-official/yf-official-methodology/releases/tag/paper-2026-10-01) · [BibTeX](../../references.bib)

本页是已发布技术稿的导读，不是独立论文，也不表示文中提出的系统已经完成实现。

## 论文解决什么问题

一个可信的样机图必须同时满足两类约束：场景遵循参考构图，原始设计保持完整。逐张旋转矩形可能看起来接近，却丢失共同透视；重新绘制素材可能保留场景外观，却改变文字、花色或设计细节。

论文将展示图视为输入图像不可变的几何场景，把采样、物理裁切、蒙版、投影、光照和合成明确为作用于原始素材的操作。

## 五个关键步骤

1. **恢复支撑平面。** 拟合两组构造线，明确线条配对，恢复交点，用同一个单应变换生成重复牌阵。检查整个视场的残差，不能只看中心单元是否吻合。
2. **区分图稿尺寸与成品尺寸。** 67 × 90 mm 图稿在渲染时按归一化比例裁成 63 × 88 mm 牌面，即左右各去除 2 mm、上下各去除 1 mm；不拉伸设计，也不覆盖源文件。
3. **在局部空间定义边界和姿态。** 圆角随牌面一起投影。扇形重建区分真实裁切边、印刷边、整体轮廓和推断的隐藏边界，再用倾斜相机、有限层间距和可见性决定最终露出的区域。
4. **让牌盒共享相机。** 六面盒体使用明确的尺寸与相机内参先验。包装扩展将一张不可变图集划分为面板，用随父面移动的刚性铰链连接，并明确缺口、插舌和厚度假设。
5. **让交互和导出使用同一模型。** 拖放分配通过逆映射和可见物体归属确定接收目标；导出按目标尺寸从源图稿重新渲染，并声明透明度、颜色和阴影规则。

## 章节地图

| 章节 | 阅读重点 |
| --- | --- |
| I–III | 研究范围、坐标系统与场景约定 |
| IV–V | 线条提取、共享平面估计与残差控制 |
| VI–VII | 物理裁切、圆角蒙版、扇形重建与遮挡 |
| VIII–IX | 共享牌盒相机与单图集折叠包装 |
| X–XII | 渲染、直接分配素材、模板状态与导出 |
| XIII–XIV | 可复现评估、验收目标与局限 |
| XV | 最终构建方案与实现前的决策 |

## 已有证据说明了什么

物理裁切是给定尺寸的精确推导。例如，670 × 900 像素图稿保留 630 × 880 像素区域，左右各裁 20 像素、上下各裁 10 像素。尺寸算对，并不能单独证明渲染器的方向处理和源文件保护正确。

合成几何实验使用固定随机种子，**每个噪声水平 200 次试验**，拟合四个受扰动角点，并检查 **100 个内部留出点**。在 **1 px 角点噪声**下，表 VII 报告射影模型的平均留出 RMSE 为 **1.041 px**，仿射近似为 **10.243 px**；单位基于 1600 像素的参考坐标系。

这些结果说明指定合成几何中的模型失配，不是独立标注的真实参考图精度，也不是应用性能数据。表 VIII 中的渲染和交互通过条件是拟议的验收目标。

## 实现时需要继续验证

- 用独立标注明确外围线条配对与牌间间隙。
- 解释恢复的三维姿态前，声明相机先验与厚度假设。
- 检查不对称面纹理、源字节不变性、裁切方向、透明边缘和拖放深度归属。
- 用实物包装复核插舌可见范围、插入间隙和刚性折叠假设。
- 实现后在注明的硬件上测量导出耗时与峰值内存。

论文提及配套数值材料，但当前发布版本只附带 PDF。本论文集尚未提供可直接运行的复现材料包。

## 复制引用

Fox Studio. *Reference-Constrained Reconstruction of Playing-Card Mockup Scenes: Geometry, Non-Destructive Rendering, and Validation*. 供设计评审的技术稿，2026。发布版本 `paper-2026-10-01`。BibTeX 键：`foxstudio2026deckstage`。

```bibtex
@misc{foxstudio2026deckstage,
  author       = {{Fox Studio}},
  title        = {Reference-Constrained Reconstruction of Playing-Card Mockup Scenes: Geometry, Non-Destructive Rendering, and Validation},
  year         = {2026},
  month        = oct,
  howpublished = {Technical manuscript for design review, GitHub Releases},
  url          = {https://github.com/yf-official/yf-official-methodology/releases/tag/paper-2026-10-01},
  note         = {English manuscript, 22 pages. Published October 1, 2026. Release paper-2026-10-01}
}
```

## 权利说明

原稿声明 © 2026 Fox Studio，保留所有权利，转载需许可。分享时请使用官方发布链接。
