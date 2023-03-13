from llama.rancher import Farmer

def test_Farmer():
    assert Farmer.wrench('hexnut')=='hexnut tightened'