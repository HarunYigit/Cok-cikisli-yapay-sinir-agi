import random
import math
import numpy as np
from typing import no_type_check

from numpy.core.fromnumeric import argmin
def sigmoid(x):
    try:
        return 1 / (1 +  math.exp(-x))
    except:
        return x* 0.00001
def reluderitevate(x):
    return np.greater(x, 0).astype(int)

def relu(xi):
    if xi > 0:
        return xi
    elif xi <= 0:
        return 0
def deritevate(y):
    return y * (1.0 - y)
class noron:
    def __init__(self):
        self.a=0
        self.z=0
        self.delta_W=0
        df=0
        while df==0:
            df=random.randint(-4,4)
        self.b = df
class katman(list):
    def __init__(self,boyut):
        for i in range(boyut):
            self.append(noron())
        self.hata=0
    def get_activ(self,nor,agirliklar):
        toplam=0
        for i in self: 
            try:
                toplam += i.z * agirliklar[i][nor]
            except:
                print(i.z,agirliklar[i][nor])
        toplam+=nor.b
        return toplam

            
class model_DL:
    def __init__(self,katmans,labda=0.6,alfa=0.01,degerler=[0,1]):
        self.katmanlar=[]
        self.alfa=alfa
        for boyut in katmans:
            self.katmanlar.append(katman(boyut))
        self.agirliklar={}
        self.labda=labda
        self.parentler={}
        self.loss=0
        self.degerler=degerler
    def recognize(self):
        for i in range(len(self.katmanlar) -1):
            katman=self.katmanlar[i]
            skatman=self.katmanlar[i+1]
            for p in katman:
                self.agirliklar[p]={}
                self.parentler[p]=[]
                for g in skatman:
                    df=0
                    while df==0:
                        df=random.randint(-4,4)
                    self.agirliklar[p][g]= df
        for i in range(0,len(self.katmanlar) -1):
            katman=self.katmanlar[i]
            skatman=self.katmanlar[i+1]
            for p in katman:
                for g in skatman:
                    self.parentler[p].append(g)
    def cikis_katmani(self):
        return self.katmanlar[len(self.katmanlar)-1]
    def print_cikis(self):
        yazilcak=[]
        for i in self.katmanlar[len(self.katmanlar)-1]:
            yazilcak.append(i.z)
        print(yazilcak,len(yazilcak))

    def set_data(self,x):
        for i in  range(len(x)):
            self.katmanlar[0][i].z=x[i]
            self.katmanlar[0][i].a=x[i]
        for i in range(len(self.katmanlar) -1):
            katman=self.katmanlar[i]
            skatman=self.katmanlar[i+1]
            for p in skatman:
                p.a= katman.get_activ(p,self.agirliklar)
                p.z=sigmoid(p.a)
    def predict(self,x):
        self.set_data(x)
        if self.cikis_katmani()[0].z > self.cikis_katmani()[1].z:
            return self.degerler[0]
        return self.degerler[1]
        
    def get_hata(self,x,y):
        toplamhata=0
        pred = self.predict(x)
        for p in range(len(self.cikis_katmani())):
            i=self.cikis_katmani()[p]
            if self.degerler[p] == y:
                istenen=0.9
            else:
                istenen=0.1
            toplamhata += ( (i.z -istenen) *  (i.z -istenen))
        toplamhata*=0.5
        self.loss=toplamhata
        if toplamhata== math.nan:
            print(i.z,istenen)
        return toplamhata
    def fit(self,xler,yler):
        hata=0
        for ghghgh in range(len(xler)):
         x=xler[ghghgh]
         y=yler[ghghgh]
         for p in range(len(self.cikis_katmani())):
            i=self.cikis_katmani()[p]
            hata=self.get_hata(x,y)
            dagitiacak_hata=i.z * (1-i.z) * (y-i.z)
            for g in self.katmanlar[1]:
                katman_hata=dagitiacak_hata * self.labda * g.z
                g.delta_W = katman_hata
                for ara in self.katmanlar[0]:
                    ara_katman_hata= (g.z * (1- g.z)) * (dagitiacak_hata * self.agirliklar[g][i])
                    ara_noron_hata= ara_katman_hata * self.labda* ara.z 
                    self.agirliklar[ara][g]+= ara_noron_hata
                self.agirliklar[g][i] += katman_hata
        #print("fit işlemi bitti hata:",hata)
    def get_los(self):
        return self.loss
    def score(self,x,y):
        dogrular=0
        for i in range(len(x)):
            dgg=self.predict(x[i])
            #if dgg == y[i]:
            #    dogrular+=1
            dogrular+=1 - (abs(dgg- y[i]))
        return (dogrular / len(x)) 
def kelvinToCelsius(kelvin):
    return kelvin - 0.273
 
xler=[]
yler=[]
devam=True
birler=0
sifirlar=0
while devam:
    x=[]
    toplam=0
    for p in range(5):
        g=random.random()
        x.append(g)
        toplam+=g
    
    if toplam / 5 >0.6:
        if birler <75:
            xler.append(x)
            yler.append(1)
            birler+=1
    else:
        if sifirlar<75:
            xler.append(x)
            sifirlar+=1
            yler.append(0)
    if sifirlar + birler==150:
        devam=False
print(xler,yler,len(xler),len(yler))
class model:
    def __init__(self) :
        self.katmanlar=[]

def get_scr_of_x(x,y):
    pred,train=modelim.predict(x) , y
    print("deneme --- train:",train,"/ pred: ",pred,"/ başarı:",1-(abs(train-pred) ),modelim.loss)
modelim=model_DL(katmans=[len(xler[0]),16,2],labda=0.6)
modelim.recognize()
modelim.set_data(xler[0])
modelim.print_cikis()
modelim.set_data(xler[0])
modelim.print_cikis()
print("a")
epoch= 150
i=0
ilkhata=0

get_scr_of_x(xler[0],yler[0])
ilkscore=modelim.score(xler,yler)
for p in range(epoch):
    i+=1
    modelim.fit(xler,yler)
    
    if i==1:
        ilkhata=modelim.get_hata(xler[0],yler[0])
    #print("score:",modelim.score(xler,yler),"hata:",modelim.get_hata(xler[0],yler[0]))
    print(i / epoch,"score:",modelim.score(xler,yler),"cikis:",modelim.cikis_katmani()[0].z, end="\r")
print("----------#######---------")
print("ilkhata:",ilkhata,"ilkscore:",ilkscore)
print("hata:",modelim.get_hata(xler[0],yler[0]),"score:",modelim.score(xler,yler))
get_scr_of_x(xler[0],yler[0])
while True:
    dd=input("sayıları giriniz:")
    sayi1=float(dd.split(" ")[0]) 
    sayi2=float(dd.split(" ")[1])
    sayi3=float(dd.split(" ")[2])
    sayi4=float(dd.split(" ")[3])
    sayi5=float(dd.split(" ")[4])
    olmasigerekne=0
    toplam=sayi1+sayi2+sayi3+sayi4+sayi5
    if toplam / 5 >0.6:
        olmasigerekne=1
    else:
        olmasigerekne=0
    get_scr_of_x([sayi1,sayi2,sayi3,sayi4,sayi5],olmasigerekne)
    