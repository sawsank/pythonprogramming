## Call Function using both positional and keyword arguments

def describe_pet(animal_type, pet_name):
    print(f"\n I have a {animal_type} named {pet_name}")

## Calling the function using positional arguments
describe_pet('hamster', 'harry')
describe_pet('dog', 'lucy')

## Calling the function using keyword arguments
describe_pet(animal_type='cat', pet_name='whiskers')
describe_pet(pet_name='buddy', animal_type='dog')
