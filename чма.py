import numpy as np
import matplotlib.pyplot as plt

# Исходная функция (нужна для вычисления значений в узлах)
def f(x):
    return 1.5 * np.exp(x/5 + 0.02) * np.sin(3*x)

# Истинная (аналитическая) производная
def f_prime_true(x):
    # По правилу дифференцирования произведения: (u*v)' = u'*v + u*v'
    # f'(x) = 1.5 * e^(x/5 + 0.02) * (1/5 * sin(3x) + 3 * cos(3x))
    return np.exp(x/5 + 0.02) * (0.3 * np.sin(3*x) + 4.5 * np.cos(3*x))

# Отрезок и узлы
a, b = -2, 1
n = 4
x_nodes = np.linspace(a, b, n)
h = x_nodes[1] - x_nodes[0]
y_nodes = f(x_nodes)

# Вычисление производных по выведенным конечным разностям
df_approx = np.zeros(n)
df_approx[0] = (-11*y_nodes[0] + 18*y_nodes[1] - 9*y_nodes[2] + 2*y_nodes[3]) / (6*h)
df_approx[1] = (-2*y_nodes[0] - 3*y_nodes[1] + 6*y_nodes[2] - y_nodes[3]) / (6*h)
df_approx[2] = (y_nodes[0] - 6*y_nodes[1] + 3*y_nodes[2] + 2*y_nodes[3]) / (6*h)
df_approx[3] = (-2*y_nodes[0] + 9*y_nodes[1] - 18*y_nodes[2] + 11*y_nodes[3]) / (6*h)

# Построение графика
x_dense = np.linspace(a - 0.2, b + 0.2, 500)
y_prime_dense = f_prime_true(x_dense)

plt.figure(figsize=(10, 6))

# СТРОИМ ГРАФИК ИСТИННОЙ ПРОИЗВОДНОЙ
plt.plot(x_dense, y_prime_dense, 'b-', label="Истинная производная $f'(x)$")

# СТРОИМ НАШИ ВЫЧИСЛЕННЫЕ ТОЧКИ
plt.plot(x_nodes, df_approx, 'rx', markersize=8, markeredgewidth=2, label="Численная производная в узлах")

plt.title('Истинная производная и её численное приближение (4 узла)')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

# Сохранение графика
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()