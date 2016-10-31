class Car(object):
    speed = 0
    num_of_wheels = 4
    num_of_wheels = 4

    def __init__(self, name=None, model=None, car_type= 'saloon'):
        self.name = name
        self.model = model
        self.car_type = car_type


        if self.name is None:
            self.name = 'General'

        if self.model is None:           
            self.model = 'GM'

        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            self.num_of_doors=2
        else:
            self.num_of_doors= 4

        if self.car_type == 'trailer':
          self.num_of_wheels = 8
        else:
          self.num_of_wheels = 4


    def is_saloon(self):
        if self.car_type == 'saloon':
            return True
        if self.car_type == 'trailer':
            return False

    def drive(self,pedal):
        if 3 < pedal <= 7:
            self.speed = 77
            return self
        elif 0 < pedal <= 3:
            self.speed = 1000
            return self
        else:
          return self