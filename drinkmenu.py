def serve_drinks(drinks, orders):
    """
    Serves drinks to customers in the order they appear on the menu.

    Args:
      drinks: A list of drink names.
      orders: A list of customer names.

    Returns:
      A list of drinks served to the customers in the correct order.
    """

    customer_drinks = {}
    for customer in orders:
        if customer not in customer_drinks:
            customer_drinks[customer] = 0  # Initialize drink index to 0

    served_drinks = []
    for customer in orders:
        served_drinks.append(drinks[customer_drinks[customer]])
        customer_drinks[customer] += 1 

    return served_drinks

if __name__ == "__main__":
    n, m = map(int, input().split())
    drinks = [input() for _ in range(n)]
    orders = [input() for _ in range(m)]

    served_drinks = serve_drinks(drinks, orders)
    for drink in served_drinks:
        print(drink)
