from numb3rs import validate

def test_single_ip_digits():
    assert validate("1.1.1.1") == True
    assert validate("9.9.9.9") == True
    assert validate("0.0.0.0") == True
    assert validate("d.d.d.d") == False

def test_invalid_ip():
    assert validate("192.168.0.1") == True
    assert validate("200.256.0.1") == False
    assert validate("275.0.1.25") == False
    assert validate("25.33.11.23") == True
    assert validate("255.255.255.255") == True
    assert validate("256.0.300.1") == False

def no_nondigits():
    assert validate("cat.dog.mouse.food") == False
