
################EX 1 trigonometrie
import math 
h = float (input("l'hypoténuse "))
a = float (input("angles "))
t = math.pi
b = h*(math.sin(a*t))
c = h*(math.cos(a*t))
pitago=math.sqrt(b**2 + c**2)
print("b est ",b,"c est ", c,  "pitago",pitago)

################# 

import random
import math
x =  random.randint(1,4)
print(x)
a = int(input("entré a "))
b = int(input("entré b "))
t =  a >b
print( "a > b",t )
g = random.randint(a,b)
print(" aléatoire de a et b ",g)

############# EX 2 le gros lot



import random
import math
x = int(input("une nombre de votre clavier0 de 100"))
b=1
p ="o"
n="o"
z=0
z2=0
sommes =0
while b!=0 :
    if b==1 :
            h  =  random.randint(0,100)
            print(h) #si tu veux 
            k_min = 0
            k_max = 100
            i =0
            e=5
            while i<=5 and e!=0 :
                i = i+1
                e= e-1
                r= e+1
                print(" devine nombre entre ",k_min ,"et",k_max,"(",r," essais )")
                
                x = int(input())
                if x == h :
                    print("gngné ")
                    break

                elif x >h :
                    print(" trop grand ")
                    k_max= x-1
                    
                    continue 

                elif x <h :
                    print(" trop petit   ")
                    k_min= x+1
                  
                    continue 
            if i <= 5 and x ==h :
                sommes = sommes + (5-r+1)
               ## d = 5 -r
               
                print(r)
               
                while b!=0:
                    z=z+1
                    
                    break 
                
                print("gagné au bout de x essais ")
            else:
                while b!=0:
                    z2=z2+1
                    break 
                print("perdu !")
    x1 = input("voulez-vous  recommencer ")
    if x1 == "o" :
        
        continue
    elif x1 =="n":
        
        print (sommes )
        print ("gagné est  " ,z," fois jouée",z+z2 , "fois essayer " ,sommes/z)
        break 
    
######### EX 2 le gros lot IA , jusqu'a la question 3

import random

k_min= 0
k_max=100
#h  = int(input("nombre secret "))
h = random.randint(0,100)
print ("je choisi ")
i = 0
j =0
l=0
somme = 0
n = int(input() )
while l<=n:
    l+=1
    somme =somme + i +j 
    while h>0 and h<100:    
        x = random.randint(k_min,k_max)
        
        
        print(" je cherche un  nombre entre ",k_min ,"et",k_max)
        print("je propose ",x )
        if x == h :
            print("b ")
            print("j'ai gagné")
            break
        elif x >h :
            print(" g ")
            k_max= x-1
            i += 1
            
            continue 
        elif x <h :
            print(" p  ")
            k_min= x+1
            j+=1
        
            continue 



print (i ,j , "et total essai ",i+j )
 
print ("moyen essai est " ,(i+j)/n ) 
























    
