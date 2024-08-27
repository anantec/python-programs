class string_reverser: 
    def __init__(self, input_string) :
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        return ''.join(reversed_words)
    
    
input_string= "hello .py"


reverser= string_reverser(input_string)
output= reverser.reverse_words()
print(output)