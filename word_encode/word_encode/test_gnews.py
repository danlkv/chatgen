from .word_encode import GoogleNews

def test_gnews():
    coder = GoogleNews()
    cake = coder.encode('cake')
    print('cake:', cake)
    assert cake.shape == (1,300)

if __name__ == '__main__':
    test_gnews()
