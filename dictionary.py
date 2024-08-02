my_stocks = {}#empty dictionary
my_stocks = {"TCS":2700,"Infosys":3000,"IDBI":140,"IDFC":100,"NTPC":220}
#print(my_stocks[0]) #error as dictionary items can't be accessed via index
#print(type(my_stocks),my_stocks)
my_stocks["SBI"] = 1700
"""print(my_stocks)
print("no of stocks",len(my_stocks))
print("All stock names",my_stocks.keys())
print("All stock names",my_stocks.values())
#print("The stock price of Infosys is",my_stocks["Infosys"])
for stock in my_stocks:
    print(stock , "has price",my_stocks[stock])
"""
"""
for stock in my_stocks.items():
    print(stock)
    print(stock[0],"has price",stock[1])
"""
for stock,price in my_stocks.items():
    print(stock,"has price",price)
print("*" * 70)
my_stocks.pop("Infosys")
print(my_stocks)
my_stocks.popitem()
print(my_stocks)
del my_stocks["TCS"]
print(my_stocks)
swapped = {}
for key,value in my_stocks.items():
   swapped[value] = key
print(swapped)
