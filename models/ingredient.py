
class Ingredient():
    def __init__(self, name, cp, tdn, price):
        self.name = name
        self.cp = float(cp)
        self.tdn = float(tdn)
        self.price = int(price)
    
    def __repr__(self):
        return f"{self.name} (CP: {self.cp}%, TDN: {self.tdn}%, Price: Rp{self.price}/kg)"