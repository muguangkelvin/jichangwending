import os

base = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

intro_cards_html1 = """<div style="margin: 40px 0;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
<div style="background: rgba(30, 41, 59, 0.75); border: 1px solid #334155; border-radius: 14px; padding: 22px; border-top: 4px solid #ef4444; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
<h3 style="color: #f87171; font-size: 16px; font-weight: 700; margin: 0 0 10px 0;">
⚠️ 晚高峰痛点与网络现状
</h3>
<p style="margin: 0; font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
随着防火墙主动探测常态化，普通直连或简易 VPS 在每日 <strong style="color: #f8fafc;">20:00–23:00 晚高峰</strong> 及敏感期频繁面临高丢包、断流甚至大面积封锁。
</p>
</div>
<div style="background: rgba(30, 41, 59, 0.75); border: 1px solid #334155; border-radius: 14px; padding: 22px; border-top: 4px solid #3b82f6; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
<h3 style="color: #60a5fa; font-size: 16px; font-weight: 700; margin: 0 0 10px 0;">
💡 企业级专线解决方案
</h3>
<p style="margin: 0; font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
针对 <strong style="color: #f8fafc;">4K影音、跨境电商、AI (ChatGPT/Claude)</strong> 交互需求，物理内网专线（IPLC/IEPL）物理出境，保障全天候零卡顿无感体验。
</p>
</div>
<div style="background: rgba(30, 41, 59, 0.75); border: 1px solid #334155; border-radius: 14px; padding: 22px; border-top: 4px solid #10b981; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
<h3 style="color: #34d399; font-size: 16px; font-weight: 700; margin: 0 0 10px 0;">
🎯 本指南涵盖核心内容
</h3>
<p style="margin: 0; font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
深度拆解 2026 最新选型标准、主流专线梯子横向实测评测，并提供全平台零基础小白跨平台客户端配置教学。
</p>
</div>
</div>
</div>"""

# 1. Update Article 1
art1_path = os.path.join(base, "content", "posts", "jichang-tuijian", "2026-wending-jichang-tuijian-wangaofeng-4k.md")
if os.path.exists(art1_path):
    with open(art1_path, "r", encoding="utf-8") as f:
        content = f.read()

    seo_end_str = "</div>"
    h2_str = "## 为什么普通梯子在晚高峰会卡？物理专线与普通直连的区别"
    
    if seo_end_str in content and h2_str in content:
        parts1 = content.split(seo_end_str, 1)
        parts2 = parts1[1].split(h2_str, 1)
        content = parts1[0] + seo_end_str + "\n\n" + intro_cards_html1 + "\n\n" + h2_str + parts2[1]

    with open(art1_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Article 1 formatted without Goldmark indentation.")

# 2. Update Article 2
art2_path = os.path.join(base, "content", "posts", "pingce", "2026-zhuliu-haokoubei-jichang-hengxiang-ceshi.md")
if os.path.exists(art2_path):
    with open(art2_path, "r", encoding="utf-8") as f:
        content = f.read()

    seo_end_str = "</div>"
    h2_str2 = "## 2026 主流高口碑机场梯子横向实测对比"

    if seo_end_str in content and h2_str2 in content:
        parts1 = content.split(seo_end_str, 1)
        parts2 = parts1[1].split(h2_str2, 1)
        content = parts1[0] + seo_end_str + "\n\n" + intro_cards_html1 + "\n\n" + h2_str2 + parts2[1]

    with open(art2_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Article 2 formatted without Goldmark indentation.")
