from llama.lima.bima import fima,gima

def test_fima():
    assert fima('a', 1) == ('a',1)


def test_gima():

    assert gima(1,2,'a') == (1,2, 'a')
