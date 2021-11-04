print("créer une mots des pass")
print("ex :: 123456")
mps="123456"
a=1
while a !=0:
    a=input("créer votre mot de pass ")
    if a==mps:
        print("créer complet  ")
        while  a!=0:
            a=input("LOGIN ACCOUNT  ")
            if a == mps:
                print("permet accès ")
                break 
            else :
                i=0
                while i < 5 :
                        i =i+1
                        a = input("again")
                        if a == mps :
                            print ("permet accès ")
                            break

                        else :
                            if i == 5 :
                                print("après 5 erreur accès refusé ")
                                break 
                            else :
                                continue
            break                
        break 
    else :
        print("refusé accès ")
        continue 

        
##while  a!=0:
##    a=input("nhap code cua ban ")
##    if a == mps:
##        print("permet accès ")
##        break 
##    else :
##        i=0
##        while i < 5 :
##                i =i+1
##                a = input("again")
##                if a == mps :
##                    print ("permet accès ")
##                    break
##
##                else :
##                    if i == 5 :
##                        print("après 5 erreur accès refusé ")
##                        break 
##                    else :
##                        continue 
                    
