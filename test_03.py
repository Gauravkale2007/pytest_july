
class Test_pytest_03():
    def test_mul(self):
        a = 5
        b = 4
        result = a * b
        print("Multiplication:",result)
        if result==20:
            print("Maths is good")
            assert True
        else:
            print("Have to Work on maths")
            assert False






