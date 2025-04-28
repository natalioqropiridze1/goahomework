number = int(input("insert nummber "))

if number > 0:
    print("this number is positive.")
    #elif მუშაობს if-ის შემდეგ, და შეამოწმებს პირობას მხოლოდ იმ შემთხვევაში თუ პირველი if არ არის
elif number < 0:
    print("this number is negative")
else:
    print("the number is 0")