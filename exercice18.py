A = int(input("Entrez le premier nombre entier : "))
B = int(input("Entrez le deuxième nombre entier : "))
operateur = input("Entrez l'opérateur : ")

if operateur == '+':
    resultat = A + B
elif operateur == '-':
    resultat = A - B
elif operateur == '*':
    resultat = A * B
elif operateur == '/':
    if B != 0:
        resultat = A / B
    else:
        print("Erreur : Division par zéro.")
else:
    print("Opérateur non reconnu.")
    


print("Le résultat de est :", resultat)
