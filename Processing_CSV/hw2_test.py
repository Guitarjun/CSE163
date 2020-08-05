"""
Arjun Srivastava
Section AB
HW2: Processing CSV Data
Contains testing for all methods from hw2_manual and hw2_pandas
"""
import pandas as pd

# You can call the method using
#    assert_equals(expected, received)
#    parse(file)
from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

# Various testing files used
test_csv = parse('/home/pokemon_test.csv')
box_csv = parse('/home/pokemon_box.csv')
test_pd = pd.read_csv('/home/pokemon_test.csv')
box_pd = pd.read_csv('/home/pokemon_box.csv')
arjun_csv = parse('/home/arjun_test.csv')
arjun_pd = pd.read_csv('/home/arjun_test.csv')


def test_species_count():
    """
    Tests species_count manual and pandas
    """
    # Testing manual
    assert_equals(3, hw2_manual.species_count(test_csv))
    assert_equals(5, hw2_manual.species_count(arjun_csv))

    # Testing pandas
    assert_equals(3, hw2_pandas.species_count(test_pd))
    assert_equals(5, hw2_pandas.species_count(arjun_pd))


def test_max_level():
    """
    Tests max_level manual and pandas
    """
    # Testing manual
    assert_equals(('Lapras', 72), hw2_manual.max_level(test_csv))
    assert_equals(('Starmie', 76), hw2_manual.max_level(arjun_csv))

    # Testing pandas
    assert_equals(('Lapras', 72), hw2_pandas.max_level(test_pd))
    assert_equals(('Starmie', 76), hw2_pandas.max_level(arjun_pd))


def test_filter_range():
    """
    Tests filter_range manual and pandas
    """
    # Testing manual
    assert_equals(
        ['Arcanine', 'Arcanine', 'Starmie'],
        hw2_manual.filter_range(test_csv, 30, 70))
    assert_equals(
        ['Arcanine', 'Rhyhorn'], hw2_manual.filter_range(arjun_csv, 30, 40))

    # Testing pandas
    assert_equals(
        ['Arcanine', 'Arcanine', 'Starmie'],
        hw2_pandas.filter_range(test_pd, 30, 70))
    assert_equals(
        ['Arcanine', 'Rhyhorn'],
        hw2_pandas.filter_range(arjun_pd, 30, 40))


def test_mean_attack_for_type():
    """
    Tests mean_attack_for_type manual and pandas
    """
    # Testing manual
    assert_equals(47.5, hw2_manual.mean_attack_for_type(test_csv, 'fire'))
    assert_equals(72, hw2_manual.mean_attack_for_type(arjun_csv, 'psychic'))

    # Testing pandas
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(test_pd, 'fire'))
    assert_equals(72, hw2_pandas.mean_attack_for_type(arjun_pd, 'psychic'))


def test_count_types():
    """
    Tests count_types manual and pandas
    """
    # Testing manual
    assert_equals({'fire': 2, 'water': 2}, hw2_manual.count_types(test_csv))
    assert_equals(
        {'poison': 1, 'fire': 1, 'psychic': 1, 'water': 1, 'rock': 1},
        hw2_manual.count_types(arjun_csv))

    # Testing pandas
    assert_equals({'fire': 2, 'water': 2}, hw2_pandas.count_types(test_pd))
    assert_equals(
        {'poison': 1, 'fire': 1, 'psychic': 1, 'water': 1, 'rock': 1},
        hw2_pandas.count_types(arjun_pd))


def test_highest_stage_per_type():
    """
    Tests highest_stage_per_type manual and pandas
    """
    # Testing manual
    assert_equals(
        {'fire': 2, 'water': 2},
        hw2_manual.highest_stage_per_type(test_csv))
    assert_equals(
        {'poison': 1, 'fire': 2, 'psychic': 2, 'water': 2, 'rock': 1},
        hw2_manual.highest_stage_per_type(arjun_csv))

    # Testing pandas
    assert_equals(
        {'fire': 2, 'water': 2},
        hw2_pandas.highest_stage_per_type(test_pd))
    assert_equals(
        {'poison': 1, 'fire': 2, 'psychic': 2, 'water': 2, 'rock': 1},
        hw2_pandas.highest_stage_per_type(arjun_pd))


def test_mean_attack_per_type():
    """
    Tests mean_attack_per_type manual and pandas
    """
    # Testing manual
    assert_equals(
        {'fire': 47.5, 'water': 140.5},
        hw2_manual.mean_attack_per_type(test_csv))
    assert_equals(
        {'poison': 40, 'fire': 45, 'psychic': 72, 'water': 34, 'rock': 40},
        hw2_manual.mean_attack_per_type(arjun_csv))

    # Testing pandas
    assert_equals(
        {'fire': 47.5, 'water': 140.5},
        hw2_pandas.mean_attack_per_type(test_pd))
    assert_equals(
        {'poison': 40, 'fire': 45, 'psychic': 72, 'water': 34, 'rock': 40},
        hw2_pandas.mean_attack_per_type(arjun_pd))


def main():
    test_species_count()
    test_max_level()
    test_filter_range()
    test_mean_attack_for_type()
    test_count_types()
    test_highest_stage_per_type()
    test_mean_attack_per_type()


if __name__ == '__main__':
    main()
