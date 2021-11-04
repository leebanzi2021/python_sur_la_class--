from turtle import *
#setup(100,100)

#carré
##i =0
##while i <4:
##    
##    i+=1
##    forward(100)
##    left(90)


#carré bis
 
##i =0
##while i <4:
##    
##    i+=1
##    forward(100)
##    right(90)
##  
##up()
##goto(-50,20)
##down()
##i=0
##while i <4:
##
##    i+=1
##    forward(100)
##    left(90)
#triangle équilatéal
##i =0
##while i <3:
##    
##    i+=1
##    forward(100)
##    right(120)

# ling de carré
#pavage de carré

##k=0
##while k <4:
##    k+=1
##    j=0
##    up()
##    goto(-200,200-60*(k-1))
##    down()
##    while j<8:
##        j+=1
##
##        i=0
##        while i <4:
##        
##            i+=1
##            forward(50)
##            right(90)
##
##        up()
##        goto(-200+60*j,200-60*(k-1))
##        down()


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

forward(50)
































































