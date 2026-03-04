
class bmw():

    def __init__(self,fuel_type,max_speed):
        self.fuel_type=fuel_type
        self.max_speed=max_speed
    def returni(self):
        self.fuel_type="diesel"
        self.max_speed=60
        return self.fuel_type,self.max_speed
    
    
    

class ferrari():

    def __init__(self,fuel_type,max_speed):
        self.fuel_type=fuel_type
        self.max_speed=max_speed
    def returni(self):
        self.fuel_type="petrol"
        self.max_speed=180
        return self.fuel_type,self.max_speed

sqr=bmw("diesel",60)
cir=ferrari("petrol",180)

#sqr.area()
#cir.area()

for i in (sqr,cir):
    i.returni()

