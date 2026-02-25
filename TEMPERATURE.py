#Krish Patel_202501100700087_ECE-B
import random
import time  


def read_temperature():
    return random.randint(0, 100)


def monitor_temperature():

    min_temp = int(input("Enter minimum temperature value: "))
    max_temp = int(input("Enter maximum temperature value: "))
    print("\n")


    if min_temp > max_temp:
        print("Minimum value cannot be greater than maximum value.")
        return

    while True:  
        temperature = read_temperature()
        print("Current temperature:", str(temperature) + "°C")
        
        
        if temperature < min_temp:
            print("Alert: Temperature is too low")
            print("\n")
        elif temperature > max_temp:
            print("Alert: Temperature is too high")
            print("\n")
        else:
            print("Temperature is within acceptable limit")
            print("\n")
        
        print("---------")
        time.sleep(2)  


monitor_temperature()
