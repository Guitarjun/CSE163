"""
Arjun Srivastava
Section AB
HW4: Python Classes and Search Engines
Document class: Represents a single file in the SearchEngine,
and will include functionality to compute the term frequency of a
term in the document
"""
import re


class Document:
    def __init__(self, file_name):
        """
        Initializes a new Document from the given file name. If the file
        is empty, the Document will represent an empty file
        """
        self._path = file_name
        self._frequencies = {}
        self._size = 0
        with open(self._path) as f:
            content = f.read().split()
            self._size = len(content)
            for token in content:
                token = re.sub(r'\W+', '', token).lower()
                if token in self._frequencies:
                    self._frequencies[token] += 1
                else:
                    self._frequencies[token] = 1

    def term_frequency(self, term):
        """
        Takes a string term as a parameter and returns the
        term-frequency of the given term in the document
        """
        fixed_term = re.sub(r'\W+', '', term).lower()
        if term not in self._frequencies:
            return 0
        return self._frequencies[fixed_term] / self._size

    def get_path(self):
        """
        Returns the path of the file this Document represents
        """
        return self._path

    def get_words(self):
        """
        Returns a list of all the unique words in this document
        """
        return self._frequencies.keys()
