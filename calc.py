class LoadCalc:
    def __init__ (self, weight, floor, elevator):
        self.weight = weight
        self.floor = floor
        self.elevator = elevator
    
    def price(self):
        self.price = self.floor * self.weight // 100 * 300
        # За каждые 100кг груза на этаж по 300 рублей