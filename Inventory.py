class Inventory:
    #initialize new inventory that will store items
    def __init__(self):  
        self.inventory = {}
        self.recycle_bin = {}

    #create and add items to the inventory
    def create(self, id, name, description, cost, quantity):
        attributes = {
            "name": name,
            "description": description,
            "cost": cost,
            "quantity": quantity
        }
        self.inventory[id] = attributes

    #update current inventory items
    def update(self,id):
        #check if id provided is valid first
        if not self.inventory[id]:
           return -1 
        print("Item found, input new values only for attributes to be changed else press ENTER")
        for key in self.inventory[id]:
            new_val = ("Update ",key,": ")
            if new_val:
                self.inventory[id][key] = new_val

        return 0

    #delete current items in inventory
    def delete(self, id):
        #check if id provided is valid first
        if not self.inventory[id]:
           return -1 
        self.recycle_bin = {
            "id": id,
            "name": self.inventory[id]["name"],
            "description": self.inventory[id]["description"],
            "cost": self.inventory[id]["cost"],
            "quantity": self.inventory[id]["quantity"]
        }
        self.inventoty.pop(id)
    
   
    def undelete(self):
        id = 0
        for key,value in self.recycle_bin.items():
            if key=="id":
                id = value
            else:
                self.inventory[id][key] = value
