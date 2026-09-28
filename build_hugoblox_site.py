import os
import json
import csv

BASE = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

# Ensure layout and asset directories
directories = [
    os.path.join(BASE, "content", "posts", "jichang-tuijian"),
    os.path.join(BASE, "content", "posts", "jiaocheng"),
    os.path.join(BASE, "content", "posts", "pingce"),
    os.path.join(BASE, "content", "posts", "faq"),
    os.path.join(BASE, "content", "posts", "daohang"),
    os.path.join(BASE, "docs"),
    os.path.join(BASE, "layouts", "_default"),
    os.path.join(BASE, "layouts", "partials"),
    os.path.join(BASE, "static", "css"),
]

for d in directories:
    os.makedirs(d, exist_ok=True)

tg_channel = "https://t.me/+uVUK4-hZhZZjYzk9"

# 1. Header partial
header_html = """
<header class="sticky top-0 z-50 bg-slate-900/95 backdrop-blur border-b border-slate-800 text-white shadow-lg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
    <div class="flex items-center space-x-3">
      <a href="/" class="flex items-center space-x-2 text-xl font-bold bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 bg-clip-text text-transparent">
        <svg class="w-7 h-7 text-blue-500 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        <span>机场稳定网</span>
      </a>
      <span class="hidden md:inline-block text-xs px-2.5 py-0.5 rounded-full bg-blue-900/60 text-blue-300 border border-blue-700/50">2026高稳定性梯子首选</span>
    </div>
    
    <nav class="hidden md:flex items-center space-x-6 text-sm font-medium">
      <a href="/" class="hover:text-blue-400 transition-colors">首页</a>
      <a href="/posts/jichang-tuijian/" class="hover:text-blue-400 transition-colors">稳定机场推荐</a>
      <a href="/posts/jiaocheng/" class="hover:text-blue-400 transition-colors">客户端教程</a>
      <a href="/posts/pingce/" class="hover:text-blue-400 transition-colors">专线与晚高峰评测</a>
      <a href="/posts/faq/" class="hover:text-blue-400 transition-colors">小白新手答疑</a>
      <a href="/posts/daohang/" class="hover:text-blue-400 transition-colors">防失联与导航</a>
      <a href="/posts/jichang-tuijian/all-airports-guide/" class="text-amber-400 hover:text-amber-300 font-semibold transition-colors">所有机场注册</a>
    </nav>

    <div class="flex items-center space-x-4">
      <a href="https://t.me/+uVUK4-hZhZZjYzk9" target="_blank" rel="sponsored nofollow noopener" class="hidden sm:inline-flex items-center space-x-1.5 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white text-xs font-semibold px-3.5 py-2 rounded-full shadow-md transition-all">
        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.56 8.16l-1.97 9.27c-.15.68-.55.84-1.12.52l-3.01-2.22-1.45 1.4c-.16.16-.3.3-.61.3l.22-3.05 5.56-5.02c.24-.22-.05-.34-.37-.13l-6.87 4.33-2.96-.92c-.64-.2-.65-.64.13-.95l11.57-4.46c.53-.19 1 .13.88.93z"/></svg>
        <span>TG 交流频道</span>
      </a>
    </div>
  </div>
</header>
"""
with open(os.path.join(BASE, "layouts", "partials", "header.html"), "w", encoding="utf-8") as f:
    f.write(header_html)

