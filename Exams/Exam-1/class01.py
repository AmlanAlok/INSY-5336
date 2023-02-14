


if __name__ == '__main__':
    price = 1000
    TAX = 0.03
    tax_amount = price * TAX
    final_price = price + tax_amount
    print()
    title = "House Price"
    print(f"{title:^50}")
    print("______________________________________________")
    print(f"Initial price: ${price:,.3f}")
    print("______________________________________________")
    print(f"Tax rate: {TAX:.0%}")
    print(f"Tax amount: ${tax_amount:,.3f}")
    print("______________________________________________")
    print(f"Final price: ${final_price:,.3f}")
