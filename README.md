# 技术日报

极简风格的技术订阅日报，每次保存 HTML 阅读版与 Markdown 文档。

- `reports/`：按日期保存的日报。
- `scripts/build_site.py`：仅用 Python 标准库生成归档首页及发布目录 `_site/`。
- `.github/workflows/pages.yml`：推送到 main 后自动部署 GitHub Pages。

本地生成：`python3 scripts/build_site.py`，然后浏览 `_site/index.html`。

GitHub 仓库 Settings → Pages → Source 设置为 GitHub Actions。
公开站点会展示 reports 内的日报内容；首次启用前确认仓库套餐支持 Pages。
