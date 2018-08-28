# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

# city_with_a = []
# city_without_a =[]
# for city in cities:
#     if "a" in city.lower():
#         city_with_a.append(city)
#     else:
#         city_without_a.append(city)
# print("city_with_a:", city_with_a, "\n")
# print("city_without_a:", city_without_a)

# total = 0
# for letter in cities:
#     total = total + letter.lower().count("n")
# print(total)

# for city in cities:
#     if "m" in city.lower():
#         print("city with \"m\":", city)

# colors = ["White", "Black", "Red", "Orange", "Brown", "Yellow"]
#
# user_input = input("Enter a color:")
#
# for color in colors:
#     if color.lower() == user_input.lower():
#         print("color is matched, color is", color.title())


# foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
#              "intermediate cuneiform", "medial cuneiform"]
#
# def guess_bones(input_string):
#     correct = 0
#     for bone in foot_bones:
#         if input_string in bone:
#             correct = correct + 1
#             foot_bones.remove(input_string)
#         else:
#             correct = 0
#     if correct > 0:
#         print("correct")
#     else:
#         print("incorrect")
#
# i = 0
#
# while i - 2 != 0:
#     user_input = input()
#     guess_bones(user_input)
#     i = i + 1


# five_fifteen = []
#
# for i in range(5, 16):
#     five_fifteen.append(i)
# print(five_fifteen)

# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# for i in range(2, 5):
#     print(spell_list[i])

# for i in range(len(spell_list)):
#     if spell_list[i] == "Annual":
#         annual_index = i
#
# for i in range(annual_index, len(spell_list)):
#     print(spell_list[i])

# for i in range(20, 10, 2):
#     print(i)

# word = input()
# odd_leters = []
# even_letters = []
# length = len(word)
#
# for i in range(length):
#     if i % 2 == 0:
#         odd_leters.append(word[i])
#     else:
#         even_letters.append(word[i])
#
# print("odd letters:", odd_leters)
# print("even letters:", even_letters)
# num = 0
# for num in range[1,10]:
#     print(num)
# multi_5 = []
# for i in range(5, 100, 5):
#     multi_5.append(i)
# print(multi_5)
# multi_5.reverse()
# print(multi_5)

# list_one = []
# list_two = []
#
# for i in range(4, 45, 4):
#     list_one.append(i)
#
# print(list_one)
# list_one.reverse()
# list_two = list_two + list_one
#
# print(list_two)
#
# list_two.extend(list_one)
#
# print(list_two)
# cities = []
# visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# visited_cities.sort()
# for city in visited_cities:
#     if city[0] < "Q":
#         cities.append(city)
#
# print(cities)

# visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
#
# sorted_cities = sorted(visited_cities)
#
# new_sorted_cities = []
# for city in sorted_cities:
#     if len(city) <= 5:
#         new_sorted_cities.append(city)
#
# print(new_sorted_cities)

# animals = ["Chimpanzee", "Panther", "Wolf", "Armadillo"]
# user_input = 0
# add_animals = []
# while user_input != " ":
#     user_input = input("entre animal:")
#     add_animals.append(user_input)
# add_animals.pop()
# animals.extend(add_animals)
#
# answer_input = input("alpha or reverse alpha order:")
#
# if answer_input == "alpha":
#     animals.sort()
#     print("alpha order:", animals)
# elif answer_input == "reverse":
#     animals.reverse()
#     print("reverse:", animals)
# rhyme = 'Jack and Jill went up the hill To fetch a pail of water'
#
# rhyme_list = rhyme.split()
#
# print(rhyme_list)
#
# for word in rhyme_list:
#     print(word)


# code_tip = "Python uses spaces for indentation"
#
# code_list = code_tip.split()
#
# for i in range(0, len(code_list), 2):
#     print(code_list[i])

# poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
#
# poem_list = poem.split("*")
#
# for word in poem_list:
#     print(word.title())

# letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
#
# print("*".join(letters))

# phrase_words = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']
#
# user_input = input("type something:")
#
# print(user_input.join(phrase_words))
#
# print("I am", end = '-')
# print("Zejing", end = '-')
# print("Cao")
# Msg_characters = list("Always test your code")
#
# for letter in Msg_characters:
#     if letter.isalpha():
#         print(letter)

# dig = list("123456789")
# total = 0
# for i in dig:
#     total = int(i) + total
#
# print(total)
# i = 1
# matter_states = ['solid', 'liquid', 'gas', 'plasma']
# for matter in matter_states:
#     print(matter, "- is state of matter #", i)
#     i = i + 1

# birds = ["turkey", "hawk", "chicken", "dove", "crow"]
#
# for bird in birds:
#     if bird.lower().startswith("c"):
#         birds.remove(bird)
#
# print(birds)

# baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
#
# with_one = 0
# with_two = 0
# with_three = 0
# for basket in baskets:
#     if basket == 1:
#         with_one = with_one + 1
#     elif basket == 2:
#         with_two = with_two + 1
#     elif basket == 3:
#         with_three = with_three + 1
#
#
# print("1pt:", with_one)
# print("2pt:", with_two)
# print("3pt:", with_three)
#
# print("total", with_one + with_two * 2 + with_three * 3)

# for i in range(0,4):
#     print("hello")

# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
# first_half = []
# second_half =[]
# for i in range(len(spell_list)):
#     if i <= int(len(spell_list)/2):
#         first_half.append(spell_list[i])
#     elif i > int(len(spell_list)/2):
#         second_half.append(spell_list[i])
#
# print("first_half:", first_half)
# print("second_half:", second_half)

