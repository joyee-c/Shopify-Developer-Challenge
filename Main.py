from Inventory import Inventory

def menu():
   print("To create and add item to inventory, press 1") 
   print("To update item in inventory, press 2")
   print("To delete item in inventory, press 3")
   print("To view all items, press 4")
   print("To undelete recently deleted item, press 5")

if __name__== "__main__":
    inv = Inventory()
    valid_choices= ["1","2","3","4","5"]
    invalid_choices = ["q","Q"]
    success = 0
    print("****INVENTORY****")
    start = input("Only press q to quit, anything else to proceed: ")

    while start not in invalid_choices:
        print("\n")
        menu()
        choice = input("Enter choice: ")
        print("\n")
        while choice not in valid_choices:
            print("Wrong choice!")
            menu()
            choice = input("Enter choice: ")
            print("\n")
        #get Item ID from user only if undeleted is not selected. Make sure ID is input, unique ID is essential for working of the Inventory system
        if choice in valid_choices[:3]:
            id = input("Item Id: ")
            while not id:
                print("ID Needed!")
                id = input("Item Id: ")

        if choice == "1":
            success = inv.create(id)
        elif choice == "2":
            success = inv.update(id)
        elif choice == "3":
            success = inv.delete(id)
        elif choice == "4":
            success = inv.print_all()
        else:
            success = inv.undelete()

        print("\n")
        if success == -1:
            print("Process not successful")
        else:
            print("Process successful")

        print("\n")
        start = input("Only press q to quit, anything else to proceed: ")

    print("****CLOSING INVENTORY****")