import numpy as np
import matplotlib.pyplot as plt


# Определение функции (вариант 20)
def f(x):
    return 1.5 * np.exp(x / 5 + 0.02) * np.sin(3 * x)


# Интервал
a, b = -2, 1


# Функция для полинома Лагранжа
def lagrange_interpolation(x, x_nodes, y_nodes):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result


# Функция для построения и сохранения графика
def make_plot(n, filename):
    # Узлы интерполяции
    x_nodes = np.linspace(a, b, n)
    y_nodes = f(x_nodes)

    # Точки для отрисовки линий
    x_plot = np.linspace(a, b, 200)
    y_true = f(x_plot)
    y_interp = [lagrange_interpolation(val, x_nodes, y_nodes) for val in x_plot]

    # Ошибка
    error = np.abs(y_true - y_interp)

    # Создаем фигуру с двумя графиками
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # График 1: функция и полином
    ax1.plot(x_plot, y_true, 'b-', label='Исходная функция f(x)')
    ax1.plot(x_plot, y_interp, 'r--', label=f'Полином Лагранжа (n={n})')
    ax1.scatter(x_nodes, y_nodes, color='black', zorder=5, label='Узлы')
    ax1.set_title(f'Интерполяция при {n} узлах')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()

    # График 2: ошибка
    ax2.semilogy(x_plot, error, 'g-', label='Абсолютная ошибка |f(x) - Ln(x)|')
    ax2.set_title('График ошибки (log scale)')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.set_xlabel('x')
    ax2.legend()

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Сохранен график: {filename}")


# Генерируем графики для 4, 10 и 15 узлов
make_plot(4, 'plot_n4.png')
make_plot(10, 'plot_n10.png')
make_plot(15, 'plot_n15.png')