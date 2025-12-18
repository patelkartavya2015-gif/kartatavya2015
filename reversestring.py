class reverseString:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]
try:
    obj = reverseString(str(input("Enter a string to reverse: ")))
    print("Reversed string:", obj.reverse())
except (TypeError, EOFError, KeyboardInterrupt):
    print("An error occurred. Please ensure you enter a valid string.")