import os
try:
    from bs4 import BeautifulSoup
except ImportError:
    # If bs4 is not available, use regex/string split as fallback
    print("bs4 not found, using string split")
    with open('code_v2.html', 'r', encoding='utf-8') as f:
        content = f.read()
    start_tag = '<div id="smooth-content">'
    end_tag = '<footer'
    start = content.find(start_tag) + len(start_tag)
    end = content.find(end_tag, start)
    with open('home_content_final.html', 'w', encoding='utf-8') as f:
        f.write(content[start:end].strip())
    exit()

with open('code_v2.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

main = soup.find('div', id='smooth-content')
if main:
    # Remove header if it's inside
    for h in main.find_all('header'):
        h.decompose()
    # Remove footer if it's inside
    for f in main.find_all('footer'):
        f.decompose()
    # Remove navigation if it's inside
    for n in main.find_all('nav'):
        n.decompose()
    
    with open('home_content_final.html', 'w', encoding='utf-8') as f:
        f.write(main.encode_contents().decode('utf-8').strip())
    print("Success")
else:
    print("Could not find smooth-content")
