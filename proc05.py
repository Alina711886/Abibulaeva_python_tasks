# Proc5. Функция rect_ps(x1, y1, x2, y2) возвращает периметр и площадь прямоугольника со сторонами,
# параллельными осям, по противоположным вершинам. Найти P и S трёх прямоугольников

def rect_ps(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    perimeter = (width + height) * 2
    area = width * height
    return perimeter, area

for i in range(3):
    x1, y1 = float(input()), float(input())
    x2, y2 = float(input()), float(input())
    print(rect_ps(x1, y1, x2, y2))