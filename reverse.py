def reverse(s):
    string = ""
    for i in s:
        string = i+ string
        # print(i)

    return string
        # print(string)

s = input("Enter the string you want to reverse: \n")
print("The sentence or word you give is :  ")
print(s)
print("\nAfter reversing the word or sentence the result is given below:\n")
print(reverse(s))