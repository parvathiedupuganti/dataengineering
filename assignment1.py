items = [{"itemid":1,"itemname":"laptop","price":40000},
         {"itemid":2,"itemname":"mouse","price":400},
         {"itemid":3,"itemname":"keyboard","price":200},
         {"itemid":4,"itemname":"tablet","price":20000},
         {"itemid":5,"itemname":"motherboard","price":3000},
         {"itemid":6,"itemname":"desktop","price":30000}
         
         ]

cart =[]

def display_menu():
    print("menu:")
    print("1. view the store")
    print("2. purchase thes item")
    print("3.update the purchased item")
    print("4.remove the item")
    print("5.view the purchased item list")
    print("6.exit and generate invoice")

def view_store():
    print("store items")
    for item in items:
        print(f"itemid: {item["itemid"]}, itemname: {item["itemname"]}, price: {item["price"]}")

def find_item(identifier):    
    for item in items:
        if isinstance(identifier,int):
            if item['itemid'] == identifier:
                return item
        else:
            if item['itemname'].lower() == identifier.lower():
                return item
    return None   
    
        
        
def purchase_item():
    while True:           
        identifier = input("enter item id or item name")
        if identifier.isdigit():
            identifier = int(identifier)
        item = find_item(identifier) 

        if item:
            quantity = int(input("enter quantity to purchase"))
            cart.append({"item" : item,"quantity": quantity,"total":item["price"]*quantity})
            cont = input("do you want to continue adding items? (yes/no): ")
            if cont.lower() == 'no':
                break
        else:
            print("item not found. please try again")
    
def update_item():
    identifier = input("enter item id or item name to be updated")
    if identifier.isdigit():
        identifier = int(identifier)

    for entry in cart:
        if entry['item']['itemid'] == identifier or entry['item']['itemname'].lower() == identifier.lower():
            quantity = int(input("enter new quantity"))
            entry[quantity] = quantity
            entry['total'] = entry['item']['price'] * quantity
            print("Item quantity updated.")
            return
    print("Item not found in cart.")  


def remove_item():
    identifier = input("enter item id or item name to be removed")
    if identifier.isdigit():
        identifier = int(identifier)
    for entry in cart:
        cart.remove(entry)
        return
    print("item not found in cart")

def view_purchased_item():
    print("purchased items:")
    for index, entry in enumerate(cart,start =1):
        item = entry["item"]        
        print(f"{index}. {item['itemname']} {entry['quantity']} {item['price']} {entry['total']}")

def generate_invoice():
    with open("invoice.txt", "w") as f:
        f.write("****** Invoice copy *******\n" )
        total =0
        for index, entry in enumerate(cart,start =1):
            item = entry["item"]        
            line = (f"{index}. {item['itemname']} {entry['quantity']} {item['price']} {entry['total']}\n")
            f.write(line)
            total += entry['total']
        f.write(f"\nTotal: {total}")

def main():
    while True:
        display_menu()
        choice = int(input("enter your choice"))
        if choice == 1:
            view_store()
        elif choice == 2:
            purchase_item()
        elif choice == 3:
            update_item()
        elif choice == 4:
            remove_item()
        elif choice == 5:
            view_purchased_item()
        elif choice == 6:
            generate_invoice()
            print("invoice generated")
        else:
            print("invalid choice. please try again")
        

if __name__ == "__main__":
    main()

    





        

        

    










    







