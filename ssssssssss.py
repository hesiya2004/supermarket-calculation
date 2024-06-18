print("********SUPER MART*********")
import datetime
import smtplib
import random
cart = []
def calculate_total(cart):
    total_quantity = 0
    total_cost = 0
    product_prices = {
        "Apple": 50,
        "Orange": 40,
        "Banana": 10,
        "Watermelon": 100,
        "Grapes": 50,
        "Potato": 20,
        "Tomato": 30,
        "Beans": 15,
        "Cauliflower": 50,
        "Onion": 30,
        "Rice": 800,
        "Oil": 110,
        "Turmeric": 15,
        "Mustard": 15,
        "Honey": 40,
        "Pasta": 60,
        "Bathroom Cleaner": 90,
        "Toilet Cleaner": 90,
        "Biscuits": 30
    }
    items_details = []
    for item, quantity in cart:
        if item in product_prices:
            price = product_prices[item]
            cost = quantity * price
            gst_rate = 0.18
            gst_amount = cost * gst_rate
            total_rate = cost + gst_amount
            items_details.append((item, price, quantity, gst_amount, total_rate))
            total_quantity += quantity
            total_cost += total_rate
    return total_quantity, total_cost, items_details
def add_item():
    try:
        with open("product.txt", 'r') as file:
            products = file.read().splitlines()
            while True:
                print("\nAvailable products:")
                for index, product in enumerate(products, start=1):
                    print(f"{index}. {product}")
                choice = input("Enter the number of the product you want to purchase (type 'done' to finish): ")
                if choice.lower() == "done":
                    break
                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(products):
                        purchase_product = products[choice_index]
                        quantity = int(input(f"Enter the quantity for {purchase_product}: "))
                        if quantity <= 0:
                            print("Invalid quantity. Please enter a positive number.")
                            continue
                        print(f"{purchase_product} selected")
                        item = (purchase_product, quantity)
                        if item not in cart:
                            cart.append(item)
                            print(f"{purchase_product} (Quantity: {quantity}) added to your cart")
                        else:
                            print(f"{purchase_product} is already in your cart")
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    except FileNotFoundError:
        print("Product file not found.")
purchase_date = datetime.datetime.now()
print("Purchase date:", purchase_date.strftime("%Y-%m-%d %H:%M:%S"))
add_item()
total_quantity, total_cost, items_details = calculate_total(cart)
gst_rate = 0.18 
discount_percent = 10  
gst_amount = total_cost * gst_rate
discount_amount = total_cost * (discount_percent / 100)
final_cost = total_cost + gst_amount - discount_amount
print("\nItems in your cart:")
for item, price, quantity, gst_amount, total_rate in items_details:
    print(f"Product: {item}")
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")
    print(f"GST Amount: {gst_amount}")
    print(f"Total Rate: {total_rate}")
    print()
print(f"Total Quantity: {total_quantity}")
print(f"Total Cost (before GST and discount): {total_cost}")
print(f"GST (18%): {gst_amount}")
print(f"Discount ({discount_percent}%): {discount_amount}")
print(f"Final Cost: {final_cost}")
def email_sending():
    try:
        receiver_mail = input("Enter your mail id: ")
        otp_number = random.randint(0000, 9999) 
        print(f"OTP: {otp_number}")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("hesiya22@gmail.com", "cmgp vkpm hpne mrml")
        message = f"Your OTP for purchase is: {otp_number}"
        s.sendmail("hesiya22@gmail.com", receiver_mail, message)
        s.quit()
        print("Mail sent successfully")
    except Exception as e:
        print(f"Error: {e}")
        print("Mail not sent")
email_sending()
