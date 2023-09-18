import datetime
import re
from collections import OrderedDict


class Admin:
    """
        👉 1. Add new food items. Food Item will have the following details:
            🔴 FoodID //It should be generated automatically by the application.
            🔴 Name
            🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc.
            🔴 Price
            🔴 Discount
            🔴 Stock. Amount left in stock in the restaurant.

        👉 2. Edit food items using FoodID.

        👉 3. View the list of all food items.

        👉 4. Remove a food item from the menu using FoodID.
    """

    __food_items = OrderedDict()
    __food_items[1] = {
        "name": "Tandoori Chicken",
        "quantity": "4 pieces",
        "price": 240,
        "discount": 0,
        "stock": 10
    }
    __food_items[2] = {
        "name": "Vegan Burger",
        "quantity": "1 Piece",
        "price": 320,
        "discount": 0,
        "stock": 10
    }
    __food_items[3] = {
        "name": "Truffle Cake",
        "quantity": "500gm",
        "price": 900,
        "discount": 0,
        "stock": 10
    }

    def __init__(self):
        pass

    @classmethod
    def add_new_food_item(cls, name: str, quantity: str, price: float or int,
                          discount: float or int, stock: int) -> None:
        food_id = 1
        try:
            item_details = Admin.__food_items
            if item_details:
                food_id = list(item_details.keys())[-1] + 1
        except KeyError:
            pass
        finally:
            Admin.__food_items[food_id] = {
                "name": name,
                "quantity": quantity,
                "price": price,
                "discount": discount,
                "stock": stock
            }

    @classmethod
    def edit_food_item(cls, food_id, name=None, quantity=None, price=None, discount=None, stock=None):
        try:
            item_details = Admin.__food_items[food_id]
            if name:
                item_details["name"] = name
            if quantity:
                item_details["quantity"] = quantity
            if price:
                item_details["price"] = price
            if discount:
                item_details["discount"] = discount
            if stock:
                item_details["stock"] = stock
            return True

        except KeyError:
            return False
            # print("This food item is not found in the database.")

    @classmethod
    def list_all_food_items(cls):
        return Admin.__food_items

    @classmethod
    def delete_food_item(cls, food_id):
        try:
            Admin.__food_items.pop(food_id)
            return True
        except KeyError:
            return False


class User:
    """
        👉 1. Register on the application. Following to be entered for registration:
            🔴 Full Name
            🔴 Phone Number
            🔴 Email
            🔴 Address
            🔴 Password

        👉 2. Log in to the application

        👉 3. The user will see 3 options:
                🔴 Place New Order
                🔴 Order History
                🔴 Update Profile

        👉 4. Place New Order: The user can place a new order at the restaurant.
                🔵 Show list of food. The list item should as follows:
                    🔴 Tandoori Chicken (4 pieces) [INR 240]
                    🔴 Vegan Burger (1 Piece) [INR 320]
                    🔴 Truffle Cake (500gm) [INR 900]

        👉 5. Users should be able to select food by entering an array of numbers. For example, if the user wants to
        order Vegan Burger and Truffle Cake they should enter [2, 3]

        👉 6. Once the items are selected user should see the list of all the items selected. The user will also get
        an option to place an order.

        👉 7. Order History should show a list of all the previous orders

        👉 8. Update Profile: the user should be able to update their profile.
    """
    __users = OrderedDict()
    __order_history = {}
    __users[1] = {
        "full_name": "Rashmi Ranjan Padhi",
        "phone_number": "8658385986",
        "email": "rrp@gmail.com",
        "address": "1st cross, bangalore, 123456",
        "password": "Rrp@1234"
    }

    def __init__(self):
        pass

    @classmethod
    def register(cls, full_name: str, phone_number: str, email: str, address: str, password: str) -> None:
        user_id = 1
        try:
            user_details = User.__users
            if user_details:
                user_id = list(user_details.keys())[-1] + 1
        except KeyError:
            pass
        finally:
            User.__users[user_id] = {
                "full_name": full_name,
                "phone_number": phone_number,
                "email": email,
                "address": address,
                "password": password
            }

    @classmethod
    def login(cls, email: str, password: str) -> int:
        for k, v in User.__users.items():
            if v["email"].lower() == email.lower() and v["password"] == password:
                return k
        return 0

    @classmethod
    def update_profile(cls, user_id: int, full_name: str = None, phone_number: str = None,
                       email: str = None, address: str = None, password: str = None) -> None:
        if full_name:
            User.__users[user_id]["full_name"] = full_name
        elif phone_number:
            User.__users[user_id]["phone_number"] = phone_number
        elif email:
            User.__users[user_id]["email"] = email
        elif address:
            User.__users[user_id]["address"] = address
        elif password:
            User.__users[user_id]["password"] = password

    @classmethod
    def update_orders(cls, user_id: int, orders: tuple):
        now = datetime.datetime.now()
        if user_id in User.__order_history:
            User.__order_history[user_id].append({
                    "orders": orders,
                    "time": now.strftime("%H:%M:%S"),
                    "date": now.strftime("%Y-%m-%d ")
                })
        else:
            User.__order_history[user_id] = [
                {
                    "orders": orders,
                    "time": now.strftime("%H:%M:%S"),
                    "date": now.strftime("%Y-%m-%d ")
                }
            ]

    @classmethod
    def show_order_history(cls, user_id):
        try:
            food_items = Admin.list_all_food_items()
            order_history = User.__order_history[user_id]
            for order in order_history:
                for item_id in order['orders']:
                    print(f"* {food_items[item_id]['name']} "
                          f"({food_items[item_id]['quantity']}) "
                          f"[INR {food_items[item_id]['price']}] ")
                print("Date: ", order['date'])
                print("Time: ", order['time'])
                print()
        except KeyError:
            print("\033[35mNo record found.\033[0m")


