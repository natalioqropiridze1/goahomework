correct_password = "natali"

while correct_password:
    user_input = input("შეიყვანეთ პაროლი: ")
    if user_input == correct_password:
        print("პაროლი სწორია")
        break
    else:
        print("არასწორი პაროლი, სცადეთ ხელახლა")