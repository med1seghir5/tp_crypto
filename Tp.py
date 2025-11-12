from math import gcd

#Tp_exo1.py
def add_mod(a, b, n):
    return (a + b) % n

def groupe_additif(n):
    elements = [i for i in range(n)]
    print(f"Les éléments du groupe additif Z/{n}Z sont : {elements}")
n = int(input("Entrez la valeur de n : "))
groupe_additif(n)
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
print(f"({a} + {b}) mod {n} = {add_mod(a, b, n)}")


#Tp_exo2.py
def table_addition(n):
    print(f"\nTable d’addition dans Z/{n}Z :\n")
    table = [[(i + j) % n for j in range(n)] for i in range(n)]
    for ligne in table:
        print(ligne)
table_addition(3)
table_addition(7)


#Tp_exo3.py
def units(n):
    U = []
    for a in range(n):
        if gcd(a, n) == 1:
            U.append(a)
    return U

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None
    k = 1
    valeur = a % n
    while valeur != 1:
        valeur = (valeur * a) % n
        k += 1
    return k

def is_cyclic(n):
    U = units(n)
    taille = len(U)
    generateurs = []

    for a in U:
        if order_mod(a, n) == taille:
            generateurs.append(a)

    if len(generateurs) > 0:
        return True, generateurs
    else:
        return False, []

for n in [11, 14, 16]:
    U = units(n)
    print(f"\n===== n = {n} =====")
    print(f"Éléments inversibles (unités) : {U}")
    print(f"Nombre d'unités = {len(U)}")

    cyclique, generateurs = is_cyclic(n)

    if cyclique:
        print("Le groupe est cyclique.")
        print(f"Générateurs possibles : {generateurs}")
    else:
        print("Le groupe n'est pas cyclique.")
