def add(number):
    return number+1

def subtract(number):
    return add(number) - 3

def test_stuff():
    assert subtract(3) == 5

# def test_answer():
#     assert piglatin("the man") == "ethay anmay"


# def test_something_that_involves_user_input(monkeypatch):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    # monkeypatch.setitem('builtins.input', lambda x: "Mark")

    # go about using input() like you normally would:
    # i = input("What is your name?")
    # assert i == "Mark"

# def function():
#     x = input("what's your name?")
#     return x + "ay"
#
# def test_function():
#     with mock.patch.object(__builtin__, 'input', lambda: 'some_input'):
#         assert module.function() == 'some_inputay'
