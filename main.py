
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} добавлен в склад")

    def remove_product(self, product):
        self.products.remove(product)
        print(f"{product.name} удален со склада")

    def get_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value

    def print_inventory(self):
        if len(self.products) == 0:
            print("Склад пуст")
        else:
            print("Склад:")
            for product in self.products:
                print(f"{product.name} - количество: {product.quantity}")

def main():
    inventory =Inventory()

    while True:
        print("\n1. Добавить продукт")
        print("\n2. Удалить продукт")
        print("\n3. Получить общую стоимость продуктов на складе")
        print("\n4. Ввести список продуктов на складе")
        print("\n5. Выйти")

        choice = input("Выберите опцию:")
        if choice == "1":
            name = input("Введите название продукта:")
            price = float(input("Введите цену продукта:"))
            quantity = int(input("Введите количество продукта:"))
            product = Product(name,price,quantity)
            inventory.add_product(product)

        elif choice == "2":
            name = input("Введите название продукта для удаления:")
            for product in inventory.products:
                if product.name == name:
                    inventory.remove_product(product)
                    break
            else:
                print("Продукт не найден на складе")

        elif choice =="3":
            total_value = inventory.get_total_value()
            print(f"Общая стоимость продуктов на складе: {total_value}")

        elif choice == "4":
            inventory.print_inventory()

        elif choice == "5":
            break

        else:
            print("Неверный выбор. Попробуйте еще раз")

if __name__ == "__main__":
    main()