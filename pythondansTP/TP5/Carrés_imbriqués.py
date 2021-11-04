from turtle import *
import math
import random 

###carre imbriqué 

##def  carre1(d):
##    i = 0
##    while i <4:
##        i+=1
##        forward(d)
##        right(90)
##    
##def carre_imbrique(d,n ):
##    i=0
##    k=d
##    while i < n :
##        up()
##        goto(-200, 200)
##        down()
##        carre1(k)
##        k =  (2/3)*d
##       
##        d=k
##        i+=1
##        
##
##carre_imbrique(100,5)
###
def aller_sans_trancer(x,y):
    turtle.shape('turtle')
    up()
    goto(x,y)
    down()
    return goto(x,y)
aller_sans_trancer(43,65)

