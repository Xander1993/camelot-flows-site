import codecs
import re

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'r', 'utf-8') as f:
    code = f.read()

# Find any occurrences of </main>\n''' that do not have a closing parenthesis.
fixed_code = re.sub(r'</main>\s*\'\'\'(?!\))', "</main>\\n''')", code)

with codecs.open('c:/Users/user/Downloads/stitch_camelot_flows_homepage/build_content_pages.py', 'w', 'utf-8') as f:
    f.write(fixed_code)

print("Parentheses fixed globally.")
