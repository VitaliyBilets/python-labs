class Plane:
       def __init__(self, name = "unnamed", number_of_passengers = 0, fuel_tank_capacity_in_liters = 0, max_speed = 0, manufacturer = "unknown", flight_hour= 0):
           self.__name = name
           self.__number_of_passengers = number_of_passengers
           self.__fuel_capacity_in_liters = fuel_tank_capacity_in_liters
           self.max_speed = max_speed
           self.manufacturer = manufacturer
           self.__flight_hour = flight_hour

       def get_flight_hour(self):
            return self.__flight_hour
       def set_flight_hour(self, flight_hour):
           self.__flight_hour += flight_hour

       def get_name(self):
           return self.__name

       def get_number_of_passengers(self):
           return self.__number_of_passengers

       def get_fuel_capacity_in_liters(self):
           return self.__fuel_capacity_in_liters

       def __str__(self):
           return f"{self.__name}, {self.__number_of_passengers} passengers, {self.__fuel_capacity_in_liters} liters, max speed {self.max_speed} k/h manufacturer {self.manufacturer}"

       def __repr__(self):
           return f"Plane(name='{self.__name}', number_of_passengers={self.__number_of_passengers}, fuel_capacity_in_liters={self.__fuel_capacity_in_liters} max_speed={self.max_speed}, manufacturer={self.manufacturer})"

       def __del__(self):
           print(f"{self.__name} destroyed.")

       def main(self):

           plane1 = Plane("Boeing 747", 416, 238840, 920, "Boeing" , 22)
           plane2 = Plane( )
           plane3 = Plane("Airbus A380", 555, 320000, 945, "Airbus",36)
           list = [ plane1, plane2, plane3 ]

           plane_min = list[0]
           for plane in list:
               if  plane_min.get_flight_hour() > plane.get_flight_hour():
                   plane_min = plane


           print(plane1)
           print(plane2)
           print(plane3)

plane_obj = Plane()

plane_obj.main()


