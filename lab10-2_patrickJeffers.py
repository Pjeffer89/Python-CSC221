# Patrick Jeffers   Lab 10-2   3/3/2022
# Based on exercise 10-2 in the book. This program imports a car module to use 
# the previously created Car class.  The program creates an instance of car and
# then demonstrates the methods of Car by accelerating and braking while getting
# and displaying the current speed.

# This imports the car module for the program to use.
import car

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    num = 5                                   # Times to speed up and slow down.
    carInstance = car.Car('1990', 'Mazda')              # Creating a Car object.
    for i in range(num):                              # Call accelerate 5 times.
        carInstance.accelerate()
        print(f'Speed: {carInstance.get_speed()}')              # Display speed.
    for i in range(num):                                   # Call brake 5 times.
        carInstance.brake()
        print(f'Speed: {carInstance.get_speed()}')              # Display speed.
        
# Calls main to start program.
if __name__ == '__main__':
    main()