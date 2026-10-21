from html import escape
from course_data import TOPICS
import math

def text(x,y,label,size=17,color='#153e36',anchor='middle'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(label)}</text>'
def box(x,y,w,h,label,fill='#dcebb9'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#89a382"/>'+text(x+w/2,y+h/2+6,label)
def arrow(x1,y1,x2,y2,color='#14634e'):
 return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="3" fill="none" marker-end="url(#a{color[1:]})"/>'
def flow(labels):
 out=''
 for i,label in enumerate(labels):
  out+=box(60,20+i*70,360,48,label)
  if i<len(labels)-1:out+=arrow(240,68+i*70,240,87+i*70)
 return out
def visual(slug,key):
 s=''
 if slug=='hakikat':
  s='<path d="M160 35L175 205H305L320 35Z" fill="#b5dbe4" stroke="#507c8a" stroke-width="3"/>'
  if key!='amati':s+=text(240,232,'Wadah utuh · periksa pembanding',15)
  for x,y in [(180,80),(300,100),(176,140),(306,160)]:s+=f'<circle cx="{x-12 if x<240 else x+12}" cy="{y}" r="5" fill="#42a1bc"/>'
  s+=text(240,25,{'amati':'Titik air di luar gelas','duga':'Dugaan: air dari udara','uji':'Bandingkan dingin dan suhu ruang'}[key])
  s+=text(240,125,'air dingin',17)
 elif slug=='pengukuran':
  start=2 if key=='geser' else 0
  s=box(40,140,400,50,'','#f1ddac')
  for i in range(11):s+=f'<path d="M{40+i*40} 140v15" stroke="#50685b"/>'+text(40+i*40,182,str(i),14)
  s+=box(40+start*40,70,240,60,'buku')+text(240,220,'Skala dalam sentimeter')
  s+=text(240,32,'Baca awal dan akhir' if key!='ulang' else 'Ulangi dengan penempatan yang sama')
 elif slug=='zat':
  for i in range(24):
   if key=='padat':x=120+(i%6)*44;y=65+(i//6)*36
   elif key=='cair':x=112+(i%6)*44+(i%3)*5;y=100+(i//6)*28
   else:x=45+(i*79)%390;y=35+(i*43)%170
   s+=f'<circle cx="{x}" cy="{y}" r="8" fill="#14634e"/>'
  s+=text(240,235,'Partikel digambar sama besar · tidak berskala',14)
 elif slug=='gaya':
  s=box(205,100,70,70,'buku')+'<path d="M30 175H450" stroke="#78916a" stroke-width="3"/>'
  if key=='seimbang':s+=arrow(195,125,80,125)+arrow(285,125,400,125)+text(240,40,'Sama besar · berlawanan arah')
  elif key=='dorong':s+=arrow(285,125,430,125)+arrow(195,125,135,125)+text(240,40,'Pengaruh keseluruhan ke kanan')
  else:s+=arrow(195,125,85,125,'#c66a33')+text(120,95,'gesekan',16)+arrow(285,70,410,70,'#217f9b')+text(335,48,'arah gerak',16)
  s+=text(240,225,'Gambar menyoroti gaya horizontal',15)
 elif slug=='energi':
  data={'senter':['Baterai: energi kimia','Proses listrik','Cahaya dan pemanasan'],'kipas':['Masukan energi listrik','Gerak baling-baling dan udara','Bunyi dan pemanasan juga terjadi'],'tangan':['Kerja otot mendukung gerak','Dua telapak saling bergesekan','Tangan dapat menjadi hangat']}
  s=flow(data[key])
 elif slug=='suhu':
  if key=='konduksi':
   s=box(35,85,410,60,'bahan penghantar','#e8d9bf')+text(90,65,'hangat',17,'#b04c28')+text(390,65,'lebih dingin',17,'#217f9b')
   s+=arrow(130,180,350,180,'#c66a33')+text(240,225,'Energi berpindah melalui bahan',16)
  elif key=='konveksi':
   s='<rect x="95" y="45" width="290" height="165" rx="15" fill="#d9edf1" stroke="#63868a"/>'
   s+=arrow(150,170,150,80,'#c66a33')+arrow(160,70,325,70)+arrow(335,80,335,170,'#217f9b')+arrow(325,180,160,180)
   s+=text(240,238,'Fluida bergerak membawa energi',16)
  else:
   s='<circle cx="80" cy="115" r="42" fill="#efc15d"/><circle cx="390" cy="115" r="32" fill="#65a3ba"/>'
   for y in [85,115,145]:s+=arrow(145,y,335,y,'#c66a33')
   s+=text(240,215,'Radiasi dapat melalui ruang hampa',16)
 elif slug=='bunyi':
  cycles=5 if key=='tinggi' else 2; amp=60 if key=='kuat' else 28
  points=' '.join(f'{35+i*2},{120-math.sin(i/205*cycles*2*math.pi)*amp:.1f}' for i in range(206))
  s='<path d="M30 120H450" stroke="#bbc9b4"/><polyline points="'+points+'" fill="none" stroke="#14634e" stroke-width="3"/>'
  s+=arrow(40,210,440,210)+text(240,240,'Waktu → · bukan lintasan udara',16)+text(240,30,'Perubahan tekanan pada satu tempat',16)
 elif slug=='cahaya':
  if key=='lihat':
   s=box(20,80,110,60,'lampu','#f4dfa1')+box(200,80,100,60,'buku')+box(365,80,95,60,'mata','#d4e7ed')
   s+=arrow(135,110,195,110,'#c66a33')+arrow(305,110,360,110)+text(240,210,'Cahaya masuk ke mata',17)
  elif key=='bayangan':
   s='<circle cx="40" cy="110" r="10" fill="#d5a743"/><path d="M440 35V220" stroke="#50685b" stroke-width="5"/><path d="M40 110L440 35M40 110L440 220" stroke="#c69f4d" fill="none"/><path d="M210 78V157" stroke="#153e36" stroke-width="10"/><path d="M440 35V220" stroke="#153e36" stroke-width="16" opacity=".25"/>'+text(240,245,'Jalur terhalang → bayangan',16)
  else:
   s='<rect x="20" y="120" width="440" height="110" fill="#d5eaf1"/><path d="M240 30V230" stroke="#93a6a6" stroke-dasharray="5 6"/>'
   s+=arrow(100,35,240,120,'#c66a33')+arrow(240,120,290,220,'#c66a33')+text(390,90,'udara')+text(390,180,'air')
 elif slug=='listrik':
  if key=='magnet':s=box(40,85,170,65,'U       S','#c9dfbb')+box(270,85,170,65,'S       U','#d1e6ef')+arrow(190,190,100,190)+arrow(290,190,380,190)+text(240,40,'S berhadapan S → menolak')
  else:
   s='<path d="M85 130V80H190M290 80H395V117M395 163V195H85V150" fill="none" stroke="#587f67" stroke-width="5"/>'
   s+='<path d="M190 80L290 '+('80' if key=='tutup' else '40')+'" stroke="#14634e" stroke-width="5"/>'
   s+='<circle cx="395" cy="140" r="23" fill="'+('#efd15e' if key=='tutup' else '#d0d9c9')+'" stroke="#647d5c"/>'
   s+='<path d="M70 130H100M80 150H90M385 130L405 150M405 130L385 150" stroke="#153e36" stroke-width="3"/>'+text(240,235,'Baterai dan lampu · model rangkaian',16)
 elif slug=='keanekaragaman':
  if key=='api':s='<path d="M240 35Q310 110 280 175Q240 220 200 175Q165 125 220 85Q220 145 240 35" fill="#d48638"/>'+text(240,235,'Membesar bukan bukti tunggal kehidupan',15)
  elif key=='biji':s='<ellipse cx="240" cy="140" rx="45" ry="62" transform="rotate(25 240 140)" fill="#b38b5c"/><path d="M240 135Q220 90 255 60" fill="none" stroke="#14634e" stroke-width="10"/>'+text(240,230,'Biji viabel dapat berada pada keadaan dorman',15)
  else:s='<path d="M220 115H260L275 210H205Z" fill="#d6bd95"/><path d="M145 120Q240 -20 335 120Z" fill="#b76845"/>'+text(240,235,'Jamur memperoleh nutrien dari bahan organik',15)
 elif slug=='tumbuhan':
  s='<path d="M240 195V60M240 190L205 225M240 195L270 225M240 195V230" stroke="#738444" stroke-width="6" fill="none"/><path d="M240 120Q140 35 150 115Q190 145 240 120M240 95Q335 20 320 95Q285 125 240 95" fill="#63a66c"/>'
  if key=='akar':s+=arrow(210,190,210,70,'#217f9b')+text(85,185,'air masuk',16)
  elif key=='daun':s+='<circle cx="60" cy="45" r="22" fill="#efc15d"/>'+arrow(88,45,160,80,'#c66a33')+text(380,45,'karbon dioksida',14)+arrow(390,55,320,90)
  else:s+='<circle cx="240" cy="48" r="22" fill="#dcab6b"/><circle cx="240" cy="48" r="8" fill="#b15d39"/>'+text(370,185,'bunga → biji',16)
 elif slug=='hewan':
  if key=='ikan':s='<ellipse cx="240" cy="120" rx="95" ry="45" fill="#64a7b9"/><path d="M145 120L90 75V165Z" fill="#64a7b9"/><path d="M220 82L255 55L275 88" fill="#488795"/><circle cx="300" cy="110" r="5" fill="#153e36"/><path d="M275 100Q260 120 275 140" stroke="#153e36" fill="none"/>'+text(240,220,'Sirip membantu gerak · insang bertukar gas',15)
  elif key=='burung':s='<ellipse cx="240" cy="140" rx="65" ry="40" fill="#76a378"/><circle cx="295" cy="85" r="30" fill="#76a378"/><path d="M322 85L355 100L320 105" fill="#d59847"/><path d="M190 140Q220 60 260 130" fill="#3e7553"/><path d="M220 170L215 205M260 170L270 205" stroke="#907449" stroke-width="5"/>'+text(240,238,'Bentuk struktur memberi petunjuk fungsi',15)
  else:s=flow(['Telur → larva','Pupa: tahap hidup dan perkembangan','Dewasa → menghasilkan generasi baru'])
 elif slug=='manusia':
  data={'cerna':['Mulut dan saluran pencernaan','Usus halus: penyerapan nutrien','Nutrien diangkut menuju jaringan'],'napas':['Udara masuk dan keluar paru-paru','Pertukaran oksigen dan karbon dioksida','Darah menghubungkan paru-paru dan jaringan'],'darah':['Jantung memompa darah','Pembuluh menghubungkan organ dan jaringan','Jalur kembali menuju jantung']}
  s=flow(data[key])
 elif slug=='ekosistem':
  if key=='rantai':s=flow(['Rumput','Belalang','Katak'])
  elif key=='jaring':
   s=box(170,10,140,45,'rumput')+box(20,95,170,45,'belalang')+box(290,95,170,45,'ulat')+box(170,185,140,45,'burung')+arrow(210,60,120,90)+arrow(270,60,360,90)+arrow(120,145,210,180)+arrow(360,145,270,180)
  else:s=flow(['Daun gugur dan sisa organisme','Pengurai memproses bahan organik','Unsur hara kembali ke lingkungan'])
 elif slug=='bumi':
  s='<path d="M0 185Q120 130 240 185T480 185V250H0Z" fill="#c2d4aa"/><path d="M10 210Q80 190 150 210T300 210" fill="none" stroke="#67afcb" stroke-width="8"/><ellipse cx="320" cy="55" rx="75" ry="28" fill="#d3e2e6"/>'
  if key=='uap':s+=arrow(90,175,90,65,'#217f9b')+text(100,35,'penguapan',16)
  elif key=='awan':
   for x in [280,320,360]:s+=arrow(x,95,x-20,155,'#217f9b')
   s+=text(120,115,'presipitasi',16)
  else:s+=arrow(240,170,170,220,'#217f9b')+arrow(330,175,430,190,'#217f9b')+text(240,35,'resapan dan limpasan',16)
 elif slug=='antariksa':
  if key=='rotasi':s='<circle cx="70" cy="115" r="32" fill="#eac366"/><circle cx="330" cy="115" r="65" fill="#6fabc4"/><path d="M330 50A65 65 0 0 1 330 180Z" fill="#213e53"/>'+arrow(125,80,240,80,'#c66a33')+arrow(125,150,240,150,'#c66a33')+text(285,210,'siang',16)+text(385,210,'malam',16)
  elif key=='revolusi':s='<ellipse cx="240" cy="120" rx="175" ry="80" fill="none" stroke="#9eaf92"/><circle cx="240" cy="120" r="30" fill="#eac366"/><circle cx="415" cy="120" r="18" fill="#6fabc4"/>'+text(240,235,'Bumi mengorbit Matahari · tidak berskala',15)
  else:
   for i in range(4):
    x=75+i*110;s+=f'<circle cx="{x}" cy="105" r="35" fill="#31495a"/>'
    if i==1:s+=f'<path d="M{x} 70A35 35 0 0 1 {x} 140Z" fill="#e5ddb7"/>'
    elif i==2:s+=f'<circle cx="{x}" cy="105" r="35" fill="#e5ddb7"/>'
    elif i==3:s+=f'<path d="M{x} 70A35 35 0 0 0 {x} 140Z" fill="#e5ddb7"/>'
   s+=text(240,200,'Ikon fase: bagian terang yang tampak',16)+text(240,228,'Bukan gambar susunan orbit',15)
 defs=''.join(f'<marker id="a{c[1:]}" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0L7 3L0 6" fill="{c}"/></marker>' for c in ['#14634e','#c66a33','#217f9b'])
 description=next(c[1]+'. '+c[2] for t in TOPICS if t['slug']==slug for c in t['cases'] if c[0]==key)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 250" role="img" aria-label="{escape(description)}"><defs>{defs}</defs>{s}</svg>'
 return svg.replace('id="a',f'id="a{slug}_{key}_').replace('url(#a',f'url(#a{slug}_{key}_')
