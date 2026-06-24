# 1st dictionary
s={
    'name':"car",
    'price':5000,
    'Qty':5,
    'colour':["black","blue"],
    'modelno':["mo1","m02"]
}
for i in range(len(s["colour"])):
    print("----------car dtails-----------")
    print("Name: ",s["name"])
    print("price: ",s["price"])
    print("Qty: ",s["Qty"])
    print("colour: ",s["colour"][i])
    print("model: ",s["modelno"][i])
    print()

# ======================================================================================
# 2nd dictonary
x={
    'category':"mobile",
    'product_name':["iphone","oppo","vivo"],
    'price':[100000,50000,4000]
}
for i in range(len(x['product_name'])):
    print("-------------phone shop-----------")
    print("product category: ",x['category'])
    print("product colour: ",x['product_name'][i])
    print("product prcie: ",x['price'][i])
    print()

# above 50000
print("---------top rated phones----------------")
for i in range(len(x['product_name'])):
    if x['price'][i] >= 50000:
        print("Product Name  :", x['product_name'][i])
        print("Product Price :", x['price'][i])
        print()



