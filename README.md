# 智能体PPT (PPT Agent)

AI 驱动的 PPT 草稿生成器，基于 Streamlit 构建。

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-orange)

## 功能

- **主题输入**：输入 PPT 主题，AI 自动生成内容
- **页数控制**：指定 PPT 页数
- **风格设定**：自定义 PPT 制作风格
- **目标任务**：明确 PPT 的目标用途
- **创造性调节**：滑块控制内容创造性（0.0-2.0）

## 项目结构

```
├── streamlit.py          # Web 前端入口
├── utils.py              # PPT 生成核心逻辑
├── app_launcher.py       # 应用启动器
├── requirements.txt      # Python 依赖
├── PPTAgent.spec         # PyInstaller 打包配置（单文件）
├── PPTAgentDir.spec      # PyInstaller 打包配置（目录）
└── build_pyinstaller.ps1 # 打包脚本
```

## 安装

```bash
git clone https://github.com/RomanCohort/ppt-agent.git
cd ppt-agent
pip install -r requirements.txt
```

## 运行

```bash
streamlit run streamlit.py
```

## 打包

```powershell
# 使用 PyInstaller 打包
python build_pyinstaller.ps1
```

## 配置

运行后在界面中输入 API Key（通过 utils.py 配置）。

## 许可证

MIT License
