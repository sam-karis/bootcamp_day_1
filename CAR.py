class Car(object):
    def __init__(self, name = None, model = None, car_type = None, num_of_doors = None, num_of_wheels = None, speed = None):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        self.speed = 0
        if self.name == None:
            self.name = 'General'

        if self.model == None:
            self.model = 'GM'

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.car_type == None or self.car_type !='trailer':
            self.car_type = 'saloon'
            return self
    def drive(self, pedal):
        self.pedal = pedal
        if self.pedal == 7 and self.car_type =='trailer':
            self.speed = 77
            return self
        elif self.pedal == 3 and self.name == 'Mercedes':
            self.speed = 1000
            return self