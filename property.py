class Property:
    def __init__(self, square_feet='', bedrooms='',bathrooms='', *args, **kwargs):
        self.bathrooms = bathrooms
        self.bedrooms = bathrooms
        self.square_feet = square_feet

    def display(self):
        print(f'PROPERTY DETAILS\n'
        f'================\n'
        f'Square Feet: {self.square_feet}\n'
        f'Bedrooms: {self.bedrooms}\n'
        f'Bathrooms: {self.bathrooms}\n')

    def prompt_init():
        return dict(
            square_feet = input("Enter the square feet: "),
            bedrooms = input("Enter number of bedrooms: "),
            bathrooms = input("Enter number of bathrooms: ")
        )
    
    prompt_init = staticmethod(prompt_init)