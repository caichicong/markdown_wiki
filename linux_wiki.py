# -*- coding:utf-8 -*-
import markdown
import codecs
import os
import shutil
import time
import stat
import sys
from urllib import quote

template_file_path = '/home/cong/note/template.html'
index_template_file_path = '/home/cong/note/index_template.html'
output_path = '/home/cong/note/'
input_path = '/home/cong/Nutstore/markdown/'
now_timestamp = int(time.time())

update_all = True

if len(sys.argv) == 2 and sys.argv[1] == 'all':
    update_all = True
else:
    update_all = False

def generate_html(markdown_file_path, html_file_path, template_file_path):
    template_file = codecs.open(template_file_path, mode="r", encoding="utf-8")
    template = template_file.read()
    template_file.close()

    markdown_file = codecs.open(markdown_file_path, mode="r", encoding="utf-8")
    text = markdown_file.read()
    markdown_file.close()

    html = markdown.markdown(text, ['extra'])
    html_file = codecs.open(html_file_path, "w", encoding="utf-8", errors="xmlcharrefreplace")

    # for linux
    content = template.replace('{body}', html).replace('{title}', markdown_file_path.decode('utf-8'))
    html_file.write(content)
    html_file.close()



if not update_all:
    for root, dirs, files in os.walk(input_path):    
        for f in files:
            if f.endswith('.md'):
                mdfile = os.path.join(root, f)
                fsstat = os.stat(mdfile)
                if now_timestamp - fsstat[stat.ST_MTIME] < 21600:
                    print mdfile
                    generate_html(mdfile, mdfile.replace(input_path, output_path), template_file_path)
    exit()



# delete all dir in output directory
paths = os.listdir(output_path) 
for path in paths:
    file_path = os.path.join(output_path, path)
    if os.path.isdir(file_path):
        shutil.rmtree(file_path, True)


# create dir 
categories = []
for c in os.listdir(input_path):
    if os.path.isdir(os.path.join(input_path, c)):
        os.mkdir(os.path.join(output_path, c))
        categories.append(c)

wiki_dir = {} 

for c in categories:
    wiki_dir[c] = []
    catepath = os.path.join(input_path, c)
    out_catepath = os.path.join(output_path, c)
    for f in os.listdir(catepath):
        # markdown file
        if f.endswith('.md'):
            md_file_path = os.path.join(catepath, f)
            html_file_path = os.path.join(out_catepath, f.replace('.md', '.html'))
            generate_html(md_file_path, html_file_path, template_file_path)
            print md_file_path
            wiki_dir[c].append(f.replace('.md', ''))
        # image file
        elif f.endswith('.png') or f.endswith('.jpg')  or f.endswith('.gif'):
		    shutil.copy(os.path.join(catepath, f), os.path.join(out_catepath, f))

# create index file

index_file_tpl = open(index_template_file_path).read()
index_file = open(os.path.join(output_path, 'index.html'), 'w')

body = ''
for c in wiki_dir:
    body += '<div>%s</div>\n' % c
    body += '<ul>\n'
    for title in wiki_dir[c]:
        # for linux
        body += '<li><a href="%s">%s</a></li>\n' % (quote(c) + '/' + quote(title) + '.html', title)
    body += '</ul>\n'

# for linux
index_file_content = index_file_tpl.replace('{body}', body).replace('{title}', u'我的笔记'.encode('utf-8'))
index_file.write(index_file_content)

