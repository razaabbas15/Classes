class IceCreamStand:
    def __init__(self,name,quality,price,flavours) :
        self.name = name.title()
        self.quality = quality
        self.price = price.title()
        self.flavours = flavours
    
    def name(self):
        print(self.name + "Choose you favourite icecream from menu")
    
    
    def quality(self):
        print(self.quality + " We provide great service and quality " )
    
    def price(self):
        print (self.price + "Our prices are cheap")
        
    def flavours(self):
        return f"{self.flavours} "
    
My_shop = IceCreamStand("Mr Coco Ice Cream Store" , "5 stars!" , "Only 100 to 500 Rs Our prices are cheap", "Choose from Vanilla , pista and chocolate. We have delicious flavours : ")

print(My_shop.price)