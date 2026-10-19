# -*- coding: utf-8 -*-
from pathlib import Path
import html, shutil
root=Path(__file__).resolve().parents[1]
site=root/'_site';site.mkdir(exist_ok=True)
reports=root/'reports'
(site/'reports').mkdir(exist_ok=True)
files=sorted(reports.glob('*.html'),reverse=True)
for p in reports.iterdir():
 if p.suffix in {'.html','.md'}:shutil.copy2(p,site/'reports'/p.name)
items=[]
for p in files:
 name=html.escape(p.stem); url='reports/'+html.escape(p.name,quote=True)
 md=p.with_suffix('.md')
 items.append(f'<article><time>{name[:10]}</time><h2><a href="{url}">{name}</a></h2><p><a href="{url}">阅读日报 →</a>'+ (f' <span>·</span> <a href="reports/{html.escape(md.name,quote=True)}" download>Markdown</a>' if md.exists() else '')+'</p></article>')
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>技术日报 · 阅读归档</title><style>*{box-sizing:border-box}body{margin:0;background:#fdfcf9;color:#292d29;font:15px/1.9 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif}main{max-width:740px;margin:70px auto;padding:0 26px}small,time,footer{font-size:12px;color:#969b91}h1{font-size:32px;font-weight:600;margin:12px 0}header p{color:#858d80}header{padding-bottom:36px;border-bottom:1px solid #e4e8df}article{padding:32px 0;border-bottom:1px solid #e4e8df}h2{font-size:20px;font-weight:500;margin:8px 0}a{color:inherit;text-decoration:none}a:hover{text-decoration:underline}article p{font-size:12px;color:#667d69}span{padding:0 12px;color:#b4b8af}footer{margin-top:44px}@media(max-width:600px){main{margin:32px auto}h1{font-size:27px}h2{font-size:18px}}</style></head><body><main><header><small>DAILY NOTES / 技术与阅读</small><h1>技术日报</h1><p>每天一点新知，留一份可回看的记录。</p></header>'''+''.join(items)+'''<footer>前端 · 系统架构 · Rust · 人工智能 · 开源与工具</footer></main></body></html>'''
(site/'index.html').write_text(page,encoding='utf-8');(site/'.nojekyll').touch()
assert files, 'No HTML reports'
print(f'Built {len(files)} reports')
