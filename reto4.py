num = int(input('ingrese un número para analizar:'))
if num > 1:
  for f in range(2, int(num/2)+1):
   if (num % f) == 0:
      print('no es un número primo')
      break
  else:
      print('Es un número primo')
else:
  print('no es un número primo')
if num % 2 == 0:
  print('es un número par')
else:
  print('es un número impar')