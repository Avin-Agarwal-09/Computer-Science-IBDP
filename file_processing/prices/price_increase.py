f = open("prices.txt","r")
g = open("updated_prices.txt","w")

prices = f.readline()
while prices != "":
    print(prices)

    y = prices.split(",")
    if "\n" in y[1]:
        y[1] = float(y[1][:-1])
    else:
        y[1] = float(y[1])
    rounded_y = f"{(y[1]*1.1):.2f}"
    y[1] = rounded_y
    print(rounded_y)
    print(y)
    string = y[0] + "," + y[1]
    g.write(f"{string}\n")
    prices = f.readline()
f.close()
g.close()



