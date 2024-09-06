class Car:
    def __init__(self, make, model, year):
        # cars attributes 
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Printing out the cars info(attributes)
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

my_car = Car("Mercedes-Benz", "c-class(200)", 2024)

my_car.display_info() #display the car information 