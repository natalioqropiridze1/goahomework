
cold_drinks = ["Coca-Cola", "Pepsi", "Sprite", "Fanta", "Mountain Dew"]
favorite_drink = "Sprite"


user_drink = input("რომელი ცივი სასმელი გიყვარს? ")

if user_drink in cold_drinks:
    print("მშვენიერია!", user_drink, "არის სიაში.")
else:
    print(user_drink, "არ არის სიაში.")

if user_drink == favorite_drink:
    print("აირჩიე ჩემი საყვარელი სასმელი :)")
else:
    print("ეს სასმელი არ არის ჩემი საყვარელი.")
name = "ნატალი" 
print(name[2])
print(name[4])
print(name[3])