# twenties = []
# total = 0
# for i in range(20, 29):
#     twenties.append(i)
#     total = total + i
# print(twenties)
# print(total)
# print(20+21+22+23+24+25+26+27+28)

# odd_nums = []
#
# for i in range(1, 26, 2):
#     odd_nums.append(i)
# print(odd_nums)
# odd_nums.reverse()
# print(odd_nums)

# elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
#  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
#  'Potassium', 'Calcium']
# even_elements = []
# for i in range(1, len(elements), 2):
#     even_elements.append(elements[i])
#
# print(even_elements)


# elements_40 = ['Hydrogen', \
#  'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
#  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', \
#  'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', \
#  'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', \
#  'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']
# odd_elements = []
# for i in range(0, len(elements_40), 2):
#     odd_elements.append(elements_40[i])
# print(odd_elements)
# numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
#
# numbers_2 = list(range(30,50,2))
#
# print(numbers_1 + numbers_2)
# numbers_1.extend(numbers_2)
# print(numbers_1)

# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
#
# spell_list.reverse()
# great_eight = []
# for word in spell_list:
#     if len(word) > 8:
#         great_eight.append(word)
#
# print(great_eight)

# elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
#  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
#  'Potassium', 'Calcium']
#
# ele_sort = sorted(elements)
#
# print(ele_sort)

# daily_fact = "Did you know that there are 1.4 billion students in the world?"
#
# fact_words = daily_fact.split()
#
# for word in fact_words:
#     print(word.upper())
#
# poem = "The bright brain, has bran!"
#
# poem_words = poem.split("b")
# print(poem_words)

# halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']
#
# hal_str = ".".join(halogens)
#
# print(hal_str)

# code_tip ="Read code aloud or explain the code step by step to a peer"
# code_c = code_tip.title()
#
# words_list = code_c.split()
#
# print("-".join(words_list))

# long_word = 'decelerating'
#
# for letter in long_word:
#     print(letter)
# questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]
# for sentense in questions:
#     print(sentense, end = '?'"\n")

# user_sring = input("enter a saying or poem:")
# words_list = user_sring.split()
#
# new_word_list = []
# for word in words_list:
#     if len(word) <= 3:
#         new_word_list.append(word.lower())
#     elif len(word) >= 7:
#         new_word_list.append(word.upper())
#     else:
#         new_word_list.append(word)
#
#
# def word_mixer(word_list):
#     word_list_sort = sorted(word_list)
#     print(word_list_sort)
#     new_words = []
#     while len(word_list_sort) > 5:
#         new_words.append(word_list_sort[4])
#         # print("5th", new_words)
#         word_list_sort.pop(4)
#         # print("pop 5th", new_words)
#         new_words.append(word_list_sort[0])
#         # print("4th", new_words)
#         word_list_sort.pop(0)
#         # print("pop 4th", new_words)
#         new_words.append(word_list_sort[-1])
#         # print("-1", new_words)
#         word_list_sort.pop()
#         # print("pop -1", new_words)
#     return new_words
#
# print(word_mixer(new_word_list))

# txt_file = open('exam.txt', 'r')
#
# cities_lines = txt_file.readlines()
#
# count = 0
# for line in cities_lines:
#     cities_lines[count] = line[:-1]
#     count += 1
# cities_lines.reverse()
# print(cities_lines)

# for city in cities_lines:
#     if city[0] >= "D":
#         print(city)
# txt_file.close()
# print(cities_lines)
# count = 0
# for city in cities:
#     cities[count] = city[:-1]
#     count += 1
#
# print(cities)

# rainbow_file = open('exam.txt', 'r')
#
# colors = rainbow_file.readlines()
#
# print(colors[0], colors[1], colors[2])
#
# rainbow_file.close()

# rainbow_text = open('exam.txt', 'r')
#
# rainbow_line = rainbow_text.readline().strip()
#
# while rainbow_line:
#     print(rainbow_line.upper())
#     rainbow_line = rainbow_text.readline().strip()

# cities_messy = open('exam.txt', 'r')
#
# line = cities_messy.readline().strip('()\n')
#
# while line:
#     print(line)
#     line = cities_messy.readline().strip('()\n')

# planets_file = open('exam.txt', 'w+')
#
# planets_file.write("Monday\nTuesday\nWednesday\nThursday\nFriday\n")
#
# planets_file.seek(0)
# planets_file_read = planets_file.read()
#
# print(planets_file_read)
#
# planets_file.seek(0, 2)
#
# planets_file.write("Saturday\nSunday")
#
# planets_file.seek(0)
# planets_file_read = planets_file.read()
# print(planets_file_read)

# task4_file = open('exam.txt', 'a+')
#
# for i in range(5):
#     item = input("entre a item:")
#     task4_file.write(item+'\n')
#
# task4_file.seek(0)
#
# task4_file_read = task4_file.read()
# print(task4_file_read)
#
# task4_file.close()

# rainbow_file = open('rainbow.txt', 'r')
#
# rainbow_list = rainbow_file.readlines()
#
# print(rainbow_list)
#
# rainbow_list.sort()
#
# for word in rainbow_list:
#     print(word[:-1])

# weather_file = open('weather.txt', 'r')
#
# weather_read = weather_file.readline().strip()
#
# print(weather_read)
#
# weather_list = weather_read.split(',')
#
# print(weather_list)
#
# city_temp = weather_file.readline().strip()
# while city_temp:
#     city_temp = weather_file.readline().strip()
# weather_file.seek(len(weather_read),0)
# city_read = weather_file.read()
# city_list = city_read.split(',')
#
# print(city_list)


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
