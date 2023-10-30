#Display available bikes
#request bike for rent(100 Rs ->1qty
#Exit
class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("total bike",self.stock)
    def rentforbike(self,q):
        if q <=0:
            print("enter the value greather than 0 and positive ")
        elif q >self.stock :
            print("enter the value less than stock")
        else:
            print("total price ",q*100)
            print("total bike",self.stock)

while True:
    uc = int(input('''
    1.Display available bikes
    2.request bike for rent(100 Rs ->1qty
    3.Exit
           '''))
    obj= bikeshop(100)



    if uc==1:
         obj.displaybike()
    elif uc==2:
        n=int(input("enter the quantity :-- "))
        obj.rentforbike(n)
    else:
        break