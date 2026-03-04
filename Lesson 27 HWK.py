capacity=int(input("Seating capacity"))


class vehicle:

    def __init__(self):
        pass
    def fare(self):
        self.fare=capacity*100
        return self.fare

class bus(vehicle):

    def __init__(self,maintenance):
        self.maintenance=maintenance
    def maintenancefee(self):
        self.maintenance=1.1*self.fare
        return self.maintenance

obj=bus(100)

print(obj)

