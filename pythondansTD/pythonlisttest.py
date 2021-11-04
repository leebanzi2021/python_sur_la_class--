ma_list=[1,2,4,5,6,8,10,11]
def indice(liste,i):
    if i in liste:
        return  liste.index(i)
    else :
        return -1
print(indice(ma_list,9))
