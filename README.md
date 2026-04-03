# Simple Tax and Revenue Calculator

A simple Python program to calculate total revenue and tax from user-inputted orders.

## Encapsulation

This program uses **Encapsulation** by wrapping data and logic inside classes:

- **`Order`** — Stores order data (`order_id`, `customer_name`, `order_date`, `total_amount`) and provides methods like `calculate_tax()` and `display_order()`.
- **`OrderProcessor`** — Manages a list of `Order` objects and handles operations like `add_order()`, `calculate_revenue()`, `calculate_total_tax()`, and `display_all_orders()`.

## How to Run

```bash
python main.py
```

## Example

Input 3 orders, and the program automatically calculates the tax and revenue.

```
Welcome to the Tax and Revenue Calculator
Enter order details:
Order ID: 1
Customer name: Ika
Order date: 2026-04-03
Total amount: 100000
Add another order? (y/n): y
Enter order details:
Order ID: 2
Customer name: Ika
Order date: 2026-04-03
Total amount: 200000
Add another order? (y/n): y
Enter order details:
Order ID: 3
Customer name: Ika
Order date: 2026-04-03
Total amount: 300000
Add another order? (y/n): n
Order List:
Order ID: 1 | Customer Name: Ika | Order Date: 2026-04-03 | Total Amount: 100000.0 | Tax: 10000.0
Order ID: 2 | Customer Name: Ika | Order Date: 2026-04-03 | Total Amount: 200000.0 | Tax: 20000.0
Order ID: 3 | Customer Name: Ika | Order Date: 2026-04-03 | Total Amount: 300000.0 | Tax: 30000.0
Total Revenue: 600000.0
Total Tax: 60000.0
Thank you for using this program!
```
