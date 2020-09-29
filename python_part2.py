# Une classe c'est un plan
# Un objet c'est une voiture faites à partir de ce plan


class Plan():  # 0
    pass  # 1 {}
# 0


class Vehicule(object):
    speed = 0

    def drive(self):
        pass

    def get_speed(self):
        return self.speed


vec = Vehicule()
vec.drive()  # drive(vec)


class Car(Vehicule):
    wheels = 4

    def drive(self):
        # self c'est la voiture qui a été construit
        print("driving")
        self.speed = 100


class SUV(Car):
    def drive(self):
        # self c'est la voiture qui a été construit
        print("driving")
        self.speed = 150


# print("Plan Car", Car.speed)  # 0

# car = Car()
# print("car", car.get_speed())  # get_speed(car)
# car.drive()
# print("car", car.get_speed())  # get_speed(car)

# print("Plan Car", Car.speed)  # 0


# print("Plan Car", Car.speed)  # 0

# suv = SUV()
# print("suv", suv.get_speed())  # get_speed(suv)
# suv.drive()
# print("suv", suv.get_speed())  # get_speed(suv)

# print("Plan Car", Car.speed)  # 0


my_string = "my StRiNg"
# print(my_string)
# print(my_string.capitalize())
# # "my StRiNg" -> "my" "StRiNg"
# print(my_string.title())
# # -> "hello" -> "        hello        "
# print(my_string.title().center(30, '|'))


l = [10, 2, 3, 4, 9, 6, 7]
#pos 0  1  2  3  4  5  6  
# print(l[-1]) # -1 récupère le dernier: 7
# print(l[3]) # 3 récupère le 4ème élément: 4

# l.append(8)
# print(l[-1]) # -1 récupère le dernier: 8

# print(l.pop(2))
# print(l)

# print(sorted(l)) # l.sort()



d = {
    'key': my_string,
    'key2': 42
}
# print(d)

# print(d['key']) # -> my_string

# d['key3'] = 84
# print(d)

# print(d.pop('key2'))
# print(d)



# for value in l:
#     print(value)

# for key, value in d.items():
#     print(key, value)




# for value in l:
#     if value == 8:
#         print(value)


notes = [0, 10, 20, 14, 11, 14, 13, 12, 15, 9, 4, 16, 14]
def count_note(note, notes):
    count = 0

    for value in notes:
        if value == note:
            count = count + 1
    
    return count

print(count_note(14, notes))

moyenne = sum(notes) / len(notes)
print(moyenne)
