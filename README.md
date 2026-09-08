\# bigdata-ai · 大数据与人工智能课程仓库



个人课程学习仓库，用于记录《大数据与人工智能》课程的学习笔记、代码、实验与配套 AI 资料。



\---



\## 一、仓库作者



\- \*\*GitHub\*\*：\[guoshanyongchun](https://github.com/guoshanyongchun)

\- \*\*邮箱\*\*：3036630975@qq.com

\- \*\*协作 AI 助手\*\*：WorkBuddy



\---



\## 二、仓库用途



本仓库目前承担三件事：



1\. \*\*课程作业与代码实验\*\*：`code/` 存放 Python / 大数据相关代码

2\. \*\*学习笔记\*\*：`notes/` 沉淀读书笔记、课程总结

3\. \*\*AI 配套学习资料\*\*：`learning-materials/` 用 AI 生成的高质量入门概念卡片（HTML + Markdown）



整套资料围绕"零基础入门大数据与人工智能课程"展开 —— 每一份都从最朴素的类比入手，避开代码、强调直觉，目标是把抽象概念"翻译成生活语言"。



\---



\## 三、目录结构



```

bigdata-ai/

├── code/                 # 课程代码与实验

├── data/                 # 数据集（大文件不入库，靠 .gitignore 排除）

├── notes/                # 学习笔记

├── learning-materials/   # AI 生成的概念卡片（HTML / Markdown）

└── README.md             # 当前文件

```



\---



\## 四、Skill 存放路径说明



本仓库关联到一个 WorkBuddy \*\*用户级 Skill\*\*（`concept-learner`），用于按统一流程生成"概念学习卡片"。Skill 文件不在仓库内，而是放在 WorkBuddy 全局配置目录：



| 项 | 路径 |

|---|---|

| \*\*Skill 文件\*\*（用户级） | `C:\\Users\\joyou\\.workbuddy\\skills\\concept-learner\\SKILL.md` |

| \*\*仓库内的学习产出\*\* | `learning-materials/` |



\---



\## 五、如何在 WorkBuddy 中调用它



在任意 WorkBuddy 对话里，通过以下任一方式触发 Skill：



\### 方式 A：直接让 WorkBuddy 加载 Skill



用 Skill 工具加载即可。加载后，Skill 会指导 WorkBuddy 按 "个人解释 / 核心机制 / 应用场景 / 易混淆点 / 资料来源" 等段落生成卡片。



\### 方式 B：自然语言召唤



直接对 WorkBuddy 说：



> "用 concept-learner 给我做一份关于 XX 的学习资料，输出为 HTML，文件名 xx.html。"



WorkBuddy 会按 SKILL.md 的 6 段式模板（适用场景 / 输入信息 / 生成步骤 / 输出结构 / 资料来源 / 自检要求）跑整个流程。



\### 输入参数速查



| 字段 | 默认 | 说明 |

|------|------|------|

| 概念名 | （必填） | 想学的概念 |

| 受众 | 入门 / 零基础 | 决定段落深度 |

| 输出格式 | Markdown | 也可指定 HTML / PDF |

| 文件名 | `<concept>.md` | 也可显式指定 |

| 存放目录 | `learning-materials/` | 已存在的优先 |



\### 调用例子



```

用 concept-learner 生成一份关于 RAG（检索增强生成）的学习资料，

受众=零基础，输出为 HTML，文件名 rag.html，放到 learning-materials/ 目录。

```



\---



\## 六、已生成的资料列表



\### 概念卡片系列（4 份）



| 期数 | 主题 | 文件 | 形式 | 主色 | 状态 |

|------|------|------|------|------|------|

| ① | 什么是 Agent | `learning-materials/agent.html` | HTML | 蓝紫 | ✅ |

| ② | 什么是 LLM Context | `learning-materials/llm-context.html` | HTML | 玫红紫 | ✅ |

| ③ | 什么是 Skill | `learning-materials/skill.html` | HTML | teal | ✅ |

| ④ | 三者协作关系 | `learning-materials/concept-relationship.md` | Markdown | — | ✅ |



\### 辅助资料



| 主题 | 文件 | 备注 |

|------|------|------|

| 区块链入门 | `learning-materials/blockchain.md` | 早期学习笔记，非 concept-learner 生成 |



\### Skill 自身



| 项 | 路径 | 状态 |

|---|---|---|

| concept-learner SKILL.md | `C:\\Users\\joyou\\.workbuddy\\skills\\concept-learner\\SKILL.md` | ✅ 已落盘 |



\---



\## 七、开发环境



\- Python 3.12

\- Git 2.55

\- Visual Studio Code

\- WorkBuddy（AI 助手）



\---



\## 八、学习进度



\- \[x] 环境搭建（Git / Python 3.12 / VS Code）

\- \[x] GitHub 账号注册与仓库创建

\- \[x] 概念卡片 ① — 什么是 Agent

\- \[x] 概念卡片 ② — 什么是 LLM Context

\- \[x] 概念卡片 ③ — 什么是 Skill

\- \[x] 概念卡片 ④ — 三者协作关系（系列总结）

\- \[x] 仓库 README 完善

\- \[ ] 课程学习（持续更新中）

\- \[ ] Skill 上手实践（在 Coze / Dify 上做一个自己的 Skill）







\---



\## 人工核查与修改



本节由本人（guoshanyongchun）填写，记录对 AI 生成内容的修改与原因，便于后续回溯。



\#### 修改记录

Lear ing materials:对Agent,大模型上下文，SKill等的个人解释及其他部分内容做了稍微修改



concept-relationship.md：删除了 Mermaid 流程图，因为流程图对纯文本阅读有干扰，去掉后更简洁。



concept-relationship.md：去掉了所有加粗标记（\*\*），星号在纯文本中显得杂乱，去掉后更干净。



README.md：概念卡片④形式列从"Markdown（Mermaid）"改为"Markdown"，因为流程图已删除，同步更新描述。



\#### 修改原则



类比段落方面，如果 AI 给的类比不够直觉，我会自己重写，优先用生活化的比喻。表格数据方面，核对文件路径、状态标记等事实性内容，确保与实际一致。个人总结方面，AI 写的总结偏模板化，我会用自己的话重新表达。风格偏好方面，偏好生活类比、简洁干净的表达，不要教科书式的说教语气。资料来源方面，优先引用官方文档，至少保留一条可靠来源。





