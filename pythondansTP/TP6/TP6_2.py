def inverse(a):
    print(a[::-1])
def input_nombre_positive(a):
    l=[]
    
    while True :
        a =int(input("entré nombre positive "))
        if a !=0 :
            l.append(a)
            continue
        else :
            break
    print(l)
    return inverse(l)

input_nombre_positive(5)

