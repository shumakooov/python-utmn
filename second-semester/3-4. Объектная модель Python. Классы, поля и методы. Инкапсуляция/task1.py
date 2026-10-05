# img/2.3-4.1.png

class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hours = 0
        self.salary = 0
        self.rises = 0 
        
        if position == 'Junior':
            self.rate = 10
        elif position == 'Middle':
            self.rate = 15
        elif position == 'Senior':
            self.rate = 20
    
    def work(self, time):
        self.hours += time
        self.salary += self.rate * time
    
    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
            self.rate = 15
        elif self.position == 'Middle':
            self.position = 'Senior'
            self.rate = 20
        elif self.position == 'Senior':
            self.rises += 1
            self.rate = 20 + self.rises
    
    def info(self):
        return f"{self.name} {self.hours}ч. {self.salary}тгр."
