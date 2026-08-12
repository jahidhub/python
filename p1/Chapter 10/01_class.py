class employee:
    language = "python"
    salary = 500000

    def greet(self):
        print(f"This a a function {self.language} and My salary is {self.salary}")


sohan = employee()
sohan.name = "jahid Hassan"
sohan.language = "javascript"
print(sohan.name, sohan.language, sohan.salary)
sohan.greet()


rohan = employee()
print(f"Rohan programing language is {rohan.language}")
