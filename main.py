def main():
    name = input('Enter your name: ')
    print(f'name = {name}')
    if(name == "hello"):
        print("world!")
    elif(name == "world"):
        print("Error you are banned")

if __name__ == '__main__':
    main()
