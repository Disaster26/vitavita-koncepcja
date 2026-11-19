import os,re
d=os.path.dirname(os.path.abspath(__file__))
r=lambda f:open(os.path.join(d,f),encoding='utf-8').read()
b=open(r'C:/Users/Admin/Downloads/Wylinka/strona/public/znak/badge.html',encoding='utf-8').read()
style=re.findall(r'<style>(.*?)</style>',b,re.S)[1].strip()
link=re.search(r'<a class="wylinka-badge".*?</a>',b,re.S).group(0).replace('utm_source=przykladowa-firma.pl','utm_source=vitavita.pl')
assert 'utm_source=vitavita.pl' in link
s=r('src.html')
for k,v in {'{{BADGE_STYLE}}':style,'{{BADGE_LINK}}':link}.items(): s=s.replace(k,v)
assert '{{' not in s
open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(s)
z=re.search(r'<symbol id="znak" viewBox="0 0 100 100">(.*?)</symbol>',s,re.S).group(1)
open(os.path.join(d,'img','favicon.svg'),'w',encoding='utf-8').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'+z+'</svg>')
print('ok',len(s))
