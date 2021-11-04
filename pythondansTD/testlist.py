##def triangle_alphabetique(c,n):
##    i=1
##    while i <=n :
##        j =1
##        while j<=i:
##        
##            print(c,end='')
##            j+=1
##            c = chr(ord(c)+1)
##            if c>= chr(ord('z')+1):
##                c='a'
##                
##        print()
##        i+=1
##triangle_alphabetique('a',12)
def triangle_alphabetique(n):
   
    i = 1
    k=1
    h=n*2
    while i <= n:
        j= 1
        ##t=" "*(h-1)
        ##print(t,end=' ')
        c=1
        while j<=i:
            j+=1
            
            
            print(c,end=' ')
            c+=1
        print ()
        i+=1
        k+=1
        ##h-=2
triangle_alphabetique(4)
