"""Create a class “Programmer” for storing information of few programmers
working at Microsoft."""


class Programmer:
    company = "Microsoft"

    def __init__(self, name, lang, salary):
        self.name = name
        self.language = lang
        self.salary = salary


sohan = Programmer("sohan", "python", 100000)
print(sohan.company, sohan.language, sohan.salary)

rohan  = Programmer("sohan", "python", 100000)
print(rohan.company, rohan.language, rohan.salary)
