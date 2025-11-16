# Variable type hint

age: int = 30


def greeting(name: str) -> str:
    print(f"My name is {name}")

greeting(age)
