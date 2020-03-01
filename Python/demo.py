import pytest
def div(a,b):
    return a/b

class Test_div:



    def setup(self):
        self.x,self.y = 1,0
        self.q,self.e = 1,2

    @pytest.mark.happy
    def test_one(self):
        assert div(self.x,self.y) == None

    @pytest.mark.parametrize("x,y,z",{
        (1,2,0.5),
        (50,20,2.5),
        
    })
    def test_two(self):
        assert div(self.q,self.e) == self.q/self.e
