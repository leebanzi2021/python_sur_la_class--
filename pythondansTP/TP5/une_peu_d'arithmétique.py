#UN PEU d'arithmétique
import math
import string 

def plus_grand_diviseur_premier(n):
    if n <=2:
        print("c'est numéro divieur ")
    else:
        i=1
        k_max = 0
        while i < n :
            
            if n%i ==0:
                
                if i > k_max :
                    k_max = i
            i+=1
        print(k_max)
    
    return k_max

def pgcd(a,b):
  
    
    while a !=b :
        if a <b :
            b = b -a
            
        else :
            
            a= a- b

    print(a)
    return a 

def ppcm(a,b):
    a =10
    b=20

    t = pgcd(a,b)
    
    h = (a*b)
    k = h/t
    print(k)
    return k
def irreductible (a,b):
    t=pgcd(a,b)
    
    if t !=1:
        print("peut_etre reduciton")
    else :
        print("pas reduction")





def trouver(a,b) :   
    l_a =[]
    l_b =[]
    i=1
    j=1
    while i < a:
        if a%i ==0:
            t=l_a.append(i)
            
        i+=1
    while j <b:
        if b%j==0:
            k=l_b.append(j)
        j+=1
    print(l_a)
    print(l_b)
##    
 
##a = 10/20
##print(a)

##n =  int(input("entré des entiers trictement positifs "))
##plus_grand_diviseur_premier(n)
##pgcd(10,20)
##ppcm(10,20
##irreductible(14,20)
trouver(10,20)
