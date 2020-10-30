import functions


USER_CHOICE = """
Enter: 
[ 1 ] to add a new car
[ 2 ] to list all cars
[ 3 ] to change the location of the car
[ 4 ] to delete a car
[ 5 ] to quit

Your choice: """


def menu():
    functions.create_txt
    user_input = int(input(USER_CHOICE))
    while user_input != 5:
        if user_input == 1:
            prompt_add_car()
        elif user_input == 2:
            list_cars()
        elif user_input == 3:
            prompt_change_location()
        elif user_input == 4:
            prompt_delete_car()
        else:
            print('Unknown command, please try again...')
        user_input = int(input(USER_CHOICE))


def prompt_add_car():
    plate = input('Plate: ')
    model = input('Model: ')
    category = input('Category: ')
    location = input('Location: ')

    functions.add_car(plate, model, category, location)


def list_cars():
    cars = functions.get_all_cars()
    for car in cars:
        print(car)   


def prompt_change_location():
    plate = input('Enter the plate to change the vehicle\'s location: ')
    location = input('New location: ')

    functions.new_location(plate, location)


def prompt_delete_car():
    plate = input('Enter the plate of the car that you want to delete: ')

    functions.delete_car(plate)


menu()

