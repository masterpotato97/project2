def paco_tacos(shopping_cart):
    ingredients = {'tortillas': 0.25, 'meat': 5.76, 'lettuce': 3.25, 'cheese': 15.15}

    print('Welcome to Paco Tacos Supplies! We have all supplies for tacos. Here is our menu and prices:')
    for item, price in ingredients.items():
        print(f'{item}: ${price:.2f}')

    your_cart = {}

    while True:
        customer_input = input('Place your order (or type "done" to finish): ')

        if customer_input == 'done':
            break

        if customer_input == 'remove':
            print('Here is your current cart:')
            for item, quantity in your_cart.items():
                print(f'{item}: {quantity} x ${ingredients[item]:.2f} = ${ingredients[item] * quantity:.2f}')

            item_to_remove = input('What item would you like to remove? ')
            if item_to_remove not in your_cart:
                print('That item is not in your cart.')
                continue

            try:
                remove_quantity = int(input(f'How many {item_to_remove} would you like to remove? '))
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue

            if remove_quantity < 1:
                print('Quantity must be greater than zero.')
                continue

            if remove_quantity >= your_cart[item_to_remove]:
                del your_cart[item_to_remove]
                print(f'{item_to_remove} has been removed from your cart.')
            else:
                your_cart[item_to_remove] -= remove_quantity
                print(f'{remove_quantity} {item_to_remove}(s) have been removed from your cart.')

            continue

        if customer_input not in ingredients:
            print('Sorry, we do not have that item.')
            continue

        try:
            quantity = int(input(f'How many {customer_input} would you like? '))
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue

        if quantity < 1:
            print('Quantity must be greater than zero.')
            continue

        if customer_input in your_cart:
            your_cart[customer_input] += quantity
        else:
            your_cart[customer_input] = quantity

        print(f'{quantity} {customer_input}(s) added to your cart.')

    total_cost = 0
    for item, quantity in your_cart.items():
        item_cost = ingredients[item] * quantity
        print(f'{item}: {quantity} x ${ingredients[item]:.2f} = ${item_cost:.2f}')
        total_cost += item_cost

    print(f'Total cost: ${total_cost:.2f}')

    if your_cart:
        shopping_cart.append(your_cart)
        print('Your order has been added to the shopping cart.')
    else:
        print('Your cart is empty.')

    return shopping_cart
