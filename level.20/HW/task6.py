sentence = input("შეიყვანე წინადადება: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for i in sentence:
    if i:
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("ხმოვნების რაოდენობა:", vowel_count)
print("თანხმოვნების რაოდენობა:", consonant_count)