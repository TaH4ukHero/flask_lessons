from pytest import raises

from is_under_queen_attack import is_under_queen_attack


class TestIsUnderQueenAttack:
    def test_WrongPosition(self):
        test = ['j5', 'a1']
        with raises(ValueError):
            is_under_queen_attack(test[0], test[1])

    def test_WrongType(self):
        test = ['a2', 11]
        with raises(TypeError):
            is_under_queen_attack(test[0], test[1])

    def test_True(self):
        test = ['a2', 'a2']
        result = is_under_queen_attack(test[0], test[1])
        assert True == result

    def test_False(self):
        test = ['b2', 'a4']
        result = is_under_queen_attack(test[0], test[1])
        assert False == result
