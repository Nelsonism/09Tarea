import numpy as n
import matplotlib.pyplot as p


# Carga archivo
Datos = n.loadtxt("data/DR9Q.dat", usecols=(80, 81, 82, 83))
# Bandas y errores
iBanda = []
iError = []
zBanda = []
zError = []
# Reparte datos
for a in Datos:
    iBanda.append(a[0]*3.631)
    iError.append(a[1]*3.631)
    zBanda.append(a[2]*3.631)
    zError.append(a[3]*3.631)
# Obtiene la recta con los datos de las bandas
Recta = n.polyfit(iBanda, zBanda, 1)
# Arreglo para plotear la recta
x = n.linspace(0, 500, 1000)
fig = p.figure()
p.plot(x, Recta[0] * x + Recta[1], 'k', label='$Recta$ $encontrada$')
print ('La recta es: '+str(round(Recta[0], 3)) +
       ' * x +'+str(round(Recta[1], 3)))
# Monte Carlo
Nmon = 100000
a = []
b = []
N = Datos.shape[0]
for i in range(Nmon):
    r = n.random.normal(0, 1, size=N)
    iB = iBanda + iError * r  # A la banda le suma el error
    zB = zBanda + zError * r  # multiplicado por la variable aleatoria
    a.append(n.polyfit(iB, zB, 1)[0])  # Utiliza polyfit para obtener
    b.append(n.polyfit(iB, zB, 1)[1])  # el ajuste del intervalo
A = n.sort(a)  # Ordena
B = n.sort(b)
Ainf = round(A[Nmon * 0.025], 3)  # Elige limites
Asup = round(A[Nmon * 0.975], 3)
Binf = round(B[Nmon * 0.025], 3)
Bsup = round(B[Nmon * 0.975], 3)
print ('El intervalo de confianza para alfa al 95% es: ['+str(Ainf)+', ' +
       str(Asup)+']')
print ('El intervalo de confianza para beta al 95% es: ['+str(Binf)+', ' +
       str(Bsup)+']')
# Plots
x = n.linspace(0, 500, 1000)
p.plot(x, x * Ainf + Binf, 'g', linestyle='-.',
       label='$Intervalo$ $de$ $confianza$')
p.plot(x, x * Asup + Bsup, 'g', linestyle='-.')
p.errorbar(iBanda, zBanda, xerr=iError, yerr=zError, fmt='o',
           label='$Datos$ $Observacionales$')
p.title('$Datos$ $y$ $recta$ $resultante$ $con$ $Quasares$')
p.xlabel('$Flujo$ $banda$ $i$ $[\mu Jy]$')
p.ylabel('$Flujo$ $banda$ $z$ $[\mu Jy]$')
p.xlim(-25, 450)
p.ylim(-25, 500)
p.legend(loc='lower right')
fig.savefig('GraficoP3.png')
p.show()
