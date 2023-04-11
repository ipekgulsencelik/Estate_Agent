from property import Property
from utilities import get_valid_input

class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    
    def __init__(self, number_stories='', garage='', fenced='', pool='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pool = pool
        self.garage = garage
        self.fenced = fenced
        self.num_stories = number_stories

    def display(self):
        super().display()
        print(f'HOUSE DETAILS\n'
              f'Number of Stories: {self.num_stories}\n'
              f'Garage: {self.garage}\n'
              f'Fenced: {self.fenced}\n'
              f'Poll: {self.pool}\n'
        )

    def prompt_init():
        parent_init = Property.prompt_init()
                
        num_stories = input("How many stories do you want? ")
        garage = get_valid_input("Do you want to garage? ", House.valid_garage)
        fenced = get_valid_input("Do you prefer to fenced? ", House.valid_fenced)
        pool = get_valid_input("Do you prefer to pool? ", ('yes', 'no'))

        parent_init.update({
            "num_stories": num_stories,
            "garage": garage,
            "fenced": fenced,
            "pool": pool
        })

        return parent_init
    
    prompt_init = staticmethod(prompt_init)