class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_amount
        return total
    
    def calculate_total_tax(self, tax_rate=0.1):
        total = 0
        for order in self.orders:
            total += order.calculate_tax(tax_rate)
        return total

    def display_all_orders(self):
        for order in self.orders:
            order.display_order()
        