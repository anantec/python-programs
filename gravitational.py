G=6.674

def gravitaional_force(m1,m2,dis):
    force= G*(m1*m2)/dis**2

    return force

def main():
    print("Gravitainal calculator\n")

    try:
        a= float(input("Enter the first mass "))
        b= float(input("\nEnter the second mass " ))
        dis= float(input("\nEnter the distance "))

        force = gravitaional_force(a,b,dis)

        print(f'\nthe gravitaional force between the object is {force:.2e}N')




    except ValueError:
        print("invalid input")

    except ZeroDivisionError:
        print("Error! THe distance can not be zero")


main()