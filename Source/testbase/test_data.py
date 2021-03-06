'''
Test data to run tests against
'''

bool_1 = True
complex_1 = 1+2j
int_1 = 1
dict_1 = {'item_1': 'Value 1', 'item_2': 'Value 2', 'item_3': 'Value 3'}
float_1 = 12.0
list_1 = ['Item 1', 'Item 2', 'Item 3']
list_unsorted = ['Item 2', 'Item 4', 'Item 1', 'Item 3']
none_1 = None
string_1 = 'This is string 1'

ANIMALS = [
    "Aardvark",
    "Beaver",
    "Cheetah",
    "Dog",
    "Elephant",
    "Flamingo",
    "Gorilla",
    "Hippo",
    "Iguana",
    "Jaguar",
    "Kangaroo",
    "Llama",
    "Matatee",
    "Newt",
    "Oselot",
    "Praying Mantis",
    "Quaill",
    "Raccoon",
    "Stingray",
    "Tiger",
    "U",        # Don't know any animals that start with U.
    "Vulture",
    "Whale",
    "X",        # Don't know any X animals either.
    "Yak",
    "Zebra"
    ]

class AClass(object):

    def __init__(self, the_id, name, value):
        
        self.id = the_id
        self.name = name
        self.value = value

    def __repr__(self):
        return 'AClass [id=' + str(self.id) + ', name="' + self.name + ', value="' + self.value + '"]'
    
    def name_and_id(self):
        return self.name + " (" + str(self.id) + ")"

a_class_1 = AClass(1, "Item 1", "Value 1")
a_class_2 = AClass(2, "Item 2", "Value 2")
a_class_3 = AClass(3, "Item 3", "Value 3")

class_list_1 = [
    a_class_1,
    a_class_2,
    a_class_3
]

class_list_unsorted = [
    a_class_3,
    a_class_1,
    a_class_2
]