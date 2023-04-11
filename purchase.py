from property import Property
from apartment import Apartment
from house import House

class Purchase(Property):
    def __init__(self, price='', taxes='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print(f'PURCHASE DETAIL\n'
              f'===============\n'
              f'selling Price: {self.price}\n'
              f'Taxes: {self.taxes}'
        )

    def prompt_init():
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? ")
        )
    
    prompt_init = staticmethod(prompt_init)