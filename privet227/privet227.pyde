x=0
x1=0
score=0##
x_0=range(0,530,60)
score_0=[1,1.250,1.800,2,3.300,4,5,9.500,11]
score_buy_0=[0,150,320,500,950,2000,5000,10000,40000]##
x_1=range(0,530,60)
score_buy_1=[200,800,2500,3600,6000,12000,25000,55000,120000]
flag=[False,False,False,False,False,False,False,False,False]##
lst=[0,150,320,500,950,2000,5000,10000,40000]
lst2=[200,800,2500,3600,6000,12000,25000,55000,120000]
def setup():
    global imgs
    imgs = [loadImage('1.png'),loadImage('2.png'),loadImage('3.png'),loadImage('4.png'),loadImage('5.png'),loadImage('6.png'),loadImage('7.png'),loadImage('8.png'),loadImage('9.png')] 
    size(530,530)
def draw():
    global score 
    background(255)
    fill(0,0,255)
    for x in x_0: 
        rect(x,20,50,50,10)##
    stroke(0)
    fill(0)
    for index in range(9):
        text(str(lst[index]),index*61,80)
    line(0,90,530,90)##
    fill(0,255,0)
    for x1 in x_1:
        rect(x1,100,50,50,10)##
    fill(0)
    for index2 in range(9):
        text(str(lst2[index2]),index2*61,160)
    line(0,170,530,170)##
    fill(0)
    text(score,0,10)##
    for index in range(len(imgs)):
        if flag[index]==True:
            if index<=4:
                image(imgs[index],100*index ,180 , 100,150)
            else:
                if (index==5):
                    image(imgs[index],100*(index - 5) ,380 , 200,100)
                else:
                    image(imgs[index],100*(index - 5)+ 100 ,380 , 100,150)##
    text(u"как построить город",200,10)
def mouseClicked():
    global score
    for index in range(len(x_0)): 
        if mouseX>x_0[index] and mouseX<x_0[index]+50 and mouseY>20 and mouseY<70 and score>=score_buy_0[index]:
            score=score+score_0[index]##
    for index1 in range(len(x_1)): 
        if mouseX>x_1[index1] and mouseX<x_1[index1]+50 and mouseY>100 and mouseY<150 and score>=score_buy_1[index1]:
            flag[index1]=True
#54
