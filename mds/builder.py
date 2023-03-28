import os, sys
import re
from bs4 import BeautifulSoup as bs

sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)

from settings.github import USER, REPO, APP_NAME, GIT_URL, VERSION, DATE_UPD
from settings.customization import LOGO


# vars
paths = []
struct = {
    '&lt;': '<',
    '&gt;': '>',
    '{logo_name}': LOGO,
    '{app_name}' : APP_NAME,
    '{USER}'     : USER,
    '{REPO}'     : REPO,
    '{GIT_URL}'  : GIT_URL,
    '{VERSION}'  : VERSION,
    '{DATE_UPD}' : DATE_UPD,
}

# init soup
with open(os.path.join(os.path.dirname(__file__), 'main.md'), 'r') as f:
    # search paths
    soup = bs(f, 'html.parser')

# init stub
with open('README.stub','w') as f:
    f.write('')
# create stub
for index, inc_tag in enumerate(soup.find_all('include')):
    path = inc_tag.get('path')
    # template readme
    with open(os.path.join(os.path.dirname(__file__), path), 'r') as f:
        readme_stub = f.read()
    inc_tag.string = readme_stub
soup.include.replaceWithChildren()
# write out stub
with open('README.stub','w') as f:
    f.write(str(soup))


with open('README.stub') as f:
    r = f.read()
for key, value in struct.items():
    r = r.replace(key, value)

# write out stub
with open('README.stub','w') as f:
    f.write(str(r))

with open('README.stub') as f:
    r = f.read()

# template readme
with open('README.stub') as f:
    readme = bs(f, 'html.parser')

# put potential variables
readme.include.replaceWithChildren()
# init md
with open('README.md','w') as f:
    f.write("")
# print(readme)
readme = str(readme)\
          .replace('<include>','')\
          .replace('</include>','')
readme = re.sub(r'<include .*?>', '', readme)
with open('README.md','w') as f:
    f.write(readme)
