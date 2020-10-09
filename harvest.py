############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow watermelon")
    yellow_watermelon.add_pairing("ice cream")
    muskmelon.add_pairing("mint")
    casaba.add_pairing("mint", "strawberries")
    
    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with {melon_type.pairings}.")
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

class Melon(object):
    """A melon in a melon harvest."""

    #self.attribute = arrtibute 

    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvester):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harves_field = harvest_field
        self.harvester = harvester
        
    def is_sellable(self, shape_rating, color_rating, harvest_field):
        return shape_rating > 5 and color_rating > 5 and harvest_field != 3 



    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



