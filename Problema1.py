EP = int(input('Ingrese la edad de el pasajero:'))
ValIni = 300
if(EP<=5):
  ValFin = 0
elif(EP==18):
  ValFin = ValIni/2
else:
  ValFin = ValIni
print(f'el valor a pagar es:{ValFin}')