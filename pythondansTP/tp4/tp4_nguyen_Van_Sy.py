import math
import string
###la bosse  des maths

##1
def valeur(x):
    t=abs(x)
    print(t)
    
valeur(-1)
##2
def signe_different(x,y):
    if (x <0 and y >0) or (x>0 and y < 0) :
        k = True 
        
    else :
        k = False
    return k 
    

k=  signe_different(6,5)
print(k)
##3
def fonction(x):
    y=3*x**2+2*x+3
    return y

x= float(input("entré x "))

k = fonction(x)
print(k)
##4
def fonction(a,b,c):
    d=b**2-4*a*c
    #denta = math.sqrt(16)
    return d

d= fonction(3,2,1)
#print(k)
print(d)

###le journal  de m.Bizarre 

def lundi(a):
    i=0
    k = s.split()
  
    while i <=(len(k)-1):
    
        #k[i]*k[i]
        t=print(" "+k[i]+" "+k[i]+" ",end='')
        i+=1
    return t 

def mardi(a):
    i=0
    k = a.split()
    while i <=(len(k)-1):
        if len(k[i])%2==0:
            t=print(k[i]*6,end=' ')
        elif  len(k[i])%2!=0:
            t=print(k[i]*3,end=' ')
        i+=1
    
    return t 


def mercredi(a):
    i = 0
    k= a.split()
    l =[]
    while  i <= (len(k)-1):
        k = a.split()
        if len(k[i])%2!=0:
            t=(a.replace(k[i],"impair")).split()
            l.append(t[i])
        else :
            l.append(k[i])
            
        i+=1
            
    n =print(" ".join(l))  
    return  n
    


def jeudi(a):
    n = 0
    i = len(a)%3
    while n < i:
        if n < i-1:
            print(a,end="")
        else :
            return(print(a))
        n = n + 1
def vendredi (a):
    return print(a) 

def tranforme(mot, num_jour ):
    if num_jour==0 or num_jour>5:
        print("erreur")
    else :
        if num_jour == 1:
            return (lundi(mot))

        if num_jour == 2:
            return (mardi(mot))
        if num_jour == 3:
            return (mercredi(mot))
        if num_jour == 4:
            return (jeudi(a))
        if num_jour == 5:
            return (vendredi(mot))
#key test    
s = "bonjour a tous  "

n= tranforme(s,3)
