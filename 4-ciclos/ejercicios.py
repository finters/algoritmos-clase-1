invalid=True

while invalid:
    num=input("ingrese un numero entero positivo: ")
    try:
        num=int(num)
        if num > 0:
            invalid=False
        else: 
            print("ingrese un numero positivo")
            print("positivo")
    except Exception:  
        print("ingrese un numero entero")
        print("exeption")
print("ññññ")
#gmerida

suma_imp=0
for i in range(1, num+1, 2):
    suma_imp+=i