import difflib
from tqdm.autonotebook import tqdm
from gensim.corpora import Dictionary

class rewrite:
    def __init__(self, lang, tr1 = 2, tr2 = 10, path2dict = None):
        self.counts = lang.word2count
        self.words = set(lang.word2count.keys())
        self.tr1 = tr1
        self.tr2 = tr2
        if path2dict:
            self.d = set(Dictionary.load(path2dict).values())
        else :
            self.d = None
        self.word2check = []
        self.other_w = {}
        for w in tqdm(self.words):
            if self.counts[w] < self.tr1 and w not in self.d:
                self.word2check.append(w)
            elif self.counts[w] > self.tr2:
                if len(w) not in self.other_w.keys(): 
                    self.other_w[len(w)] = []
                self.other_w[len(w)].append(w)
    
    def get_sim(self, h = 0.9):
        self.res = []
        self.hz = []
        for w in tqdm(self.word2check):
            met = 0
            wor = w
            for j in range(-3, 4, 1):
                if len(w) + j in self.other_w.keys():
                    for i in self.other_w[len(w) + j]:
                        m = difflib.SequenceMatcher(a = w, b = i).ratio()
                        if m > h and m > met:
                            wor = i
                            met = m
            if wor != w:            
                self.res.append([w, wor, met])
            else:
                self.hz.append(w)
        return self.res
    
    
    @staticmethod
    def clean_text(text, sims):
        for item in tqdm(sims):
            text = item[1].join(text.split(item[0]))
        return text     