numbers = ()
while True:
    number = float(input("შეიყვანე რიცხვი: "))
    
    if number == -1:
        break
    
    numbers.app(number)

average = sum(numbers) / len(numbers) if numbers else 0
print("შეყვანილი რიცხვების საშუალო:", average)