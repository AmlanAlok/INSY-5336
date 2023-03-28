

class Car:
    def __init__(self, make, year, price):
        self.make = make
        self.year = year
        self.price = price

    def get_total_price(self):
        return self.price*1.1

    def display(self):
        print(self.make)
        print(self.year)
        print(self.get_total_price())


if __name__ == '__main__':

    c = Car('Zoro', 1964, 1000)
    c.display()


