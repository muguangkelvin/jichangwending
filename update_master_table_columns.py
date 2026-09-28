import os

BASE = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

airports_extended_data = [
    {
        "rank": 1,
        "name": "灵动云",
        "short_name": "灵动云",
        "intro": "2026年度冠军专线，原生IPLC+BGP中转，晚高峰4K秒开，丢包率趋于0%。",
        "price": "￥15.00/月起",
        "traffic": "150GB - 2000GB",
        "period_type": "月付 / 季付 / 年付 (IPLC专线)",
        "lines": "原生IPLC专线+BGP",
        "ai_unlock": "完全解锁 ChatGPT / Claude / Netflix / 4K",
        "review_url": "/posts/pingce/wangaofeng-4k-wending-jichang-tuijian/",
        "aff_url": "https://varnexa.lingdongaff.com/#/?code=JoIy7bO1"
    },
    {
        "rank": 2,
        "name": "暮光网络",
        "short_name": "暮光网络",
        "intro": "IEPL企业级全专线中转，超大带宽不限速，适合长视频观赏与外贸团队。",
        "price": "￥18.00/月起",
        "traffic": "200GB - 3000GB",
        "period_type": "月付 / 年付 (IEPL专线)",
        "lines": "IEPL专线+广深/沪日",
        "ai_unlock": "完美支持 AI工具全家桶 + HIFI音频",
        "review_url": "/posts/pingce/iplc-bgp-xianlu-shendu-duibi/",
        "aff_url": "https://varnexa.twilightaff.com/#/?code=KvGly3jY"
    },
    {
        "rank": 3,
        "name": "飞猫云",
        "short_name": "飞猫云",
        "intro": "老牌稳定高口碑梯子，IPLC内网专线保障，不限个人设备数，性价比极高。",
        "price": "￥12.00/月起",
        "traffic": "100GB - 1500GB",
        "period_type": "月付 / 年付 (IPLC专线)",
        "lines": "BGP入口+IPLC内网专线",
        "ai_unlock": "全节点支持 OpenAI API 与流媒体",
        "review_url": "/posts/pingce/gaowendingxing-tizi-kangminganqi-ceshi/",
        "aff_url": "https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH"
    },
    {
        "rank": 4,
        "name": "微风网络 Breezenet",
        "short_name": "微风网络",
        "intro": "极速切线低门槛，支持便宜月付/年付，防封锁能力强，适合小白与备用节点。",
        "price": "￥9.90/月起",
        "traffic": "80GB - 1000GB",
        "period_type": "便宜月付 / 年付 (BGP)",
        "lines": "优质BGP中转",
        "ai_unlock": "支持网页端与客户端常见流媒体及AI",
        "review_url": "/posts/pingce/pianyi-jichang-vs-gaoduan-zhuanxian-jichang/",
        "aff_url": "https://edp01.breezenetaff.com/#/?code=He4n3zxg"
    },
    {
        "rank": 5,
        "name": "隐形人",
        "short_name": "隐形人",
        "intro": "加密二次混淆传输，匿名性极高，无日志留存。",
        "price": "￥20.00/月",
        "traffic": "180GB / 月",
        "period_type": "月付 (隧道专线)",
        "lines": "隧道专线",
        "ai_unlock": "解锁主流AI工具与流媒体",
        "review_url": "/posts/pingce/gaowendingxing-tizi-kangminganqi-ceshi/",
        "aff_url": "https://varnexa.invisibleaff.com/#/?code=FlyoraeM"
    },
    {
        "rank": 6,
        "name": "浪网 WaveNet",
        "short_name": "浪网",
        "intro": "千兆端口大带宽，专为高清冲浪与大文件下载设计。",
        "price": "￥22.00/月",
        "traffic": "500GB / 月",
        "period_type": "月付 (千兆BGP)",
        "lines": "千兆BGP中转",
        "ai_unlock": "解锁8K超清视频与AI",
        "review_url": "/posts/pingce/4k-8k-chaogaoqing-shipin-jichang-cesu/",
        "aff_url": "https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ"
    },
    {
        "rank": 7,
        "name": "梯子云 LadderCloud",
        "short_name": "梯子云",
        "intro": "多协议兼容，支持 Clash / Shadowrocket / Sing-box 订阅。",
        "price": "￥16.80/月",
        "traffic": "200GB / 月",
        "period_type": "月付 (混合专线)",
        "lines": "混合专线",
        "ai_unlock": "支持ChatGPT与流媒体",
        "review_url": "/posts/pingce/2026-tizi-wending-cesu-paihang/",
        "aff_url": "https://varnexa.ladderaff.com/#/?code=bYVSMHMh"
    },
    {
        "rank": 8,
        "name": "飞V",
        "short_name": "飞V",
        "intro": "优化网游联机与语音节点，低延迟抗丢包。",
        "price": "￥19.90/月",
        "traffic": "250GB / 月",
        "period_type": "月付 (游戏专线)",
        "lines": "游戏加速专线",
        "ai_unlock": "支持主流流媒体与语音",
        "review_url": "/posts/pingce/youxi-jiasu-diyanzi-jiedian-pingce/",
        "aff_url": "https://varnexa.flyvaff.com/#/?code=qaMgTyhY"
    },
    {
        "rank": 9,
        "name": "星岛梦",
        "short_name": "星岛梦",
        "intro": "平价高性价比，节点分布均衡，适合日常浏览。",
        "price": "￥15.00/月",
        "traffic": "150GB / 月",
        "period_type": "月付 (BGP中转)",
        "lines": "BGP中转",
        "ai_unlock": "支持常规流媒体",
        "review_url": "/posts/pingce/2026-wending-jichang-cesu-pingce-baogao/",
        "aff_url": "https://kfccbb.xingdaomeng.com/#/?code=tLbhLnNf"
    },
    {
        "rank": 10,
        "name": "光速云",
        "short_name": "光速云",
        "intro": "IPLC专线保障，节点响应极快，晚高峰流畅。",
        "price": "￥18.00/月",
        "traffic": "200GB / 月",
        "period_type": "月付 (IPLC专线)",
        "lines": "IPLC专线",
        "ai_unlock": "解锁ChatGPT与4K",
        "review_url": "/posts/pingce/wangaofeng-4k-wending-jichang-tuijian/",
        "aff_url": "https://mdlky.gsyaff.com/#/?code=5snwJVcD"
    },
    {
        "rank": 11,
        "name": "唯兔云（V2云）",
        "short_name": "唯兔云",
        "intro": "深度优化 V2ray 协议，抗封锁能力优异。",
        "price": "￥12.00/月",
        "traffic": "120GB / 月",
        "period_type": "月付 (优质中转)",
        "lines": "优质中转",
        "ai_unlock": "支持AI与海外视频",
        "review_url": "/posts/pingce/2026-wending-jichang-cesu-pingce-baogao/",
        "aff_url": "https:/fast.v2yunvipaff.com/#/?code=xkiG3YWN"
    },
    {
        "rank": 12,
        "name": "U1S1（有一说一）",
        "short_name": "U1S1",
        "intro": "透明无虚标，流量实打实扣除，稳定运行。",
        "price": "￥10.00/月",
        "traffic": "100GB / 月",
        "period_type": "月付 (BGP中转)",
        "lines": "BGP中转",
        "ai_unlock": "解锁主流海外服务",
        "review_url": "/posts/pingce/pianyi-jichang-vs-gaoduan-zhuanxian-jichang/",
        "aff_url": "https://pkdj7.vipaff.cc/#/?code=nYbe5pKy"
    },
    {
        "rank": 13,
        "name": "极连云",
        "short_name": "极连云",
        "intro": "多入口负载均衡，秒连节点，多地域选择。",
        "price": "￥16.00/月",
        "traffic": "180GB / 月",
        "period_type": "月付 (多入口)",
        "lines": "多入口中转",
        "ai_unlock": "全流媒体解锁",
        "review_url": "/posts/pingce/yuansheng-ip-jichang-jiedian-chatgpt-tiktok/",
        "aff_url": "https://kdjhao.jlyvipaff.com/#/?code=rO50GIZj"
    },
    {
        "rank": 14,
        "name": "全球云",
        "short_name": "全球云",
        "intro": "拥有上百个全球节点，适合跨境办公与多出口需求。",
        "price": "￥25.00/月",
        "traffic": "350GB / 月",
        "period_type": "月付 (全球IPLC)",
        "lines": "全球IPLC",
        "ai_unlock": "完全解锁AI与流媒体",
        "review_url": "/posts/pingce/waimao-bangong-wending-zhuanxian-jichang/",
        "aff_url": "https://sswdh.gcvipaff.com/#/?code=Ys0xKqnU"
    },
    {
        "rank": 15,
        "name": "光年梯",
        "short_name": "光年梯",
        "intro": "超低延迟，节点稳定性强，全天候高可用。",
        "price": "￥14.00/月",
        "traffic": "130GB / 月",
        "period_type": "月付 (专线中转)",
        "lines": "专线中转",
        "ai_unlock": "支持ChatGPT",
        "review_url": "/posts/pingce/2026-tizi-wending-cesu-paihang/",
        "aff_url": "https://ggmq.gntaff.com/#/?code=34i9Naos"
    },
    {
        "rank": 16, "name": "Sogo云", "short_name": "Sogo云", "intro": "平价入门机场，适合低预算学习办公。", "price": "￥8.80/月", "traffic": "80GB", "period_type": "便宜月付", "lines": "普通BGP", "ai_unlock": "基础解锁", "review_url": "/posts/pingce/pianyi-jichang-vs-gaoduan-zhuanxian-jichang/", "aff_url": "https://wzjc.sogoyunaff.cc/#/?code=nWA62UuJ"},
    {
        "rank": 17, "name": "宇宙云 YuZhou", "short_name": "宇宙云", "intro": "大容量套餐，适合重度观影与文件下载。", "price": "￥30.00/月", "traffic": "1000GB", "period_type": "大流量月付", "lines": "千兆中转", "ai_unlock": "支持4K流媒体", "review_url": "/posts/pingce/4k-8k-chaogaoqing-shipin-jichang-cesu/", "aff_url": "https://wzjc.yuzoucloud.cc/#/?code=hMqs74rd"},
    {
        "rank": 18, "name": "二猫云 2mao", "short_name": "二猫云", "intro": "双入口冗余容灾，防止断连与单点故障。", "price": "￥13.00/月", "traffic": "120GB", "period_type": "双线月付", "lines": "双路BGP", "ai_unlock": "支持主流软件", "review_url": "/posts/pingce/gaowendingxing-tizi-kangminganqi-ceshi/", "aff_url": "https://waaa.2maoyunaff.cc/#/?code=tbIH9UGF"},
    {
        "rank": 19, "name": "一翻云 1fly", "short_name": "一翻云", "intro": "傻瓜式配置，一键导入即用。", "price": "￥15.00/月", "traffic": "150GB", "period_type": "月付", "lines": "智能中转", "ai_unlock": "解锁AI", "review_url": "/posts/pingce/2026-wending-jichang-cesu-pingce-baogao/", "aff_url": "https://wzjc.1flyunaff.cc/#/?code=vq9IugSn"},
    {
        "rank": 20, "name": "边缘节点 EdgeNova", "short_name": "边缘节点", "intro": "基于边缘计算架构的节点服务，降低接入延时。", "price": "￥20.00/月", "traffic": "200GB", "period_type": "Edge专线", "lines": "Edge专线", "ai_unlock": "全平台解锁", "review_url": "/posts/pingce/iplc-bgp-xianlu-shendu-duibi/", "aff_url": "https://work.edgenovaaff.cc/#/?code=6Mi7km72"},
    {
        "rank": 21, "name": "可信云", "short_name": "可信云", "intro": "加密高防护，适合商务办公与隐私连接。", "price": "￥22.00/月", "traffic": "220GB", "period_type": "加密月付", "lines": "加密IPLC", "ai_unlock": "解锁办公与AI", "review_url": "/posts/pingce/waimao-bangong-wending-zhuanxian-jichang/", "aff_url": "https://work.kosingaff.com/#/?code=BmIpbeEn"},
    {
        "rank": 22, "name": "速界 SuJie", "short_name": "速界", "intro": "IEPL专线抗压，晚高峰表现平稳。", "price": "￥17.00/月", "traffic": "160GB", "period_type": "IEPL专线", "lines": "IEPL专线", "ai_unlock": "解锁流媒体", "review_url": "/posts/pingce/wangaofeng-4k-wending-jichang-tuijian/", "aff_url": "https://work.speedworldaff.cc/#/?code=YhcpJLbr"},
    {
        "rank": 23, "name": "快狸 KuaiLi", "short_name": "快狸", "intro": "节点切换快，路由优化到位。", "price": "￥14.50/月", "traffic": "140GB", "period_type": "月付", "lines": "BGP中转", "ai_unlock": "支持主流应用", "review_url": "/posts/pingce/2026-tizi-wending-cesu-paihang/", "aff_url": "https://work.kuailicloud.cc/#/?code=7BsufMC0"},
    {
        "rank": 24, "name": "无忧", "short_name": "无忧", "intro": "故障自动告警切线，无忧断连。", "price": "￥15.00/月", "traffic": "150GB", "period_type": "混合月付", "lines": "混合线路", "ai_unlock": "支持流媒体", "review_url": "/posts/pingce/gaowendingxing-tizi-kangminganqi-ceshi/", "aff_url": "https://wep01.worryfreeaff.com/#/?code=vak0gPse"},
    {
        "rank": 25, "name": "灵猫", "short_name": "灵猫", "intro": "套餐种类多，支持灵活定制与按需购买。", "price": "￥11.00/月", "traffic": "100GB", "period_type": "灵活月付", "lines": "中转线路", "ai_unlock": "支持ChatGPT", "review_url": "/posts/pingce/pianyi-jichang-vs-gaoduan-zhuanxian-jichang/", "aff_url": "https://vip02.civetaff.com/#/?code=Z4KLo3Wz"},
    {
        "rank": 26, "name": "闪跃 FlashLeap", "short_name": "闪跃", "intro": "延迟极低，网页加载与搜索秒开。", "price": "￥19.00/月", "traffic": "200GB", "period_type": "闪跃专线", "lines": "闪跃专线", "ai_unlock": "全面解锁", "review_url": "/posts/pingce/2026-wending-jichang-cesu-pingce-baogao/", "aff_url": "https://vip02.flashleapaff.com/#/?code=wnLaKVaU"},
    {
        "rank": 27, "name": "飞为（Firefly）", "short_name": "飞为", "intro": "线路优化到位，稳定性有保证。", "price": "￥16.00/月", "traffic": "150GB", "period_type": "月付", "lines": "BGP专线", "ai_unlock": "支持AI与视频", "review_url": "/posts/pingce/2026-tizi-wending-cesu-paihang/", "aff_url": "https://vip02.fireflyaff.com/#/?code=1n1ZIJab"},
    {
        "rank": 28, "name": "跨界", "short_name": "跨界", "intro": "跨境电商与海外社交媒体独立原生IP支持。", "price": "￥28.00/月", "traffic": "300GB", "period_type": "跨境专线", "lines": "跨境原生IP", "ai_unlock": "全流媒体+TikTok+AI", "review_url": "/posts/pingce/waimao-bangong-wending-zhuanxian-jichang/", "aff_url": "https://vip02.kuajieaff.com/#/?code=RQ4b2tfV"}
]

