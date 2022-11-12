#Christina Williams
#M03 Lab

#superclass called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
#Automobile class (inherit attribute from vehicle class) - year / make / model / doors (2 or 4) roof (solid / sun roof)

year=input("Enter the vehicle year")
vehicletype=input("Enter the type of vehicle. Car, truck, plane, boat or broomstick")
make=input("Enter the vehicle make")
model=input("Enter vehicle model")
door=input("Enter the number of doors on the vehicle")
roof=input("Enter the type of roof. Solid or sun roof ")

class vehicle(object):
    def __init__(self):
        self.vehicletype =vehicletype
        self.year=year
        self.make =make
        self.model =model
        self.doors=door
        self.roof=roof

class Automobile(vehicle):
    def __init__(self):
        super(vehicle, self).__init__()
        super().__init__()

print('Vehicle Type:%s '%(vehicletype))
print('Year:%s '%(year))
print('Make:%s '%(make))
print('Model:%s '%(model))
print('Doors:%s '%(door))
print('Roof:%s '%(roof))


#print(), Year:%s, Make:%s, Model:%s, Door:%s, Roof:%s '% (vehicletype,year,make,model,door,roof))

def main():
    automobile = Automobile()

main()