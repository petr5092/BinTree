from bin_tree import *
def test_1():
    lst = BinarySearchTree()
    for i in [10]:
        lst.insert(i)
    lst.delete(10)
    return lst.print_in_order()


def test_2():
    lst = BinarySearchTree()
    for i in [10, 3]:
        lst.insert(i)
    lst.delete(10)
    return lst.print_in_order()

def test_3():
    lst = BinarySearchTree()
    for i in [10, 12]:
        lst.insert(i)
    lst.delete(10)
    return lst.print_in_order()

def test_4():
    lst = BinarySearchTree()
    for i in [10, 5, 12]:
        lst.insert(i)
    lst.delete(10)
    return lst.print_in_order()

def test_5():
    lst = BinarySearchTree()
    for i in [10, 5, 12, 6, 3]:
        lst.insert(i)
    lst.delete(5)
    return lst.print_in_order()

def test_6():
    lst = BinarySearchTree()
    for i in [10, 5, 13, 12, 11]:
        lst.insert(i)
    lst.delete(10)
    return lst.print_in_order()

def test_7():
    lst = BinarySearchTree()
    for i in [10, 5, 13, 12, 11, 2, 1, 3]:
        lst.insert(i)
    lst.delete(10)
    return lst.count_node()


def test_8():
    lst = BinarySearchTree()
    for i in [10, 5, 13, 12, 11, 2]:
        lst.insert(i)
    lst.delete(10)
    return lst.hight_tree()

def test_9():
    lst = BinarySearchTree()
    for i in [10, 5, 13, 12, 11, 2, 1, 3]:
        lst.insert(i)
    lst.delete(3)
    return lst.width_tree()

def test_control():
    print(test_1() == None)
    print(test_2() == [[3, None]])
    print(test_3() == [[12, None]])
    print(test_4() == [[5, 12], [12, None]])
    print(test_5() == [[3, 6], [6, 10], [10, None], [12, 10]])
    print(test_6() == [[5, 11], [11, None], [12, 13], [13, 11]])
    print(test_7() == 7)
    print(test_8() == 3)
    print(test_9() == 2, test_9())

test_control()