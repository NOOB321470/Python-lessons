from random import randint
class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f'This potion named and quality: {self.name, self.quality}'
    def get_quality(self):
        return self.quality
    def get_name(self):
        return self.name
    def __add__(self, other):
        a = len(self.name) // 2
        b = len(other.name) // 2
        r = self.name[:a] + other.name[b:]
        r2 = (self.quality + other.quality) // 2
        return Potion(r, r2)
    def __sub__(self, other):
         a2 = len(self.name) // 2
         b2 = len(other.name) // 2
         r3 = self.name[:a2] + other.name[b2:]
         r4 = (self.quality - other.quality) // 2
         return Potion(r3, r4)
    def print_quality(self):
        if self.quality>75:
            print('Potion is very good')
        elif self.quality > 50:
            print('Potion is average')
        else:
            print('Potion has bad quality')
class QualityPotion(Potion):
    def special(self):
        return QualityPotion(self.name, self.quality + 20)
class NotQualityPotion(Potion):
    def special(self):
        return NotQualityPotion(self.name, self.quality - 20)
quality = randint(1, 100)
qPotion = QualityPotion('Veritaserum', quality)

print(qPotion)
Half = Potion('ff', 22)
Half2 = Potion('hh', 32)
Half3 = Half - Half2
print(Half3)
game = True
potions = {}