# -*- coding:utf-8 -*-
import markdown
import codecs
import os
import shutil
from urllib import quote

# windows
# template_file_path = 'd:\\output\\template.html'
# index_template_file_path = 'd:\\output\\index_template.html'
# output_path = 'd:\\output\\'
# input_path = 'd:\\markdown\\'

# linux
template_file_path = '/home/cong/markdown_wiki/template.html'
index_template_file_path = '/home/cong/markdown_wiki/index_template.html'
output_path = '/home/cong/Desktop/output/'
input_path = '/home/cong/Desktop/input/'

# usage : generate_html('d:/markdown/a/a.md', 'd:/output/a.html', 'd:/output/template.html')

def generate_html(markdown_file_path, html_file_path, template_file_path):
    template_file = codecs.open(template_file_path, mode="r", encoding="utf-8")
    template = template_file.read()

    markdown_file = codecs.open(markdown_file_path, mode="r", encoding="utf-8")
    text = markdown_file.read()
    markdown_file.close()

    html = markdown.markdown(text, ['extra'])
    html_file = codecs.open(html_file_path, "w", encoding="utf-8", errors="xmlcharrefreplace")
    content = template.replace('{body}', html)
    html_file.write(content)

# delete all dir in output directory
paths = os.listdir(output_path) 
for path in paths:
    file_path = os.path.join(output_path, path)
    if os.path.isdir(file_path):
        shutil.rmtree(file_path, True)

# create dir
categories = os.listdir(input_path)
for c in categories:
    os.mkdir(os.path.join(output_path, c))

wiki_dir = {} 

for c in categories:
    wiki_dir[c] = []
    catepath = os.path.join(input_path, c)
    outpath = os.path.join(output_path, c)
    for f in os.listdir(catepath):
        md_file_path = os.path.join(catepath, f)
        html_file_path = os.path.join(outpath, f.replace('.md', '.html'))
        generate_html(md_file_path, html_file_path, template_file_path)
        wiki_dir[c].append(f.replace('.md', ''))

index_file_tpl = open(index_template_file_path).read()

index_file = codecs.open(os.path.join(output_path, 'index.html'), "w", encoding="utf-8", errors="xmlcharrefreplace")

body = ''
for c in wiki_dir:
    body += '<div>%s</div>\n' % c
    body += '<ul>\n'
    for title in wiki_dir[c]:
        body += '<li><a href="%s">%s</a></li>\n' % (quote(c) + '/' + quote(title) + '.html', title)
    body += '</ul>\n'

index_file_content = index_file_tpl.replace('{body}', body)

# windows 下使用gbk编码
# index_file.write(index_file_content.decode('gbk'))
index_file.write(index_file_content.decode('utf-8'))

