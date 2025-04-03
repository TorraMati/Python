ms = int(input("Ingrese su tiempo de reaccion en ms: "))
if ms < 200:
    print("rapido")
elif ms >= 200 and ms <=500:
    print("normal")
else:
    print("lento")