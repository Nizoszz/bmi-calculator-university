class ValidatorBmi:
    def __init__(self, bmi, name):
        self.bmi = bmi;
        self.name = name;
    
    def validate(self):
        classifications = {
            16: 'Severe Thinness',
            17: 'Moderate Thinness',
            18.5: 'Mild Thinness',
            25: 'Healthy',
            30: 'Overweight',
            35: 'Obesity Grade I',
            40: 'Obesity Grade II (severe)',
            float('inf'): 'Obesity Grade III (morbid)',
        }

        for limit, classification in sorted(classifications.items()):
            if self.bmi < limit:
                print(f"{self.name}, your BMI is {self.bmi}, classified as: {classification}");
                return self.bmi
        
        print(f"{self.name}, classification not available")
        return;
