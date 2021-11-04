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























