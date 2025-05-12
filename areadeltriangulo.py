print("ingresa la base de el triangulo")
base=float(input())
if base == 0:
    exit()
print("ingresa la altura del triangulo")
altura=float(input())
area=(base*altura)/2
print("el area del triangulo es:",area)
if area>100:
  print("el area es grande")
else:
  print("el area es normal")
