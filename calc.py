class LoadCalc:
    BASE_COST = {
        50: 300,
        100: 1000,
        300: 2000
    }

    def __init__ (self, weight, floor, elevator):
        self.weight = weight
        self.floor = floor
        self.elevator = elevator
        
    def price(self):
        base_cost = self.BASE_COST.get(self.weight, 0)

        if self.elevator:
            return base_cost
        
        manual_cost = (self.floor - 1) * self.weight // 100 * 300
        # За каждые 100кг груза на этаж по 300 рублей

        return manual_cost + base_cost