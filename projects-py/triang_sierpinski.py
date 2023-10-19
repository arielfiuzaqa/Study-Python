import matplotlib.pyplot as plt

def plot_triangle(x, y, size, depth):
    if depth == 0:
        # Desenha um triângulo preto nas coordenadas x, y
        triangle = plt.Polygon([[x, y], [x + size, y], [x + size / 2, y + size]], closed=True, edgecolor='black')
        plt.gca().add_patch(triangle)
    else:
        # Calcula o tamanho reduzido para os próximos triângulos
        new_size = size / 2
        # Calcula as coordenadas dos três triângulos menores
        x1, y1 = x, y
        x2, y2 = x + size / 2, y + size
        x3, y3 = x + size, y
        # Chamadas recursivas para cada triângulo menor
        plot_triangle(x1, y1, new_size, depth - 1)
        plot_triangle(x2, y2, new_size, depth - 1)
        plot_triangle(x3, y3, new_size, depth - 1)

# Tamanho da figura e profundidade do fractal
fig_size = 4
max_depth = 2

# Cria uma figura vazia
plt.figure(figsize=(fig_size, fig_size))
plt.gca().set_aspect('equal')

# Chama a função principal para desenhar o fractal
plot_triangle(1, 1, fig_size - 2, max_depth)

# Remove eixos e exibe a imagem
plt.axis('off')
plt.show()
