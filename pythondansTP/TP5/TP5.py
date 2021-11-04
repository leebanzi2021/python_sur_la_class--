def capital(y,a ):
    i=0
    t=0
    while i < y:
        
        t = a*1.05 -11
        a = t
        i+=1

    print(t)
    return t
def gagne_argent(y,a ):
    t=capital(y,a)
    if t <a:
        print("l'argent diminu ")
    else :
        print ("l'argent haut ou égal")



def placement_min(y ,a ):
   
    
    if a >= (11)/0.05:
        print("l'argent suffit pour ne pas perdu fixe  ")
        return a

    else :
        print("perdu l'argent quand  tu économies")
    
def dure_min(a,but):
    
    i=0
    t=0
    if a >= 220:
        while t< but:
            
            t = a*1.05 -11
            a = t
            i+=1
    else :
        print("tu as besoin écomonie plus ")
    return print("min années pout  atteindre le capital souhaité ",i)
     
def capital_debut_principal(y,a,but):
    
    capital(y,a)
    gagne_argent(y,a )
    dure_min(a , but )
    placement_min(y ,a )
    dure_min(a,but)
    

y = int(input("nb_annees"))
a = int(input("en euros "))
but =int(input("nombre l'argent tu veut "))
capital_debut_principal(y,a,but)