# Generate Markdown table for all-airports-guide.md
top4_box = """
<div style="background: linear-gradient(135deg, #f0f7ff 0%, #e6f0fa 100%); border: 2px solid #0056b3; border-radius: 12px; padding: 22px; margin: 28px 0; box-shadow: 0 4px 15px rgba(0,86,179,0.12);">
  <h3 style="color: #004085; margin-top: 0; font-size: 21px; border-bottom: 2px solid #0056b3; padding-bottom: 10px; font-weight: bold;">🏆 2026年度四大高稳定性翻墙机场推荐（晚高峰不卡顿首选）</h3>
  <p style="font-size: 14.5px; color: #333; margin-bottom: 18px; line-height: 1.6;">在选择稳定梯子节点与机场服务时，晚高峰丢包率与节点抗封锁能力是两大核心指标。编辑部经过长达数月实时监控测速，重磅推荐以下4家头部顶级机场：</p>
  
  <div style="margin-bottom: 16px; padding: 14px; background: #ffffff; border-radius: 8px; border-left: 6px solid #e60000; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0; color:#cc0000; font-size: 17px;">🥇 第1名：灵动云 - 2026高稳定性梯子第一名（晚高峰4K秒开）</h4>
    <p style="margin: 0 0 10px 0; font-size: 14px; color: #444; line-height: 1.6;"><strong>专线优势：</strong> 原生IPLC专线 + BGP多线中转，针对ChatGPT/Claude与海外流媒体极速解锁，晚高峰丢包率接近于零。</p>
    <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: linear-gradient(90deg, #e60000, #ff3333); color: #ffffff; padding: 10px 22px; border-radius: 6px; font-weight: bold; text-decoration: none; font-size: 15px; box-shadow: 0 3px 6px rgba(230,0,0,0.3);">👉 官方注册入口：前往【灵动云】官网开通体验</a>
  </div>

  <div style="margin-bottom: 16px; padding: 14px; background: #ffffff; border-radius: 8px; border-left: 6px solid #0066cc; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0; color:#0052a3; font-size: 17px;">🥈 第2名：暮光网络 - 晚高峰不限速与大流量办公影音首选</h4>
    <p style="margin: 0 0 10px 0; font-size: 14px; color: #444; line-height: 1.6;"><strong>专线优势：</strong> IEPL企业级全专线中转，超大带宽保障，完美支持全平台客户端一键订阅导入，外贸与重度用户首选。</p>
    <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: linear-gradient(90deg, #0066cc, #1a8cff); color: #ffffff; padding: 10px 22px; border-radius: 6px; font-weight: bold; text-decoration: none; font-size: 15px; box-shadow: 0 3px 6px rgba(0,102,204,0.3);">👉 官方注册入口：前往【暮光网络】官网开通体验</a>
  </div>

  <div style="margin-bottom: 16px; padding: 14px; background: #ffffff; border-radius: 8px; border-left: 6px solid #28a745; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0; color:#1e7e34; font-size: 17px;">🥉 第3名：飞猫云 - 老牌高性价比稳定机场（抗敏感期封锁）</h4>
    <p style="margin: 0 0 10px 0; font-size: 14px; color: #444; line-height: 1.6;"><strong>专线优势：</strong> 多年老牌口碑沉淀，IPLC内网专线保障，不限制个人设备连接数，价格平民且全天候节点高可用。</p>
    <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: linear-gradient(90deg, #28a745, #34ce57); color: #ffffff; padding: 10px 22px; border-radius: 6px; font-weight: bold; text-decoration: none; font-size: 15px; box-shadow: 0 3px 6px rgba(40,167,69,0.3);">👉 官方注册入口：前往【飞猫云】官网开通体验</a>
  </div>

  <div style="margin-bottom: 10px; padding: 14px; background: #ffffff; border-radius: 8px; border-left: 6px solid #6f42c1; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0; color:#512da8; font-size: 17px;">🏅 第4名：微风网络 Breezenet - 极速轻量与防失联备用推荐</h4>
    <p style="margin: 0 0 10px 0; font-size: 14px; color: #444; line-height: 1.6;"><strong>专线优势：</strong> 极速切线与低成本体验，包含便宜月付与低流量年付方案，适合小白入门与备用网络保障。</p>
    <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: linear-gradient(90deg, #6f42c1, #8762d6); color: #ffffff; padding: 10px 22px; border-radius: 6px; font-weight: bold; text-decoration: none; font-size: 15px; box-shadow: 0 3px 6px rgba(111,66,193,0.3);">👉 官方注册入口：前往【微风网络】官网开通体验</a>
  </div>
</div>
"""

