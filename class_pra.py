class Car:
    def __init__(self,name,model):
        self.name=name;
        self.model=model;
    def driving(self):
        print(f'{self.name} is driving and model no is{self.model}')
car=Car('toyota','AAA');
car.driving();