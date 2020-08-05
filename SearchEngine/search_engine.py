"""
Arjun Srivastava
Section AB
HW4: Python Classes and Search Engines
Search Engine class: Manages a collection of Documents,
and handles computing the relevance of a Documents to a given term
"""
import os
import re
import math
from document import Document


class SearchEngine:
    def __init__(self, dir_name):
        """
        Takes in a directory name (string), and constructs
        an inverse index representing all documents in the given directory
        """
        self._inv_index = {}
        documents = [Document(dir_name + '/' + file_name)
                     for file_name in os.listdir(dir_name)]
        self._num = len(documents)
        for document in documents:
            words = document.get_words()
            for word in words:
                if word not in self._inv_index:
                    self._inv_index[word] = [document]
                else:
                    self._inv_index[word].append(document)

    def _calculate_idf(self, term):
        """
        Takes a term as a string argument and
        returns the IDF score for that term over all documents
        managed by the SearchEngine
        """
        docs = set()
        term = re.sub(r'\W+', '', term).lower()
        for k, v in self._inv_index.items():
            if k == term:
                docs.add(doc for doc in v)
        score = len(docs)
        if score == 0:
            return 0
        else:
            return math.log((self._num / score))

    def search(self, query):
        """
        Takes the given string term and returns a
        list of document names sorted in decreasing
        order of TF-IDF. If no document contains the
        given term, returns None
        """
        scores = []
        terms = query.split()
        terms = [re.sub(r'\W+', '', word).lower() for word in terms]
        docs = set()
        for word in terms:
            if word in self._inv_index:
                for doc in self._inv_index[word]:
                    docs.add(doc)
        if len(docs) == 0:
            return None
        for doc in docs:
            tf_idf = 0
            for word in terms:
                tf_idf += self._calculate_idf(word) * doc.term_frequency(word)
            scores.append((doc.get_path(), tf_idf))
        scores = sorted(scores, key=lambda d: d[1])
        result = []
        for pair in scores:
            result.append(pair[0])
        result.reverse()
        return result
