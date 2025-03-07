import os
import re
from pathlib import Path

# 指定包含Markdown文件的目录
content_dir = 'content/posts'

# 遍历所有Markdown文件
for md_file in Path(content_dir).glob('*.md'):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 修复普通URL图片链接
    pattern1 = r'!\[(.*?)\]\(\$(https?://[^)]+)\)'
    replacement1 = r'![\1](\2)'
    content = re.sub(pattern1, replacement1, content)
    
    # 2. 修复Data URL图片链接
    pattern2 = r'!\[(.*?)\]\(\$(data:image/[^)]+)\)'
    replacement2 = r'![\1](\2)'
    content = re.sub(pattern2, replacement2, content)
    
    # 写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已修复: {md_file}")