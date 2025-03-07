import os
import re
from pathlib import Path

# 指定包含Markdown文件的目录
content_dir = 'content/posts'

# 遍历所有Markdown文件
for md_file in Path(content_dir).glob('*.md'):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找并替换带有$的图片链接
    pattern = r'!\[(.*?)\]\(\$(https?://.*?)\)'
    replacement = r'![\1](\2)'
    
    modified_content = re.sub(pattern, replacement, content)
    
    # 写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"已修复: {md_file}")