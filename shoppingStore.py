class shoppingCard():
    items={
        'shampoo':15000,
        'Conditioner':15000,
        'lotion': 18000,
        'serum': 21000,
        'facial foam':11000,
        'mostizer':17000,
        'soap':5000,
        'hair coat':4000
    }
    def __init__(self):
        self.orders=[];
        self.total=0;
    def shoppingItems(self,order):
        self.orders.append(order);
        self.total+= self.items[order];
    def printBill(self):
        for order in self.orders:
          print(f'{order} : {self.items[order]}');
        print(f'Total Amount : {self.total}')

def startProgram():
    item=shoppingCard();
    while True:
        order=input("Enter order: ");
        item.shoppingItems(order);
        another=input("Another order? y/n :")
        if another== 'y':
            continue;
        elif another == 'n':
            item.printBill();
            break;
        else:
            print("pls type only y or n :");
            continue;
startProgram();