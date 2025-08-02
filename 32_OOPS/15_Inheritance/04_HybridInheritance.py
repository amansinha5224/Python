'''
Hybrid Inheritance:-
    - This type of inheritance is the combination of two or more types of inheritance 
'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def displayVehicleInfo(self):
        print(f"BRAND: {self.brand}\nMODEL: {self.model}")

class FuelVehicle(Vehicle):
    def __init__(self, brand, model, fuelType, fuelCapacity):
        Vehicle.__init__(self, brand, model)
        self.fuelType = fuelType
        self.fuelCapacity = fuelCapacity
    
    def displayFuelInfo(self):
        super().displayVehicleInfo()
        print(f"FUEL TYPE: {self.fuelType}\nFUEL CAPACITY: {self.fuelCapacity} Liters")

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, batteryCapacity, chargingTime):
        Vehicle.__init__(self, brand, model)
        self.batteryCapacity = batteryCapacity
        self.chargingTime = chargingTime

    def displayElectricInfo(self):
        super().displayVehicleInfo()
        print(f"BATTERY CAPACITY: {self.batteryCapacity} kWh\nCHARGHING TIME: {self.chargingTime} hrs")

class HybridVehicle(FuelVehicle, ElectricVehicle):
    def __init__(self, brand, model, fuelType, fuelCapacity, batteryCapacity, chargingTime, hybridMode = "Off"):
        FuelVehicle.__init__(self, brand, model, fuelType, fuelCapacity)
        ElectricVehicle.__init__(self, brand, model, batteryCapacity, chargingTime)
        self.hybridMode = hybridMode
    
    def displayHybridInfo(self):
        self.displayVehicleInfo()
        print(f"FUEL TYPE: {self.fuelType}")
        print(f"FUEL CAPACITY: {self.fuelCapacity} Liters")
        print(f"BATTERY CAPACITY: {self.batteryCapacity} kWh")
        print(f"CHARGING TIME: {self.chargingTime} hrs")
        print(f"HYBRID MODE: {self.hybridMode}")


vehicle1 = FuelVehicle("BMW", "Series 7", "Petrol", 100)
vehicle2 = ElectricVehicle("Audi", "Etron GT", 93, 5)
vehicle3 = HybridVehicle("Toyota", "Camry", "Petrol", 85, 50, 3, "On")

vehicle1.displayFuelInfo()
print()
vehicle2.displayElectricInfo()
print()
vehicle3.displayHybridInfo()
print()