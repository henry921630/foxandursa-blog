import xml.etree.ElementTree as ET
import re
import os
import html
from datetime import datetime
from pathlib import Path

# 解析XML文件
xml_file = r'c:\Users\henry\Downloads\blog-03-06-2025.xml'
output_dir = 'hugo_posts'
os.makedirs(output_dir, exist_ok=True)

# 定义命名空间
ns = {
    'atom': 'http://www.w3.org/2005/Atom',
}

# 解析XML
tree = ET.parse(xml_file)
root = tree.getroot()

# 处理每个博客文章
for entry in root.findall('.//atom:entry', ns):
    # 跳过评论和模板
    if entry.find('.//atom:category[@term="http://schemas.google.com/blogger/2008/kind#comment"]', ns) is not None:
        continue
    if entry.find('.//atom:category[@term="http://schemas.google.com/blogger/2008/kind#template"]', ns) is not None:
        continue
        
    # 获取标题、内容、日期等
    title_elem = entry.find('./atom:title', ns)
    content_elem = entry.find('./atom:content', ns)
    published_elem = entry.find('./atom:published', ns)
    
    if title_elem is None or content_elem is None or published_elem is None:
        continue
    
    title = title_elem.text or ""
    content = content_elem.text or ""
    published = published_elem.text
    
    # 获取链接
    link = entry.find('./atom:link[@rel="alternate"]', ns)
    url = link.get('href') if link is not None else ""
    
    # 转换日期格式
    try:
        pub_date = datetime.strptime(published, '%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        try:
            pub_date = datetime.strptime(published, '%Y-%m-%dT%H:%M:%S%z')
        except ValueError:
            pub_date = datetime.now()
    
    date_str = pub_date.strftime('%Y-%m-%d')
    
    # 处理HTML内容
    if content:
        # 提取图片
        img_pattern = r'<img.*?src="(.*?)".*?>'
        images = re.findall(img_pattern, content)
        
        # 转换图片标签为Markdown格式
        for img_url in images:
            img_md = f'![](${img_url})'
            img_html = f'<img.*?src="{re.escape(img_url)}".*?>'
            content = re.sub(img_html, img_md, content)
        
        # 移除其他HTML标签
        content = re.sub(r'<div.*?>|</div>', '', content)
        content = re.sub(r'<span.*?>|</span>', '', content)
        content = re.sub(r'<p>(.*?)</p>', r'\1\n\n', content)
        content = re.sub(r'<br\s*/?>', '\n', content)
        content = re.sub(r'<.*?>', '', content)
        
        # 解码HTML实体
        content = html.unescape(content)
    
    # 创建Hugo前置元数据
    front_matter = f"""---
title: "{title}"
date: {pub_date.strftime('%Y-%m-%dT%H:%M:%S%z')}
draft: false
url: "{url}"
---

{content}
"""
    
    # 创建文件名
    safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '-')
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    filename = f"{date_str}-{safe_title}.md"
    
    # 写入文件
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
        f.write(front_matter)
    
    print(f"已处理: {title}")

print(f"转换完成！文件保存在 {os.path.abspath(output_dir)} 目录")