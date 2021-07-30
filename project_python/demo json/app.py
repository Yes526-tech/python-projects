def add_product(product_name, price, is_selling, category):
    product = {
        "product_name": product_name,
        "price": price,
        "is_selling": is_selling,
        "category": category

    }

    import json
    with open("app.json", "w") as file:
        json.dump(product, file)


add_product("samsung", 1500, True, ["phone", "electronic"])


def get_product():
    import json
    with open("app.json") as file:
        product = json.load(file)
    categories = ' '.join([category for category in product["category"]])
    print(
        f"product name: {product['product_name']}, price: {product['price']}, is_selling: {product['is_selling']}, category: {categories}")


get_product()
