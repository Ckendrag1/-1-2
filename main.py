import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Запрос длины пароля у пользователя с проверкой
length = int(input("Введите длину пароля (от 6 до 10): "))

if 6 <= length <= 10:
    password = ""
    for i in range(length):
        password += random.choice(chars)
    print("Сгенерированный пароль:", password)
else:
    print("Ошибка: длина пароля должна быть от 6 до 10 символов.")
