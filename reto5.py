num = int(input('ingrese el número al que desea calcular su factorial:'))
for f in range (1,num,1):
  num *= f
  print(num)
print(f'el factorial del valor ingresado es:{num}')