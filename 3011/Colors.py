'''colors'''
a = str(input())
b = str(input())
if a + b =="RedYellow" or a + b =="YellowRed":
    print("Orange")
elif a +b =="RedBlue" or a+ b =="BlueRed":
    print("Violet")
elif a + b =="YellowBlue" or a + b =="BlueYellow":
    print("Green")
elif a and b == "Red" :
    print("Red")
elif a and b == "Yellow" :
    print("Yellow")
elif a and b == "Blue" :
    print("Blue")
else:
    print("Error")
