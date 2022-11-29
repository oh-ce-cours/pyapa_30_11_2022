# for nombre in range(1, 101):
#     if nombre % 3 == 0 and nombre % 5 == 0:
#         print("fizzbuzz")
#     elif nombre % 3 == 0:
#         print("fizz")
#     elif nombre % 5 == 0:
#         print("buzz")
#     else:
#         print(nombre)

# for nombre in range(1, 101):
#     res = ""
#     if nombre % 3 == 0:
#         res += "fizz"
#     if nombre % 5 == 0:
#         res += "buzz"
#     if not res:
#         res = str(nombre)
#     print(res)

for nombre in range(1, 101):
    res = ""
    res += "fizz" * (nombre % 3 == 0)
    if nombre % 5 == 0:
        res += "buzz"
    if not res:
        res = str(nombre)
    print(res)

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
