class Talaba:
    def __init__(self, ism, fam, yil):
        self.ism = ism
        self.fam = fam
        self.yil = yil
        self.bosqich = 1
    def set_bosqich(self, bosqich):
        self.bosqich = bosqich
    def update_bosqich(self):
        self.bosqich += 1
    def get_info(self):
        return f"{self.ism} {self.fam} {self.bosqich} - bosqich talabasi"

class Fan:
    def __init__(self, nomi):
        self.nome = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]

t_1 = Talaba("Oybek","Mallayev", 1985)
t_2 = Talaba("Jamshid","Olimov", 1923)
t_3 = Talaba("Jalil","Qodirov", 2021)
f = Fan("Matematika")
f.add_student(t_1)
f.add_student(t_2)
f.add_student(t_3)

# print(f.talabalar)
for i in f.get_students():
    print(i)