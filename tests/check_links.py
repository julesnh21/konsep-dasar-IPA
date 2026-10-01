from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
root=Path(__file__).resolve().parents[1]
errors=[]
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  for attr in ('href','src'):
   value=attrs.get(attr,'')
   if not value or value.startswith(('#','http:','https:','data:','mailto:')): continue
   target=(self.current.parent/unquote(value.split('#')[0].split('?')[0])).resolve()
   if not target.exists():errors.append(f'{self.current.relative_to(root)}: {value}')
parser=Links()
for file in root.rglob('*.html'):
 parser.current=file;parser.feed(file.read_text())
assert not errors,'Broken local paths: '+repr(errors)
print('Passed: all HTML local links and assets resolve.')
