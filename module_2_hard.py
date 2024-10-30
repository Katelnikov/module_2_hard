numbers = []
n = int(input('Введите число от 3 до 20: '))

if n < 3 or n > 20:
    print("Число должно быть от 3 до 20.")
else:
    for i in range(1, 21):
        for j in range(1, 21):
            k = i + j
            if n % k == 0 and i < j:
                numbers.append((i, j))
                print(f'{k} = {i} + {j}', end='; ')

    print("\nНайденные пары:", numbers)
