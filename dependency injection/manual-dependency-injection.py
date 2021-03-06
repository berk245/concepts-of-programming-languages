# Injecting Dependency Manually

class Config:
    def serve_name(self, username):
        return username
    def serve_day(self, day):
        return day

    #Config object does not have any hardcoded variables and
    # returns only the inputs provided. This makes it highly flexible 
    # and easy to change.    

class Logger:
    def __init__(self,name, day):
        print(f'Hello {name}, what a beautiful {day}')
    
    #Logger does not know where the name and day are coming from.
    #It only worries about printing them. This makes it less prone to 
    #bugs and crashes.


def main():
    print_hello = Logger(
                    name = Config().serve_name(username = 'My Name Here'),
                    day = Config().serve_day(day = 'Sunday')
                    )
    # Before dependency injection, the programmer had to go into the Config object to change the day printed.
    #After, you only need to change the parameter when initalizing the class.
    



if __name__ == '__main__':
    main()