def choissir_force_de_chevaux(a,f):

    i=0
    position_chevaux =[]
    while i < len(a):
        if a[i] == f or a[i]+1 == f or a[i]-1 ==f:
             position_chevaux.append(i)
        i+=1
    j=0
             
    while j <len(position_chevaux):
        p=print("les chevaux meme focre à position suivant :",position_chevaux[j]+1)
        y=print("diffent force ",abs(a[position_chevaux[j]]-9))
        j+=1
    

def plus_proches(list1):
    return choissir_force_de_chevaux(list1,9)
    


list1 =[7,10,13,8,9,10,4,7,12,1]

plus_proches(list1)
