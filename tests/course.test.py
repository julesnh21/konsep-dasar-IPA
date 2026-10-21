from pathlib import Path
from html.parser import HTMLParser
import sys
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root))
from course_data import TOPICS,MEETINGS
assert len(TOPICS)==16 and len(MEETINGS)==16
slugs={t['slug'] for t in TOPICS}
covered=[s for m in MEETINGS for s in m[2]]
assert set(covered)==slugs and len(covered)==16
assert [m[0] for m in MEETINGS if not m[2]]==[8,16]
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if a.get('href','').startswith('#'):self.refs.append(a['href'][1:])
for t in TOPICS:
 page=root/'topik'/t['slug']/'index.html';s=page.read_text();p=Check();p.feed(s)
 assert len(p.ids)==len(set(p.ids)),f'Duplicate ids: {t["slug"]}'
 assert all(r in p.ids for r in p.refs),f'Broken anchor: {t["slug"]}'
 assert s.count('data-panel=')==3
 assert len(t['sections'])>=4 and len(t['checks'])>=2
 assert all(token not in s for token in ['ΣF','mgh','cos θ','½mv','F =','ΔE','μ =']),t['slug']
 assert ('id="distance"' in s)==(t['slug']=='gaya')
assert 'Belum tersedia' not in (root/'index.html').read_text()
print('PASS: 16 complete topics, full semester coverage, 2 assessment sessions, unique IDs, anchors and conceptual physics scope.')
