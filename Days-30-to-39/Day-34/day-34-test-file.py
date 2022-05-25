#Type Hints

age: int
name: str
height: float 
is_human: bool

#Can specify data types for inputs

def police_check(age: int):
    if age < 18:
        print("Illegal")
    elif age >= 18:
        print("Legal")

police_check(18)

#Can specify data types for outputs

def score_checker(score: int) -> bool:
    if score > 65:
        passed = True
    else:
        passed = False
    return passed

print(score_checker(66))