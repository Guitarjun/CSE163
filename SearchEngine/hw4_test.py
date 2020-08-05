from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine
"""
Arjun Srivastava
Section AB
HW4: Python Classes and Search Engines
Contains testing for the Search Engine
"""


def test_document():
    """
    Tests the Document class
    """
    testing_doc = Document('testing_files/test.txt')
    assert_equals(
        ['this', 'is', 'a', 'testing', 'file', 'please',
            'note', 'that', 'it', 'done'],
        testing_doc.get_words())
    assert_equals(1/7, testing_doc.term_frequency('testing'))
    assert_equals('testing_files/test.txt', testing_doc.get_path())


def test_search_engine():
    """
    Tests the SearchEngine class
    """
    engine_test = SearchEngine('testing_files')
    assert_equals(None, engine_test.search('lion'))
    assert_equals(['testing_files/doc3.txt',
                  'testing_files/doc1.txt'],
                  engine_test.search('dogs'))


def main():
    print('Testing Document class...')
    test_document()
    print('Testing Search Engine class...')
    test_search_engine()
    print('All tests complete!')


if __name__ == '__main__':
    main()
