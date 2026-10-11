from food_item import FoodItem
from menu import  Menu
from user import Customer,Admin,User,Employee
from restaurant import Restaurant
from order import Order

mama_restaurant=Restaurant("Mama Restaurant")

def customer_menu():
    name=input("Enter Your Name: ")
    phone=input("Enter Your Phn.No: ")
    email=input("Enter Your Email: ")
    address = input("Enter Your Address: ")
    customer = Customer(name=name,phone=phone,email=email,address=address)



    while True:
        print(f"Welcome {customer.name}!!")
        print("1.View Menu")
        print("2.Add item to cart")
        print("3.View Cart")
        print("4.PayBill")
        print("5.Exit")


        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(mama_restaurant)

        elif choice ==2 :
            item_name = input("Enter item name:")
            item_quantity=int(input("Enter item quantity:"))
            customer.add_to_cart(mama_restaurant,item_name,item_quantity)


        elif choice ==3:
            customer.view_cart()


        elif choice==4:
            customer.pay_bill()


        elif choice==5:
            break

        else:
            print("Invalid Input")






def admin_menu():
    name=input("Enter Your Name: ")
    phone=input("Enter Your Phn.No: ")
    email=input("Enter Your Email: ")
    address = input("Enter Your Address: ")
    admin = Admin(name=name,phone=phone,email=email,address=address)



    while True:
        print(f"Welcome {admin.name}!!")
        print("1.Add New Item")
        print("2.Add New Employee")
        print("3.View Employee")
        print("4.View Items")
        print("5.Delete Items")
        print("6.Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            item_name=input("Enter Item Name: ")
            item_price = int(input("Enter Item Price:  "))
            item_quantity=int(input("Enter Item Quantity: "))

            it = FoodItem(name=item_name,price=item_price,quantity=item_quantity)

            admin.add_new_item(mama_restaurant,it)

        elif choice ==2 :
           name=input("Enter employee name: ")
           phone=int(input("Enter employee phone number: "))
           mail = input("Enter employee mail:")
           address = input("Enter employee address: ")
           age=int(input("Enter employee age: "))
           designation=input("Enter employee designation: ")
           salary = int(input("Enter employee salary: "))

           emp = Employee(name=name,phone=phone,email=mail,address=address,age=age,designation=designation,salary=salary)
           admin.add_employee(mama_restaurant,emp)


        elif choice ==3:
            admin.view_employee(mama_restaurant)


        elif choice==4:
             admin.view_menu(mama_restaurant)


        elif choice==5:
            item_name=input("Enter item name:")
            admin.remove_item(mama_restaurant,item_name)

        elif choice==6:
            break

        else:
            print("Invalid Input")




while True:
    print("Welcome!!")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")
    choice = int(input("Enter your choice: "))

    if choice==1:
        customer_menu()

    elif choice==2:
        admin_menu()

    elif choice==3:
        break

    else:
        print("Invalid Input!!!")