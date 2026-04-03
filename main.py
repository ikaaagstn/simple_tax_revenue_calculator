from order import Order
from order_processor import OrderProcessor

if __name__ == "__main__":
    print("Welcome to the Tax and Revenue Calculator") 
    
    order_processor = OrderProcessor()

    input_order = True
    while input_order:

        order = Order()
        print("Enter order details:")
        order.order_id = int(input("Order ID: "))
        order.customer_name = input("Customer name: ")
        order.order_date = input("Order date: ")
        order.total_amount = float(input("Total amount: "))
        
        order_processor.add_order(order)
        
        add_order = input("Add another order? (y/n): ")
        
        if add_order == "n":
            break
    
    
    print("Order List:")
    order_processor.display_all_orders()
    total_revenue = order_processor.calculate_revenue()
    total_tax = order_processor.calculate_total_tax()
    print(f"Total Revenue: {total_revenue}")
    print(f"Total Tax: {total_tax}")

    print("Thank you for using this program!")
        
