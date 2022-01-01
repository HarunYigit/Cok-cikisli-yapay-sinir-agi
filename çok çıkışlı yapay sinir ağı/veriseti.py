import random
xler=[]
yler=[]
for x in range(50):
    x=[]
    toplam=0
    for p in range(5):
        g=random.random()
        x.append(g)
        toplam+=g
    xler.append(x)
    if toplam / 5 >0.7:
        yler.append(1)
    else:
        yler.append(0)
print(xler,yler)