from bs4 import BeautifulSoup
from markdownify import markdownify
import os

def html2md(html: str):
    with open(html) as f:
        soup = BeautifulSoup(f.read(), "lxml")

    main = soup.find('main')
    md = markdownify(str(main))
    h2 = soup.find('h2')
    if h2 is None:
        h2 = ''
    else:
        h2 = h2.text
    front = (
        '---',
        f'title: {h2}',
        '---',
    )
    return '\n'.join(front)+md

def html2md_in_dir(input: str, output: str):
    if not os.path.exists(input):
        raise FileNotFoundError(f'Directory `{input}` not found.')
    if not os.path.exists(output):
        os.mkdir(output)

    dir_list = os.listdir(input)
    html_list = [html for html in dir_list if html.endswith('.html')]

    for html in html_list:
        md = html2md(input+'/'+html)
        with open(output+'/'+os.path.splitext(html)[0]+'.md', 'w') as f:
            f.write(md)

if __name__=="__main__":
    html2md_in_dir('html', 'md2')
