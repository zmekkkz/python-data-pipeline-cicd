import main

def test_transform():
    data = [1, 2, 3]
    result = main.transform(data)
    assert result == [2, 4, 6]
