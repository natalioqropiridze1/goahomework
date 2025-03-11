# თავდაპირველი წიგნების ფასები
book_price_1 = 25.00
book_price_2 = 18.50
book_price_3 = 32.75
book_price_4 = 40.00
book_price_5 = 22.30

# ფასდაკლების ოდენობა
discount_amount = 5.00

# ახალი ფასები (ძველი ფასებიდან ვაკლებთ ფასდაკლებას)
new_book_price_1 = book_price_1 - discount_amount
new_book_price_2 = book_price_2 - discount_amount
new_book_price_3 = book_price_3 - discount_amount
new_book_price_4 = book_price_4 - discount_amount
new_book_price_5 = book_price_5 - discount_amount

# ბეჭდავს ახალ ფასებს
print("New book prices after discount:")
print("წიგნი 1: $" + str(new_book_price_1))
print("წიგნი 2: $" + str(new_book_price_2))
print("წიგნი 3: $" + str(new_book_price_3))
print("წიგნი 4: $" + str(new_book_price_4))
print("წიგნი 5: $" + str(new_book_price_5))