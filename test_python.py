import math


def test_filter():
    # pass
    list5 = list(range(5, 11))
    list10 = list(range(1, 11))
    s1 = ['Amber', 'Ashe', 'John', 'Peter', 'Alex', 'Jessica', 'Tim']
    s2 = ['Amber', 'Ashe', 'Peter', 'Alex', 'Jessica']  # with symbol 'e'
    s3 = ['Ashe', 'Jessica']  # with symbol 's'
    assert list(filter(lambda x: x >= 5, list10)) == list5, 'The length of lists is not equal!'
    assert list(filter(lambda x: x == 1, list10))[0] == list10[0], 'The first elements are not equal!'
    assert list(filter(lambda x: 'e' in x, s1)) == s2, 'Check of symbol "e" failed!'
    assert list(filter(lambda x: 's' in x, s1)) == s3, 'Check of symbol "s" failed!'


def test_map():
    # pass
    list1 = list(range(1, 11))
    list2 = list(range(2, 12))
    list3 = list(range(0, 10))
    assert list(map(lambda x: x + 1, list1)) == list2, 'Error with increment in map function!'
    assert list(map(lambda x: x - 1, list1)) == list3, 'Error with decrement in map function!'


def test_sorted():
    # pass
    list1 = list(range(4, 7)) + list(range(7, 11)) + list(range(1, 4))  # mixed list
    list2 = list(range(1, 11))  # ordered list
    list3 = list(range(10, 0, -1))  # ordered and reversed list
    assert sorted(list1) == list2, 'Error in sorted function with order sorting!'
    assert sorted(list1, reverse=True) == list3, 'Error in sorted function with reverse order sorting!'
    assert sorted(list1, key=lambda x: x < 4) == list1, 'Error in sorted function with key option!'


def test_pi():
    # pass
    assert len(str(math.pi)) == 17, 'Length of result should be 17 !'

    try:
        actual_whole = str(math.pi).split('.')[0]
    except:
        actual = ''
    assert actual_whole == '3', 'Whole part is not correct (should be "3")!'

    try:
        actual_fractional = str(math.pi)[2:]
    except:
        actual = ''
    assert actual_fractional == '141592653589793', 'Fractional part is not correct (should be "141592653589793")!'


def test_sqrt():
    # pass
    # print()
    list1 = [1, 4, 9, 16, 25]
    list2 = [1, 2, 3, 4, 5]
    assert list(map(math.sqrt, list1)) == list2, 'Something wrong with sqrt function!'


def test_pow():
    # pass
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 9, 64, 625]
    assert [pow(list1[i], i) for i in range(len(list1))] == list2, 'Something wrong with pow function!'


def test_hypot():
    # pass
    list1 = [10, 2, 4, 13]  # 17.0
    list2 = [4, 7, 8]  # 11.357816691600547
    list3 = [12, 14]  # 18.439088914585774
    # print( str(math.hypot(*list1)) )
    # print( str(math.hypot(*list2)) )
    # print( str(math.hypot(*list3)) )
    assert str(math.hypot(*list1)) == '17.0',               'Something wrong with hypot function!'
    assert str(math.hypot(*list2)) == '11.357816691600547', 'Something wrong with hypot function!'
    assert str(math.hypot(*list3)) == '18.439088914585774', 'Something wrong with hypot function!'


if __name__ == '__main__':
    pass
    # test_hypot()
