items = []
prices = []


i = 0
while i < 5:
    item=input(f"{i+1}. Enter Item: ")
    items.append(item)

    price = int(input("  Enter the price: "))
    prices.append(price)  
    i = i + 1  


total = sum(prices)/len(prices)
print(f"Average price: {total} pesos")

a = 0
for i in range(len(prices)):
    if prices[i] >= total:
        print(f"{a+1}. {items[i]}: {prices[i]} pesos")
        a = a + 1
    
        
    

