import os

BASE = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

# 1. Write custom 404.html template in layouts/404.html
layout_404 = """
<!DOCTYPE html>
<html lang="zh-cn" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>页面未找到 - {{ .Site.Title }}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col justify-between font-sans">
  {{ partial "header.html" . }}

  <main class="flex-grow max-w-xl mx-auto px-4 py-20 text-center flex flex-col items-center justify-center">
    <div class="text-7xl font-black text-blue-500 mb-4 tracking-wider">404</div>
    <h1 class="text-2xl font-bold text-white mb-3">抱歉，您要查找的页面不存在或已重定向</h1>
    <p class="text-slate-400 text-sm mb-8 leading-relaxed">
      您访问的链接可能已被更新。欢迎返回首页查看2026最新高稳定性机场推荐与教程。
    </p>
    <div class="flex space-x-4">
      <a href="/" class="px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-lg transition-all">
        🏠 返回首页
      </a>
      <a href="/posts/jichang-tuijian/all-airports-guide/" class="px-6 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-blue-300 font-bold text-xs border border-slate-700 transition-all">
        🚀 28家机场注册大全
      </a>
    </div>
  </main>

  {{ partial "footer.html" . }}
</body>
</html>
"""
with open(os.path.join(BASE, "layouts", "404.html"), "w", encoding="utf-8") as f:
    f.write(layout_404)

# 2. Section _index.md creator
sections_info = [
    ("content/posts/_index.md", "全部文章与评测教程", "机场稳定网 (jcwending.homes) 汇总所有梯子推荐、客户端教程与评测。"),
    ("content/posts/jichang-tuijian/_index.md", "稳定机场推荐", "2026高稳定性梯子首选、晚高峰4K不卡顿IPLC/IEPL专线机场推荐。"),
    ("content/posts/jiaocheng/_index.md", "客户端教程", "Windows / macOS / iPhone / Android / 软路由科学上网客户端配置教程。"),
    ("content/posts/pingce/_index.md", "专线与晚高峰评测", "机场测速评测、IPLC专线抗封锁机制与晚高峰丢包延迟测试。"),
    ("content/posts/faq/_index.md", "小白新手答疑", "魔法上网入门解惑、节点超时排查、订阅更新失败与解锁解答。"),
    ("content/posts/daohang/_index.md", "防失联与导航", "机场稳定网防失联发布页、永久有效镜像与客户端官方下载导航。")
]

for rel_path, title, desc in sections_info:
    full_path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    content = f"""---
title: "{title}"
date: 2026-09-28
draft: false
description: "{desc}"
---
"""
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Section _index.md files and custom 404.html created successfully!")
