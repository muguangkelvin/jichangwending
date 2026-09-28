import os

base = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

# Goldmark requires HTML blocks NOT to have 4+ space leading indentation
config_steps_html = """<div style="background: rgba(15, 23, 42, 0.8); border: 1px solid #334155; border-radius: 16px; padding: 26px; margin: 40px 0; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4); font-family: sans-serif;">
<h2 style="color: #60a5fa; margin-top: 0; font-size: 20px; font-weight: 800; border-bottom: 2px solid #1e3a8a; padding-bottom: 12px; margin-bottom: 20px;" id="全平台零基础小白极速配置3分钟上手">
🚀 全平台零基础小白极速配置指南（3分钟上手）
</h2>
<div style="display: flex; flex-direction: column; gap: 18px;">
<div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 18px; border-left: 5px solid #3b82f6;">
<h3 style="margin: 0 0 8px 0; color: #38bdf8; font-size: 16px; font-weight: 700;">
1️⃣ 第一步：获取机场订阅链接
</h3>
<p style="margin: 0; font-size: 14px; color: #cbd5e1; line-height: 1.7;">
登录已购买机场的后台仪表盘（如灵动云官网），在用户中心点击 <strong style="color: #f8fafc;">“一键导入订阅”</strong> 或复制 <strong style="color: #f8fafc;">“通用订阅链接 (Subscription URL)”</strong> 到剪贴板。
</p>
</div>
<div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 18px; border-left: 5px solid #a855f7;">
<h3 style="margin: 0 0 10px 0; color: #c084fc; font-size: 16px; font-weight: 700;">
2️⃣ 第二步：下载对应系统的客户端软件
</h3>
<ul style="margin: 0; padding-left: 20px; font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
<li style="margin-bottom: 4px;"><strong style="color: #f8fafc;">Windows / macOS</strong>：推荐使用 <code style="color: #38bdf8; background: #0f172a; padding: 2px 6px; border-radius: 4px;">Clash Verge Rev</code>（支持 TUN 模式）或 <code style="color: #38bdf8; background: #0f172a; padding: 2px 6px; border-radius: 4px;">Clash Nyanpasu</code>。</li>
<li style="margin-bottom: 4px;"><strong style="color: #f8fafc;">iOS (iPhone/iPad)</strong>：在非国区 App Store 下载 <code style="color: #38bdf8; background: #0f172a; padding: 2px 6px; border-radius: 4px;">Shadowrocket (小火箭)</code> 或 <code style="color: #38bdf8; background: #0f172a; padding: 2px 6px; border-radius: 4px;">Stash</code>。</li>
<li><strong style="color: #f8fafc;">Android 安卓手机</strong>：推荐使用 <code style="color: #38bdf8; background: #0f172a; padding: 2px 6px; border-radius: 4px;">Clash Meta for Android</code> 或 <code style="color: #38bdf8; background: #0f172a; padding: 2px 6px; border-radius: 4px;">Sing-box</code>。</li>
</ul>
</div>
<div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 18px; border-left: 5px solid #10b981;">
<h3 style="margin: 0 0 8px 0; color: #34d399; font-size: 16px; font-weight: 700;">
3️⃣ 第三步：导入配置并开启规则代理
</h3>
<p style="margin: 0 0 8px 0; font-size: 14px; color: #cbd5e1; line-height: 1.7;">
⚠️ 代理模式切记勾选 <strong style="color: #38bdf8;">「Rule（规则分流）」</strong>，避免国内常规流量绕路走梯子。
</p>
<ul style="margin: 0; padding-left: 20px; font-size: 13.5px; color: #cbd5e1; line-height: 1.8;">
<li style="margin-bottom: 4px;">打开客户端，进入 <strong style="color: #f8fafc;">“配置 / Profiles”</strong> 页面，粘贴订阅链接并点击 <strong style="color: #f8fafc;">“下载 / 保存”</strong>；</li>
<li style="margin-bottom: 4px;">在节点列表中勾选延迟较低的地区节点（如香港或新加坡 IPLC 专线）；</li>
<li>开启系统代理总开关，即可流畅无感访问海外网络。</li>
</ul>
</div>
</div>
</div>"""

# Process all markdown post files in content/posts
posts_dir = os.path.join(base, "content", "posts")
count = 0
for root, dirs, files in os.walk(posts_dir):
    for file in files:
        if file.endswith(".md") and file != "_index.md":
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Find starting markers for config steps section
            markers = [
                '<div style="background: rgba(15, 23, 42, 0.8);',
                "## 全平台零基础小白极速配置（3分钟上手）",
                "## 全平台主流客户端配置步骤与最佳实践",
                "## 全平台零基础小白极速配置（3步骤上手）",
                "全平台零基础小白极速配置（3分钟上手）",
                "全平台零基础小白极速配置",
            ]

            found_marker = None
            for m in markers:
                if m in content:
                    found_marker = m
                    break

            if found_marker:
                parts = content.split(found_marker)
                before = parts[0]
                after = parts[1]
                
                tg_marker = "官方 Telegram"
                if tg_marker in after:
                    tg_parts = after.split(tg_marker)
                    content = before + config_steps_html + "\n\n" + tg_marker + tg_parts[1]
                else:
                    content = before + config_steps_html + "\n\n官方 Telegram 交流频道：[https://t.me/+uVUK4-hZhZZjYzk9](https://t.me/+uVUK4-hZhZZjYzk9)\n"
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1

print(f"Successfully updated configuration steps layout in {count} post files!")
