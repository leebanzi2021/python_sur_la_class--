a = 0 #float(input("noté d'examen ") )
max_de_a  = -1
min_de_a  = 21
sommes = 0
nb_notes = 0

n = int(input("combien notes tu as besoin ?"))
while nb_notes < n :
    a = float(input("noté examen "))
    if  0<=a<=20:
        nb_notes = 1+ nb_notes
        sommes = a + sommes
        if a > max_de_a:
            max_de_a = a
            print(max_de_a)
        if a < min_de_a:
            min_de_a = a
    else :
        print("erreur et again")
        continue 

if nb_notes > 0:
    moyen = sommes/nb_notes 
    
    print("valeur note a est", "max est " ,max_de_a,"min est ",min_de_a,"moyen est ", moyen)
