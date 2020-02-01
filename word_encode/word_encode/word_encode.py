"""Main module."""
import numpy as np
import gensim

class W2V:
    """ An abstract word encoder """

    def fit(self, data):
        raise NotImplementedError

    def encode(self, text: str):
        raise NotImplementedError

    def decode(self, vectors: np.array):
        raise NotImplementedError

class GoogleNews(W2V):
    """
    https://rare-technologies.com/word2vec-tutorial/
    """
    def __init__(self, addr='./GoogleNews_word2vec/GoogleNews-vectors-negative300.bin'):
        self.addr = addr
        self.model = gensim.models.KeyedVectors.load_word2vec_format(
            self.addr, binary=True)

    def fit(self, data):
        pass

    def encode(self, text):
        words = text.split()
        return np.array([self.model[word] for word in words])

    def decode(self, vectors):
        """
        See: https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.similar_by_vector
        """

        # use np.vectorize?
        return np.array([self.model.similar_by_vector(vec, topn=1)[0][0] 
                         for vec in vectors])

