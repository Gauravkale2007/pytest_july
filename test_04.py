class Test_pytest04():
    def test_my_method(self):
        a = 10
        b = 2
        Result = a/b
        print("Division is :", Result)
        if Result ==5:
            print("Good")
            assert True
        else:
            print("Very Bad")
            assert False


