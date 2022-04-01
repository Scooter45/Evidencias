can = int(input('cantidad de números que desea comparar (2-3)'))
if(can==2):
  num1 = int(input('ingrese la primera cifra a comparar:'))
  num2 = int(input('ingrese la segunda cifra a comparar:'))
  print(f'{max(num1,num2)} es el número mayor y {min(num1,num2)} es el número menor')
elif(can==3):
  num1 = int(input('ingrese la primera cifre a comparar:'))
  num2 = int(input('ingrese la segunda cifra a comparar:'))
  num3 = int(input('ingrese la tercera cifra a comparar:'))
  print(f'{max(num1,num2,num3)} es el número mayor y {min(num1,num2,num3)} es el número menor')
else:
  print('por favor reinicie el código y dijite una cantidad de números válida')