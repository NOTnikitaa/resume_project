import math

with open('task2_circle.txt', 'r') as f:
  center_x, center_y = map(float, f.readline().split())
  radius = float(f.readline())


with open('task2_points.txt', 'r') as f:
      for line in f:
        point_x, point_y = map(float, line.split())

        distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2) # Расчет расстояния от точки до центра окружности
        if distance < radius:
          print("1")
        elif distance > radius:
          print("2")
        else:
          print("0")