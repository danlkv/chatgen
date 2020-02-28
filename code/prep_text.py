
import re


symbols_for_empasize = '#$%&\\\'()*+"-/:;<=>@[\\\\]^_`{|}~\\£“”!?,.' 
numbers =["0","1","2","3","4","5","6","7","8","9" ]
spec_sym = {
#     "'" : " ' ",
    '—' : '-',
    '“' : '"',
    '”' : '"',
    "`"  : "'"
}
stop_simbols = '§½ÀÁÆÉàáâäæçèéêëíîïóôöúüýŒœηοςτϰוח•■\xa0'

class preprocessing_text:
    '''
    example of using
    
    model = preprocessing_text()
    
    clear_test = model.clear_text(text)
    
    enjoy 
    
    '''
    def __init__(self):
        pass
    def clear_text(self, text):
        
        data = []
        for item in text.split('\n'):
            final = []
            if item != '':
                new_line = self.clear_line(item)
                if new_line != "":
                    final.append(new_line)
            data.append(" ".join(final))
#         ans = []
#         for item in data:
#             for n in item.split(" "):
#                 if n != '':
#                     ans.append(n)
        return "\n".join(data)
    def clear_line(self, line):
        words = line.lower().split(" ")
        words = self.clear_words(words)
        ln = " ".join(words)
        res = self.emphasise(ln)
        return res
        
    def clear_words(self, words):
        ans = []
        for word in words:
            if word != '':
                flag = True
                for w in word:
                    if w in stop_simbols:
                        flag = False
                if flag:
                    ans.append(word)
        return ans
    def emphasise(self, ln):  
        a = re.split("[.]", ln)
        ans = []
        for item in a:
            if item != '':
                ans.append(item)
        ln = ".".join(ans)
        for s in spec_sym.keys():
            ln = re.sub(s,spec_sym[s], ln )

        for s in symbols_for_empasize:
            ln= (" "+ s+ " ").join(ln.split(s))
            
        for s in numbers:
            ln = re.sub(s," " + s + " ", ln )
        return ln