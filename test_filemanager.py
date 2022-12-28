from account import add_item, increment_acount, decrement_acount
from victory import date_spelling


def test_add_item():
    key1 = 'key1'
    key2 = 'key2'
    value1 = 100
    value2 = 200
    dd = {}
    dd = add_item(dd, key1, value1)
    assert dd.get(key1) == value1, 'Can not add key1 and value into dict : function "add_item()"'
    dd = add_item(dd, key2, value2)
    assert dd.get(key2) == value2, 'Can not add key2 and value into dict : function "add_item()"'
    assert len(list(dd)) == 2, 'Can not add keys into dict : function "add_item()"'


def test_increment_acount():
    assert increment_acount(1, 2) == 3, 'Error in function "increment_acount()"'
    assert increment_acount(10, 10) == 20, 'Error in function "increment_acount()"'
    assert increment_acount(100, 100) == 200, 'Error in function "increment_acount()"'


def test_decrement_acount():
    assert decrement_acount(2, 1) == 1, 'Error in function "decrement_acount()"'
    assert decrement_acount(20, 10) == 10, 'Error in function "decrement_acount()"'
    assert decrement_acount(200, 100) == 100, 'Error in function "decrement_acount()"'


def test_date_spelling():
    assert date_spelling(
        '22.10.1870') == 'двадцатьвторое октября 1870 года', 'Wrong date translation to text : function "date_spelling()"'
    assert date_spelling(
        '10.12.1821') == 'десятое декабря 1821 года', 'Wrong date translation to text : function "date_spelling()"'
    assert date_spelling(
        '23.11.1803') == 'двадцатьтретье ноября 1803 года', 'Wrong date translation to text : function "date_spelling()"'


if __name__ == '__main__':
    pass
    # print(date_spelling('22.10.1870')) # 'двадцатьвторое октября 1870 года'
    # print(date_spelling('10.12.1821')) # 'десятое декабря 1821 года'
    # print(date_spelling('23.11.1803')) # 'двадцатьтретье ноября 1803 года'
