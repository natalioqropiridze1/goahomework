current_height = float(input("სიმაღლე "))
years = int(input("წლები"))

# სავარაუდო სიმაღლის გამოთვლა
growth_per_year = 0.5  # სმ
future_height = current_height + (years * growth_per_year)

# შედეგის გამოყვანა
print(future_height)