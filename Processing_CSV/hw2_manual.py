"""
Arjun Srivastava
Section AB
HW2: Processing CSV Data
Contains the various methods to perform
operations on the data manually (no libraries)
"""


def species_count(data):
    """
    Returns the number of unique Pokemon species
    (determined by the name attribute) found in the dataset
    """
    species = set()
    for poke in data:
        species.add(poke['name'])
    return len(species)


def max_level(data):
    """
    Finds the Pokemon with the max level and returns a tuple of length 2,
    where the first element is the name of the Pokemon and the second
    is its level
    If there is a tie, the Pokemon that
    appears earlier in the file is returned
    """
    level = 0
    name = ''
    for poke in data:
        if poke['level'] > level:
            level = poke['level']
            name = poke['name']
    return name, level


def filter_range(data, low, high):
    """
    Takes as arguments a smallest (inclusive) and largest
    (exclusive) level value
    and returns a list of Pokemon names having a level
    within that range
    The list contains the species names in the same
    order that they appear in
    the provided list of dictionaries
    """
    inRange = []
    for poke in data:
        if poke['level'] in range(low, high):
            inRange.append(poke['name'])
    return inRange


def mean_attack_for_type(data, poketype):
    """
    Takes a Pokemon type (string) as an argument and that
    returns the average attack stat for all the Pokemon
    in the dataset with that type
    If there are no Pokemon of the given type, returns None
    """
    sum_ = 0
    n = 0
    for poke in data:
        if poke['type'] == poketype:
            sum_ += poke['atk']
            n += 1
    if n == 0:
        return None
    return sum_ / n


def count_types(data):
    """
    Returns a dictionary with keys that are Pokemon types
    and values that are the number of times that type
    appears in the dataset
    """
    typemap = {}
    for poke in data:
        poketype = poke['type']
        if poketype not in typemap:
            typemap[poketype] = 1
        else:
            typemap[poketype] += 1
    return typemap


def highest_stage_per_type(data):
    """
    Calculates the largest stage reached for each type of
    Pokemon in the dataset and returns a dictionary that
    has keys that are the Pokemon types
    and values that are the highest value of stage column
    for that type of Pokemon
    """
    stages = {}
    for poke in data:
        poketype = poke['type']
        if poketype not in stages:
            stages[poketype] = poke['stage']
        else:
            if poke['stage'] > stages[poketype]:
                stages[poketype] = poke['stage']
    return stages


def mean_attack_per_type(data):
    """
    Calculates the average attack for every type of Pokemon in the dataset
    and returns a dictionary that has keys that are the Pokemon types
    and values that are the average attack for that Pokemon type
    """
    attack_sum = {}
    nums = {}
    averages = {}
    for poke in data:
        poketype = poke['type']
        if poketype not in attack_sum:
            attack_sum[poketype] = poke['atk']
            nums[poketype] = 1
        else:
            attack_sum[poketype] += poke['atk']
            nums[poketype] += 1
    for poketype in attack_sum.keys():
        averages[poketype] = attack_sum[poketype] / nums[poketype]
    return averages
