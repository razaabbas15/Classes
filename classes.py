class student:

    def winner(self):
        return f"He is {self.name}. He is descendent of {self.descendent}. His clan is {self.clan}. his age is {self.age} He Has {self.eyes} and Abilities like {self.jutsus}."
    
Madara = student()
Hashirama = student()

Madara.name = "Madara Uchiha"
Madara.descendent = "Indra Otsutsuki"
Madara.clan = "Uchiha"
Madara.eyes = "Eternal mangekyou shariangan and Rinnengan"
Madara.age = 90
Madara.jutsus = ["Fire ball" , "Susano" , "Fire dragon" , "Planetary devastation"]

Hashirama.name = "Hashirama Senju"
Hashirama.descendent = "Asura Otsutsuki"
Hashirama.clan = "Senju"
Hashirama.eyes = "Sage Eyes"
Hashirama.age = 70
Hashirama.jutsus = ["Wood Forest" , "Wood Golem" , "Thousand Hand Slap" , "Sage Mode"]


print(Hashirama.winner())
print(Madara.winner())
