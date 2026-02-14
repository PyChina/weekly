#!/usr/bin/env python3
"""
自动修复 Markdown 文件中图片缺少 alt 属性的问题
"""

import os
import re
import sys
from pathlib import Path


def extract_filename_from_url(url):
    """从 URL 提取文件名作为 alt 文本"""
    # 解码 hex 编码的 URL
    if all(c in '0123456789abcdefABCDEF' for c in url[:20]) and len(url) > 20:
        try:
            decoded = bytes.fromhex(url).decode('utf-8', errors='ignore')
            if decoded:
                url = decoded
        except:
            pass
    
    # 提取文件名
    filename = os.path.basename(url.split('?')[0].split('#')[0])
    
    # 移除扩展名
    name = os.path.splitext(filename)[0]
    
    # 如果文件名是乱码或太短，返回通用描述
    if len(name) < 3 or re.match(r'^[0-9a-f]{20,}$', name, re.I):
        return "图片"
    
    # 替换特殊字符
    name = name.replace('-', ' ').replace('_', ' ')
    
    return name[:50]  # 限制长度


def fix_md_file(filepath):
    """修复单个 Markdown 文件中的图片 alt 属性"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    fixes = []
    
    # 模式 1: ![alt](url) - 已经有 alt 的跳过
    # 模式 2: ![](url) - 需要修复
    # 使用正则匹配 ![...](url)
    
    def replace_empty_alt(match):
        alt_text = match.group(1)
        url = match.group(2)
        
        if alt_text.strip():
            return match.group(0)  # 已有 alt，保持不变
        
        new_alt = extract_filename_from_url(url)
        fixes.append(f"  - {url[:60]}... -> alt: '{new_alt}'")
        return f'![{new_alt}]({url})'
    
    # 修复 ![](url) 格式
    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_empty_alt, content)
    
    # 修复 <img src="..." /> 格式（没有 alt 属性的）
    def replace_img_tag(match):
        before = match.group(1)
        src = match.group(2)
        after = match.group(3)
        
        # 检查是否已有 alt 属性
        if 'alt=' in before or 'alt=' in after:
            return match.group(0)
        
        new_alt = extract_filename_from_url(src)
        fixes.append(f"  - <img src={src[:60]}...> -> alt: '{new_alt}'")
        return f'<img{before}src="{src}" alt="{new_alt}"{after}>'
    
    content = re.sub(r'<img([^>]*)src="([^"]+)"([^>]*)/?>', replace_img_tag, content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return fixes
    
    return []


def scan_and_fix_content_dir(content_dir):
    """扫描并修复 content 目录下的所有 markdown 文件"""
    content_path = Path(content_dir)
    all_fixes = {}
    
    for md_file in content_path.rglob('*.md'):
        fixes = fix_md_file(md_file)
        if fixes:
            all_fixes[str(md_file)] = fixes
    
    return all_fixes


def main():
    content_dir = sys.argv[1] if len(sys.argv) > 1 else 'content'
    
    print(f"扫描目录: {content_dir}")
    print("=" * 60)
    
    fixes = scan_and_fix_content_dir(content_dir)
    
    if fixes:
        print(f"\n共修复 {len(fixes)} 个文件:")
        for filepath, file_fixes in fixes.items():
            print(f"\n{filepath}:")
            for fix in file_fixes:
                print(fix)
        return 1
    else:
        print("未发现需要修复的图片 alt 属性")
        return 0


if __name__ == '__main__':
    sys.exit(main())
