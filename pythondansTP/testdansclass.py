''' i=1 '''
''' j=0 '''
''' n=0 '''
''' while i<=10: '''
''' 	i+=2 '''
''' 	j+=1 '''
''' 	k =  (5-j)*" " +  (i-2)*"#"  '''
''' 	print(k) '''
''' t=5 '''
# L = int(input("veuillez  saisir  le nombre  de  lignes "))
# for i in range(0,L): 
    # for j in range(0,i+1): 
        # n = j+1 
        # print(n,end=" ") 
    # print() 
""" L = int(input("nombres lignes besoin ")) """
""" i = 0 """
""" j = 0  """
""" while i < L : """
"""      """
"""     i += 1 """
"""     while j <L : """
"""         j += 1 """
"""          """
"""         k = j +1 """
"""         print(k, end="") """
# a , b, x = int 
# x % 5 == 0 and a<x<b  or x % 2 != 0 and x>b 

# a , x = int 
# x % 2!=0 and x % a == 0 #c'est arrestion 
# not  (x %2==0 or x % a !=0) # c'est  négatif  




# exercise examnal 
# sup_val = 0
# inf_val = 0
# éga_val =0 
# 
# val = float(input("entré le nombre val "))
# nb = int(input("entré  le nombre nb   "))
# i = 0
# while i <nb :
    # i += 1 
    # print("le nombre d'éléments  de cette  série est",i , "puis " )
# 
    # x = int(input("entré le nombre nb "))
    # if x < val  :
        # sup_val += 1 
    # elif x> val :
        # inf_val +=1
    # elif x == val:
        # éga_val +=1
        # 
# print("sup_val est", sup_val,"inf_val est" ,inf_val, "éga_val est ", éga_val )

# exmemel

# max_1=0
# max_2= 0
# 
# while max_1!=1: 
    # a = input("entré nombre ")
    # if a == "":
        # print("vide  nombre  ,terminal")
        # break 
# 
        # 
    # else :
        # a = int(a)
        # if a > max_1:
            # 
            # max_2= max_1
            # max_1=a
            # 
        # elif   a > max_2 :
        # 
            # max_2 = a
        # print ( max_2 ,max_1)
a1 = 1 
a2= 1
i =2
n = int(input("entré n de Fibonacci"))
print(" 1,1,",end="" )
while i < n :
    i+=1

    a3 = a2 +a1 
    a1 = a2
    a2 = a3
    
    print(a3,end=",")


    




