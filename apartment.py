from property import Property
from utilities import get_valid_input

class Apartment(Property):
    valid_laundries = ("coin", "credit_card", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super(Apartment, self).display()
        print(f'APARTMENT DETAILS\n'
        f'Laundry: {self.laundry}\n'
        f'Balcony: {self.balcony}\n'
        )

    def prompt_init():
        parent_init = Property.prompt_init()

        balcony = get_valid_input("Does apartment have a balcony?", Apartment.valid_balconies)
        laundry = get_valid_input("What laundry type do you prefer", Apartment.valid_laundries)

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        
        return parent_init
    
    prompt_init = staticmethod(prompt_init)