class Pet:

    all = []
    
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        
        
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.pet_type = pet_type
        
        
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be of type Owner or None.")
        self.owner = owner
        
        
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """
        Returns a list of pets belonging to this owner.
        """
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Assigns the current owner to the given pet.
        Raises an exception if the pet is not an instance of Pet.
        """
        if not isinstance(pet, Pet):
            raise Exception("The provided pet must be an instance of Pet.")
        
        pet.owner = self

    def get_sorted_pets(self):
        """
        Returns a list of this owner's pets sorted by their names.
        """
        return sorted(self.pets(), key=lambda pet: pet.name)



owner = Owner("John")
pet1 = Pet("Buddy", "dog")
pet2 = Pet("Whiskers", "cat", owner)  
owner.add_pet(pet1)  

print("Owner's pets:", [pet.name for pet in owner.pets()])  
print("Sorted pets:", [pet.name for pet in owner.get_sorted_pets()])  
