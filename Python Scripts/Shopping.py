products={
    '001':{'Name': 'Coca-Cola', 'Price': 1},
    '002':{'Name': 'Fanta', 'Price': 1},
    '003':{'Name': 'Pepsi', 'Price': 1},
    '004':{'Name': 'Milk', 'Price': 2.5},
    '005':{'Name': 'Water', 'Price': 1},
    '006':{'Name': 'Orange Juice', 'Price': 2}
}

cart={}

def clear_cart():
    global cart
    cart={}
    print("Cart Cleared")

def view_cart():
    if not cart:
        print("Cart is Empty")
    else:
        print("\n Your current cart: ")
        total=0
        for product_id, quantity in cart.items():
            product=products[product_id]
            item_total=products['Price']*quantity
            total+=item_total
            print(f"{product_id} => {product['Name']} : {quantity} x ${product['Price']} = ${item_total:.2f}")
            print(f"\n your total cost is : ${total:2f}")

def add_to_cart(product_id,quantity):
    if product_id in products:
        if product_id in cart:
            cart[quantity]+=quantity
        else:
            cart[quantity]=quantity
        print(f"Added {quantity} {products[product_id]['Name']}(s) to the cart.")
    else:
        print("Invalid Product ID")

def remove_from_cart(product_id,quantity):
    if cart[product_id] <= quantity:
        del cart[product_id]
        print(f"removed all {products[product_id]['Name']}(s) from the cart.")
    if cart[product_id] >= quantity:
        product_id-= quantity
        print(f"removed {quantity} {products[product_id]['Name']}(s) from the cart.")
    else:
        print("This product is not in the cart.")
    
def edit_cart():
    product_id=input("Enter product ID that you want to edit: ")
    if product_id in cart:
        action=input("Do you want to (A)dd or (R)emove? :").upper
        if action =='A':
            quantity=input('Enter quanity to add: ')
            add_to_cart(product_id,quantity)
        if action =='B':
            quantity=input('Enter quantity to remove: ')
            remove_from_cart(product_id,quantity)
        else:
            print("Invalid action ")
    else:
        print("This product is not in cart ")

def view_products():
    print("\n Available Products")
    for id, product in products.items:
        print(f"ID: {id}, Name: {products['Name']}, Price: ${products['Price']:.2f}")

print("===== Welcome to My store =====")
print("\n Here are our list of products: ")
view_products()

while True:
    print("What would you like to do?")
    print("\n--- What would you like to do? ---")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Edit cart")
    print("4. Clear cart")
    print("5. View available products")
    print("6. Exit")
    
    choice=input("Enter your choice(1-6)")
    if choice=='1':
        product_id=input("Enter product ID: ")
        quantity=int(input("Enter quanity: "))
        add_to_cart(product_id,quantity)
    if choice=='2':
        view_cart()
    if choice=='3':
        edit_cart()
    if choice=='4':
        clear_cart()
    if choice=="5":
        view_products()
    if choice=="6":
        print("Goodbye, please come again! ")
        break
    else:
        print("Invalid choice. Please try again ")
