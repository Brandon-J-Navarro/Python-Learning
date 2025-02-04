# __main__.py
from datetime import datetime

def my_printName_function(user_name) -> None:
    print('Hello', user_name, '!')
    print(user_name,'Python is WEIRD!\n')

def my_printAge_function(user_birthYear) -> None:
    date = datetime.now()
    user_age = date.year - user_birthYear
    print('You are', user_age, 'old!\n')
    for i in range(user_birthYear, date.year + 1):
        print("You have lived through years:", i)

if __name__ == "__main__":
    user_name = input('Enter your name: ')
    my_printName_function(user_name)
    user_birthYear = int(input("Enter you Birth year: "))
    my_printAge_function(user_birthYear)
