# class Player:
#     demage = 20

#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health

#     def hit(self, obj):
#         obj.health = obj.health - self.demage


# class PlayerOffline(Player):
#     type = "Offline"


# class PlayerOnline(Player):
#     type = "Online"

#     def hit(self, obj):
#         obj.health = obj.health - (2 *self.demage)

#     def regen(self):
#         self.health += 10 if self.health < 200 else 0


# p1 = PlayerOffline('P1', 200)
# p2 = PlayerOnline('P2', 200)


# p1.hit(p2)
# p2.regen()

# print(p2.name, p2.health)
# print(p1.name, p1.health)




# wildan = PlayerOnline('wildan')
# alx = PlayerOnline('Alx')

# print(wildan.name, wildan.health)
# print(alx.name, alx.health)

# wildan.hit(alx)

# print(wildan.name, wildan.health)
# print(alx.name, alx.health)

# data abstraksi
class Alamat:

    def __init__(self, negara, provinsi, kota, kecamatan, kelurahan, jalan=''):
        self.negara = negara
        self.provinsi = provinsi
        self.kota = kota
        self.kecamatan = kecamatan
        self.kelurahan = kelurahan
        self.jalan = jalan

    def to_dict(self):
        return {
            'negara': self.negara,
            'provinsi': self.provinsi,
            'kota': self.kota,
            'kecamatan': self.kecamatan,
            'kelurahan': self.kelurahan,
            'jalan': self.jalan,
        }

alamatt = Alamat(
        'Indo',
        'Jawa Tengah',
        'Tegal',
        'Suka Maju',
        'Sukorejo',
        'Jl. Pendidikan'
    )


print(alamatt.to_dict())
