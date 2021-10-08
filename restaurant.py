class restaurantTable():
    menus={
        'cola':600,
        'hamburger':3000,
        'pizza':5500,
        'orange juice':1000,
        'fried chicken':1500,
        'french fried':1000,
        'hotdog':1500,
        'coffee':800
    }
    def __init__(self):
        self.total=0;
        self.orders=[];
    def addOrder(self,order):
        self.orders.append(order);
        self.total+=self.menus[order];
    def printBill(self):
        for order in self.orders:
          print(f'{order} : {self.menus[order]}');
        print(f'Total Bill amount : {self.total}')

def startProgram():
    table=restaurantTable();
    while True:
        order=input("Enter order: ");
        table.addOrder(order);
        another= input("another order? y/n:");
        if another =='y':
            continue;
        elif another =='n':
            table.printBill()
            break;

startProgram();

    
        