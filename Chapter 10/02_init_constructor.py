class employee:
    language = "Python"
    salary = 100000

    def __init__(self, name, salary, lang):
        self.name = name
        self.salary = salary
        self.language = lang


sohan = employee("Sohan", 120000, "javascript")
print(sohan.name, sohan.language, sohan.salary)
