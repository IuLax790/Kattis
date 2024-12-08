# Input reading
n = int(input().strip())  # Number of books

# Reading book prices
book_prices = []
for _ in range(n):
    book_prices.append(int(input().strip()))

# Sort prices in descending order
book_prices.sort(reverse=True)

# Calculate the minimal price
minimal_price = 0
for i in range(n):
    if (i % 3) != 2:  # Skip every third book (cheapest in each group of three)
        minimal_price += book_prices[i]

# Output the result
print(minimal_price)
