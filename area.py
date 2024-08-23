import math

pi=math.pi
e= 2.71828
gravity = 9.8 #m/s^2

def circle_area(r):
    return pi*r*r;

def exponential_growth(amount, time):
    return amount*(gravity**time);


r= int(input("Enter the radius of circle to get input:"))
initial_amout = int(input("\nEnter the initial amout:"))
time = int(input("\nEnter the time:"))

area=circle_area(r)
print(f"Area of circle with radius {r} is : {area}")

exponent = exponential_growth(initial_amout,time)
print(f"\nThe amount after time {time} with initial amount {initial_amout} is : {exponent}")
