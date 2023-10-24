# class Catalogue:
#     def __init__(self, name: str):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product_name: str):
#         self.products.append(product_name)
#
#     def get_by_letter(self, first_letter: str):
#         list_with_c = []
#         for product in self.products:
#             product_like_list = list(product)
#             if product_like_list[0] == first_letter:
#                 list_with_c.append(product)
#         return list_with_c
#
#     def __repr__(self):
#         sorted_list = sorted(self.products)
#         product_list = '\n'.join(sorted_list)
#         return f"Items in the {self.name} catalogue:\n{product_list}"
#
#
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered_products = [product for product in self.products if product.startswith(first_letter)]
        return filtered_products

    def __repr__(self):
        sorted_list = sorted(self.products)
        product_list = '\n'.join(sorted_list)
        return f"Items in the {self.name} catalogue:\n{product_list}"

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
