class Employee:
    amt_koef = 1.10
    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay

    def koef_pay(self):
        self.pay *= self.amt_koef

class Developer(Employee):
    amt_koef = 1.04
    def __init__(self, name, surname, pay, lang_prog):
        super().__init__(name, surname, pay)
        self.lang_prog = lang_prog

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay+other.pay
        return None

emp1= Employee('Rozi', 'Rahi', 250000)
dev1 = Developer('Arina', 'Gab', 150000, 'python')
dev1.koef_pay()
print(dev1.pay)
print(dev1.__dict__)
total_pay = dev1+emp1
print(total_pay)
