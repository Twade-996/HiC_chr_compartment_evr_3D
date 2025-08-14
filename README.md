## HiC_chromosome_evr_3D
From hic data to chromosome 3D dynamic models

## 致谢 (Acknowledgments)

本研究的实现离不开以下优秀的开源软件和公开数据集的支持。我们对所有开发者、贡献者及数据提供方表示最诚挚的感谢。

### 数据来源

*   **NCBI GEO: GSE63525**: 本项目所使用的 Hi-C 数据集来源于 Rao 等人于 2014 年发表在 *Cell* 上的研究。此数据集是本项目分析工作的基石。
    *   **访问链接**: [GEO Accession GSE63525](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525)
    *   **主要出版物**: Rao, S. S. P., Huntley, M. H., Durand, N. C., et al. (2014). A 3D map of the human genome at kilobase resolution reveals principles of chromatin looping. *Cell*, *159*(7), 1665-1680.

### 核心分析软件

*   **Juicer**: 由 Aiden Lab 开发的一站式 Hi-C 数据处理流程，用于将原始测序数据生成互作矩阵。
    *   **许可证**: MIT License (但商业用途可能需要额外许可，请查阅官网)
    *   **GitHub**: [aidenlab/juicer](https://github.com/aidenlab/juicer)
    *   **引用**: Durand, N. C., et al. (2016). Juicer provides a one-click system for analyzing loop-resolution Hi-C experiments. *Cell systems*, *3*(1), 95-98.

*   **HiCExplorer**: 一套功能强大的 Hi-C 数据分析和可视化工具集，本项目使用其进行矩阵校正、TAD 识别和 A/B 室分析。 [1, 2, 4, 5]
    *   **许可证**: GPL-3.0 license. [1]
    *   **GitHub**: [deeptools/HiCExplorer](https://github.com/deeptools/HiCExplorer)
    *   **引用**: Ramirez, F., et al. (2018). Galaxy HiCExplorer: a web server for reproducible Hi-C data analysis, quality control and visualization. *Nucleic acids research*, *46*(W1), W11-W16. [12]

*   **CscoreTool**: 用于 Hi-C 数据 A/B 区室分析的工具。 [10]
    *   **许可证**: 未明确指定 (请参考仓库说明或联系作者)
    *   **GitHub**: [scoutzxb/CscoreTool](https://github.com/scoutzxb/CscoreTool)
    *   **引用**: 请引用其 GitHub 仓库链接或相关出版物。

*   **EVR (Error-Vector Resultant)**: 用于从互作数据中进行染色质三维结构重建的工具。
    *   **许可证**: MIT License
    *   **GitHub**: [mbglab/EVR](https://github.com/mbglab/EVR)
    *   **引用**: 请引用其 GitHub 仓库链接或相关出版物。
