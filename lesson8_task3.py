import math

def rectangle(x, y):
    return x * y

def triangle(x, y):
    return x * y / 2

def circle(radius):
    return math.pi * radius ** 2

def calculator():
    results = []
    
    while True:
        print("Виберіть операцію:")
        print("1. Площа прямокутника")
        print("2. Площа трикутника")
        print("3. Площа круга")
        
        choice = input("Введіть номер операціЇ (1/2/3): ")
        
        if choice == '1':
            num1 = float(input("Введіть довжину прямокутника: "))
            num2 = float(input("Введите ширину прямокутника: "))
            result = rectangle(num1, num2)
            operation = f"Площадь прямокутника с довжиной {num1} и шириной {num2} = {result}"
            print(operation)
            results.append(operation)
        
        elif choice == '2':
            num1 = float(input("Введіть основу трикутника: "))
            num2 = float(input("Введіть висоту трикутника: "))
            result = triangle(num1, num2)
            operation = f"Площа трикутника с основою {num1} и висотою {num2} = {result}"
            print(operation)
            results.append(operation)
        
        elif choice == '3':
            radius = float(input("Введіть радіус круга: "))
            result = circle(radius)
            operation = f"Площа круга с радіусом {radius} = {result:.2f}"
            print(operation)
            results.append(operation)
        
        else:
            print("спробуйте знову")

if __name__ == "__main__":
    calculator()