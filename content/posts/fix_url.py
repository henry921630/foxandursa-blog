import os
import re
from pathlib import Path

# 指定包含Markdown文件的目录
content_dir = 'content/posts'

# 遍历所有Markdown文件
for md_file in Path(content_dir).glob('*.md'):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找并替换带有协议的URL
    pattern = r'url: "https?://[^"]+"'
    
    # 方案1：提取相对路径
    def replace_url(match):
        full_url = match.group(0)
        # 从完整URL中提取相对路径
        import urllib.parse
        url_part = full_url.split('"')[1]
        parsed_url = urllib.parse.urlparse(url_part)
        relative_url = parsed_url.path
        # 移除可能的域名部分
        relative_url = relative_url.replace("/www.foxandursa.com", "")
        # 确保路径以/开头
        if not relative_url.startswith('/'):
            relative_url = '/' + relative_url
        return f'url: "{relative_url}"'
    
    # 替换URL
    modified_content = re.sub(pattern, replace_url, content)
    
    # 方案2：完全移除url字段
    # modified_content = re.sub(r'url: "https?://[^"]+"\n', '', content)
    
    # 写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"已修复: {md_file}")