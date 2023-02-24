

lado = int(input("Digite el lado del cuadrado: "))

print("*" * lado)   
for i in range(lado - 2):
    print("*" + " " * (lado - 2) + "*")
print("*" * lado)

print("")

while lado > 0:
    print("*" * lado)
    lado -= 1
