import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1.5 * np.exp(x / 5 + 0.02) * np.sin(3 * x)


a, b = -2, 1  # интервал
n_nodes = 11  # Количество узлов


# Вспомогательные фцнкции
def get_coeffs(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef[0, :]


def eval_newton(coef, x_nodes, x_vals):
    n = len(x_nodes) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x_vals - x_nodes[n - k]) * p
    return p


# Генерация данных
# Гладкая сетка для линий
x_smooth = np.linspace(a, b, 1000)
y_true = f(x_smooth)

# А) Равномерная
nodes_uni = np.linspace(a, b, n_nodes)

# Б) Чебышёвская
k = np.arange(n_nodes)
nodes_cheb = (a + b) / 2 + (b - a) / 2 * np.cos((2 * k + 1) * np.pi / (2 * n_nodes))

# В) Случайная
np.random.seed(42)  # Фиксируем сид для красоты
nodes_rand = np.sort(np.random.uniform(a, b, n_nodes))

# Собираем все конфигурации в список для цикла
configs = [
    ("Равномерная", nodes_uni, 'forestgreen', 'darkgreen'),
    ("Чебышёвские", nodes_cheb, 'blue', 'blue'),
    ("Случайные", nodes_rand, 'purple', 'indigo')
]

# Построение графика
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Проходим по колонкам (0, 1, 2)
for col, (title, nodes, color_main, color_err) in enumerate(configs):
    # Считаем полином
    y_nodes = f(nodes)
    coefs = get_coeffs(nodes, y_nodes)
    y_poly = eval_newton(coefs, nodes, x_smooth)

    # Считаем ошибку (абсолютную)
    error = np.abs(y_true - y_poly)
    max_error = np.max(error)

    # График (Функция vs Полином)
    ax_top = axes[0, col]
    # Исходная функция
    ax_top.plot(x_smooth, y_true, color='red', linewidth=2, alpha=0.7, label='f(x)')
    # Полином
    ax_top.plot(x_smooth, y_poly, color=color_main, linestyle='--', linewidth=2, label='P(x)')
    # Узлы
    ax_top.scatter(nodes, y_nodes, color=color_err, s=50, edgecolors='black', zorder=5, label='Узлы')

    # Оформление верхнего
    ax_top.set_title(title, fontsize=12)
    ax_top.grid(True, alpha=0.3)
    ax_top.legend(loc='upper right', framealpha=0.9)

    # Нижний график (Ошибка, логарифмическая шкала)
    ax_bot = axes[1, col]
    # Рисуем ошибку
    ax_bot.semilogy(x_smooth, error, color=color_main, linewidth=1.5)

    # Оформление нижнего
    ax_bot.set_title(f"Ошибка ({title})", fontsize=11)
    ax_bot.grid(True, which="both", ls="-", alpha=0.2)  # Сетка для логарифма

    # Текстовая плашка с макс. ошибкой (как на скрине)
    text_str = f"Max: {max_error:.2e}"  # Формат 1.23e-02
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    # Размещаем текст в левом верхнем углу (координаты 0.05, 0.95 относительно осей)
    ax_bot.text(0.05, 0.95, text_str, transform=ax_bot.transAxes, fontsize=10,
                verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('final_report_plot.png', dpi=300)  # Сохраняем в файл
plt.show()