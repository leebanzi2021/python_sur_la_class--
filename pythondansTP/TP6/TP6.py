import math
import random
def minimum(a):
    t =min(a)
    print(t)
    return t 
def contient(a,ele):
    if len(a)==0:
        return False
    return True 

def minimum2(a):
    t = min(a)
    k=a.count(t)
    i=0
    while i<k:
        a.remove(t)
        i+=1   
    print(a)
    t2=min(a)
    print (t,t2)
    return t ,t2










list_a =[0,5,5,9,4,-4,-4]
minimum(list_a)
contient(list_a,0)
minimum2(list_a )



































