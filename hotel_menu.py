menu = {
    'Pasta':40,
    'Hukka':300,
    'Burger':30,
    'Coffee':90,
    'Pizza':100,
}
print('Welcome to our Python Restaurant')
print("Paste: 40\nHukka: 300\nBurger: 30\nCoffer: 90\nPizza: 100")

order_total = 0
order1 = input('What you want to order: ')

if order1 in menu:
    order_total += menu[order1]
    print(f'Your {order1} is successfully added in the orderlist')
else:
    print(f'Ordered item {order1} is not available yet!')
    
another_order = input('Do you want to add another item? (Yes/No)')
if another_order == 'yes':
    order2 = input('Enter the name of the another item: ')
    if order2 in menu:
        order_total += menu[order2]
        print(f'Item {order2} has been added to order')
    else:
        print('Ordered item {order2} is not available')
    
print(f"The total amount of items to pay is {order_total}")
    
