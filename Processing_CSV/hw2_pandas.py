"""
Arjun Srivastava
Section AB
HW2: Processing CSV Data
Contains various methods to perform operations
on the data using pandas
"""


def species_count(df):
    """
    Returns the number of unique Pokemon species
    (determined by the name attribute) found in the dataset
    """
    return len(df['name'].unique())


def max_level(df):
    """
    Finds the Pokemon with the max level and returns a tuple of length 2,
    where the first element is the name of the Pokemon
    and the second is its level
    If there is a tie, the Pokemon that appears earlier will be returned
    """
    idmax = df['level'].idxmax()
    name = df.loc[idmax, 'name']
    return name, df['level'].max()


def filter_range(df, low, high):
    """
    Takes as arguments a smallest (inclusive) and largest (exclusive) level
    value and returns a list of Pokemon names having a level within that range
    """
    in_range = df[(df['level'] >= low) & (df['level'] < high)]
    return list(in_range['name'])


def mean_attack_for_type(df, poketype):
    """
    Takes a Pokemon type (string) as an argument and that returns
    the average attack stat for all the Pokemon in the dataset with that type
    If there are no Pokemon of the given type, returns None
    """
    mean = 0
    mean = df.groupby('type')['atk'].mean()
    if mean[poketype] == 0:
        return None
    else:
        return mean[poketype]


def count_types(df):
    """
    Returns a dictionary with keys that are Pokemon types
    and values that are the number of times that type
    appears in the dataset
    """
    counts = df.groupby('type').size()
    return dict(counts)


def highest_stage_per_type(df):
    """
    Calculates the largest stage reached for each type of
    Pokemon in the dataset and returns a dictionary that
    has keys that are the Pokemon types
    and values that are the highest value of stage column
    for that type of Pokemon
    """
    highest = df.groupby('type')['stage'].max()
    return dict(highest)


def mean_attack_per_type(df):
    """
    Calculates the average attack for every type of Pokemon in the dataset
    and returns a dictionary that has keys that are the Pokemon types
    and values that are the average attack for that Pokemon type
    """
    mean = df.groupby('type')['atk'].mean()
    return dict(mean)
