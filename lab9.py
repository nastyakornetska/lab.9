'''
text = input("Введіть текстовий рядок: ")

S1 = {char for char in text if char.isdigit()}  # Множина цифр
S2 = {char for char in text if char.isupper()}  # Множина великих літер
S3 = {text[i] for i in range(len(text)) if i % 2 == 1}  

union_S1_S3 = S1.union(S3)
union_S2_S3 = S2.union(S3)

print("Множина S1 (цифри):", S1)
print("Множина S2 (великі літери):", S2)
print("Множина S3 (символи на парних позиціях):", S3)
print("Об'єднання S1 і S3:", union_S1_S3)
print("Об'єднання S2 і S3:", union_S2_S3)
'''


'''
vegetables = []
num_cultures = int(input("Введіть кількість овочевих культур: "))

for _ in range(num_cultures):
    culture = {}
    culture['Назва культури'] = input("Введіть назву культури: ")
    culture['Країна походження насіння'] = input("Введіть країну походження насіння: ")
    culture['Середня врожайність (ц/Га)'] = float(input("Введіть середню врожайність (в ц/Га): "))
    culture['Необхідність обробки від шкідників'] = input("Чи потрібна обробка від шкідників? (так/ні): ")
    culture['Метод збирання врожаю'] = input("Введіть метод збирання врожаю: ")

    vegetables.append(culture)

print("\nВідомості про овочеві культури:")
for idx, veg in enumerate(vegetables, 1):
    print(f"\nКультура {idx}:")
    for key, value in veg.items():
        print(f"{key}: {value}")
'''


'''
vegetables = []

num_cultures = int(input("Введіть кількість овочевих культур: "))

for _ in range(num_cultures):
    culture = {}
    culture['Назва культури'] = input("Введіть назву культури: ")
    culture['Країна походження насіння'] = input("Введіть країну походження насіння: ")
    culture['Середня врожайність (ц/Га)'] = float(input("Введіть середню врожайність (в ц/Га): "))
    culture['Необхідність обробки від шкідників'] = input("Чи потрібна обробка від шкідників? (так/ні): ")
    culture['Метод збирання врожаю'] = input("Введіть метод збирання врожаю: ")

    details = {}
    details['Колір'] = input("Введіть колір плода: ")
    details['Середня вага одного плода'] = int(input("Введіть середню вагу одного плода: "))
    details['Одиниці ваги плода'] = input("Введіть одиниці ваги плода (наприклад, г, кг): ")
    culture['Відомості про плоди'] = details

    vegetables.append(culture)

print("\nВідомості про овочеві культури:")
for idx, veg in enumerate(vegetables, 1):
    print(f"\nКультура {idx}:")
    for key, value in veg.items():
        if key == 'Відомості про плоди':
            print(f"{key}:")
            for fruit_key, fruit_value in value.items():
                print(f"  {fruit_key}: {fruit_value}")
        else:
            print(f"{key}: {value}")
'''



text = input("Введіть текстовий рядок: ")
words = text.split()
modified_words = []
digit_sets = []

for word in words:
    if len(word) > 1:
        modified_word = word[-1] + word[:-1]
    else:
        modified_word = word  
    modified_words.append(modified_word)
    
    digit_set = {char for char in word if char.isdigit()}
    if digit_set:
        digit_sets.append(digit_set)

if digit_sets:
    intersection_set = set.intersection(*digit_sets)
else:
    intersection_set = set()

print("\nСлова з перенесеною останньою літерою на початок:")
print(" ".join(modified_words))
print("\nПеретин множин цифр у кожному слові:", intersection_set)