# 2. Footer partial
footer_html = """
<footer class="bg-slate-950 text-slate-400 text-sm border-t border-slate-900 py-12 mt-16">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-3 gap-8">
    <div>
      <h3 class="text-white text-base font-bold mb-3 flex items-center space-x-2">
        <span>机场稳定网</span>
      </h3>
      <p class="text-xs leading-relaxed text-slate-400">
        专注2026年高稳定性梯子推荐、晚高峰不卡顿IPLC专线机场评测、全平台客户端配置教程（Windows/macOS/iOS/Android/软路由）与防失联订阅更新维护。
      </p>
    </div>
    
    <div>
      <h4 class="text-white text-sm font-semibold mb-3">核心导航板块</h4>
      <ul class="space-y-2 text-xs">
        <li><a href="/posts/jichang-tuijian/" class="hover:text-blue-400">稳定机场推荐 (晚高峰4K秒开)</a></li>
        <li><a href="/posts/jiaocheng/" class="hover:text-blue-400">科学上网客户端教程 (Clash / 小火箭)</a></li>
        <li><a href="/posts/pingce/" class="hover:text-blue-400">专线与晚高峰评测 (IPLC vs BGP)</a></li>
        <li><a href="/posts/faq/" class="hover:text-blue-400">小白新手答疑 (节点超时排查)</a></li>
      </ul>
    </div>
    
    <div>
      <h4 class="text-white text-sm font-semibold mb-3">防失联社区与免责声明</h4>
      <p class="text-xs leading-relaxed mb-3">
        官方 Telegram 交流频道：<a href="https://t.me/+uVUK4-hZhZZjYzk9" target="_blank" rel="sponsored nofollow noopener" class="text-cyan-400 underline font-semibold">https://t.me/+uVUK4-hZhZZjYzk9</a>
      </p>
      <p class="text-xs text-slate-500">
        © 2026 机场稳定网. 本站为非商业网络技术评测博客，所有推荐仅供合规跨境办公与学术交流。
      </p>
    </div>
  </div>
</footer>
"""
with open(os.path.join(BASE, "layouts", "partials", "footer.html"), "w", encoding="utf-8") as f:
    f.write(footer_html)

