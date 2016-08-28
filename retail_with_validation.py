# This program calculates retail prices.

mark_up = 2.5  # the markup percentage
another = 'y'  # Variable to control the loop

# Process one or more items.
while another == 'y' or another == 'Y':
    # Get the item's wholesale cost.
    wholesale = float (input ("Enter the item's" + \
                             "wholesale cost:"))

    # Validate the wholesale cost.
    while wholesale < 0:
        print('error: the cost cannot be negative.')
        wholesale = float(input('Enter the correct' + \
                                'wholesale cost;'))

    # Calculate the retail price.
    retail = wholesale * mark_up

    # Display the retail price.
    print('Retail price: $', format(retail, ',.2f'))

    # Do this again?
    anthoer = input('Do you have another item? ' + \
                        '(Enter y for yes):')