def admin_console():
    while True:
        print("\033[33mSelect the below option that you want to operate:\033[0m")
        print("1. Add new food item")
        print("2. Edit an existing food item")
        print("3. Display all existing food items")
        print("4. Delete a food item")
        opt = int(input())
        if isinstance(opt, int) and 0 < opt < 5:
            if opt == 1:
                print("\033[33mPlease Enter the below Food Item Details:\033[0m")
                while True:
                    try:
                        name = input("Name: ")
                        if isinstance(name, str):
                            break
                        else:
                            print("\n\033[31m\"Oh Ooo! Please enter a valid string type value.\"\033[0m")
                    except ValueError:
                        print("\n\033[31m\"Oh Ooo! Please enter a valid string type value.\"\033[0m")
                while True:
                    try:
                        quantity = input("Quantity: ")
                        if isinstance(quantity, str):
                            break
                        else:
                            print("\n\033[31m\"Oh Ooo! Please enter a valid integer type value.\"\033[0m")
                    except ValueError:
                        print("\n\033[31m\"Oh Ooo! Please enter a valid integer type value.\"\033[0m")
                while True:
                    try:
                        price = float(input("Price: "))
                        if isinstance(price, float):
                            break
                        else:
                            print("\n\033[31m\"Oh Ooo! Please enter a valid float type value.\"\033[0m")
                    except ValueError:
                        print("\n\033[31m\"Oh Ooo! Please enter a valid float type value.\"\033[0m")
                while True:
                    try:
                        discount = float(input("Discount: "))
                        if isinstance(discount, float):
                            break
                        else:
                            print("\n\033[31m\"Oh Ooo! Please enter a valid float type value.\"\033[0m")
                    except ValueError:
                        print("\n\033[31m\"Oh Ooo! Please enter a valid float type value.\"\033[0m")
                while True:
                    try:
                        stock = int(input("Stock: "))
                        if isinstance(discount, float):
                            break
                        else:
                            print("\n\033[31m\"Oh Ooo! Please enter a valid integer type value.\"\033[0m")
                    except ValueError:
                        print("\n\033[31m\"Oh Ooo! Please enter a valid integer type value.\"\033[0m")
                Admin.add_new_food_item(name, quantity, price, discount, stock)

            elif opt == 2:
                try:
                    food_id = int(input("\033[36mEnter food id to update information: \033[0m"))
                    if not Admin.list_all_food_items()[food_id]:
                        print("\n\033[35m\"Sorry! This item doesn't exist in the database.\033[0m")
                    else:
                        while True:
                            print("\033[33mSelect the below option that you want to modify:\033[0m")
                            print("1. Name")
                            print("2. Quantity")
                            print("3. Price")
                            print("4. Discount")
                            print("5. Stock")
                            try:
                                opt = int(input())
                                if isinstance(opt, int):
                                    value = input("\033[36mEnter value to modify: \033[0m")
                                    if opt == 1 and isinstance(value, str):
                                        Admin.edit_food_item(food_id=food_id, name=value)
                                    elif opt == 2 and isinstance(value, str):
                                        Admin.edit_food_item(food_id=food_id, quantity=value)
                                    elif opt == 3 and isinstance(value, float or int):
                                        Admin.edit_food_item(food_id=food_id, price=value)
                                    elif opt == 4 and isinstance(value, float or int):
                                        Admin.edit_food_item(food_id=food_id, discount=value)
                                    elif opt == 5 and isinstance(value, int):
                                        Admin.edit_food_item(food_id=food_id, stock=value)
                                    else:
                                        print("\n\033[31m\"Wrong value entered. Please select any option between 1-5 to"
                                              "proceed further.\"\033[0m")
                                        continue
                                    print("\033[32mYay! Updated Successfully.\033[0m")
                                    break
                                else:
                                    print("\n\033[31m\"Wrong value entered. Please provide integer value to "
                                          "proceed.\"\033[0m")
                            except ValueError:
                                print("\n\033[31m\"Wrong value entered. Please select any option between 1-5 to "
                                      "proceed further.\"\033[0m")
                except ValueError:
                    print("\n\033[35m\"Wrong value entered. Please enter any integer number to proceed.\"\033[0m")
                except KeyError:
                    print("\n\033[35m\"Sorry! This item doesn't exist in the database.\033[0m\n")
            elif opt == 3:
                print("***********************************************************************************************")
                print("                                    All Available Food Items")
                print("***********************************************************************************************")
                if not Admin.list_all_food_items():
                    print("No Item Available to Display.")
                for k, v in Admin.list_all_food_items().items():
                    print(f"Food ID: {k}")
                    print(f"Name: {v['name']}")
                    print(f"Quantity: {v['quantity']}")
                    print(f"Price: {v['price']}")
                    print(f"Discount: {v['discount']}")
                    print(f"Stock: {v['stock']}")
                    print()
                print("***********************************************************************************************")
            elif opt == 4:
                try:
                    food_id = int(input("\033[33mEnter food id to delete: \033[0m"))
                    if not Admin.delete_food_item(food_id):
                        print("\n\033[35m\"Sorry! This item doesn't exist in the database.\033[0m")
                    else:
                        print("\n\033[32m\"Item got deleted successfully.\033[0m")
                except ValueError:
                    print("\n\033[35m\"Wrong value entered. Please enter any integer number to proceed.\"\033[0m")
            else:
                print("\n\033[35m\"Wrong value entered. Please select any option between 1-4 to proceed "
                      "further.\"\033[0m")
        else:
            print("\n\033[35m\"Wrong value entered. Please select any option between 1-4 to proceed further.\"\033[0m")
        if input("\033[36mDo you want to logout(y/n): \033[0m") == 'y':
            break


