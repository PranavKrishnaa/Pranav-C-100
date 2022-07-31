class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")

    def changeGear(self, gear_type):
        print("Gear Changed")

audi = Car("a6","red","audi", 162)
print(audi.start())
