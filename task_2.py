
from collections import defaultdict, deque
import heapq

def min_steps_to_last_island(islands):
    n = len(islands)
    
    # Мы будем использовать приоритетную очередь для алгоритма Дейкстры
    min_heap = []
    heapq.heappush(min_heap, (0, 0))  # (количество шагов, индекс острова)
    
    # Массив для хранения минимального количества шагов до каждого острова
    min_steps = [float('inf')] * n
    min_steps[0] = 0

    # Хранение островов по материкам
    continent_map = defaultdict(list)
    for i in range(n):
        continent_map[islands[i]].append(i)
    
    visited = [False] * n

    while min_heap:
        steps, current = heapq.heappop(min_heap)
        
        if visited[current]:
            continue
        visited[current] = True
        
        # Если мы добрались до последнего острова, возвращаем количество шагов
        if current == n - 1:
            return steps
        
        # Соседи (паром)
        for neighbor in [current - 1, current + 1]:
            if 0 <= neighbor < n and not visited[neighbor]:
                if steps + 1 < min_steps[neighbor]:
                    min_steps[neighbor] = steps + 1
                    heapq.heappush(min_heap, (steps + 1, neighbor))
        
        # Порталы (перемещение по материкам)
        same_continent = continent_map[islands[current]]
        for neighbor in same_continent:
            if neighbor != current and not visited[neighbor]:
                if steps + 1 < min_steps[neighbor]:
                    min_steps[neighbor] = steps + 1
                    heapq.heappush(min_heap, (steps + 1, neighbor))
        
        # После обработки текущего острова, временно удаляем доступ к его материкам
        continent_map[islands[current]] = []

    return -1  # Это не должно произойти в рамках данной задачи

# Чтение входных данных, ожидание ввода в формате одной строки, состоящей из целых чисел
islands_input = list(map(int, input().strip().split()))
result = min_steps_to_last_island(islands_input)
print(result)

