# Завдання:
#
# Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.
# Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі,
# у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин,
# а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

import heapq
import random


def minimal_connection_cost(cable_lengths: list) -> int:
    heapq.heapify(cable_lengths)  # перетворення списку у пріоритетну чергу (heap)

    total_cost = 0

    while len(cable_lengths) > 1:
        # об'єднання двох найменших кабелів
        min1 = heapq.heappop(cable_lengths)
        min2 = heapq.heappop(cable_lengths)

        # обчислення витрат на з'єднання
        connection_cost = min1 + min2
        total_cost += connection_cost

        # додаємо новий об'єднаний кабель до черги
        heapq.heappush(cable_lengths, connection_cost)

    return total_cost


if __name__ == "__main__":
    cables = [random.randint(2, 20) for _ in range(5, random.randint(5, 20))]
    print("Дано кабелі:")
    print(cables)
    result = minimal_connection_cost(cables)
    print("Мінімальні витрати на з'єднання:", result)
