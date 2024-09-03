def main():
    # Creating the books_inventory dictionary.
    books_inventory = {
    'isbn 001': {'title': 'Python Programming', 'quantity': 100, 'price': 29.99},
    'isbn 002': {'title': 'Data Science Essentials', 'quantity': 50, 'price': 39.95},
    'isbn 003': {'title': 'Web Development Basics', 'quantity': 75, 'price': 24.99},
    'isbn 004': {'title': 'Machine Learning Fundamentals', 'quantity': 60, 'price': 49.99},
    'isbn 005': {'title': 'Network Security Handbook', 'quantity': 40, 'price': 34.99}
    }
    # printing the dictionary.
    print('BOOKSTORE INVENTORY MANAGEMENT\n')
    print('DISPLAYING THE BOOKSTORE INVENTORY BEFORE UPDATE\n')
    # Traversing the dictionary
    for book_id, book_details in books_inventory.items():
        print(f'ID: {book_id}')
        for key,value in book_details.items():
            if(key == 'price'):
                print(f'{key.capitalize()}: ${value}')
            else:
                print(f'{key.capitalize()}: {value}')
        print()
    # Simulating the sales
    # Decrementing the quantity of each book by 5 by traversing the dictionary upto 5 times
    for i in range(0,5):
        for book_details in books_inventory.values():
            val = book_details['quantity']
            book_details['quantity'] = val - 5;

    # Simulating restocking
    # Incrementing the quantity of each book by 5 by traversing the dictionary upto 3 times.
    for i in range(0,5):
        for book_details in books_inventory.values():
            val = book_details['quantity']
            book_details['quantity'] = val + 3;
    
    # printing the dictionry.
    print('\nDISPLAYING THE BOOKSTORE INVENTORY AFTER UPDATE\n')
    for book_id, book_details in books_inventory.items():
        print(f'ID: {book_id}')
        for key,value in book_details.items():
            if(key == 'price'):
                print(f'{key.capitalize()}: ${value}')
            else:
                print(f'{key.capitalize()}: {value}')
        print()

    # implementing the optional enhancements
    
    # optional enhancement - 1.
    # calculating the revenue generated of selling the books.
    total_revenue = 0
    for book_details in books_inventory.values():
        total_revenue += (book_details['quantity'] * book_details['price'])
    print(f'The total revenue earned after selling all the books is ${total_revenue:.2f}')

    # optional enhancement - 2
    # calculating the profit by adding the purchase price key into the dictionary.
    list_purchase_keys = [15.00, 20.00, 12.50, 25.00, 18.00]
    index = 0;
    for book_details in books_inventory.values():
        book_details['purchase_key'] = list_purchase_keys[index]
        index += 1

    # We have already calculated the total revenue, we just need to calculate
    # the total purchase cost to calculate overall profit after selling all the books
    total_purchase_cost = 0
    for book_details in books_inventory.values():
        total_purchase_cost += (book_details['quantity'] * book_details['purchase_key'])

    total_cost = total_revenue - total_purchase_cost
    # printing the total profit.
    print(f'The total profit earned after selling all the book is: {total_cost:.2f}')

    
    

main()
