import pandas as pd
import matplotlib.pyplot as plt

'''
country = ['Colombia', 'Ecuador', 'México']
population = [50, 12, 129]
colors = ['yellow', 'red', 'green']

plt.bar(country,population, color = colors )
plt.title('Population vs Country')
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()

'''
'''
mes = ['ene', 'feb', 'mar', 'abr', 'may', 'jun']
promedio_temperatura = [29, 32, 31, 28, 27, 29 ]

mes_ = ['ene', 'feb', 'mar', 'abr', 'may', 'jun']
promedio_temperatura_ = [28, 30, 27, 31, 28, 28 ]

plt.plot(mes, promedio_temperatura, marker='d', linestyle='--', color='g', label='Barranquilla')
plt.plot(mes_,promedio_temperatura_, marker='o',linestyle='-', color='r', label='Medellín')
plt.title('Promedio de temperatura Barranquilla vs Medellín 2022')
plt.xlabel('Mes')
plt.ylabel('Promedio de temperatura (°c)')
plt.legend()
plt.show()

'''

'''


gastos = ['Servicios públicos', 'Alimentación', 'Transporte', 'Arriendo', 'Recreación', 'Salud', 'Ahorro']

valor = [200000, 1000000, 300000, 900000, 350000, 100000, 250000]
suma = sum(valor)
print(suma)


plt.pie(valor, labels = gastos, autopct='%1.1f%%')
plt.title('Porcentaje de gastos mensuales')
#plt.legend(loc='upper left')
plt.show()

'''
tuits = ['Experiencias\n personales', 'Política', 'Religión', 'Deporte', 'Tecnología']
num_tuits = [314000, 1346800, 400000, 1800000, 950000]
total_tuits = sum(num_tuits)
print(total_tuits)

plt.pie(num_tuits, labels= tuits, autopct='%1.1f%%')
plt.title('Temáticas que más se postean en Twitter Colombia')
plt.text(-1.5,-1.5,f'Muestra: {total_tuits} tuits', fontsize=12)
plt.show()