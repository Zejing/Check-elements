

element_file = open('element.txt', 'r')

elements = element_file.readline().strip()
element_list = []
while elements:
    element_list.append(elements.lower())
    elements = element_file.readline().strip()

print("list any 5 of the first 20 elements in the Period table")
user_input_list = []
while len(user_input_list) != 5:
    user_input = input("Enter the name of an element:")
    if user_input in user_input_list:
        print(user_input, " was already entered")
    else:
        user_input_list.append(user_input)

find_list = []
not_find_list = []
accuracy = 0
for answer in user_input_list:
    if answer in element_list:
        accuracy += 1
        find_list.append(answer)
    else:
        not_find_list.append(answer)

print(accuracy*20, "%", "correct")
print("Found:", " ".join(find_list).capitalize())
print("Not Found:", " ".join(not_find_list).capitalize())
