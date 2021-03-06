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





