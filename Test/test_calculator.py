import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square("fifty")

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("square(2) should be 4")

#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("square(3) should be 9")

#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("square(0) should be 0")

#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("square(-2) should be 4")

#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("square(-3) should be 9")

# if __name__ == "__main__":
#     main()