import os
import re
import sys
import subprocess

try:
    import opencc
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencc"])
    import opencc

converter = opencc.OpenCC('s2twp.json')

def translate_file(src, dst):
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate content
    translated = converter.convert(content)
    
    # Replace variable names zhCN to zhTW
    translated = re.sub(r'zhCN', 'zhTW', translated)
    
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(translated)
    print(f"Translated {src} to {dst}")

base_dir = '/Users/liyungchih/.gemini/antigravity/scratch/openhuman/app/src/lib/i18n'
chunks_dir = os.path.join(base_dir, 'chunks')

for i in range(1, 6):
    src = os.path.join(chunks_dir, f'zh-CN-{i}.ts')
    dst = os.path.join(chunks_dir, f'zh-TW-{i}.ts')
    translate_file(src, dst)

src_index = os.path.join(base_dir, 'zh-CN.ts')
dst_index = os.path.join(base_dir, 'zh-TW.ts')
with open(src_index, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('zh-CN', 'zh-TW').replace('zhCN', 'zhTW')
with open(dst_index, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Created {dst_index}")
