stock_count = int(input("how many items are in stock?"))

if stock_count == 0:
    print("out of stock")
elif stock_count <= 5:
    print("low stock order soon")
else:
    print("in stock")

    sum = 0
    for i in range(2,51,2):
        sum +=i
        print("the sum of even numbers from 2 to 50 is:"sum)