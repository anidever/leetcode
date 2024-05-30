from enum import Enum


class ElevatorDirection(Enum):
    Up = "Up"
    Down = "Down"
    Idle = "Idle"


class ElevatorSystemManager:
    def __init__(self, num_elevators, num_floors):
        self.floors = num_floors
        self.elevators = [ElevatorCar(i) for i in range(num_elevators)]
        self.requests = []

    def handle_request(self, floor, request_direction):
        while self.requests:
            elevator = self._select_elevator(floor, request_direction)
            elevator.destination_list.append(floor)

    def _select_elevator(self, request_floor, request_direction):
        for elevator in self.elevators:
            if (elevator.direction == request_direction) and (request_floor in elevator.destination_list):
                # Perfect fit, elevator needs to pass the request floor in the desired direction!
                return elevator

    def get_user_request(self):
        """
        Prompts the user for a request (floor and direction or specific floor).

        Returns:
            A tuple containing the floor number (integer) and request type
            (ElevatorDirection or None).
        """
        while True:
            try:
                floor = int(input("Enter your floor number (1-10): "))
                if 1 <= floor <= self.floors:  # Adjust this range based on your number of floors
                    request_type = input("Enter direction (Up/Down): ")
                    if request_type.upper() in (ElevatorDirection.Up.name, ElevatorDirection.Down.name):
                        request_type = ElevatorDirection(request_type.upper())
                    else:
                        request_type = None  # Specific floor request (no direction)
                    return floor, request_type
                else:
                    print("Invalid floor number. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number for floor.")


class ElevatorCar:
    def __init__(self, elevator_id, current_floor="Ground"):
        self.id = elevator_id
        self.current_floor = current_floor
        self.direction = ElevatorDirection.Idle  # Initial state: Idle
        self.destination_list = []
