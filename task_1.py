def max_rectangle_area(length):
    l, r = 0, len(length) - 1
    max_area = 0
    
    while l < r:
        # Вычисляем площадь
        height = min(length[l], length[r])
        width = r - l
        area = height * width
        
        # Обновляем максимальную площадь
        max_area = max(max_area, area)
        
        # Двигаем указатель
        if length[l] < length[r]:
            l += 1
        else:
            r -= 1
    return max_area

line = input()
#lengths= [2, 4, 3, 2, 1, 4, 1]  
lengths = list(map(int, line.split(' ')))  # Высоты заборов на участках
result = max_rectangle_area(lengths)
print("Максимальная площадь:", result)
