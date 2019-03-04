class Vampire:

    coven = []

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

    def __str__(self):
        return ("Vamp is {}, age {}, in coffin {} and drank blood {}".format(self.name, self.age, self.in_coffin, self.drank_blood_today))

    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire

    def drink_blood(self):
        self.drank_blood_today = True
        return self.drank_blood_today

    @classmethod
    def sunrise(cls):
        for num in range(0, len(cls.coven)):
            num_vampire = cls.coven[num]
            if not num_vampire.in_coffin or not num_vampire.drank_blood_today:
                Vampire.coven.remove(num_vampire)
        return Vampire.coven

    @classmethod
    def sunset(cls):
        for num in range(0, len(cls.coven)):
            num_vampire = cls.coven[num]
            num_vampire.drank_blood_today = False
            num_vampire.in_coffin = False

    def go_home(self):
        self.in_coffin = True


v1 = Vampire.create("Lestate", 100, True, True)
print(v1)
v2 = Vampire.create("Queen Akasha", 200, True, True)
v3 = Vampire.create("Armand", 300, False, True)
print(Vampire.coven)
print(len(Vampire.coven))
Vampire.sunrise()
print(len(Vampire.coven))
Vampire.sunset()
print(v1.drank_blood_today)
print(v2.in_coffin)
print(v3.in_coffin)
print(v1.drank_blood_today)
v1.go_home()
print(v1.in_coffin)
