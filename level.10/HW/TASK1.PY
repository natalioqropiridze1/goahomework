""""2) შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის 
მონაცემი ინახება ამ ცვლადში და დაპრინტავთ."""


data = input("შეიყვანეთ მნიშვნელობა: ")

data_type = type(data)

print ("შეყვანილი მონაცემის ტიპია:"+str(type(data)))