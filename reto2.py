n1 = int(input('ingrese la nota 1 (30% de valor):'))
n2 = int(input('ingrese la nota 2 (30% de valor):'))
n3 = int(input('ingrese la nota 3 (40% de valor):'))
nf = ((n1*30)+(n2*30)+(n3*40))/100
print(f'la nota final fue:{nf}' ) 
if nf >= 3:
    print('el estudiante aprobó')
else:
    print('el estudiante reprobó')