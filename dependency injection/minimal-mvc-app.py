class Config():
    def serve_name(self):
        return('Your Name')
    def serve_day(self):
        return('Sunday')
class Logger:
    def __init__(self):
        print(f'Hello {Config().serve_name()}, what a beautiful {Config().serve_day()}')

def main():
    Logger()

# Injecting Dependency Manually

class Config2:
    def serve_name(self, username):
        return username
    def serve_day(self, day):
        return day

    #Config object does not have any hardcoded variables and
    # returns only the inputs provided. This makes it highly flexible 
    # and easy to change.    

class Logger2:
    def __init__(self,name, day):
        print(f'Hello {name}, what a beautiful {day}')
    
    #Logger2 does not know where the name and day are coming from.
    #It only worries about printing them. This makes it less prone to 
    #bugs and crashes.


def manual_di_main():
    print_hello = Logger2(
                    name = Config2().serve_name(username = 'My Name Here'),
                    day = Config2().serve_day(day = 'Sunday')
                    )
    # Before dependency injection, the programmer had to go into the Config object to change the day printed.
    #After, you only need to change the parameter when initalizing the class.
    



# if __name__ == '__main__':
#     manual_di_main()



#DI with Dependency Injector library
import sys
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide


class Config3:
    def __init__(self, username, day):
        self.username = username
        self.day = day
    
    def serve_name(self):
        return self.username
    
    def serve_day(self):
        return self.day
    

        

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    name_and_day_config = providers.Singleton(
        Config3,
        username = config.username,
        day = config.day
    )    

    logger = providers.Factory(
        Logger2,
        name = config.username,
        day = config.day
    )

@inject
def main_with_di_library(logger: Logger2 = Provide[Container.logger]):
    ...

if __name__ == '__main__':
    container = Container()
    container.config.username = 'Your name'
    container.config.day = 'Sunday'
    container.wire(modules=[sys.modules[__name__]])

    main_with_di_library()
