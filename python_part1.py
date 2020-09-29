ram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

bits = 0 or 1


ram = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
my_variable = 1
my_variable2 = 1.2


int = "integer"
float = ""

string = "my sentence"
string.capitalize()  # "My Sentence"

# {
#     x = 1
#     print(x)  # 1
# }
# print(x)  # Error: Undefined variable :x


def function():  # indentation 0
    x = 1  # indentation 1
    print(x)  # 1


# print(x)  # Error: Undefined variable :x # Indentation 0


# print == console.log

def sum_two_numbers(a, b):
    return a + b


summed = sum_two_numbers(1, 2)
# print(summed)

# print(sum(1, 2))

# 'A' == 65: True


def choose(name):
    if name == "Tiphaine" and name != "LAURENT":  # < > <= >= !=
        return 42
    else:
        return 84

# print(choose("LAURENT"))


def repeat(sentence, number): # définition en premier
    count = 0
    while count != number:
        count = count + 1
        print(sentence)


# repeat("Bonjour", 5)		  # utilisation en deuxième
# Bonjour
# Bonjour
# Bonjour
# Bonjour
# Bonjour


def repeat_for(sentence, number):
	for count in range(number):
		print(sentence)

# repeat_for("Bonjour", 5)







def name_dice(dice_value):
	if dice_value == 0:
		print("Face zero")
	elif dice_value == 1:
		print("Face one")
	elif dice_value == 5: # sinon si # else if
		print("Face five")

def name_dice(dice_value):
	if dice_value == 0:
		print("Face zero")
	else:
		if dice_value == 1:
			print("Face one")
		else:
			if dice_value == 5:
				print("Face five")

name_dice(1)









