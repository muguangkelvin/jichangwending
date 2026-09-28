import os
import re

public_dir = r"c:\Users\USER\Desktop\博客\jichangwending.homes\public"

print("--- VERIFYING BUILT SITE OUTPUT ---")

# 1. Check HTML files count
html_files = []
for root, dirs, files in os.walk(public_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

print(f"Total HTML pages generated: {len(html_files)}")

# 2. Check rel="sponsored nofollow noopener"
missing_rel = 0
aff_links_found = 0
for hf in html_files:
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        links = re.findall(r'<a\s+[^>]*href=["\'](https?://[^"\']+)["\'][^>]*>', content)
        for link in links:
            if any(domain in link for domain in ["lingdongaff.com", "twilightaff.com", "flycatvipaff.cc", "breezenetaff.com", "varnexa", "xingdaomeng", "gsyaff"]):
                aff_links_found += 1
                # verify rel attribute
                match = re.search(r'<a\s+[^>]*href=["\']' + re.escape(link) + r'["\'][^>]*>', content)
                if match:
                    tag = match.group(0)
                    if "sponsored" not in tag or "nofollow" not in tag or "noopener" not in tag:
                        missing_rel += 1

print(f"Affiliate links verified in HTML: {aff_links_found}")
print(f"Links missing rel='sponsored nofollow noopener': {missing_rel}")

# 3. Check Telegram channel link
tg_found = False
for hf in html_files:
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        if "https://t.me/+uVUK4-hZhZZjYzk9" in content:
            tg_found = True
            break

print(f"Telegram channel link found in built HTML: {tg_found}")

# 4. Check word counts under 2500 Chinese chars
post_dir = r"c:\Users\USER\Desktop\博客\jichangwending.homes\content\posts"
over_length = 0
for root, dirs, files in os.walk(post_dir):
    for f in files:
        if f.endswith(".md"):
            with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                text = file.read()
                # Count Chinese characters
                zh_chars = len(re.findall(r'[\u4e00-\u9fa5]', text))
                if zh_chars > 2500:
                    over_length += 1
                    print(f"Warning: {f} has {zh_chars} Chinese chars (>2500)")

print(f"Posts exceeding 2500 Chinese characters: {over_length}")
print("--- VERIFICATION COMPLETED SUCCESSFULLY ---")
