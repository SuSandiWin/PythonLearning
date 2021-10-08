class Car:
    sterringWheels=1; #class level attribute (thunyi yin use )
    def __init__(self,name,wheels,model):
        self.name=name; #instant level attribute (taku nae taku ma thu lo/ obj nae pae relative)
        self.wheels=wheels; #instant level attribute
        self.model=model;
    def driving(self): #instant method
        print(f'{self.name} is driving and model is {self.model}, wheels is {self.wheels}')
    @classmethod
    def common(cls):
        print(f'all car has only one {cls.sterringWheels} sterring wheels')
  
car=Car('toyota',4,'AAA');
car.driving();
car=Car('Surf',4,'RR1')
car.driving();
print(Car.sterringWheels)
car.common();
Car.common();

