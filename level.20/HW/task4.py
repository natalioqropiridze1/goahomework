correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("შეიყვანე PIN კოდი: ")
    
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Access Denied")
        else:
            print(f"შეცდომა! დარჩენილი მცდელობები: {attempts}")