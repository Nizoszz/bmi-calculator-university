from src.validator_bmi import ValidatorBmi;
from src.people import People;
def main():
    person_name = input("Enter your name: ");
    person_weight = float(input("Enter your weight: "));
    person_height = float(input("Enter your height: "));
    people = People(name=person_name, weight=person_weight, height=person_height);
    bmi_classification = ValidatorBmi(people.calculateBmi(), people.name);
    result = bmi_classification.validate();

if __name__ == "__main__":
    main()