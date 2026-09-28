import os
import json
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

# Ensure directories exist
directories = [
    os.path.join(BASE_DIR, "content", "posts", "jichang-tuijian"),
    os.path.join(BASE_DIR, "content", "posts", "jiaocheng"),
    os.path.join(BASE_DIR, "content", "posts", "pingce"),
    os.path.join(BASE_DIR, "content", "posts", "faq"),
    os.path.join(BASE_DIR, "content", "posts", "daohang"),
    os.path.join(BASE_DIR, "docs"),
    os.path.join(BASE_DIR, "layouts", "partials"),
    os.path.join(BASE_DIR, "layouts", "shortcodes"),
    os.path.join(BASE_DIR, "static"),
]

for d in directories:
    os.makedirs(d, exist_ok=True)

tg_channel = "https://t.me/+uVUK4-hZhZZjYzk9"

# Airports data dictionary
airports_data = [
    {
        "rank": 1,
        "name": "灵动云",
        "url": "https://varnexa.lingdongaff.com/#/?code=JoIy7bO1",
        "tag": "【2026年度冠军 · 稳定性之王】",
        "desc": "全站首推顶级IPLC/BGP专线机场，针对晚高峰4K影音与ChatGPT大模型做了专属链路优化。全天候抗封锁，丢包率趋于0%，小白首选。",
        "price": "￥15.00 / 月起",
        "traffic": "150GB - 2000GB / 月",
        "lines": "原生IPLC专线 + BGP多线中转",
        "ai_unlock": "完全解锁 ChatGPT / Claude / Midjourney / Netflix / Disney+ / Youtube 4K"
    },
    {
        "rank": 2,
        "name": "暮光网络",
        "url": "https://varnexa.twilightaff.com/#/?code=KvGly3jY",
        "tag": "【晚高峰不卡顿 · 影音办公首选】",
        "desc": "极高性价比与高带宽专线，晚高峰时段稳定流畅播放4K/8K视频。节点覆盖港台美日新英等地区，具备多端协同一键导入功能。",
        "price": "￥18.00 / 月起",
        "traffic": "200GB - 3000GB / 月",
        "lines": "IEPL企业级专线 + 广深/沪日专线",
        "ai_unlock": "完美支持 AI工具全家桶 + HIFI无损音频流媒体"
    },
    {
        "rank": 3,
        "name": "飞猫云",
        "url": "https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH",
        "tag": "【老牌稳定梯子 · 多设备并发】",
        "desc": "运营多年口碑优异，具备超强抗敏感期能力。节点延迟低至30ms，支持不限制设备数连接，特别适合家庭多设备与外贸团队。",
        "price": "￥12.00 / 月起",
        "traffic": "100GB - 1500GB / 月",
        "lines": "BGP入口 + IPLC内网专线",
        "ai_unlock": "全节点支持 OpenAI API 与主流海外流媒体"
    },
    {
        "rank": 4,
        "name": "微风网络 Breezenet",
        "url": "https://edp01.breezenetaff.com/#/?code=He4n3zxg",
        "tag": "【轻量高效 · 备用防失联首选】",
        "desc": "主打极速响应与低门槛体验，套餐灵活且支持按量付费或便宜年付。线路经过多重加密，节点维护迅速，断连自动切线。",
        "price": "￥9.90 / 月起",
        "traffic": "80GB - 1000GB / 月",
        "lines": "优质BGP中转 + 动静结合节点",
        "ai_unlock": "支持网页端与客户端常见流媒体及AI应用"
    },
    {
        "rank": 5,
        "name": "隐形人",
        "url": "https://varnexa.invisibleaff.com/#/?code=FlyoraeM",
        "tag": "【隐私安全 · 隐形加密专线】",
        "desc": "注重用户隐私保护与高度匿名传输，协议经过二次混淆加密，绝无日志留存。",
        "price": "￥20.00 / 月起",
        "traffic": "180GB / 月",
        "lines": "隧道中转 + 专线",
        "ai_unlock": "支持主流 AI 与海外应用"
    },
    {
        "rank": 6,
        "name": "浪网 WaveNet",
        "url": "https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ",
        "tag": "【冲浪极速 · 大带宽节点】",
        "desc": "专为大流量冲浪与文件下载设计，千兆带宽端口，晚高峰依然能拉满速。",
        "price": "￥22.00 / 月起",
        "traffic": "500GB / 月",
        "lines": "千兆BGP中转",
        "ai_unlock": "解锁4K/8K视频及AI工具"
    },
    {
        "rank": 7,
        "name": "梯子云 LadderCloud",
        "url": "https://varnexa.ladderaff.com/#/?code=bYVSMHMh",
        "tag": "【多协议兼容 · 稳定梯子】",
        "desc": "支持 Clash / Shadowrocket / Sing-box / V2ray 等全平台客户端订阅导入。",
        "price": "￥16.80 / 月起",
        "traffic": "200GB / 月",
        "lines": "混合专线",
        "ai_unlock": "全面支持ChatGPT与流媒体"
    },
    {
        "rank": 8,
        "name": "飞V",
        "url": "https://varnexa.flyvaff.com/#/?code=qaMgTyhY",
        "tag": "【极速飞驰 · 游戏低延迟】",
        "desc": "专门针对亚服、美服游戏与实时语音进行了节点优化，低延迟不掉线。",
        "price": "￥19.90 / 月起",
        "traffic": "250GB / 月",
        "lines": "游戏加速专线",
        "ai_unlock": "支持基础流媒体与AI工具"
    },
    {"rank": 9, "name": "星岛梦", "url": "https://kfccbb.xingdaomeng.com/#/?code=tLbhLnNf", "tag": "【梦幻速度】", "desc": "高性价比节点服务，线路稳定。", "price": "￥15.00/月", "traffic": "150GB", "lines": "BGP中转", "ai_unlock": "支持流媒体"},
    {"rank": 10, "name": "光速云", "url": "https://mdlky.gsyaff.com/#/?code=5snwJVcD", "tag": "【光速传输】", "desc": "极速网络响应，晚高峰表现出色。", "price": "￥18.00/月", "traffic": "200GB", "lines": "IPLC专线", "ai_unlock": "解锁ChatGPT"},
    {"rank": 11, "name": "唯兔云（V2云）", "url": "https:/fast.v2yunvipaff.com/#/?code=xkiG3YWN", "tag": "【V2协议专家】", "desc": "深度优化V2ray协议，抗封锁能力强。", "price": "￥12.00/月", "traffic": "120GB", "lines": "优质中转", "ai_unlock": "支持AI与视频"},
    {"rank": 12, "name": "U1S1（有一说一）", "url": "https://pkdj7.vipaff.cc/#/?code=nYbe5pKy", "tag": "【真实实在】", "desc": "价格透明，无虚标流量，稳定运行。", "price": "￥10.00/月", "traffic": "100GB", "lines": "BGP中转", "ai_unlock": "解锁主流服务"},
    {"rank": 13, "name": "极连云", "url": "https://kdjhao.jlyvipaff.com/#/?code=rO50GIZj", "tag": "【极速连接】", "desc": "秒连节点，多地域选择。", "price": "￥16.00/月", "traffic": "180GB", "lines": "多入口中转", "ai_unlock": "全流媒体解锁"},
    {"rank": 14, "name": "全球云", "url": "https://sswdh.gcvipaff.com/#/?code=Ys0xKqnU", "tag": "【全球覆盖】", "desc": "拥有上百个全球节点，适合跨境办公。", "price": "￥25.00/月", "traffic": "350GB", "lines": "全球IPLC专线", "ai_unlock": "完全解锁AI与流媒体"},
    {"rank": 15, "name": "光年梯", "url": "https://ggmq.gntaff.com/#/?code=34i9Naos", "tag": "【光年速度】", "desc": "超低延迟，全天候稳定可用。", "price": "￥14.00/月", "traffic": "130GB", "lines": "专线中转", "ai_unlock": "支持ChatGPT"},
    {"rank": 16, "name": "Sogo云", "url": "https://wzjc.sogoyunaff.cc/#/?code=nWA62UuJ", "tag": "【便民平价】", "desc": "适合预算有限的小白用户。", "price": "￥8.80/月", "traffic": "80GB", "lines": "普通BGP", "ai_unlock": "基础解锁"},
    {"rank": 17, "name": "宇宙云 YuZhou", "url": "https://wzjc.yuzoucloud.cc/#/?code=hMqs74rd", "tag": "【海量流量】", "desc": "超大流量包，适合重度下载用户。", "price": "￥30.00/月", "traffic": "1000GB", "lines": "千兆中转", "ai_unlock": "支持4K流媒体"},
    {"rank": 18, "name": "二猫云 2mao", "url": "https://waaa.2maoyunaff.cc/#/?code=tbIH9UGF", "tag": "【双线备用】", "desc": "双入口冗余，防止断连。", "price": "￥13.00/月", "traffic": "120GB", "lines": "双路BGP", "ai_unlock": "支持主流软件"},
    {"rank": 19, "name": "一翻云 1fly", "url": "https://wzjc.1flyunaff.cc/#/?code=vq9IugSn", "tag": "【一键翻墙】", "desc": "傻瓜式配置，导入即用。", "price": "￥15.00/月", "traffic": "150GB", "lines": "智能中转", "ai_unlock": "解锁AI"},
    {"rank": 20, "name": "边缘节点 EdgeNova", "url": "https://work.edgenovaaff.cc/#/?code=6Mi7km72", "tag": "【边缘加速】", "desc": "基于边缘计算架构的节点服务。", "price": "￥20.00/月", "traffic": "200GB", "lines": "Edge专线", "ai_unlock": "全平台解锁"},
    {"rank": 21, "name": "可信云", "url": "https://work.kosingaff.com/#/?code=BmIpbeEn", "tag": "【可信安全】", "desc": "高安全加密，适合商务办公。", "price": "￥22.00/月", "traffic": "220GB", "lines": "加密IPLC", "ai_unlock": "解锁办公与AI"},
    {"rank": 22, "name": "速界 SuJie", "url": "https://work.speedworldaff.cc/#/?code=YhcpJLbr", "tag": "【速界极速】", "desc": "专线抗压，晚高峰不卡顿。", "price": "￥17.00/月", "traffic": "160GB", "lines": "IEPL专线", "ai_unlock": "解锁流媒体"},
    {"rank": 23, "name": "快狸 KuaiLi", "url": "https://work.kuailicloud.cc/#/?code=7BsufMC0", "tag": "【灵动快速】", "desc": "节点切换迅速，稳定性好。", "price": "￥14.50/月", "traffic": "140GB", "lines": "BGP中转", "ai_unlock": "支持主流应用"},
    {"rank": 24, "name": "无忧", "url": "https://wep01.worryfreeaff.com/#/?code=vak0gPse", "tag": "【上网无忧】", "desc": "无忧断连，售后维护及时。", "price": "￥15.00/月", "traffic": "150GB", "lines": "混合线路", "ai_unlock": "支持流媒体"},
    {"rank": 25, "name": "灵猫", "url": "https://vip02.civetaff.com/#/?code=Z4KLo3Wz", "tag": "【灵活轻盈】", "desc": "套餐种类多，支持按需定制。", "price": "￥11.00/月", "traffic": "100GB", "lines": "中转线路", "ai_unlock": "支持ChatGPT"},
    {"rank": 26, "name": "闪跃 FlashLeap", "url": "https://vip02.flashleapaff.com/#/?code=wnLaKVaU", "tag": "【闪电跳跃】", "desc": "延迟极低，网页加载秒开。", "price": "￥19.00/月", "traffic": "200GB", "lines": "闪跃专线", "ai_unlock": "全面解锁"},
    {"rank": 27, "name": "飞为（Firefly）", "url": "https://vip02.fireflyaff.com/#/?code=1n1ZIJab", "tag": "【萤火星光】", "desc": "稳定运营，线路优化到位。", "price": "￥16.00/月", "traffic": "150GB", "lines": "BGP专线", "ai_unlock": "支持AI与视频"},
    {"rank": 28, "name": "跨界", "url": "https://vip02.kuajieaff.com/#/?code=RQ4b2tfV", "tag": "【跨界互联】", "desc": "适合跨境电商与海外社交媒体运营。", "price": "￥28.00/月", "traffic": "300GB", "lines": "跨境原生IP专线", "ai_unlock": "全流媒体+TikTok+AI"}
]

