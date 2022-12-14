# for nombre in range(1, 101):
#     if nombre % 3 == 0 and nombre % 5 == 0:
#         print("fizzbuzz")
#     elif nombre % 3 == 0:
#         print("fizz")
#     elif nombre % 5 == 0:
#         print("buzz")
#     else:
#         print(nombre)


def est_divisible_par(numerateur: int, denominateur: int) -> bool:
    """Permet de savoir si un nombre est divisible par un autre.

    Paramètres:
        numerateur: int : le numérateur
        denominateur : int : le dénominateur

    Retourne :
        booléen : est-ce que les nombres sont divisibles
    """

    return numerateur % denominateur == 0


def fizzbuzz_2():
    for nombre in range(1, 101):
        res = regle_fizz_buzz_2(nombre)
        print(res)


def regle_fizz_buzz_2(nombre: int) -> str:
    res = ""
    if est_divisible_par(nombre, 3):
        res += "fizz"
    if est_divisible_par(nombre, 5):
        res += "buzz"
    if not res:
        res = str(nombre)
    return res


print("\n".join(map(regle_fizz_buzz_2, range(1, 101))))
# for nombre in range(1, 101):
#     res = "fizz" * int(nombre % 3 == 0) + "buzz" * int(nombre % 5 == 0) or str(nombre)
#     print(res)

# for n in range(100):
#     if n % 3 == 0:
#         if n % 5 == 0:
#             print("fizzbuzz")
#         else:
#             print("fizz")
#     elif n % 5 == 0:
#         print("buzz")
#     else:
#         print(n)
