from property import Property
from utilities import get_valid_input

class Rental(Property):
    def __init__(self, furnished='', extras='', rent='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.furnished = furnished
        self.rent = rent
        self.extras = extras

    def display(self):
        super().display()
        print(f'RENTAL DETAILS\n'
              f'Rent: {self.rent}\n'
              f'Furnished: {self.furnished}\n'
              f'Extras: {self.extras}\n'
        )

    def prompt_init():
        return dict(
            furnished= get_valid_input("Has property furnished? ",("yes", "no")),
            extras = input("What are the extras prefer? "),
            rent = input("What is the established monthly rent? "),
        )
    
    prompt_init = staticmethod(prompt_init)


from apartment import Apartment
class ApartmentRental(Apartment, Rental):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())

        return init
    
    prompt_init = staticmethod(prompt_init)


from house import House
class HouseRental(House, Rental):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())

        return init
    
    prompt_init = staticmethod(prompt_init)