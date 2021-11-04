from turtle import *
import turtle
import random
##i=0
##while i <360:
##    turtle.forward(2)
##    turtle.left(1)
##    i+=1

##turtle.circle(115)
##l= int(input("longeur de côté "))
##d= int(input("dintance entre les carré et les triangle "))
##l= 40
##d=10
##k=0
##f =0
##a=0
##r =0
##
##
##while k <8 :
##    k+=1
##    
##    
##    print(r)
##    if k%2 ==0:
##        i =0
##        
##        while i <3:
##            
##            i+=1
##            
##            forward(l+r)
##            right(120)
##    
##           
##    elif  k%2 !=0:
##        j =0
##       
##        while j <4:
##            
##            j+=1
##           
##            forward(l+r)
##            right(90)
##    if k >2 :
##        r +=15
##        
##       
##    up()
##    goto(((l+d)*(k-1)+(r)),0 )
##    down()
##            
##
##
##forward(l+r )



##import turtle
##def carre():
##    # trace un carre de taille 100
##    i = 1 # compteur du nb de cotes
##    while i <= 4 :
##        turtle.forward(100)
##        turtle.right(90)
##        i = i + 1
## programme principal, avec appel de fonction
##carre()
##turtle.up()
##turtle.forward(130)
##turtle.down()
##carre()
##i=1
##while i <= 4 :
##    turtle.forward(100)
##    turtle.right(90)
##    i = i + 1
##
##    carre(-50,20,100)

##    
##k =0
##while k <8 :
##    up()
##    forward(50 +10)
##    down()
##    i=0
##    k +=1
##    while i<4:
##        forward(50)
##        right(90)
##        i+=1
##
##from kandinsky import *

##nbr= 8
##rayon  = 40
##for i in range(0,nbr):
##    turtle.circle(rayon)
##    turtle.left(360/nbr)
##rosace()

##print(3*"\n" )
##i= 1
##while i  <= 5 :
##    up()
##    goto(-200,200-50*r)
##    down()
##    
##    j=0
##    
##    while  j <= 4:
##        ##print ("*", end='')
##        forward(50*j)
##        nbr= 8
##        rayon  = 40
##        for i in range(0,nbr):
##            turtle.circle(rayon)
##            turtle.left(360/nbr)
##        forward(200)
##        j+=1
##
##
##        rosace()
##
##
##        
##
##    print()
##    i+=1


##j=0
##    
##while  j <= 4:
##    ##print ("*", end='')
##    
##    nbr= 8
##    rayon  = 40
##    for i in range(0,nbr):
##        turtle.circle(rayon)
##        turtle.left(360/nbr)
    
##        forward(*j)
##        
##    rosace()
##    
##
##
##    
##    j +=1

##tp=int(input("entré tp "))
##tl=int(input("entré tl "))
##
##nbr= int(input("entré nbr"))
##
##rayon  = 20
##j=0
##r=0
##while j<tp:
##    
##    j+=1
##    r+=1
##    k=0
##    up()
##    goto(-200,200-(20*2*2)*(r-1))
##    down()
##    
##    while k<tl:
##        color1=random.randint(1,255)
##        color2=random.randint(1,255)
##        color3=random.randint(1,255)
##        colormode(255)
##        pencolor(color1,color2,color3)
##        k+=1
##        for i in range(0,nbr):
##            turtle.circle(rayon)
##            turtle.left(360/nbr)
##        up()
##        forward(20*2*2)
##        down()
##
##rosace()
####for i in range(0,nbr):
##    turtle.circle(rayon)
##    turtle.left(360/nbr)
##forward(200)
##def carre() :
### trace un carre de taille 100
##i = 1 # compteur du nb de cotes
##while i <= 4 :
##    turtle.forward(100)
##    turtle.right(90)
##    i = i + 1
### 2.3.2
##def carre(n):
##    j =0
##    while j <4:    
##        j+=1
##        forward(n)
##        right(90)
##    
##def triangle(n):
##    i =0
##    while i <3:
##            
##        i+=1
##        forward(n)
##        right(120)
##    
##l= int(input("longeur de côté "))
##d= int(input("dintance entre les carré et les triangle "))
##        
##k=0
##while k <8:
##    k+=1
##    
##    up()
##    goto(-200 + (l+d)*(k-1),200 )
##    down()
##    if k %2==0:
##        triangle(l)
##    else:
##        carre(l)

##carré bis
def carre(a,b,l):
    i =0
    up()
    goto(a,b)
    down()
    while i<4:
        forward(l)
        right(90)
        i+=1

carre(0,0,50)
carre(-10,-10,50)









    
        
