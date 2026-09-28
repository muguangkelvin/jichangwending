import os

BASE = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

# Modern Hugo Blox Tailwind single article layout
modern_single_html = """<!DOCTYPE html>
<html lang="zh-cn" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ .Title }} - {{ .Site.Title }}</title>
  <meta name="description" content="{{ .Description }}">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    svg, i.fab, i.fas, i.fa {
      max-width: 20px !important;
      max-height: 20px !important;
      vertical-align: middle;
    }
    /* Table Styling for Markdown tables */
    .prose table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 2rem 0;
      border-radius: 0.75rem;
      overflow: hidden;
      border: 1px solid #334155;
      background-color: #1e293b;
    }
    .prose th {
      background-color: #0f172a;
      color: #38bdf8;
      font-weight: 700;
      padding: 0.875rem 1rem;
      text-align: left;
      font-size: 0.875rem;
      border-bottom: 1px solid #334155;
    }
    .prose td {
      padding: 0.875rem 1rem;
      border-bottom: 1px solid #334155;
      font-size: 0.875rem;
      color: #cbd5e1;
      vertical-align: middle;
    }
    .prose tr:last-child td {
      border-bottom: none;
    }
    .prose tr:nth-child(even) {
      background-color: #0f172a/40;
    }
    .prose tr:hover {
      background-color: #334155/50;
    }
    /* Custom admonition / notice styling */
    blockquote {
      border-left: 4px solid #3b82f6;
      background: #1e293b;
      padding: 1rem 1.25rem;
      border-radius: 0.5rem;
      margin: 1.5rem 0;
      color: #94a3b8;
    }
  </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">

  {{ partial "header.html" . }}

  <main class="flex-grow max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 w-full">
    <!-- Breadcrumb & Category -->
    <nav class="flex items-center space-x-2 text-xs text-slate-400 mb-6">
      <a href="/" class="hover:text-blue-400">首页</a>
      <span>/</span>
      <a href="/posts/jichang-tuijian/" class="hover:text-blue-400">
        {{ if isSet .Params "categories_name" }}{{ .Params.categories_name }}{{ else if .Params.categories }}{{ delimit .Params.categories ", " }}{{ else }}稳定机场推荐{{ end }}
      </a>
      <span>/</span>
      <span class="text-slate-300 truncate max-w-xs sm:max-w-md">{{ .Title }}</span>
    </nav>

    <!-- Article Container -->
    <article class="bg-slate-950/40 border border-slate-800 rounded-2xl p-6 sm:p-10 shadow-2xl">
      <!-- Article Header -->
      <header class="mb-8 pb-6 border-b border-slate-800">
        <span class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-blue-500/10 text-blue-400 border border-blue-500/20 mb-4">
          {{ if isSet .Params "categories_name" }}{{ .Params.categories_name }}{{ else if .Params.categories }}{{ delimit .Params.categories ", " }}{{ else }}稳定机场推荐{{ end }}
        </span>
        
        <h1 class="text-2xl sm:text-4xl font-extrabold text-white tracking-tight leading-tight mb-4">
          {{ .Title }}
        </h1>
        
        <div class="flex flex-wrap items-center gap-4 text-xs text-slate-400">
          <span class="flex items-center space-x-1.5"><i class="far fa-calendar-alt text-blue-400"></i><span>发布于 {{ .Date.Format "2006-01-02" }}</span></span>
          <span class="flex items-center space-x-1.5"><i class="fas fa-user-edit text-purple-400"></i><span>编辑：机场稳定网编辑部</span></span>
          <span class="flex items-center space-x-1.5"><i class="fas fa-globe text-cyan-400"></i><span>域名：jcwending.homes</span></span>
        </div>
      </header>

      <!-- Article Main Content -->
      <div class="prose prose-invert lg:prose-lg max-w-none text-slate-200 leading-relaxed">
        {{ .Content }}
      </div>

      <!-- Bottom Telegram & Share Blox -->
      <div class="mt-12 pt-8 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 bg-slate-900/80 p-6 rounded-xl border border-slate-800">
        <div>
          <h4 class="text-base font-bold text-white mb-1">📢 遇到梯子排障或节点选购疑问？</h4>
          <p class="text-xs text-slate-400">欢迎加入官方 Telegram 社区防失联交流频道获得实时帮助。</p>
        </div>
        <a href="https://t.me/+uVUK4-hZhZZjYzk9" target="_blank" rel="sponsored nofollow noopener" class="px-5 py-2.5 rounded-full font-medium bg-slate-800/90 hover:bg-slate-700 text-cyan-400 border border-slate-700/80 transition-all text-xs flex items-center space-x-2 shadow-sm whitespace-nowrap">
          <i class="fab fa-telegram-plane text-cyan-400 text-xs" style="width:14px; height:14px;"></i>
          <span>加入官方 TG 防失联频道</span>
        </a>
      </div>
    </article>
  </main>

  {{ partial "footer.html" . }}

</body>
</html>
"""

# Destination single layout files
single_layout_files = [
    os.path.join(BASE, "layouts", "_default", "single.html"),
    os.path.join(BASE, "layouts", "posts", "single.html"),
    os.path.join(BASE, "layouts", "page", "single.html")
]

for sf in single_layout_files:
    os.makedirs(os.path.dirname(sf), exist_ok=True)
    with open(sf, "w", encoding="utf-8") as f:
        f.write(modern_single_html)

print("Single article layouts updated to match Hugo Blox Tailwind dark design!")
