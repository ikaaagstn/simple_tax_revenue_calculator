class Order:
    def __init__(self):
        self.order_id = 0
        self.customer_name = ""
        self.order_date = ""
        self.total_amount = 0
    
    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate

    def display_order(self):
        print(f"Order ID: {self.order_id} | Customer Name: {self.customer_name} | Order Date: {self.order_date} | Total Amount: {self.total_amount} | Tax: {self.calculate_tax(0.1)}")
        
    