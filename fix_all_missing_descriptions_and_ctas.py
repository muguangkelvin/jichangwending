import os

base = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

master_dict = {
    # 防失联与导航 (daohang)
    "jcwending-fangshilian-fabuye-beiyong-daohang": (
        "提供机场稳定网（jichangwending.homes）官方永久防失联发布页入口、备用镜像域名与 Telegram 官方频道订阅。",
        "查看防失联发布页 →"
    ),
    "2026-beiyong-jingxiang-daohang-fangshilian": (
        "保存官方备用镜像站点与防失联 Telegram 订阅通道，即使主站域名受限也能随时获得最新的节点与客户端更新。",
        "查看备用镜像导航 →"
    ),
    "quanpingtai-client-xiazai-daohang": (
        "整理 Windows、macOS、iOS、Android 全平台正版客户端 GitHub 官方开源下载页面与正版安装包获取地址。",
        "查看客户端下载导航 →"
    ),

    # 稳定机场推荐 (jichang-tuijian)
    "wangaofeng-4k-wending-jichang-tuijian": (
        "实测晚高峰 20:00-23:00 时段 4K/8K 超清视频播放流畅度，深度拆解 IPLC 内网专线抗拥堵特性与极速中转节点推荐。",
        "阅读 4K 专线测评 →"
    ),
    "2026-changqi-shiyong-wending-tizi-pandian": (
        "针对长期订阅需求用户，盘点运营多年、抗封锁能力强、节点响应低至 30ms 的稳定梯子，规避跑路风险。",
        "查看长期梯子指南 →"
    ),
    "diannao-wending-tizi-jichang-ceshi": (
        "对比测试 Windows 与 macOS 电脑端各大机场节点连接稳定性，含 Clash Verge 与 Sing-box 运行性能实测。",
        "查看电脑端测试 →"
    ),
    "pianyi-wending-beiyong-jichang-tuijian": (
        "精选月付低至 9.9 元或按量计费不限时长的平价备用机场，为断网突发状况提供第二重高可用安全保障。",
        "查看备用机场推荐 →"
    ),
    "waimao-bangong-wending-zhuanxian-jichang": (
        "专为外贸企业、跨境电商及海外社媒运营打造，提供独享纯净原生 IP、大带宽双向 IEPL 专线与多设备并发协同。",
        "查看外贸专线方案 →"
    ),
    "iplc-qiyeji-neiwang-zhuanxian-jichang": (
        "解析企业级 IPLC 双向点对点专线优势，数据不经过公网 GFW 检查，从物理层面根除晚高峰丢包与断流。",
        "查看 IPLC 专线推荐 →"
    ),
    "liumeiti-ai-jiesuo-wending-jichang": (
        "精选 100% 原生住宅 IP 节点，无痛解封 ChatGPT 4o、Claude 3.5 Sonnet、Netflix 4K 及 Disney+ 区域限制。",
        "查看 AI/流媒体解锁 →"
    ),
    "duoshebei-xie-tong-wending-jichang": (
        "适合多台电脑、手机及路由器全家共享，盘点不限制客户端连接数、流量实打实的高性价比机场。",
        "查看多设备梯子盘点 →"
    ),
    "kangminganqi-gaowendingxing-tizi-shouxuan": (
        "剖析敏感封锁时期机场防失联策略，包含 Anycast 多入口容灾与智能切线原理，确保全天候网络畅通。",
        "查看抗封锁切线指南 →"
    ),
    "xingjiabi-zuigao-wending-jichang-ceshi": (
        "对比全网热门机场单位 G 流量单价、套餐月费与网速表现，附最新站内专属折扣优惠码领用方法。",
        "查看性价比测速表 →"
    ),
    "2026-wending-jichang-tuijian-wangaofeng-4k": (
        "深入拆解 2026 年最新机场选型标准、IPLC/IEPL 物理专线与普通直连对比，附全平台客户端零基础配置教程。",
        "阅读完整选型指南 →"
    ),
    "all-airports-guide": (
        "汇总全网 28 家优质梯子与机场服务，提供官网直达注册链接、详细简介、月流量、周期/类型、专线测评与解封支持对比。",
        "查看 28 家注册大全 →"
    ),

    # 客户端教程 (jiaocheng)
    "iphone-shadowrocket-xiaohuojian-jiaocheng": (
        "一步步教 iOS 用户下载使用小火箭 Shadowrocket，包含外区 Apple ID 切换、扫码与订阅 URL 一键导入。",
        "查看小火箭配置教程 →"
    ),
    "clash-verge-wending-dingyue-jiedian-daoru": (
        "详细演示新一代 Clash Verge Rev 客户端安装配置，涵盖开启 TUN 模式、导入通用订阅与开启规则分流。",
        "查看 Verge 配置指南 →"
    ),
    "android-clash-singbox-peizhi-jiaocheng": (
        "针对安卓手机用户推荐 Clash for Android 与 Sing-box 客户端，解决后台被杀、耗电与订阅更新问题。",
        "查看安卓配置教程 →"
    ),
    "macos-clash-meta-singbox-jiaocheng": (
        "苹果 Mac 电脑专属科学上网指南，介绍 M 系列芯片适配、Clash Meta 规则分流与无感开机启动。",
        "查看 Mac 配置教程 →"
    ),
    "windows-clash-verge-rev-jiaocheng": (
        "Windows 10/11 系统极速开局教程，中文界面轻松导入机场订阅，开启开机自启与系统代理。",
        "查看 Win 版详细设置 →"
    ),
    "singbox-quanpingtai-tongyong-dingyue-jiaocheng": (
        "拆解新一代 Sing-box 独立通用内核特性，支持全平台规则配置导入、低资源占用与 Hysteria 2 协议。",
        "查看 Sing-box 教程 →"
    ),
    "shadowrocket-peizhi-changjian-cuowu-paicha": (
        "总结 Shadowrocket 节点全部超时、黄灯红灯、无法连接网络常见原因，提供本地证书安装与 DNS 修正。",
        "查看小火箭排障步骤 →"
    ),
    "openwrt-passwall-openclash-ruanloutou-jiaocheng": (
        "手把手教你在 OpenWrt 软路由中配置 PassWall 与 OpenClash，实现全家电视、手机、游戏机透明出海。",
        "查看软路由搭建教程 →"
    ),
    "ipad-ios-wugan-fanqiang-fenliu-guize": (
        "讲解 iOS/iPadOS 策略组分流设置，避免微信/淘宝等国内流量走梯子，实现全天候无感后台保活。",
        "查看无感分流技巧 →"
    ),
    "clash-guize-fenliu-youhua-zhinan": (
        "深度教学 Clash 规则集优化，自定义 Direct/Proxy/Reject 策略组，节省机场套餐流量并提升访问速度。",
        "查看分流优化指南 →"
    ),
    "jichang-dingyue-lianjie-zhuanhuan-anquan": (
        "讲解在线 Subconverter 订阅转换工具隐患，教你搭建本地安全转换，防止订阅 URL 被他人盗用流量。",
        "查看订阅安全技巧 →"
    ),
    "xiaobai-zero-jichu-kexue-shangwang-jiaocheng": (
        "零基础科普指南，从什么是机场节点、订阅链接格式到下载客户端、导入节点，全方位扫盲过关。",
        "查看零基础通关教程 →"
    ),

    # 专线与晚高峰评测 (pingce)
    "2026-wending-jichang-cesu-pingce-baogao": (
        "发布 2026 年度最新晚高峰 21 点测速报告，对比各大机场丢包率、延迟抖动与 4K 拖动缓冲时间。",
        "查看测速报告数据 →"
    ),
    "iplc-bgp-xianlu-shendu-duibi": (
        "从网络拓扑与物理光纤传输原理出发，对比分析 IPLC 物理专线与普通 BGP 中转在拥堵高峰期的表现。",
        "查看线路深度对比 →"
    ),
    "gaowendingxing-tizi-kangminganqi-ceshi": (
        "实测高隐匿专线梯子在敏感封锁期的表现，解析 Anycast 入口自动切线与动态 IP 恢复机制。",
        "查看抗封锁切线原理 →"
    ),
    "4k-8k-chaogaoqing-shipin-jichang-cesu": (
        "使用 YouTube 详细统计信息 (Stats for nerds) 实测各大机场连接速率，挑战 8K 60帧视频无缓冲播放。",
        "查看超高清带宽测速 →"
    ),
    "yuansheng-ip-jichang-jiedian-chatgpt-tiktok": (
        "测试 28 家机场节点机房 IP 纯净度，统计 ChatGPT、Claude 及 TikTok 海外版无阻访问成功率。",
        "查看原生 IP 解封测试 →"
    ),
    "youxi-jiasu-diyanzi-jiedian-pingce": (
        "针对英雄联盟外服、Steam 联机、绝地求生等网游玩家，评测亚服香港/日本/韩国节点的 Ping 值与零跳包体验。",
        "查看游戏低延迟评测 →"
    ),
    "pianyi-jichang-vs-gaoduan-zhuanxian-jichang": (
        "揭秘低价“垃圾机场”超卖与虚标真相，对比月付几元与企业专线在服务器带宽采购成本上的本质区别。",
        "查看机场对比真相 →"
    ),
    "2026-tizi-wending-cesu-paihang": (
        "根据多月实测综合评分，筛选出综合稳定度、解锁率与客服口碑排名前 5 的年度高可用梯子服务商。",
        "查看梯子稳定排行 →"
    ),
    "2026-zhuliu-haokoubei-jichang-hengxiang-ceshi": (
        "全面横向评测灵动云、暮光、飞猫、微风、隐形人、浪网 WaveNet、梯子云、飞V等8款主流服务，附横向对比表。",
        "阅读 8 款机场横向评测 →"
    ),

    # 小白新手答疑 (faq)
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

            lines = content.split("\n")
            title = ""
            for line in lines:
                if line.startswith("title:"):
                    title = line.replace("title:", "").strip().strip('"')
                    break
            
            if slug in master_dict:
                desc, cta = master_dict[slug]
            else:
                desc = f"关于{title}的深度解析与实用技巧指南。"
                cta = "查看指南详情 →"

            # Check if description and cta_text exist in frontmatter
            new_lines = []
            fm_count = 0
            has_desc = False
            has_cta = False

            for line in lines:
                if line.strip() == "---":
                    fm_count += 1
                    if fm_count == 2:
                        if not has_desc:
                            new_lines.append(f'description: "{desc}"')
                        if not has_cta:
                            new_lines.append(f'cta_text: "{cta}"')
                    new_lines.append(line)
                    continue

                if fm_count == 1:
                    if line.startswith("description:"):
                        new_lines.append(f'description: "{desc}"')
                        has_desc = True
                        continue
                    if line.startswith("cta_text:"):
                        new_lines.append(f'cta_text: "{cta}"')
                        has_cta = True
                        continue

                new_lines.append(line)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            count += 1

print(f"Processed all {count} post files!")
