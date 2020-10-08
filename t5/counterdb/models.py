from django.db import models

# Create your models here.

from django.db import models
import hashlib
import hmac

class Release_Number(models.Model):
    major_t = models.IntegerField(null='False')
    middle_t = models.IntegerField(null='False')
    minor_t = models.IntegerField(null='False')
    stand = models.ForeignKey(
        'Syst_stand',
        on_delete=models.CASCADE,
        )

    @property
    def hash (self):

        return self.stand.thash
    @property
    def number (self):
         return "D-{:02d}.{:03d}.{:02d}".format(self.major_t, self.middle_t ,self.minor_t)

    def __str__(self):
        
        return "D-{:02d}.{:03d}.{:02d}".format(self.major_t, self.middle_t ,self.minor_t) 


class Release_Number_Queue(models.Model):
    major_t = models.IntegerField(null='False')
    middle_t = models.IntegerField(null='False')
    minor_t = models.IntegerField(null='False')
    status = models.IntegerField(null='False') #0 free,1 reserv,2 register


    def hash (self):
      
        return self.stand.thash

    stand = models.ForeignKey(
        'Syst_stand',
        on_delete=models.CASCADE,
        )
    @property
    def number (self):
         return "D-{:02d}.{:03d}.{:02d}".format(self.major_t, self.middle_t ,self.minor_t)



    def __str__(self):

        return "D-{:02d}.{:03d}.{:02d}".format(self.major_t, self.middle_t ,self.minor_t)

# Create your models here.
class Task(models.Model):
    thash=models.CharField(max_length=1000,null='False', blank='False', verbose_name='hash')
    job=models.CharField(max_length=1000,null='False', blank='False', verbose_name='job')
    #strm=models.DateTimeField(auto_now=False, auto_now_add=False)
    #endm=models.DateTimeField(auto_now=False, auto_now_add=False)
    #num_hi=models.CharField(max_length=3,null='False', blank='False', verbose_name='num_hi')
    #num_lo=models.CharField(max_length=2,null='False', blank='False', verbose_name='num_lo')
    #num_start=models.CharField(max_length=5,null='False', blank='False', verbose_name='num_start')
    version=models.CharField(max_length=1000,null='True', blank='True', verbose_name='version')
    status= models.BooleanField(verbose_name='Статус')
    def stand (self):
        p=Syst_stand.objects.filter(thash=self.thash)
        return p.values()[0]['stand']
    def syst (self):
        p=Syst_stand.objects.filter(thash=self.thash)
        return p.values()[0]['syst']
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.version () )


class Syst_stand (models.Model):
    syst  = models.CharField(max_length=1000,null='False', blank='False', verbose_name='Система')
    stand = models.CharField(max_length=1000,null='False', blank='False', verbose_name='Стенд')
    art = models.CharField(max_length=1000,null='False', blank='False', verbose_name='Артиф')
    tested= models.BooleanField(verbose_name='Тестирование')
    simple= models.BooleanField(verbose_name='Простой',default='False')
    thash = models.CharField(max_length=1000,null='False', blank='True', verbose_name='Хеш')
    nexus_url=models.URLField(max_length=1000,  blank='True', verbose_name='NEXUS URL')
    nexus_user=models.URLField(max_length=1000,  blank='True', verbose_name='NEXUS URL')
    nexus_password = models.CharField(max_length=1000,null='False', blank='True', verbose_name='Пароль') 

    def _thash(self):
         st=bytearray(self.syst+self.stand,'UTF8')
         hs=hashlib.sha1(st).hexdigest()
         return hs

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self._thash())
    def save(self, *args, **kwargs):
        self.thash=self._thash()
        super().save(*args, **kwargs)
       # return super(Syst_stand, self).save(*args, **kwargs)

#class Repository (models.Model):
#    login
#    password
