from math import gcd
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
