class People:
    def __init__(self, name, weight, height):
        self.name = name;
        self.weight = weight;
        self.height = height;
    
    def calculateBmi(self):
        result = self.weight / (self.height * self.height);
        return round(result, 2);