# Helper to produce Top 4 Recommendation Box in Markdown
def get_top4_recommendation_box():
    return f"""
<div style="background: linear-gradient(135deg, #f6f8fa 0%, #e9edf2 100%); border: 2px solid #0066cc; border-radius: 10px; padding: 20px; margin: 25px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
  <h3 style="color: #0066cc; margin-top: 0; font-size: 20px; border-bottom: 2px solid #0066cc; padding-bottom: 8px;">🔥 2026年四大核心稳定机场推荐榜单（编辑部重磅首推）</h3>
  <p style="font-size: 14px; color: #555; margin-bottom: 15px;">以下4家机场均经过编辑部晚高峰实测，具备极高稳定性、抗封锁能力与4K超清解锁能力，请根据个人需求选择：</p>
  
  <div style="margin-bottom: 15px; padding: 12px; background: #fff; border-radius: 6px; border-left: 5px solid #ff4d4f;">
    <h4 style="margin:0 0 5px 0; color:#d9363e;">🥇 第1名：灵动云 - 2026年度稳定性与速度总冠军</h4>
    <p style="margin: 0 0 8px 0; font-size: 14px; color: #444;"><strong>特点：</strong> 原生IPLC专线+BGP中转，晚高峰4K秒开，丢包率趋于0%，完全解锁ChatGPT/Claude与Netflix。</p>
    <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: #ff4d4f; color: #fff; padding: 8px 18px; border-radius: 5px; font-weight: bold; text-decoration: none; font-size: 14px;">👉 显眼入口：前往【灵动云】官网注册开通</a>
  </div>

  <div style="margin-bottom: 15px; padding: 12px; background: #fff; border-radius: 6px; border-left: 5px solid #1890ff;">
    <h4 style="margin:0 0 5px 0; color:#096dd9;">🥈 第2名：暮光网络 - 晚高峰不卡顿与影音办公首选</h4>
    <p style="margin: 0 0 8px 0; font-size: 14px; color: #444;"><strong>特点：</strong> IEPL企业级专线，高带宽大流量，多端协同订阅导入，适合长视频观赏与大文件传输。</p>
    <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: #1890ff; color: #fff; padding: 8px 18px; border-radius: 5px; font-weight: bold; text-decoration: none; font-size: 14px;">👉 显眼入口：前往【暮光网络】官网注册开通</a>
  </div>

  <div style="margin-bottom: 15px; padding: 12px; background: #fff; border-radius: 6px; border-left: 5px solid #52c41a;">
    <h4 style="margin:0 0 5px 0; color:#389e0d;">🥉 第3名：飞猫云 - 老牌稳定梯子与多设备并发推荐</h4>
    <p style="margin: 0 0 8px 0; font-size: 14px; color: #444;"><strong>特点：</strong> 运营多年口碑相传，超强抗敏感期断连，不限设备连接数，性价比极高。</p>
    <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: #52c41a; color: #fff; padding: 8px 18px; border-radius: 5px; font-weight: bold; text-decoration: none; font-size: 14px;">👉 显眼入口：前往【飞猫云】官网注册开通</a>
  </div>

  <div style="margin-bottom: 10px; padding: 12px; background: #fff; border-radius: 6px; border-left: 5px solid #722ed1;">
    <h4 style="margin:0 0 5px 0; color:#531dab;">🏅 第4名：微风网络 Breezenet - 轻量高效与防失联备用</h4>
    <p style="margin: 0 0 8px 0; font-size: 14px; color: #444;"><strong>特点：</strong> 极速响应低门槛，支持便宜月付/年付，防封锁能力出众，适合新手入坑与备用节点。</p>
    <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" style="display: inline-block; background: #722ed1; color: #fff; padding: 8px 18px; border-radius: 5px; font-weight: bold; text-decoration: none; font-size: 14px;">👉 显眼入口：前往【微风网络】官网注册开通</a>
  </div>
</div>
"""

print("Generator helper defined successfully.")
