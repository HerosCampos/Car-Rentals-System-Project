cars_file = 'cars.txt'


def create_txt():
    with open(cars_file, 'a'):
        pass


def add_car(plate, model, category, location):
    with open(cars_file, 'a') as file:
        file.write(f'{plate},{model},{category},{location}\n')


def get_all_cars():
    with open(cars_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'plate': line[0], 'model': line[1], 'category': line[2], 'location': line[3]}
        for line in lines
    ]


def new_location(plate, location):
    cars = get_all_cars()
    for car in cars:
        if car['plate'] == plate:
            car['location'] = f'{location}'
    _save_all_cars(cars)


def _save_all_cars(cars):
    with open(cars_file, 'w') as file:
        for car in cars:
            file.write(f"{car['plate']},{car['model']},{car['category']},{car['location']}\n")


def delete_car(plate):
    cars = get_all_cars()
    cars = [car for car in cars if car['plate'] != plate]
    _save_all_cars(cars)
