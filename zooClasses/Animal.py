class Animal:
    name = '' #име на животното
    kind = '' #вид на животното
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind

        def eat(self):
            print(f'{self.kind} is eating...')