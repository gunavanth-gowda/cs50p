items = {}

while True:
    try:
        item = input()
        if item in items:
            items[item]+=1
        else:
            items[item]=1
    except EOFError:
        break

for item, count in sorted(items.items()):
    print(f"{count} {item.upper()}")
