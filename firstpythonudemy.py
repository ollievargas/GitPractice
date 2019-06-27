store_address = ["Elm Street", "33", "Texas"]
pins = {"Bob": 1122, "John": 2233, "Joseph": 3344}

print(store_address[0], store_address[1], store_address[2])
pin = int(input("Enter your pin code. "))

def find_in_file(user_car):
    myfile = open("sample.txt")
    cars = myfile.read()
    myfile.close()
    cars = cars.splitlines()

    if user_car in cars:
        return "That vehicle is in the list."
    else:
        return "No such vehicle found!"

if pin in pins.values():
    car = input("Enter vehicle. ")
    print(find_in_file(car))
else:
    print("Incorrect pin!")
    print("This information can only be accessed by: ")
    for key in pins.keys():
        print(key)