# 3. Index layout (layouts/index.html) - Chinese category names & Hugo reference date format 2006-01-02
index_html = """
<!DOCTYPE html>
<html lang="zh-cn" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ .Site.Title }}</title>
  <meta name="description" content="{{ .Site.Params.description }}">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">

  {{ partial "header.html" . }}

  <main class="flex-grow">
    <!-- Hero Module -->
    <section class="relative overflow-hidden bg-gradient-to-b from-slate-900 via-indigo-950 to-slate-900 py-16 sm:py-24 border-b border-slate-800/80">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <span class="inline-flex items-center px-4 py-1.5 rounded-full text-xs font-semibold bg-blue-500/10 text-blue-400 border border-blue-500/20 mb-6">
          🔥 2026年高稳定性梯子首选 · 晚高峰4K流畅不卡顿 · 全天候抗封锁专线
        </span>
        
        <h1 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-tight max-w-4xl mx-auto">
          2026稳定机场推荐：<span class="bg-gradient-to-r from-blue-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">晚高峰4K不卡顿</span>、全天候抗封锁专线梯子与小白配置教程
        </h1>
        
        <p class="mt-6 text-base sm:text-lg text-slate-300 max-w-3xl mx-auto leading-relaxed">
          围绕域名品牌 <strong class="text-white">机场稳定网</strong>，面向科学上网零基础小白与进阶玩家，提供极速稳定的 IPLC/IEPL 专线梯子节点测评、全平台客户端（Clash Verge / Shadowrocket / Sing-box）一键导入教程与防失联订阅维护。
        </p>

        <div class="mt-10 flex flex-wrap justify-center gap-4">
          <a href="/posts/jichang-tuijian/all-airports-guide/" class="px-7 py-3.5 rounded-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white shadow-lg shadow-blue-500/25 transition-all text-sm">
            🚀 查看28家稳定机场注册大全
          </a>
          <a href="https://t.me/+uVUK4-hZhZZjYzk9" target="_blank" rel="sponsored nofollow noopener" class="px-7 py-3.5 rounded-xl font-bold bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 transition-all text-sm flex items-center space-x-2">
            <i class="fab fa-telegram-plane"></i>
            <span>加入官方 TG 防失联频道</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Top 4 Primary Airports Comparison Cards Blox -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
      <div class="text-center mb-12">
        <h2 class="text-2xl sm:text-3xl font-bold text-white">🏆 2026年度四大高稳定性机场榜单（编辑部重磅推荐）</h2>
        <p class="text-slate-400 text-sm mt-2">晚高峰零丢包、IPLC专线中转、全平台客户端一键订阅导入</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Rank 1 -->
        <div class="bg-gradient-to-b from-slate-800 to-slate-900 border-2 border-red-500/80 rounded-2xl p-6 relative shadow-xl hover:border-red-500 transition-all">
          <span class="absolute -top-3 right-4 bg-red-600 text-white text-xs font-black px-3 py-1 rounded-full shadow">第1名 稳定性冠军</span>
          <h3 class="text-xl font-bold text-white mb-2">灵动云</h3>
          <p class="text-xs text-red-400 font-semibold mb-3">原生IPLC专线 + BGP中转</p>
          <ul class="text-xs text-slate-300 space-y-2 mb-6">
            <li>✓ 晚高峰4K超清秒开</li>
            <li>✓ 解锁 ChatGPT / Claude / Netflix</li>
            <li>✓ 丢包率趋于0%，全天候高抗封</li>
          </ul>
          <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" class="block w-full text-center py-2.5 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold text-xs shadow-md transition-all">
            👉 官方直达入口：前往【灵动云】开通
          </a>
        </div>

        <!-- Rank 2 -->
        <div class="bg-gradient-to-b from-slate-800 to-slate-900 border-2 border-blue-500/80 rounded-2xl p-6 relative shadow-xl hover:border-blue-500 transition-all">
          <span class="absolute -top-3 right-4 bg-blue-600 text-white text-xs font-black px-3 py-1 rounded-full shadow">第2名 影音办公</span>
          <h3 class="text-xl font-bold text-white mb-2">暮光网络</h3>
          <p class="text-xs text-blue-400 font-semibold mb-3">IEPL企业级全专线中转</p>
          <ul class="text-xs text-slate-300 space-y-2 mb-6">
            <li>✓ 晚高峰大带宽不限速</li>
            <li>✓ 多端一键订阅，外贸办公首选</li>
            <li>✓ 支持全流媒体与高画质视频</li>
          </ul>
          <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" class="block w-full text-center py-2.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-md transition-all">
            👉 官方直达入口：前往【暮光网络】开通
          </a>
        </div>

        <!-- Rank 3 -->
        <div class="bg-gradient-to-b from-slate-800 to-slate-900 border-2 border-emerald-500/80 rounded-2xl p-6 relative shadow-xl hover:border-emerald-500 transition-all">
          <span class="absolute -top-3 right-4 bg-emerald-600 text-white text-xs font-black px-3 py-1 rounded-full shadow">第3名 老牌高口碑</span>
          <h3 class="text-xl font-bold text-white mb-2">飞猫云</h3>
          <p class="text-xs text-emerald-400 font-semibold mb-3">老牌稳定梯子 · 不限设备数</p>
          <ul class="text-xs text-slate-300 space-y-2 mb-6">
            <li>✓ 运营多年，超级抗敏感期封锁</li>
            <li>✓ 支持多设备协同并发使用</li>
            <li>✓ IPLC内网专线保障，高性价比</li>
          </ul>
          <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" class="block w-full text-center py-2.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md transition-all">
            👉 官方直达入口：前往【飞猫云】开通
          </a>
        </div>

        <!-- Rank 4 -->
        <div class="bg-gradient-to-b from-slate-800 to-slate-900 border-2 border-purple-500/80 rounded-2xl p-6 relative shadow-xl hover:border-purple-500 transition-all">
          <span class="absolute -top-3 right-4 bg-purple-600 text-white text-xs font-black px-3 py-1 rounded-full shadow">第4名 极速备用</span>
          <h3 class="text-xl font-bold text-white mb-2">微风网络</h3>
          <p class="text-xs text-purple-400 font-semibold mb-3">极速轻量 · 便宜月付/年付</p>
          <ul class="text-xs text-slate-300 space-y-2 mb-6">
            <li>✓ 极速切线，低门槛防失联备用</li>
            <li>✓ 节点维护迅速，断连自动切线</li>
            <li>✓ 适合小白入门与便宜替代方案</li>
          </ul>
          <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" class="block w-full text-center py-2.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs shadow-md transition-all">
            👉 官方直达入口：前往【微风网络】开通
          </a>
        </div>
      </div>
    </section>

    <!-- Articles Blox with Chinese Category Display & Correct Date -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 border-t border-slate-800">
      <div class="flex items-center justify-between mb-8">
        <h2 class="text-2xl font-bold text-white">📚 最新稳定机场评测与科学上网教程</h2>
        <a href="/posts/jichang-tuijian/" class="text-xs font-semibold text-blue-400 hover:underline">查看全部文章 →</a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {{ range first 6 (where .Site.RegularPages "Section" "posts") }}
        <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-5 hover:border-blue-500/50 transition-all flex flex-col justify-between">
          <div>
            <span class="text-xs text-blue-400 font-bold uppercase tracking-wider block mb-2">
              {{ if isSet .Params "categories_name" }}{{ .Params.categories_name }}{{ else if .Params.categories }}{{ delimit .Params.categories ", " }}{{ else }}稳定机场推荐{{ end }}
            </span>
            <h3 class="text-base font-bold text-white hover:text-blue-300 mb-2 leading-snug">
              <a href="{{ .RelPermalink }}">{{ .Title }}</a>
            </h3>
            <p class="text-xs text-slate-400 line-clamp-2 leading-relaxed">{{ .Description }}</p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-700/40 flex items-center justify-between text-xs text-slate-500">
            <span>{{ .Date.Format "2006-01-02" }}</span>
            <a href="{{ .RelPermalink }}" class="text-blue-400 hover:underline">阅读全文 →</a>
          </div>
        </div>
        {{ end }}
      </div>
    </section>
  </main>

  {{ partial "footer.html" . }}

</body>
</html>
"""
with open(os.path.join(BASE, "layouts", "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# 4. Single article view layout (layouts/_default/single.html)
single_html = """
<!DOCTYPE html>
<html lang="zh-cn" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ .Title }} - {{ .Site.Title }}</title>
  <meta name="description" content="{{ .Description }}">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">

  {{ partial "header.html" . }}

  <main class="flex-grow max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 w-full">
    <article class="prose prose-invert lg:prose-lg max-w-none">
      <header class="mb-8 pb-6 border-b border-slate-800">
        <h1 class="text-2xl sm:text-4xl font-extrabold text-white leading-tight mb-4">{{ .Title }}</h1>
        <div class="flex items-center space-x-4 text-xs text-slate-400">
          <span>发布时间：{{ .Date.Format "2006-01-02" }}</span>
          <span>分类：{{ if isSet .Params "categories_name" }}{{ .Params.categories_name }}{{ else if .Params.categories }}{{ delimit .Params.categories ", " }}{{ else }}网站公告{{ end }}</span>
          <span>品牌：机场稳定网</span>
        </div>
      </header>

      <div class="text-slate-200 leading-relaxed space-y-6">
        {{ .Content }}
      </div>
    </article>
  </main>

  {{ partial "footer.html" . }}

</body>
</html>
"""
with open(os.path.join(BASE, "layouts", "_default", "single.html"), "w", encoding="utf-8") as f:
    f.write(single_html)

# 5. List view layout (layouts/_default/list.html)
list_html = """
<!DOCTYPE html>
<html lang="zh-cn" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ .Title }} - {{ .Site.Title }}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">

  {{ partial "header.html" . }}

  <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 w-full">
    <div class="mb-10">
      <h1 class="text-3xl font-extrabold text-white mb-2">{{ .Title }}</h1>
      <p class="text-slate-400 text-sm">机场稳定网 精选相关分类测评与教程</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {{ range .Pages }}
      <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-5 hover:border-blue-500/50 transition-all flex flex-col justify-between">
        <div>
          <span class="text-xs text-blue-400 font-bold uppercase tracking-wider block mb-2">
            {{ if isSet .Params "categories_name" }}{{ .Params.categories_name }}{{ else if .Params.categories }}{{ delimit .Params.categories ", " }}{{ else }}稳定机场推荐{{ end }}
          </span>
          <h2 class="text-lg font-bold text-white hover:text-blue-300 mb-2 leading-snug">
            <a href="{{ .RelPermalink }}">{{ .Title }}</a>
          </h2>
          <p class="text-xs text-slate-400 line-clamp-3 leading-relaxed">{{ .Description }}</p>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-700/40 flex items-center justify-between text-xs text-slate-500">
          <span>{{ .Date.Format "2006-01-02" }}</span>
          <a href="{{ .RelPermalink }}" class="text-blue-400 hover:underline">阅读全文 →</a>
        </div>
      </div>
      {{ end }}
    </div>
  </main>

  {{ partial "footer.html" . }}

</body>
</html>
"""
with open(os.path.join(BASE, "layouts", "_default", "list.html"), "w", encoding="utf-8") as f:
    f.write(list_html)

print("Hugo Blox - Tailwind layout templates updated with safe category and date handling!")
