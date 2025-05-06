from app import even_or_odd, addition, subtract

def test_even():
    assert even_or_odd(2) == "Even"

def test_odd():
    assert even_or_odd(3) == "Odd"

def test_zero():
    assert even_or_odd(0) == "Invalid Input"

def test_negative():
    assert even_or_odd(-1) == "Invalid Input"

def test_add1():
    assert addition(1,2) == 3

def test_add2():
    assert addition(10,20) == 30

def test_add3():
    assert addition(-1,2) == 1

def test_sub1():
    assert subtract(20,2) == 18

def test_sub2():
    assert subtract(20,20) == 0

def test_sub3():
    assert subtract(10,4) == 6