def print menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))
def miles_km():
    def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))
def celcius_farienheight():
    C = float (input (' Enter Temp. in celcius:'))
    fairenheight = C * (9/5) + 32
    print 
def fairenheight_celcius():
    F = float (input('Enter Temp. in fairenheight'))
    celcius = 
    print


if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    