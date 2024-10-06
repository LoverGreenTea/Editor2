from PIL import Image, ImageFilter

Image = Image.open("GreenTea.jpg")

while True:
    print("1. Показати Зображення")
    print("2. Зберегти Зображення")
    print("3. Чорне біле")
    print("4. перевернути зображення")
    print("5. сам не знаю")
    print("6.")
    operator = input("Введіть Операцію")
    if operator == "1":
        Image.show()
    elif operator == "2":
        name = input("")
        Image.save(name)
    elif operator == "3":
        Image = Image.convert("L")
    elif operator == "4":
        Image = Image.rotate(90)
    elif operator == "5":
        Image = Image.filter(ImageFilter.EMBOSS)