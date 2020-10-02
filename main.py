from Car import Car, IdleCar
from City import City
from Position import Position, Direction

if __name__ == "__main__":
    city = City(4, 4)

    c = Car(IdleCar, 0, Position(5, 0), Position(0, 0), city)
    car_list = [c]
    car_positions_list = []
    for i in car_list:
        car_positions_list.append(i.state.props.position)
    print(city.print_city_with_cars(car_positions_list))
    c.move()
    print(c.state.props.position)
