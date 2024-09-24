class People:
    def __init__(self, color_eyes):
        self.color_eyes = color_eyes
        self.colvo_ey = 2
    def subscribe(self, who):
        print(f'{self} подписался на {who}')
vasa = People("blue")
petya = People("red")
print(vasa.__dict__)
print(vasa)
vasa.taty = "yes"
print(vasa.__dict__)
vasa.subscribe("Неколай")
