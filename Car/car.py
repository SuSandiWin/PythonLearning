class Car:
    sterringWheel=1
    def __init__(self,name,model,wheels):
        self.name=name;
        self.model=model;
        self.wheels=wheels;
    def driving(self):
        print(f'{self.name} is driving and model is {self.model}');
    @classmethod
    def common(cls):
        print(f'all car has only {cls.sterringWheel} sterring wheel');

