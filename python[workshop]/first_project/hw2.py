num_products = int(input("Сколько продуктов вы можете унести из магазина? "))

shopping_list = []

for i in range(num_products):
    product = input("Введите наименование продукта: ").lower()
    if product in shopping_list:
        print(f"Продукт {product} уже есть в списке!")
    else:
        shopping_list.append(product)

print("Список покупок:")
for product in shopping_list:
    print(f"- {product}")
