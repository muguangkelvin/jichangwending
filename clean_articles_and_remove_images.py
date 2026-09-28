import os

base = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

# 1. Update Article 1
art1_path = os.path.join(base, "content", "posts", "jichang-tuijian", "2026-wending-jichang-tuijian-wangaofeng-4k.md")
if os.path.exists(art1_path):
    with open(art1_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove duplicate title # 2026...
    content = content.replace('# 2026稳定机场推荐：晚高峰4K不卡顿、全天候抗封锁专线梯子与小白配置教程\n\n', '')
    
    # Styled SEO keywords box with ample margin top/bottom
    seo_old = '> **SEO 搜索核心关键词**：`2026稳定机场推荐`、`晚高峰4K不卡顿`、`IPLC/IEPL内网专线`、`抗封锁机场节点`、`Clash Verge配置教程`、`Shadowrocket小火箭订阅`、`ChatGPT/Netflix流媒体解锁`、`科学上网梯子防跑路指南`。'
    seo_new = """<div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 18px 24px; margin: 36px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <p style="margin:0; font-size: 13.5px; color: #94a3b8; line-height: 1.8;">
    <strong style="color:#38bdf8;">🏷️ SEO 搜索核心关键词：</strong> <code>2026稳定机场推荐</code> · <code>晚高峰4K不卡顿</code> · <code>IPLC/IEPL内网专线</code> · <code>抗封锁机场节点</code> · <code>Clash Verge配置教程</code> · <code>Shadowrocket小火箭订阅</code> · <code>ChatGPT/Netflix流媒体解锁</code> · <code>科学上网梯子防跑路指南</code>
  </p>
</div>"""
    content = content.replace(seo_old, seo_new)

    # Remove image block 1
    img1_block = """<div style="margin: 32px 0; border: 1px solid #334155; border-radius: 12px; padding: 12px; background: rgba(15, 23, 42, 0.6); text-align: center;">
  <img src="/images/network-monitor-dashboard.png" alt="2026稳定机场晚高峰网络监测与丢包率对比面板" style="border-radius: 8px; width: 100%; max-width: 900px; display: block; margin: 0 auto;" />
  <p style="font-size: 13px; color: #94a3b8; margin-top: 10px; margin-bottom: 2px;">图 1：机场稳定网 2026 晚高峰全局节点延迟与丢包率实时数据监控面板</p>
</div>"""
    content = content.replace(img1_block, '')
    
    with open(art1_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Article 1 cleaned.")

# 2. Update Article 2
art2_path = os.path.join(base, "content", "posts", "pingce", "2026-zhuliu-haokoubei-jichang-hengxiang-ceshi.md")
if os.path.exists(art2_path):
    with open(art2_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove duplicate title # 2026...
    content = content.replace('# 2026主流高口碑机场梯子横向实测对比（含灵动云/暮光/飞猫/微风等8款评测）\n\n', '')

    seo_old2 = '> **SEO 搜索核心关键词**：`2026稳定机场推荐`、`灵动云机场测评`、`晚高峰4K不卡顿`、`IPLC/IEPL内网专线`、`暮光云加速`、`飞猫云梯子`、`微风加速器`、`抗封锁机场节点`、`Clash Verge配置教程`、`Shadowrocket小火箭订阅`、`ChatGPT/Netflix流媒体解锁`、`科学上网梯子防跑路指南`。'
    seo_new2 = """<div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 18px 24px; margin: 36px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <p style="margin:0; font-size: 13.5px; color: #94a3b8; line-height: 1.8;">
    <strong style="color:#38bdf8;">🏷️ SEO 搜索核心关键词：</strong> <code>2026稳定机场推荐</code> · <code>灵动云机场测评</code> · <code>晚高峰4K不卡顿</code> · <code>IPLC/IEPL内网专线</code> · <code>暮光云加速</code> · <code>飞猫云梯子</code> · <code>微风加速器</code> · <code>抗封锁机场节点</code> · <code>Clash Verge配置教程</code> · <code>Shadowrocket小火箭订阅</code> · <code>ChatGPT/Netflix流媒体解锁</code> · <code>科学上网梯子防跑路指南</code>
  </p>
</div>"""
    content = content.replace(seo_old2, seo_new2)

    # Remove image block 2
    img2_block = """<div style="margin: 32px 0; border: 1px solid #334155; border-radius: 12px; padding: 12px; background: rgba(15, 23, 42, 0.6); text-align: center;">
  <img src="/images/server-speed-rack.png" alt="2026年企业级IPLC/IEPL物理专线机房节点监控与速率测量" style="border-radius: 8px; width: 100%; max-width: 900px; display: block; margin: 0 auto;" />
  <p style="font-size: 13px; color: #94a3b8; margin-top: 10px; margin-bottom: 2px;">图 2：2026 年企业级物理专线数据中心与极速传输节点测速基准</p>
</div>"""
    content = content.replace(img2_block, '')

    with open(art2_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Article 2 cleaned.")

# Also check other generated posts for duplicate H1 headers
posts_dir = os.path.join(base, "content", "posts")
for root, dirs, files in os.walk(posts_dir):
    for file in files:
        if file.endswith(".md") and file != "_index.md":
            p = os.path.join(root, file)
            with open(p, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            # Check if there's an H1 title after frontmatter
            in_fm = False
            fm_count = 0
            new_lines = []
            for line in lines:
                if line.strip() == "---":
                    fm_count += 1
                    new_lines.append(line)
                    continue
                if fm_count == 2 and line.startswith("# "):
                    # Skip duplicate H1 title in markdown content
                    continue
                new_lines.append(line)
            
            with open(p, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

print("All posts cleaned of duplicate H1 headings!")
