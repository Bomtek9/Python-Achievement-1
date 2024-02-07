def ShoppingList(object):
    def _init_(self, list_name, shopping_list):
        shopping_list = []
        self.list_name = list_name
        self.shopping_list = shopping_list
        
    def add_item(self, item):
        self.item = item    
        if item in self.shopping_list:
            print("Item already exists")
        else: self.shopping_list.append(item)
        print("Item added to list")
        
    def remove_item(self, item):
        self.item = item
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item removed from list")
        
    def view_list(self):
        print("Shopping List: ", self.list_name)
        print("-----------------")
        for item in self.shopping_list:
            print(item)
        
        
        
        
    