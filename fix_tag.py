import xml.etree.ElementTree as ET
import os
import re
from pathlib import Path

# 設定檔案路徑
xml_file = r'c:\Users\henry\Downloads\blog-03-06-2025.xml'  # 原始 Blogger XML 檔案
hugo_posts_dir = 'content/posts'  # 修正為實際的 Hugo 文章目錄

# 定義命名空間
ns = {
    'atom': 'http://www.w3.org/2005/Atom',
}

# 解析 XML
tree = ET.parse(xml_file)
root = tree.getroot()

# 建立文章標題到標籤的映射
title_to_tags = {}
url_to_tags = {}

# 從 XML 提取所有文章的標題和標籤
for entry in root.findall('.//atom:entry', ns):
    # 跳過評論和模板
    if entry.find('.//atom:category[@term="http://schemas.google.com/blogger/2008/kind#comment"]', ns) is not None:
        continue
    if entry.find('.//atom:category[@term="http://schemas.google.com/blogger/2008/kind#template"]', ns) is not None:
        continue
    
    # 獲取標題
    title_elem = entry.find('./atom:title', ns)
    if title_elem is None or title_elem.text is None:
        continue
    
    title = title_elem.text.strip()
    
    # 獲取連結
    link = entry.find('./atom:link[@rel="alternate"]', ns)
    url = link.get('href') if link is not None else ""
    
    # 提取標籤
    tags = []
    for category in entry.findall('./atom:category', ns):
        term = category.get('term')
        # 只處理實際的標籤，排除 Blogger 系統標籤
        if term and not term.startswith('http://schemas.google.com/blogger/2008/kind#'):
            tags.append(term)
    
    # 儲存標題到標籤的映射
    title_to_tags[title] = tags
    if url:
        url_to_tags[url] = tags

# 處理每個 Hugo 文章
count = 0
for file_path in Path(hugo_posts_dir).glob('*.md'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析前置元數據
    front_matter_match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not front_matter_match:
        continue
    
    front_matter = front_matter_match.group(1)
    
    # 檢查是否已有標籤
    if 'tags:' in front_matter:
        continue
    
    # 提取標題
    title_match = re.search(r'title:\s*"(.*?)"', front_matter)
    if not title_match:
        continue
    
    title = title_match.group(1)
    
    # 提取 URL
    url_match = re.search(r'url:\s*"(.*?)"', front_matter)
    url = url_match.group(1) if url_match else ""
    
    # 查找對應的標籤
    tags = title_to_tags.get(title, [])
    if not tags and url:
        tags = url_to_tags.get(url, [])
    
    if not tags:
        continue
    
    # 添加標籤到前置元數據
    new_front_matter = front_matter
    if tags:
        # 確保在前置元數據的最後添加標籤
        new_front_matter += f"\ntags: {tags}"
    
    # 更新文件內容
    new_content = content.replace(front_matter_match.group(0), f"---\n{new_front_matter}\n---")
    
    # 寫回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    count += 1
    print(f"已更新: {file_path.name}")

print(f"完成！共更新了 {count} 個文章")