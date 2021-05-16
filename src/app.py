import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())


def add():
    new_item = input("Enter a name:")
    queue.enqueue(new_item)
    if queue.size() == 1:
        print("You are the first in line")
        print_queue()
    else:
        print(f"Successfully added to line, there are {queue.size() - 1} people before you!")
        print_queue()

def dequeue():
    if queue.size() == 0:
        print(queue.size())
        print("There is no people on the list to delete, try something else")
    else:
        queue.dequeue()
        # send()

def save():
    with open("queue.json", "w") as queue_json:
        # se guarda el contenido de la lista de diccionarios
        # python como diccionarios json en el archivo
        json.dump(queue.get_queue(), queue_json)
        # imprime un aviso para el usuario
    print("Changes have been saved.\n")


def load():
    with open("queue.json") as file:
        # data = file.read()
        data = json.load(file)
        queue.load_saved_queue(data)
        # print(data)
        return data
        
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
print(f"The actual saved list contains {len(load())} people on it")
print(load())
load()
# queue.load_saved_queue(load())
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        add()
    elif option == 2:
        dequeue()
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        option = str(input("Would you like to save changes???  Y/N: "))
        if option == "y" or option == "Y":
            save()
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
