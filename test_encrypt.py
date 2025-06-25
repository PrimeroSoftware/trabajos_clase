def encrypt(text, shift_value):
    result = ""
    # Traverse the original text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + shift_value-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + shift_value - 97) % 26 + 97)
    return result

def test_encrypt():
    # Test uppercase letters
    assert encrypt("ABC", 1) == "BCD"
    assert encrypt("XYZ", 2) == "ZAB"
    
    # Test lowercase letters
    assert encrypt("abc", 1) == "bcd"
    assert encrypt("xyz", 2) == "zab"
    
    # Test mixed case text
    assert encrypt("Hello", 1) == "Ifmmp"
    assert encrypt("Python", 3) == "Sbwkrq"
    
    # Test with different shift values
    assert encrypt("ABC", 0) == "ABC"
    assert encrypt("ABC", 26) == "ABC"
    assert encrypt("xyz", 25) == "wxy"

def run_tests():
    try:
        test_encrypt()
        print("All tests passed successfully!")
    except AssertionError as e:
        print("Test failed:", str(e))

if __name__ == "__main__":
    run_tests()
