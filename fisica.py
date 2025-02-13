import pygame
import math
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hexágono giratorio con círculo")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Parámetros del hexágono
num_sides = 6
radius = 200
center = (width // 2, height // 2)
angle = 0
angular_speed = 0.02

# Parámetros del círculo
circle_radius = 20
circle_pos = list(center)  # Empezar en el centro
circle_speed = [3, 3]
gravity = 0.1
friction = 0.98

# Función para obtener los vértices del hexágono
def get_hexagon_points(center, radius, angle):
    points = []
    for i in range(num_sides):
        x = center[0] + radius * math.cos(angle + 2 * math.pi * i / num_sides)
        y = center[1] + radius * math.sin(angle + 2 * math.pi * i / num_sides)
        points.append((x, y))
    return points

# Función para verificar si un punto está dentro del hexágono
def point_in_hexagon(point, hexagon_points):
    x, y = point
    n = len(hexagon_points)
    inside = False
    for i in range(n):
        x1, y1 = hexagon_points[i]
        x2, y2 = hexagon_points[(i + 1) % n]
        if y > min(y1, y2):
            if y <= max(y1, y2):
                if x <= max(x1, x2):
                    if y1 != y2:
                        xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if y1 == y2:
                        if y == y1 and x <= max(x1, x2):
                            inside = not inside
                    else:
                        if x1 == x2 or x <= xinters:
                            inside = not inside
    return inside

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Obtener los puntos del hexágono
    hexagon_points = get_hexagon_points(center, radius, angle)
    angle += angular_speed  # Rotar el hexágono

    # Dibujar el hexágono
    pygame.draw.polygon(screen, BLACK, hexagon_points, 2)

    # Actualizar la posición del círculo
    circle_speed[1] += gravity
    circle_pos[0] += circle_speed[0]
    circle_pos[1] += circle_speed[1]

    # Verificar colisiones con los límites del hexágono
    if not point_in_hexagon(circle_pos, hexagon_points):
        # Si el círculo sale del hexágono, invertir la dirección y aplicar fricción
        circle_speed[0] = -circle_speed[0] * friction
        circle_speed[1] = -circle_speed[1] * friction
        # Asegurarse de que el círculo no se salga del hexágono
        circle_pos[0] = max(min(circle_pos[0], center[0] + radius), center[0] - radius)
        circle_pos[1] = max(min(circle_pos[1], center[1] + radius), center[1] - radius)

    # Dibujar el círculo
    pygame.draw.circle(screen, RED, (int(circle_pos[0]), int(circle_pos[1])), circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()