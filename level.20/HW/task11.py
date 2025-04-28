colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = int(input("შეიყვანე ინდექსი (0-3): "))
new_color = input("შეიყვანე ახალი ფერი: ")
colors[index] = new_color  # ინდექსზე არსებული ფერის შეცვლა
print(colors)