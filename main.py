#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author   : cheer
# @Copyright: No FUCKING rights reserved.

import json
import os.path
import os
from utils import to_chinese


def gen_content(f, word: str, curr_dir: str = 'lists'):
    manifest_file = os.path.join(curr_dir, '_manifest.txt')
    if not os.path.isfile(manifest_file):
        print(f'{curr_dir}：找不到清单文件。')
        return

    depth = len(manifest_file.split(os.sep))
    root = depth == 2
    with open(manifest_file, 'r', encoding='utf-8') as mf:
        seq = 0
        for line in mf:
            line = line.strip()
            if not line or line.startswith('#'):
                # 忽略掉注释行和空白行
                continue

            parts = line.split('=', 2)
            dir_or_file = parts[0]
            title = parts[1] if len(parts) == 2 else os.path.splitext(dir_or_file)[0]

            if root:
                seq = seq + 1
                f.write(f'## 第{to_chinese(seq)}篇 {title}{word}\n\n')
            else:
                f.write(f'{"#" * depth} {title}{word}\n\n')

            dir_or_file = os.path.join(curr_dir, dir_or_file)
            if os.path.isfile(dir_or_file):
                # 读取文章内容
                with open(dir_or_file, 'r', encoding='utf-8') as af:
                    lines = (f'{line.strip()}{word}' for line in af if line.strip())
                    f.write('　　' + '，'.join((f'{line}' for line in lines)) + '。\n\n')
            elif os.path.isdir(dir_or_file):
                gen_content(f, word, dir_or_file)
            else:
                print(f'{dir_or_file}：文件或目录不存在。')


def main():
    with open('manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    with open('out/scripture.md', 'w', encoding='utf-8') as f:
        word = manifest["word"]
        # 写标题
        f.write(f'# {word}经\n\n')
        # 写作者
        f.write('作者：' + manifest.get('author', '佚名') + '\n\n')
        # 写内容
        gen_content(f, word)

    print('生成完成。')


if __name__ == '__main__':
    main()
