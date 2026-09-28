import os

base = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

faq_map = {
    "faq-1-20": (
        "精选科学上网常见问题与稳定机场排障教程全展开解答，第1部分包含第1至20题关于节点选购与软件配置详解。",
        "查看 FAQ 第 1-20 题 →"
    ),
    "faq-21-40": (
        "精选科学上网常见问题与稳定机场排障教程全展开解答，第2部分包含第21至40题关于 Clash 规则分流与延迟排查。",
        "查看 FAQ 第 21-40 题 →"
    ),
    "faq-41-60": (
        "精选科学上网常见问题与稳定机场排障教程全展开解答，第3部分包含第41至60题关于流媒体/ChatGPT风控解封说明。",
        "查看 FAQ 第 41-60 题 →"
    ),
    "faq-61-80": (
        "精选科学上网常见问题与稳定机场排障教程全展开解答，第4部分包含第61至80题关于软路由PassWall与小火箭技巧。",
        "查看 FAQ 第 61-80 题 →"
    ),
    "faq-81-100": (
        "精选科学上网常见问题与稳定机场排障教程全展开解答，第5部分包含第81至100题关于订阅安全与备用导航维持。",
        "查看 FAQ 第 81-100 题 →"
    ),
    "mofa-shangwang-rumen-changjian-yinan-jieda": (
        "汇总科学上网零基础新手最关心的 10 大核心疑问，包含怎么选套餐、怎么买流量、遇到打不开网页怎么办。",
        "查看新手入门解答 →"
    ),
    "jiedian-chaoshi-tizi-lianbushang-paicha": (
        "逐步教你排查“节点超时 (Timeout)”与“无法连接”错误，修正本地 DNS 设置、系统时间同步与代理开关。",
        "查看排障深度教程 →"
    ),
    "wangaofeng-diaoxian-kadun-yuanyin-pouxi": (
        "剖析 ISP 运营商国际出口 QOS 限速、公网骨干网拥堵与机场节点带宽分配原理，找出晚上掉线的根本原因。",
        "查看晚高峰掉线剖析 →"
    ),
    "jichang-dingyue-jiedian-gengxin-shibai": (
        "解决 Clash 或小火箭提示“Update Failed”错误，提供更换备用更新节点、直接导入剪贴板与开启全局更新技巧。",
        "查看更新失败解决步骤 →"
    ),
    "iplc-hkt-hkbn-jiedian-qubie": (
        "科普香港原生宽带 (HKT/HKBN) 与 IPLC 物理专线架构异同，解释为什么专线成本更高但稳定性出众。",
        "查看节点区别探秘 →"
    ),
    "liumeiti-chatgpt-jiesuo-shibai-jiejuew": (
        "解决 ChatGPT 提示 “Access Denied” 与 Netflix 仅显示自制剧痛点，教你使用分流规则固定解锁节点。",
        "查看解锁失败解决指南 →"
    )
}

posts_dir = os.path.join(base, "content", "posts")
count = 0

for root, dirs, files in os.walk(posts_dir):
    for file in files:
        if file.endswith(".md") and file != "_index.md":
            slug = file.replace(".md", "")
            filepath = os.path.join(root, file)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Check if slug is in faq_map or needs updating
            if slug in faq_map:
                desc, cta = faq_map[slug]
            else:
                # If no cta_text present, generate one from title
                lines = content.split("\n")
                title = ""
                for line in lines:
                    if line.startswith("title:"):
                        title = line.replace("title:", "").strip().strip('"')
                        break
                
                desc = f"关于{title}的深度解析与实用技巧指南。"
                cta = f"阅读{title[:8]}... →"

            # Parse lines and replace description & cta_text
            lines = content.split("\n")
            new_lines = []
            fm_count = 0
            has_cta = False
            has_desc = False

            for line in lines:
                if line.strip() == "---":
                    fm_count += 1
                    if fm_count == 2:
                        if not has_cta and slug in faq_map:
                            new_lines.append(f'cta_text: "{faq_map[slug][1]}"')
                    new_lines.append(line)
                    continue

                if fm_count == 1:
                    if line.startswith("description:"):
                        if slug in faq_map:
                            new_lines.append(f'description: "{faq_map[slug][0]}"')
                        has_desc = True
                        continue
                    if line.startswith("cta_text:"):
                        if slug in faq_map:
                            new_lines.append(f'cta_text: "{faq_map[slug][1]}"')
                        has_cta = True
                        continue

                new_lines.append(line)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            count += 1

print(f"Updated FAQ & all posts: {count} files processed!")
