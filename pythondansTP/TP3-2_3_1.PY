from turtle import *
import random
import turtle
speed(1000)
#setup(100,100)

#carré
i =0
while i <4:
    
    i+=1
    forward(100)
    left(90)


#carré bis
 
i =0
while i <4:
    
    i+=1
    forward(100)
    right(90)
  
up()
goto(-50,20)
down()
i=0
while i <4:

    i+=1
    forward(100)
    left(90)
#triangle équilatéal
i =0
while i <3:
    
    i+=1
    forward(100)
    right(120)

# ling de carré
#pavage de carré

k=0
while k <4:
    k+=1
    j=0
    up()
    goto(-200,200-60*(k-1))
    down()
    while j<8:
        j+=1

        i=0
        while i <4:
        
            i+=1
            forward(50)
            right(90)

        up()
        goto(-200+60*j,200-60*(k-1))
        down()


# ligne de carré et triangle alternés

l= int(input("longeur de côté "))
d= int(input("dintance entre les carré et les triangle "))
k=0
while k <8 :
    k+=1
    up()
    goto(-200 + (l+d)*(k-1),200 )
    down()
    if k%2 ==0:
        i =0
        while i <3:
            
            i+=1
            forward(l)
            right(120)
    elif  k%2 !=0:
        j =0
        while j <4:
            
            j+=1
            forward(l)
            right(90)

forward(l)

##ligne de carré et triangles alterné  de tailles croissants 

from turtle import *

up()
goto(-200,200)
down()

nb_f = int(input("Nombre de figure a tracer :"))
n = 0
i = 0
j = 0

while n < nb_f:

    if n >= 1:
        up()
        forward(50+(15*n))
        down()
        i = 0
        j = 0
        
    while i < 4:
        forward(40+(15*n))
        right(90)
        i = i + 1

    up()
    forward(50+(15*n))
    down()
    
    while j < 3:
        forward(40+(15*n)+15)
        right(120)
        j = j + 1

    n = n + 1
## rosace ete pavage de rosaces 
tp=int(input("entré tp "))
tl=int(input("entré tl "))

nbr= int(input("entré nbr"))

rayon  = 20
j=0
r=0
while j<tp:
    
    j+=1
    r+=1
    k=0
    up()
    goto(-200,200-(20*2*2)*(r-1))
    down()
    
    while k<tl:
        color1=random.randint(1,255)
        color2=random.randint(1,255)
        color3=random.randint(1,255)
        colormode(255)
        pencolor(color1,color2,color3)
        k+=1
        for i in range(0,nbr):
            turtle.circle(rayon)
            turtle.left(360/nbr)
        up()
        forward(20*2*2)
        down()

































































