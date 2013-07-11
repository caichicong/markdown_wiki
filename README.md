markdown_wiki
=============

把markdown文件转换成wiki

假定markdown文件的目录结构是这样子的

	天然呆
       ---平泽唯.md
       --- 柊司.md
	傲娇
       ---凉宫春日.md
       ---2.md
	中二病
       ---樱满集.md
    

生成的html文件目录结构是这样子的

	天然呆
       ---平泽唯.html
       --- 柊司.html
	傲娇
       ---凉宫春日.html
       ---2.html
	中二病
       ---樱满集.html
    github.css
    index.html

## 功能构想

1. 一个文件夹对应一个笔记本，一个markdown对应一个笔记. 支持tag

2. 不考虑安全问题, 权限问题,  版本管理

3. 支持markdown extra语法

4. 多机同步，多平台同步问题用 **坚果云** 解决

5. 笔记之间的链接靠超链接完成 

6. 笔记的搜索考虑用coreseek解决，当然很懒的话，用grep命令解决  -_-#

## 程序流程

1 遍历指定目录下的所有文件夹，在生成目录里建立相同的文件夹

2 遍历所有markdown，生成对应的html

3 复制图片文件

4 生成目录

5 生成tag page


