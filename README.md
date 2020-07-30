# pingan-scripture-gen 《平安经》生成器

## 这是什么

`pingan-scripture-gen` 是一个 CLI 工具，它可以快速地生成[《平安经》](https://baike.baidu.com/item/%E5%B9%B3%E5%AE%89%E7%BB%8F/52832038) 经文，主要用途就是拿来水著作（保平安）。

## 前置条件

需要 Python 3。

## 版本日志

| 发布时间 | 版本 | 说明 |
| ---- | ---- | ---- |
| 2020-07-30 | v0.0.0-preview | 初始版本（预览版） |  

## 如何使用

在 Shell/命令行中执行：

```shell script
python ./main.py
```

执行后，会在 `out` 目录输出 [`scripture.md`](out/scripture.md) 文件。然后您就可以使用任何一款 Markdown 查看器打开这个文件来欣赏您的佳作，陶冶性情。

## 自定义

默认情况下，生成的是《平安经》，您完全可以改成《快乐经》、《啥也不是经》或者任何其他经。只需要修改 **清单文件** `manifest.json` 文件的 `word` 属性即可。

### 清单文件属性说明

- `author` 作者，可以改成你自己名字。
- `title` 头衔。这个 v0.0.0 还没有实现。
- `publisher` 出版社。这个 v0.0.0 还没有实现。
- `word` 经文主旨词。例如改成“脑残”，就会生成《脑残经》。

### 经文内容

经文内容在 `lists` 文件夹中。请遵循下列协议来自定义经文。

文件夹定义了经书的结构（章节、子章节等），每个 txt 文件则定义了一篇经文。

每个文件夹中中都有个 `_manifest.txt` 文件，这是一个章节和经文的清单。文件格式定义如下：

- UTF-8 编码。
- 空白行和 `#` 开头的注释行会被忽略。
- 每行表示一个章节的文件夹名称，或者一篇经文的文件名称。
- 如果标题中包含文件系统不允许的字符（例如`/`），请使用 `<文件(夹)名>=<标题>`。例如：`国家地区=国家/地区`，会生成一个名为「国家/地区」的标题，其子章节或经文内容就来自于“国家地区”这个目录。
- 经文的 txt 文件定义相当简单，每行表示经文中主旨词前的语句。同样的，空白行和 `#` 开头的注释行会被忽略。平安经生成器会按顺序将他们接上主旨词生成经文。

### 已知的问题

1. 这是一个除了嘲讽某领导和他的傻逼作品之外，完全没什么用的工具。所以请不要在生产环境中使用该软件。由此造成的任何后果与作者无关。
2. 由于我并没有找到《平安经》的全文，所以 `lists` 文件夹并不包含完整的数据。欢迎各位提 PR 补充。

### 协议

本软件在「你TM想干嘛就干嘛」公共许可证下发布。

>            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
>                    Version 2, December 2004
> 
> Copyright (C) 2020 cheer <x****@tongji.edu.cn>
> 
> Everyone is permitted to copy and distribute verbatim or modified
> copies of this license document, and changing it is allowed as long
> as the name is changed.
> 
>            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
>   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
> 
>  0. You just DO WHAT THE FUCK YOU WANT TO.