master_post_content = f"""---
title: "【2026全网最全】28家主流稳定机场推荐与官网注册链接大全（含价格/节点/AI解锁/专线测评）"
date: 2026-09-28
draft: false
tags: ["稳定机场推荐", "梯子稳定推荐", "机场稳定网", "晚高峰不卡顿机场", "所有机场注册大全"]
categories: ["稳定机场推荐"]
categories_name: "稳定机场推荐"
description: "汇总全网28家主流翻墙梯子与机场服务，提供官网注册链接、机场简介、月流量、周期/类型、专线评测及ChatGPT解锁支持全方位对比。"
---

# 【2026全网最全】28家主流稳定机场推荐与官网注册链接大全

编辑部为您整理了全网 28 家优质机场的**详细简介、月流量、周期/类型、线路架构、AI解锁能力、站内深度测评链接与官方直达注册入口**。

{top4_box}

## 28家稳定机场详细资料与注册链接汇总表

| 排名 | 机场名称 | 机场简介 | 参考价格 | 流量 | 周期/类型 | 线路类型 | 流媒体与AI解锁 | 机场测评 | 官方注册入口 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
"""

for ap in airports_extended_data:
    btn_text = f"👉 注册{ap['short_name']}"
    review_btn = f"<a href='{ap['review_url']}' style='background:#1e293b; color:#38bdf8; padding:4px 10px; border-radius:6px; border:1px solid #334155; text-decoration:none; font-size:12px; font-weight:bold; white-space:nowrap; display:inline-block;'>🔍 查看测评</a>"
    aff_btn = f"<a href='{ap['aff_url']}' target='_blank' rel='sponsored nofollow noopener' style='background:linear-gradient(90deg, #0066cc, #1a8cff); color:#ffffff; padding:6px 14px; border-radius:6px; font-weight:bold; text-decoration:none; white-space:nowrap; display:inline-block;'>{btn_text}</a>"
    
    master_post_content += f"| {ap['rank']} | **{ap['name']}** | {ap['intro']} | {ap['price']} | {ap['traffic']} | {ap['period_type']} | {ap['lines']} | {ap['ai_unlock']} | {review_btn} | {aff_btn} |\n"

master_post_content += f"""

---

官方 Telegram 交流频道：[https://t.me/+uVUK4-hZhZZjYzk9](https://t.me/+uVUK4-hZhZZjYzk9)
"""

master_post_path = os.path.join(BASE, "content", "posts", "jichang-tuijian", "all-airports-guide.md")
with open(master_post_path, "w", encoding="utf-8") as f:
    f.write(master_post_content)

print("Updated all-airports-guide.md with 10 detailed columns!")
