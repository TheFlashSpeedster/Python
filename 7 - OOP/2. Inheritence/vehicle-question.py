"""
Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance
charge. So total fare for bus instance will become the final amount = total
fare + 10% of the total fare.

Example:
Vehicle Fare: 5000
Bus Fare: 5500.0
"""

class Vehicle:
  def __init__(self, seating_capacity):
    self.seating_capacity = seating_capacity

  def get_fare(self):
    return self.seating_capacity * 100

class Bus(Vehicle):
  def __init__(self, seating_capacity):
    super().__init__(seating_capacity)

  def get_fare(self):
    vehicle_fare = super().get_fare()
    maintenance_fare = 0.10 * vehicle_fare
    total_fare = vehicle_fare + maintenance_fare
    return total_fare
  
# Normal Vehicle Fare
vehicle1 = Vehicle(50)
print(vehicle1.get_fare())

# Bus Fare
vehicle2 = Bus(50)
print(vehicle2.get_fare())