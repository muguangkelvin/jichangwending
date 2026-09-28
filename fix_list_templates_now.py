import os

base = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

template_html = """<!DOCTYPE html>
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
  </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">

  {{ partial "header.html" . }}

  <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 w-full">
    <!-- Header Banner -->
    <div class="mb-10 pb-6 border-b border-slate-800">
      <div class="flex items-center space-x-3 mb-3">
        <span class="px-3.5 py-1 rounded-full text-xs font-bold bg-blue-500/10 text-blue-400 border border-blue-500/30">
          分类与专题指南
        </span>
        <span class="text-xs text-slate-400 font-medium">机场稳定网</span>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">{{ .Title }}</h1>
      <p class="mt-3 text-sm sm:text-base text-slate-300 max-w-3xl leading-relaxed">
        {{ if .Description }}{{ .Description }}{{ else }}汇总本站所有精选梯子推荐、IPLC专线测评与全平台客户端配置教程。{{ end }}
      </p>
    </div>

    <!-- 3-Column Grid Cards matching Blox Architecture -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-stretch">
      {{ range .Pages }}
      <div class="group bg-slate-800/70 border border-slate-700/70 hover:border-blue-500/60 rounded-2xl p-6 shadow-lg hover:shadow-2xl hover:shadow-blue-500/10 transition-all flex flex-col justify-between h-full">
        <div>
          <!-- Meta Header -->
          <div class="flex items-center justify-between mb-4">
            <span class="text-xs font-bold text-blue-400 bg-blue-950/60 px-3 py-1 rounded-full border border-blue-500/30">
              {{ if isSet .Params "categories_name" }}{{ .Params.categories_name }}{{ else if .Params.categories }}{{ delimit .Params.categories ", " }}{{ else }}稳定机场推荐{{ end }}
            </span>
            <span class="text-xs text-slate-400"><i class="far fa-calendar-alt mr-1.5 text-blue-400"></i>{{ .Date.Format "2006-01-02" }}</span>
          </div>

          <!-- Card Title (fixed height for grid alignment) -->
          <h2 class="text-base sm:text-lg font-bold text-white group-hover:text-blue-300 mb-3 leading-snug line-clamp-2 h-14 flex items-center">
            <a href="{{ .RelPermalink }}" class="hover:underline decoration-blue-400/50 underline-offset-4">{{ .Title }}</a>
          </h2>

          <!-- Card Summary (fixed height for grid alignment) -->
          <p class="text-xs sm:text-sm text-slate-300 line-clamp-3 leading-relaxed mb-6 h-16 overflow-hidden">
            {{ .Description }}
          </p>
        </div>

        <!-- Meta Footer & Dynamic CTA Button -->
        <div class="pt-4 border-t border-slate-700/50 flex items-center justify-between mt-auto">
          <span class="text-xs text-slate-400 font-medium">机场稳定网精选</span>
          <a href="{{ .RelPermalink }}" class="inline-flex items-center text-xs font-bold text-blue-400 hover:text-blue-300 group-hover:translate-x-1 transition-transform space-x-1">
            <span>{{ if isSet .Params "cta_text" }}{{ .Params.cta_text }}{{ else }}阅读完整指南 →{{ end }}</span>
          </a>
        </div>
      </div>
      {{ end }}
    </div>

    <!-- Top 4 Airport Banner in Section Pages -->
    <section class="mt-16 p-6 rounded-2xl bg-gradient-to-r from-slate-800 via-indigo-950 to-slate-800 border border-slate-700/80 shadow-xl">
      <div class="flex flex-col md:flex-row items-center justify-between gap-4">
        <div>
          <h3 class="text-lg font-bold text-white mb-1">🚀 找不到合适的节点？直接查看28家稳定机场注册大全</h3>
          <p class="text-xs text-slate-300">包含四大首推机场（灵动云、暮光网络、飞猫云、微风网络）及优惠码汇总。</p>
        </div>
        <a href="/posts/jichang-tuijian/all-airports-guide/" class="px-6 py-2.5 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-bold text-xs shadow-md transition-all whitespace-nowrap">
          立即前往注册大全 →
        </a>
      </div>
    </section>
  </main>

  {{ partial "footer.html" . }}

</body>
</html>
"""

targets = [
    os.path.join(base, "layouts", "_default", "list.html"),
    os.path.join(base, "layouts", "_default", "section.html"),
    os.path.join(base, "layouts", "posts", "list.html"),
    os.path.join(base, "layouts", "posts", "section.html"),
    os.path.join(base, "layouts", "section", "posts.html"),
]

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    with open(t, "w", encoding="utf-8") as f:
        f.write(template_html)

print("Template write done!")
