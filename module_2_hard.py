numbers = []
n = int(input('Введите число от 3 до 20: '))

# Проверяем, что введенное число в правильном диапазоне
if n < 3 or n > 20:
    print("Число должно быть от 3 до 20.")
else:
    for i in range(1, 21):
        for j in range(1, 21):
            k = i + j
            # Проверяем кратность и условие i < j
            if n % k == 0 and i < j:
                numbers.append((i, j))  # Сохраняем пару как кортеж
                print(f'{k} = {i} + {j}', end='; ')

    # Выводим все найденные пары
    print("\nНайденные пары:", numbers)