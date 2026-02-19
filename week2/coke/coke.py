amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin_inserted = int(input("Insert Coin: "))
    if coin_inserted in [25, 10, 5]:
        amount_due -= coin_inserted
        if amount_due <= 0:
            print("Change Owed:", amount_due * -1)
            break
