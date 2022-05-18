class Inventory:
    #initialize new inventory that will store items and bin to store most recently deleted item
    def __init__(self):  
        self.inventory = {}
        self.recycle_bin = {}

    #create and add items to the inventory
    def create(self, id):
        #check if item being created already exists
        if id in self.inventory:
            print("Cannot create item, it already exists in inventory")
            return -1
        name = input("Item Name: ")
        description = input("Item Description: ")
        cost = input("Item Cost: ")
        quantity = input("Item Quantity: ")
        attributes = {
            "name": name,
            "description": description,
            "cost": cost,
            "quantity": quantity
        }
        self.inventory[id] = attributes

        return 0

    #update current inventory items
    def update(self,id):
        #check if item exists first
        if id not in self.inventory:
            print("Cannot update item, it does not exist in inventory")
            return -1 
        print("Item found, input new values only for attributes to be changed else press ENTER")
        for key in self.inventory[id]:
            print("Update",key,":", end="")
            new_val = input()
            if new_val:
                self.inventory[id][key] = new_val

        return 0

    #delete current items in inventory
    def delete(self, id):
        #check if item exists first
        if id not in self.inventory:
            print("Cannot delete item, it does not exist in inventory")
            return -1 
        self.recycle_bin = {
            "id": id,
            "name": self.inventory[id]["name"],
            "description": self.inventory[id]["description"],
            "cost": self.inventory[id]["cost"],
            "quantity": self.inventory[id]["quantity"]
        }
        self.inventory.pop(id)
        return 0
    
    #undelete the most recently deleted item
    def undelete(self):
        id = 0
        if not self.recycle_bin:
            print("No recently deleted item")
            return -1
        for key,value in self.recycle_bin.items():
            if key=="id":
                id = value
                self.inventory[id] = {}
            else:
                self.inventory[id][key] = value

        return 0

    def print_all(self):
        if not self.inventory:
            print("Inventory is empty")
            return -1
        for key,value in self.inventory.items():
            print("__",key,"__")
            for k,v in value.items():
                print(k,":",v)
            print("______________")

        return 0
