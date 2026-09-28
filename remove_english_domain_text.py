import os
import re

BASE = r"c:\Users\USER\Desktop\博客\jichangwending.homes"

print("Removing all 'jcwending.homes' English text occurrences...")

# 1. Process layout files
layouts_dir = os.path.join(BASE, "layouts")
for root, dirs, files in os.walk(layouts_dir):
    for file in files:
        if file.endswith(".html"):
            fp = os.path.join(root, file)
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
            # Replace jcwending.homes, (jcwending.homes), 域名：jcwending.homes
            content = content.replace("域名：jcwending.homes", "品牌：机场稳定网")
            content = content.replace(" (jcwending.homes)", "")
            content = content.replace("(jcwending.homes)", "")
            content = content.replace("jcwending.homes", "机场稳定网")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)

# 2. Process content files
content_dir = os.path.join(BASE, "content")
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            fp = os.path.join(root, file)
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace(" (jcwending.homes)", "")
            content = content.replace("(jcwending.homes)", "")
            content = content.replace("jcwending.homes", "机场稳定网")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)

# 3. Update build_hugoblox_site.py to ensure future builds don't re-inject it
builder_script = os.path.join(BASE, "build_hugoblox_site.py")
if os.path.exists(builder_script):
    with open(builder_script, "r", encoding="utf-8") as f:
        b_content = f.read()
    b_content = b_content.replace("域名：jcwending.homes", "品牌：机场稳定网")
    b_content = b_content.replace(" (jcwending.homes)", "")
    b_content = b_content.replace("(jcwending.homes)", "")
    b_content = b_content.replace("jcwending.homes", "机场稳定网")
    with open(builder_script, "w", encoding="utf-8") as f:
        f.write(b_content)

# 4. Update build_all_content.py
content_builder_script = os.path.join(BASE, "build_all_content.py")
if os.path.exists(content_builder_script):
    with open(content_builder_script, "r", encoding="utf-8") as f:
        c_content = f.read()
    c_content = c_content.replace(" (jcwending.homes)", "")
    c_content = c_content.replace("(jcwending.homes)", "")
    c_content = c_content.replace("jcwending.homes", "机场稳定网")
    with open(content_builder_script, "w", encoding="utf-8") as f:
        f.write(c_content)

print("English domain text 'jcwending.homes' removed from all layout & markdown files!")
