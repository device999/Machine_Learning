import source

class TestSource:

    def test_addition(self):
        assert 4 == source.add(2, 2)
        assert 5 == source.add(2, 3)

    def test_subtraction(self):
        assert 2 == source.subtract(4, 2)