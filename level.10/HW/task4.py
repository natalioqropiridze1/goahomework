"""5) მომხმარებელს შემოატანინეთ თავისი ასაკი, შემდეგ შემოატანინეთ წლების რაოდენობა. მიღებული ინფორმაცია შეინახეთ 
ცვლადებში და გამოითვალეთ, რამდენი წლის იქნება მომხმარებელი y (მომხმარებლის მიერ შემოტანილი) წლის შემდეგ. საბოლოოდ 
გამოუტანეთ შედეგი შემდეგი სახით: "[წლები] წლის შემდეგ თქვენ იქნებით [მომავალი ასაკი] წლის". დავალების შესასრულებლად 
გამოიყენეთ მონაცემთა ტიპების ხელოვნურად შეცვლის მეთოდები: int() - რომ შეასრულოთ ართიმეტიკული მოქმედებები, str() - რომ 
დაბეჭდოთ შედეგი შეცდომების გარეშე"""

# მომხმარებლის ასაკის შეყვანა
age = input("შეიყვანეთ თქვენი ასაკი:")

# წლების რაოდენობის შეყვანა
years = input("რამდენი წლის შემდეგ გაინტერესებთ თქვენი ასაკი? ")

# მოცემული წლის შემდეგ ასაკის დაანგარიშება
future_age = int(age) + int(years)

# შედეგის დაბეჭდვა
print(str(years) + " წლის შემდეგ თქვენ იქნებით " + str(future_age) + " წლის.")
