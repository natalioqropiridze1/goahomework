total = 0  

while True:
    number = int(input("შეიყვანე რიცხვი: "))
    if number < 0: 
        break
    total += number  
print("დახარჯული დადებითი რიცხვების ჯამი:", total)