age = int(input("Возраст: "))
has_access = True

print(f"Допуск имеется: {has_access}")

if age >= 18 and has_access:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")
