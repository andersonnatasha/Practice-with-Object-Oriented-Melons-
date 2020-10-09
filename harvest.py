############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, 
                is_bestseller):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        
    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        
        self.code = new_code
       


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    muskmelon = MelonType("Muskmelon", "musk", 1998, "green",True, True,)
    muskmelon.add_pairing("mint")
    
    casaba = MelonType("Casaba", "cas", 2003, "orange", False, False)
    casaba.add_pairing("mint", "strawberries")
    #casaba.add_pairing("strawberries")
    
    yellow_watermelon = MelonType("Yellow watermelon", "yw", 2013, "yellow", False, True)
    yellow_watermelon.add_pairing("ice cream")

    
    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with") 
        for pairing in melon_type.pairings:
            print(f"- {pairing}")
            print()

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}

    for melon_type in melon_types:
        melon_dict[melon_type.code] = melon_type
    
    return melon_dict
        
        
    # Fill in the rest

############
# Part 2   #
############

class Melon(MelonType):
    """A melon in a melon harvest."""

    #self.attribute = arrtibute 

    def __init__(self, shape_rating, color_rating, harvest_field, harvester):
        super().__init__(code, first_harvest, color, is_seedless, is_bestseller, 
                 name)
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harves_field = harvest_field
        self.harvester = harvester
        
    def is_sellable(self, shape_rating, color_rating, harvest_field):
        return shape_rating > 5 and color_rating > 5 and harvest_field != 3 


def make_melons(melon_types):
    """Returns a list of Melon objects."""


# creaing empty list 
# list of objets of class melon that 
# has all of the attributes we defines above 
#
    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