def user_console():
    print("\033[33mSelect the below option that you want to operate:\033[0m")
    print("1. Register")
    print("2. Log In")
    opt = int(input())
    if isinstance(opt, int) and 0 < opt < 3:
        if opt == 1:
            print("\033[33mPlease Enter the below Details:\033[0m")
            while True:
                full_name = input("Full Name: ")
                if len(full_name) > 5 and full_name.replace(" ", "").isalpha():
                    break
                else:
                    print("\n\033[35m\"Please provide a valid name.\033[0m")

            while True:
                phone_number = input("Phone Number: ")
                pattern = re.compile("(0|91)?[6-9][0-9]{9}")
                if bool(pattern.match(phone_number)):
                    break
                else:
                    print("\n\033[35m\"Please provide a valid Phone Number.\033[0m")

            while True:
                email = input("Email: ")
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                if bool(re.fullmatch(pattern, email)):
                    break
                else:
                    print("\n\033[35m\"Please provide a valid Mail ID.\033[0m")

            address = input("Address: ")

            while True:
                password = input("Password: ")
                reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
                pat = re.compile(reg)
                if bool(re.search(pat, password)):
                    break
                else:
                    print("\n\033[35m\"Please provide a valid Password.\033[0m")
            User.register(full_name, phone_number, email, address, password)
            print("\033[32m\"User created successfully.\033[0m")
        elif opt == 2:
            while True:
                email = input("Email: ")
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                if bool(re.fullmatch(pattern, email)):
                    break
                else:
                    print("\n\033[35m\"Please provide a valid Mail ID.\033[0m")

            while True:
                password = input("Password: ")
                reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
                pat = re.compile(reg)
                if bool(re.search(pat, password)):
                    break
                else:
                    print("\n\033[35m\"Please provide a valid Password.\033[0m")
            res = User.login(email, password)
            if not res:
                print("\n\033[31m\"Invalid Credential!.\033[0m")
            else:
                while True:
                    print("\n\033[33mSelect One:\033[0m\n")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    ch = int(input())
                    if isinstance(ch, int) and 0 < ch < 4:
                        if ch == 1:
                            food_items = Admin.list_all_food_items()
                            for item in food_items.values():
                                print(f"🔴 {item['name']} ({item['quantity']}) [INR {item['price']}] ")
                            orders = input("\n\033[36mPlease select item(s) as \"[1, 2]\": \033[0m").replace("[", ""). \
                                replace("]", "").replace(" ", "").split(",")

                            orders = [int(n) for n in orders]
                            print("\033[33mBelow items are selected.\033[0m")
                            for item_id in orders:
                                print(f"🔴 {food_items[item_id]['name']} "
                                      f"({food_items[item_id]['quantity']}) "
                                      f"[INR {food_items[item_id]['price']}] ")
                            confirm = input("\n\033[36mType y/yes to place the order: \033[0m")
                            if confirm == 'y' or confirm == 'yes':
                                User.update_orders(res, tuple(orders))
                                print("\033[32mHurray! Your order got placed successfully.\033[0m")
                        elif ch == 2:
                            User.show_order_history(res)
                        elif ch == 3:
                            while True:
                                full_name = None
                                phone_number = None
                                email = None
                                address = None
                                password = None
                                print("\033[33mSelect the below option which one to update: \033[0m")
                                print("1. Full Name")
                                print("2. Phone Number")
                                print("3. Email")
                                print("4. Address")
                                print("5. Password")
                                try:
                                    select_to_update = int(input())
                                except ValueError:
                                    print("\n\033[35m\"Wrong value entered. Please select between 1-5 to proceed "
                                          "further.\"\033[0m")
                                    continue
                                if select_to_update == 1:
                                    while True:
                                        full_name = input("\033[36mFull Name: \033[0m")
                                        if len(full_name) > 5 and full_name.replace(" ", "").isalpha():
                                            break
                                        else:
                                            print("\n\033[35m\"Please provide a valid name.\033[0m")
                                elif select_to_update == 2:
                                    while True:
                                        phone_number = input("Phone Number: ")
                                        pattern = re.compile("(0|91)?[6-9][0-9]{9}")
                                        if bool(pattern.match(phone_number)):
                                            break
                                        else:
                                            print("\n\033[35m\"Please provide a valid Phone Number.\033[0m")
                                elif select_to_update == 3:
                                    while True:
                                        email = input("Email: ")
                                        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                                        if bool(re.fullmatch(pattern, email)):
                                            break
                                        else:
                                            print("\n\033[35m\"Please provide a valid Mail ID.\033[0m")
                                elif select_to_update == 4:
                                    address = input("Address: ")
                                elif select_to_update == 5:
                                    while True:
                                        password = input("Password: ")
                                        reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8," \
                                              r"20}$"
                                        pat = re.compile(reg)
                                        if bool(re.search(pat, password)):
                                            break
                                        else:
                                            print("\n\033[35m\"Please provide a valid Password.\033[0m")
                                else:
                                    print("\n\033[35m\"Wrong value entered. Please select between 1-5 to proceed "
                                          "further.\"\033[0m")
                                    continue
                                User.update_profile(res, full_name=full_name, phone_number=phone_number,
                                                    email=email, address=address, password=password)
                                print("\n\033[32m\"Yay! Updated successfully..\033[0m")
                                break
                        else:
                            print("\n\033[35m\"Wrong value entered. Please select between 1-3 to proceed "
                                  "further.\"\033[0m")
                            continue
                    else:
                        print("\n\033[35m\"Wrong value entered. Please select between 1-3 to proceed further.\"\033[0m")
                        continue
                    if input("\033[36mDo you want to logout(y/n): \033[0m") == 'y':
                        break
        else:
            print("\n\033[35m\"Wrong value entered. Please select either 1 or 2 to proceed further.\"\033[0m")
    else:
        print("\n\033[35m\"Wrong value entered. Please select either 1 or 2 to proceed further.\"\033[0m")


def console_print():
    while True:
        try:
            login_type = int(input("\n\033[33mLogin as:\033[0m\n1. Admin\n2. User\033[0m\n"))
            if login_type == 1:
                admin_console()
            elif login_type == 2:
                user_console()
            else:
                print("\n\033[31m\"Wrong value entered. Please provide either 1 or 2 to proceed further.\"\033[0m")
        except ValueError:
            print("\n\033[31m\"Wrong value entered. Please provide either 1 or 2 to proceed further.\"\033[0m")


if __name__ == "__main__":
    console_print()

# \033[33m \033[0m
