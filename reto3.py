print('Secuencia fibonacci')
hasta = int(input('ingrese  un valor límite:'))
val1 = 0
val2 = 1
resultado = 0
while(resultado<=hasta):
  print(f'{val1}+{val2}={resultado}')
  val1=val2
  val2=resultado
  resultado=val1+val2