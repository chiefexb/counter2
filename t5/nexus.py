import requests
from lxml import etree
base_url=''
nexus=''
r=requests.get(base_url ,verify=False,auth=(nexus ))
#JUST for commit



xml= etree.fromstring(r.text)
data=xml.getchildren()[0]
items =data.getchildren()
it=[]
for item in items: 
    t=item.find('text').text
    print (t,t.startswith('D-') )
    if t.startswith('D-'):
        it.append(t)
print (it [-1])
    
