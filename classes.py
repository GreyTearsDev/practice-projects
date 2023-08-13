# class User:
#     '''Models a user 
#     Attributes: first_name, last_name, user_name, age, password'''
    
#     def __init__(self, first_name, last_name, user_name, age, password):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.age = age
#         self.password = password
#         self.login_attempts = 0
        
#     def describe_user(self):
#         '''Describe the use'''
#         print('User Description:')
#         print(f'\nFull name: {self.first_name} {self.last_name}')
#         print(f'User name: {self.user_name} \nAge: {self.age}')
#         print(f'Password: {self.password}')
        
#     def greet_user(self):
#         '''Greet user'''
#         print(f'\nWelcome, {self.user_name}')
    
#     def increment_login_attempts(self):
#         '''Increment the amount of login attempts'''
#         self.login_attempts += 1
    
#     def reset_login_attempts(self):
#         '''Reset the login attempts to 0'''
#         self.login_attempts = 0
        
# user_first = User('Grey', 'Tears', 'GreyTearDev', 00000, 'password_is_a_horrible_password' )
# user_first.increment_login_attempts()    
# user_first.increment_login_attempts() 
# user_first.increment_login_attempts() 
# user_first.increment_login_attempts() 
# user_first.increment_login_attempts() 
# print(user_first.login_attempts)
# user_first.reset_login_attempts()
# print(user_first.login_attempts)

          
        
# user001 = User('Marta', 'Correia', 'corMax', 14, '%\babyb00k4')
# user002 = User('Daniel', 'Livulu', 'Dal-i', 15, 'one1p13ce')
# user003 = User('Jardito', 'Samuku', 'B00tie_Samu', 15, 'be4st%_luck')
# user004 = User('Ricardo', 'Madison', 'marDor', 17, 'makimi4348')
# user005 = User('Randy', 'Robertson', 'RaRoBoy', 15, 'matterNo7M1g0')

# user001.describe_user()
# user001.greet_user()
# print('\n',('*' * 18), '\n')

# user002.describe_user()
# user002.greet_user()
# print('\n',('*' * 18), '\n')

# user003.describe_user()
# user003.greet_user()
# print('\n',('*' * 18), '\n')

# user004.describe_user()
# user004.greet_user()
# print('\n',('*' * 18), '\n')

# user005.describe_user()
# user005.greet_user()
# print('\n',('*' * 18), '\n')



# class Restaurant:
#     '''Attempt at modeling a restaurant.
#     Attributes: restaurant_name, cuisine_type.'''
    
#     def __init__(self, restaurant_name, cuisine_type):
#         '''Initialize the attributes.'''
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
        
#     def describe_restaurant(self):
#         '''Give a generic description of the restaurant.'''
#         print(f'"{self.restaurant_name}" specializes in {self.cuisine_type}')
    
#     def open_restaurant(self):
#         '''Announce that the restaurant is open.'''
#         print('We are open!')
    
#     def costumers_served(self):
#         '''Print the amount of served clients.'''
#         print(f'So far, we have served {self.number_served} costumers.')
        
#     def set_number_served(self, number_of_clients):
#         '''Set the number of costumers that have been served.'''
#         self.number_served = number_of_clients
    
#     def increment_number_served(self, increment):
#         '''Increment the number of costumers who've been served'''
#         self.number_served += increment
        
            
# restaurant = Restaurant('O Kazukuta', 'traditional Angolan cuisine')
# restaurant.open_restaurant()
# restaurant.describe_restaurant()
# restaurant.set_number_served(45) 
# restaurant.costumers_served()  
# restaurant.increment_number_served(5)
# restaurant.costumers_served()


class Car:
    '''A simple attempt to represent a car.
    Attributes: make, model, year.'''
    
    def __init__(self, make, model, year):
        '''initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23
        
    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print(f'This car has a {self.odometer_reading} miles on it.')
        
    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')
    
    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles
    
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


class ElectricCar(Car):         
    '''Represent aspects of a car, specific to electric vehicles.'''
    
    def __init__(self, make, model, year):          
        '''Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.'''
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f'This car has a {self.battery_size}-kWh battery.')         
        

my_tesla = ElectricCar('tesla', 'model s', 2019)            
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()