class employee:
    def __init__(self,name:str,price:int,quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def revenue_generated(self):
        return self.price * self.quantity

print(employee("Name",10,1000).revenue_generated())