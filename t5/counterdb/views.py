from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import  json
from counterdb.models import *
import datetime
from lxml import etree
import requests as req
def nexus():
    base_url=''
    nexus=''
    r=req.get(base_url ,verify=False,auth=(nexus ))
    xml= etree.fromstring(r.text)
    data=xml.getchildren()[0]
    items =data.getchildren()
    it=[]
    for item in items:
        t=item.find('text').text
        #print (t,t.startswith('D-') )
        if t.startswith('D-'):
            it.append(t)
    #print (it [-1])

    return it [-1], it

def regnumber(request):
    gt=request.GET
    a={}
    if ( 'hash' in  list (gt.keys()) ):
        p=Syst_stand.objects.filter(thash=gt['hash'])
        if p.count()>0:
            a['hash']='OK'
        else:
            a['hash']='no found'
    else:
        a['hash']='no found'
    if ( 'number' in  list (gt.keys()) ):
         a['number']='OK'
    else:
        a['number']='no found'
    if list( a.values() ).count('OK') >1:
        p2=Syst_stand.objects.filter(thash=gt['hash'])
        a= gt['number'].strip('D-').split('.')
        major_t  = int(a[0])
        middle_t = int(a[1])
        minor_t  = int(a[2])
        p3=Release_Number_Queue.objects.all().filter(stand=p2[0]).filter( major_t= major_t).filter(middle_t=middle_t).filter(minor_t=minor_t)
        if p3.count()>0:
            p4=p3[0]
            if p4.status in [1,2]:
                p4.status=2
                p4.save()
                rez='Номер Зафиксирован'
            elif p4.status ==0 :
                rez='Номер нужно зарезервировать'
        else:
            rez='Номер не найден'
    else:
        rez=str(a)
    return HttpResponse(str(rez ) )

def freenumber(request):
    gt=request.GET
    a={}
    if ( 'hash' in  list (gt.keys()) ):
        p=Syst_stand.objects.filter(thash=gt['hash'])
        if p.count()>0:
            a['hash']='OK'
        else:
            a['hash']='no found'
    else:
        a['hash']='no found'
    if ( 'number' in  list (gt.keys()) ):
         a['number']='OK'
    else:
        a['number']='no found'
    if list( a.values() ).count('OK') >1:
        p2=Syst_stand.objects.filter(thash=gt['hash'])
        a= gt['number'].strip('D-').split('.')
        major_t  = int(a[0])
        middle_t = int(a[1])
        minor_t  = int(a[2])
        
        p3=Release_Number_Queue.objects.all().filter(stand=p2[0]).filter( major_t= major_t).filter(middle_t=middle_t).filter(minor_t=minor_t)
        if p3.count()>0:
            p4=p3[0]
            if p4.status in [0,1]:
                p4.status=0
                p4.save()
                rez='Номер освобожден'
            else:
                rez='Номер недоступен'
        else:
            rez='Номер не найден'
    else:
        rez=str(a)
    return HttpResponse(str(rez ) )

def getnumber(request):
    gt=request.GET
    a={}
    if ( 'hash' in  list (gt.keys()) ):
        p=Syst_stand.objects.filter(thash=gt['hash'])
        if p.count()>0:
            a['hash']='OK'
        else:
            a['hash']='no found'
    else:
        a['hash']='no found'
    if list( a.values() ).count('OK') >0:
        p2=Syst_stand.objects.filter(thash=gt['hash'])
         
        #if p2[0].tested and     p2[0].simple:
        #p=Release_Number.objects.get(stand=p2[0].id)
        if Release_Number_Queue.objects.all().filter(stand=p2[0]).filter(status=0).count()>0:
            p=Release_Number_Queue.objects.all().filter(stand=p2[0]).filter(status=0)[0]
            p.status=1
            p.save()
        else:
            p=Release_Number.objects.get(stand=p2[0])
            major_t=p. major_t
            middle_t=p.middle_t
            minor_t =p.minor_t
            minor_t=minor_t+1
            if minor_t>99:
                middle_t=middle_t+1
                minor_t=0
            p.major_t  = major_t
            p.middle_t = middle_t
            p.minor_t  = minor_t
            p.save()
            p3=Release_Number_Queue.objects.create(stand=p2[0], major_t= major_t,middle_t=middle_t,minor_t=minor_t,status=1)
            p3.save()

            #Release_Number_Queue
            #nexus_number=nexus()
            #if nexus_number != str(p):
            #    a= nexus_number[0].strip('D-').split('.')
            #    major_t  = int(a[0])
            #    middle_t = int(a[1])
            #    minor_t  = int(a[2])
            #else:
        rez=str(p)
    else:
        rez=str(a)
    return HttpResponse(str(rez ) )

def counter(request):
    gt=request.GET
    a={}
    if (['hash','job','startm','endm','ver','status'].sort() == list(gt.keys()).sort() ):
        print (list(gt.keys()).sort())
        
        p=Syst_stand.objects.filter(thash=gt['hash'])
        if p.count()>0:
            a['hash']='OK'
        else:
            a['hash']='no found'
        #try:
        #   startd=datetime.datetime.strptime(gt['startm'],'%d.%m.%Y_%H:%M:%S')
        #except:
        #   a['startm']='not'+gt['startm']
        #else:
        #   a['startm']='OK'
        #try:
        #   endd=datetime.datetime.strptime(gt['endm'],'%d.%m.%Y_%H:%M:%S')
        #except:
        #   a['endm']='not '+gt['endm']
        #else:
        #   a['endm']='OK'
        #if gt['status'] in ['0','1']:
        #    a['status']='OK'
        #else:
        #    a['status']='not'
        
         
        if list(a.values()).count('OK') >0:    
      
             a['res']='TRUE' 
        else:  a['res']='FALSE'
    else:
        a['res']='FALSE'
    if a['res']=='TRUE':
        if a['status']=='1':
            st=True
        else:
            st=False
        p2=Task(thash=gt['hash'],job=gt['job'],strm=startd,endm=endd, version=gt['ver'],status=st )
        p2.save()
     #json.dumps(gt)   
    return HttpResponse (json.dumps(a) )

def index (request):
    
    #t = get_template('templates/base.html')
    #now = datetime.datetime.now()
    #html = t.render(context=None, request=None)
    #p=Task.objects.filter(thash=gt['hash'])
    #p=Task.objects
    #a=p.values_list()
    #p2=Task.objects.all()
    p2=Release_Number.objects.all()
    #html=json.dumps(a['job'])
    p=Syst_stand.objects.filter(id=1)
    t = get_template('templates/base3.html')
    now = datetime.datetime.now()
    nexus_number=nexus()[0]
    nexus_numbers=nexus()[1]
    
    p3=Release_Number_Queue.objects.all().filter(stand=p[0])
    html = t.render(context={'numbers':p2,'nexus_number':nexus_number,'rel_que':p3,'nexus_numbers':nexus_numbers }, request=None)
    return HttpResponse(html)
