import numpy as np
import matplotlib.pyplot as plt

# Исходная функция
def f(x):
    return 1.5 * np.exp(x/5 + 0.02) * np.sin(3*x)

# Отрезок и узлы
a, b = -2, 1
n = 4
x_nodes = np.linspace(a, b, n)
h = x_nodes[1] - x_nodes[0]
y_nodes = f(x_nodes)

# Вычисление производных по выведенным формулам
df = np.zeros(n)
df[0] = (-11*y_nodes[0] + 18*y_nodes[1] - 9*y_nodes[2] + 2*y_nodes[3]) / (6*h)
df[1] = (-2*y_nodes[0] - 3*y_nodes[1] + 6*y_nodes[2] - y_nodes[3]) / (6*h)
df[2] = (y_nodes[0] - 6*y_nodes[1] + 3*y_nodes[2] + 2*y_nodes[3]) / (6*h)
df[3] = (-2*y_nodes[0] + 9*y_nodes[1] - 18*y_nodes[2] + 11*y_nodes[3]) / (6*h)

# Печать таблицы в консоль
print(" i |    xi   |   f(xi) |  f'(xi)")
print("-" * 35)
for i in range(n):
    print(f" {i} | {x_nodes[i]:7.4f} | {y_nodes[i]:7.4f} | {df[i]:7.4f}")

# Построение графика
x_dense = np.linspace(a - 0.2, b + 0.2, 500)
y_dense = f(x_dense)

plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_dense, 'b-', label='Функция f(x)')
plt.plot(x_nodes, df, 'rx', markersize=8, label="Значения f'(x) в узлах")

plt.title('Функция и её производные (4 узла)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

# Сохранение графика
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()