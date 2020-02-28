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
        self.set_of_words = set(self.model.vocab.keys())
        self.size = 300

    def fit(self, data):
        pass

    
    
    def encode(self, text):
        code = []
        for line in text.split("\n"):
            code.append(self.encode_line(line))
        return code
        
    
    
    
    def encode_line(self, text):
        words = text.split()
        
        enc = []
        
        for word in words:
            if word.lower() in self.set_of_words:
                enc.append(self.model[word.lower()])
            elif word.upper() in self.set_of_words:
                enc.append(self.model[word.upper()])
            elif word in self.set_of_words:
                enc.append(self.model[word])
            else:
                enc.append(np.zeros(self.size))
        return np.array(enc)

    
    def decode(self, vectors, string = False):
        s = []
        
        for line in vectors:
            s.append(self.decode_line(line, string = string))
        if string:
            return "\n".join(s)
        else:
            return s
    
    
    def decode_line(self, vectors, string = False):
        """
        See: https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.similar_by_vector
        """
        
        
        
        words = [self.model.similar_by_vector(vec, topn=1)[0][0] 
                         for vec in vectors]
        # use np.vectorize?
        if string:
            return " ".join(words)
        else:
            return np.array(words)

