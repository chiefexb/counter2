#!venv/bin/python
import requests
#f=open('./data.csv')
#lr=f.readlines()
#startm endm    job     status  hash    ver
base_url="http://10.53.132.109/number_get"

req=requests.get(base_url,params=
   {'startm' :'',
    'endm'   :'',
     'job'    :'job',
     'status' :'OK',
     'hash'   :'8a046ec12f2fd5669ceb6ce5d7ece7cfa1146a12',
     'number'    :'D-03.032.08'
            
         })
print (req.url, req.status_code ,req.text)


