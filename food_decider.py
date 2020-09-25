import random


#! automatically populate from key maybe?
restaurants = {'Hardin Valley': ['Double Dogs', 'Don Gallo', 'Poke', 'Hard Knox', 'Mikata', 'Food Truck'],
               'Turkey Creek': ['Blaze Pizza', 'Mimis', 'Taste of Thai', 'Bombay Palace'],
               'Downtown': ['Balter Beerworks', 'Southcoast Pizza']
               }

######
## INPUT SPACE
######
isVegetarian = False

# this can be a list
neighborhoodPref = None

#! more options


######
## END input space
######

if neighborhoodPref:
    for i in neighborhoodPref:
        if i not in restaurants.keys():
            raise ValueError('Your neighborhood is not in the list of restaurants.')



#! add in weights (markov)

candidates = []
for k, v in restaurants.items():
    if neighborhoodPref is None or k in neighborhoodPref:
        candidates.extend(v)

choice = random.choices(candidates)[0]
print(choice)

#! backend maybe google search and show hours and such

