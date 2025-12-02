"""Auto-generated weapon catalogue for the prototype."""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class WeaponData:
    name: str
    damage: int
    penetration: float
    recoil: float
    fire_rate: float
    magazine_size: int
    reload_time: float
    price: int

CATALOGUE = {}


@dataclass
class Pistol_Mk01:
    damage: int = 25
    penetration: float = 0.31
    recoil: float = 0.119
    fire_rate: float = 4.55
    magazine_size: int = 13
    reload_time: float = 1.79
    price: int = 425

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk01",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk01"] = Pistol_Mk01().to_data()


@dataclass
class SMG_Mk01:
    damage: int = 18
    penetration: float = 0.21
    recoil: float = 0.199
    fire_rate: float = 10.05
    magazine_size: int = 31
    reload_time: float = 2.29
    price: int = 1225

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk01",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk01"] = SMG_Mk01().to_data()


@dataclass
class Rifle_Mk01:
    damage: int = 35
    penetration: float = 0.66
    recoil: float = 0.079
    fire_rate: float = 6.05
    magazine_size: int = 31
    reload_time: float = 2.59
    price: int = 2725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk01",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk01"] = Rifle_Mk01().to_data()


@dataclass
class Sniper_Mk01:
    damage: int = 80
    penetration: float = 0.91
    recoil: float = 0.399
    fire_rate: float = 1.25
    magazine_size: int = 11
    reload_time: float = 3.19
    price: int = 4525

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk01",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk01"] = Sniper_Mk01().to_data()


@dataclass
class Shotgun_Mk01:
    damage: int = 10
    penetration: float = 0.11
    recoil: float = 0.299
    fire_rate: float = 1.05
    magazine_size: int = 9
    reload_time: float = 2.49
    price: int = 1725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk01",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk01"] = Shotgun_Mk01().to_data()


@dataclass
class Pistol_Mk02:
    damage: int = 26
    penetration: float = 0.32
    recoil: float = 0.118
    fire_rate: float = 4.60
    magazine_size: int = 14
    reload_time: float = 1.78
    price: int = 450

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk02",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk02"] = Pistol_Mk02().to_data()


@dataclass
class SMG_Mk02:
    damage: int = 19
    penetration: float = 0.22
    recoil: float = 0.198
    fire_rate: float = 10.10
    magazine_size: int = 32
    reload_time: float = 2.28
    price: int = 1250

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk02",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk02"] = SMG_Mk02().to_data()


@dataclass
class Rifle_Mk02:
    damage: int = 36
    penetration: float = 0.67
    recoil: float = 0.078
    fire_rate: float = 6.10
    magazine_size: int = 32
    reload_time: float = 2.58
    price: int = 2750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk02",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk02"] = Rifle_Mk02().to_data()


@dataclass
class Sniper_Mk02:
    damage: int = 81
    penetration: float = 0.92
    recoil: float = 0.398
    fire_rate: float = 1.30
    magazine_size: int = 12
    reload_time: float = 3.18
    price: int = 4550

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk02",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk02"] = Sniper_Mk02().to_data()


@dataclass
class Shotgun_Mk02:
    damage: int = 11
    penetration: float = 0.12
    recoil: float = 0.298
    fire_rate: float = 1.10
    magazine_size: int = 10
    reload_time: float = 2.48
    price: int = 1750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk02",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk02"] = Shotgun_Mk02().to_data()


@dataclass
class Pistol_Mk03:
    damage: int = 26
    penetration: float = 0.33
    recoil: float = 0.117
    fire_rate: float = 4.65
    magazine_size: int = 15
    reload_time: float = 1.77
    price: int = 475

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk03",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk03"] = Pistol_Mk03().to_data()


@dataclass
class SMG_Mk03:
    damage: int = 19
    penetration: float = 0.23
    recoil: float = 0.197
    fire_rate: float = 10.15
    magazine_size: int = 33
    reload_time: float = 2.27
    price: int = 1275

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk03",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk03"] = SMG_Mk03().to_data()


@dataclass
class Rifle_Mk03:
    damage: int = 36
    penetration: float = 0.68
    recoil: float = 0.077
    fire_rate: float = 6.15
    magazine_size: int = 33
    reload_time: float = 2.57
    price: int = 2775

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk03",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk03"] = Rifle_Mk03().to_data()


@dataclass
class Sniper_Mk03:
    damage: int = 81
    penetration: float = 0.93
    recoil: float = 0.397
    fire_rate: float = 1.35
    magazine_size: int = 13
    reload_time: float = 3.17
    price: int = 4575

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk03",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk03"] = Sniper_Mk03().to_data()


@dataclass
class Shotgun_Mk03:
    damage: int = 11
    penetration: float = 0.13
    recoil: float = 0.297
    fire_rate: float = 1.15
    magazine_size: int = 11
    reload_time: float = 2.47
    price: int = 1775

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk03",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk03"] = Shotgun_Mk03().to_data()


@dataclass
class Pistol_Mk04:
    damage: int = 27
    penetration: float = 0.34
    recoil: float = 0.116
    fire_rate: float = 4.70
    magazine_size: int = 16
    reload_time: float = 1.76
    price: int = 500

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk04",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk04"] = Pistol_Mk04().to_data()


@dataclass
class SMG_Mk04:
    damage: int = 20
    penetration: float = 0.24
    recoil: float = 0.196
    fire_rate: float = 10.20
    magazine_size: int = 34
    reload_time: float = 2.26
    price: int = 1300

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk04",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk04"] = SMG_Mk04().to_data()


@dataclass
class Rifle_Mk04:
    damage: int = 37
    penetration: float = 0.69
    recoil: float = 0.076
    fire_rate: float = 6.20
    magazine_size: int = 34
    reload_time: float = 2.56
    price: int = 2800

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk04",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk04"] = Rifle_Mk04().to_data()


@dataclass
class Sniper_Mk04:
    damage: int = 82
    penetration: float = 0.94
    recoil: float = 0.396
    fire_rate: float = 1.40
    magazine_size: int = 14
    reload_time: float = 3.16
    price: int = 4600

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk04",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk04"] = Sniper_Mk04().to_data()


@dataclass
class Shotgun_Mk04:
    damage: int = 12
    penetration: float = 0.14
    recoil: float = 0.296
    fire_rate: float = 1.20
    magazine_size: int = 12
    reload_time: float = 2.46
    price: int = 1800

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk04",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk04"] = Shotgun_Mk04().to_data()


@dataclass
class Pistol_Mk05:
    damage: int = 27
    penetration: float = 0.35
    recoil: float = 0.115
    fire_rate: float = 4.75
    magazine_size: int = 12
    reload_time: float = 1.75
    price: int = 525

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk05",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk05"] = Pistol_Mk05().to_data()


@dataclass
class SMG_Mk05:
    damage: int = 20
    penetration: float = 0.25
    recoil: float = 0.195
    fire_rate: float = 10.25
    magazine_size: int = 30
    reload_time: float = 2.25
    price: int = 1325

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk05",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk05"] = SMG_Mk05().to_data()


@dataclass
class Rifle_Mk05:
    damage: int = 37
    penetration: float = 0.70
    recoil: float = 0.075
    fire_rate: float = 6.25
    magazine_size: int = 30
    reload_time: float = 2.55
    price: int = 2825

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk05",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk05"] = Rifle_Mk05().to_data()


@dataclass
class Sniper_Mk05:
    damage: int = 82
    penetration: float = 0.95
    recoil: float = 0.395
    fire_rate: float = 1.45
    magazine_size: int = 10
    reload_time: float = 3.15
    price: int = 4625

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk05",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk05"] = Sniper_Mk05().to_data()


@dataclass
class Shotgun_Mk05:
    damage: int = 12
    penetration: float = 0.15
    recoil: float = 0.295
    fire_rate: float = 1.25
    magazine_size: int = 8
    reload_time: float = 2.45
    price: int = 1825

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk05",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk05"] = Shotgun_Mk05().to_data()


@dataclass
class Pistol_Mk06:
    damage: int = 28
    penetration: float = 0.36
    recoil: float = 0.114
    fire_rate: float = 4.80
    magazine_size: int = 13
    reload_time: float = 1.74
    price: int = 550

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk06",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk06"] = Pistol_Mk06().to_data()


@dataclass
class SMG_Mk06:
    damage: int = 21
    penetration: float = 0.26
    recoil: float = 0.194
    fire_rate: float = 10.30
    magazine_size: int = 31
    reload_time: float = 2.24
    price: int = 1350

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk06",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk06"] = SMG_Mk06().to_data()


@dataclass
class Rifle_Mk06:
    damage: int = 38
    penetration: float = 0.71
    recoil: float = 0.074
    fire_rate: float = 6.30
    magazine_size: int = 31
    reload_time: float = 2.54
    price: int = 2850

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk06",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk06"] = Rifle_Mk06().to_data()


@dataclass
class Sniper_Mk06:
    damage: int = 83
    penetration: float = 0.95
    recoil: float = 0.394
    fire_rate: float = 1.50
    magazine_size: int = 11
    reload_time: float = 3.14
    price: int = 4650

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk06",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk06"] = Sniper_Mk06().to_data()


@dataclass
class Shotgun_Mk06:
    damage: int = 13
    penetration: float = 0.16
    recoil: float = 0.294
    fire_rate: float = 1.30
    magazine_size: int = 9
    reload_time: float = 2.44
    price: int = 1850

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk06",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk06"] = Shotgun_Mk06().to_data()


@dataclass
class Pistol_Mk07:
    damage: int = 28
    penetration: float = 0.37
    recoil: float = 0.113
    fire_rate: float = 4.85
    magazine_size: int = 14
    reload_time: float = 1.73
    price: int = 575

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk07",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk07"] = Pistol_Mk07().to_data()


@dataclass
class SMG_Mk07:
    damage: int = 21
    penetration: float = 0.27
    recoil: float = 0.193
    fire_rate: float = 10.35
    magazine_size: int = 32
    reload_time: float = 2.23
    price: int = 1375

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk07",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk07"] = SMG_Mk07().to_data()


@dataclass
class Rifle_Mk07:
    damage: int = 38
    penetration: float = 0.72
    recoil: float = 0.073
    fire_rate: float = 6.35
    magazine_size: int = 32
    reload_time: float = 2.53
    price: int = 2875

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk07",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk07"] = Rifle_Mk07().to_data()


@dataclass
class Sniper_Mk07:
    damage: int = 83
    penetration: float = 0.95
    recoil: float = 0.393
    fire_rate: float = 1.55
    magazine_size: int = 12
    reload_time: float = 3.13
    price: int = 4675

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk07",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk07"] = Sniper_Mk07().to_data()


@dataclass
class Shotgun_Mk07:
    damage: int = 13
    penetration: float = 0.17
    recoil: float = 0.293
    fire_rate: float = 1.35
    magazine_size: int = 10
    reload_time: float = 2.43
    price: int = 1875

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk07",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk07"] = Shotgun_Mk07().to_data()


@dataclass
class Pistol_Mk08:
    damage: int = 29
    penetration: float = 0.38
    recoil: float = 0.112
    fire_rate: float = 4.90
    magazine_size: int = 15
    reload_time: float = 1.72
    price: int = 600

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk08",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk08"] = Pistol_Mk08().to_data()


@dataclass
class SMG_Mk08:
    damage: int = 22
    penetration: float = 0.28
    recoil: float = 0.192
    fire_rate: float = 10.40
    magazine_size: int = 33
    reload_time: float = 2.22
    price: int = 1400

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk08",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk08"] = SMG_Mk08().to_data()


@dataclass
class Rifle_Mk08:
    damage: int = 39
    penetration: float = 0.73
    recoil: float = 0.072
    fire_rate: float = 6.40
    magazine_size: int = 33
    reload_time: float = 2.52
    price: int = 2900

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk08",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk08"] = Rifle_Mk08().to_data()


@dataclass
class Sniper_Mk08:
    damage: int = 84
    penetration: float = 0.95
    recoil: float = 0.392
    fire_rate: float = 1.60
    magazine_size: int = 13
    reload_time: float = 3.12
    price: int = 4700

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk08",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk08"] = Sniper_Mk08().to_data()


@dataclass
class Shotgun_Mk08:
    damage: int = 14
    penetration: float = 0.18
    recoil: float = 0.292
    fire_rate: float = 1.40
    magazine_size: int = 11
    reload_time: float = 2.42
    price: int = 1900

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk08",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk08"] = Shotgun_Mk08().to_data()


@dataclass
class Pistol_Mk09:
    damage: int = 29
    penetration: float = 0.39
    recoil: float = 0.111
    fire_rate: float = 4.95
    magazine_size: int = 16
    reload_time: float = 1.71
    price: int = 625

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk09",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk09"] = Pistol_Mk09().to_data()


@dataclass
class SMG_Mk09:
    damage: int = 22
    penetration: float = 0.29
    recoil: float = 0.191
    fire_rate: float = 10.45
    magazine_size: int = 34
    reload_time: float = 2.21
    price: int = 1425

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk09",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk09"] = SMG_Mk09().to_data()


@dataclass
class Rifle_Mk09:
    damage: int = 39
    penetration: float = 0.74
    recoil: float = 0.071
    fire_rate: float = 6.45
    magazine_size: int = 34
    reload_time: float = 2.51
    price: int = 2925

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk09",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk09"] = Rifle_Mk09().to_data()


@dataclass
class Sniper_Mk09:
    damage: int = 84
    penetration: float = 0.95
    recoil: float = 0.391
    fire_rate: float = 1.65
    magazine_size: int = 14
    reload_time: float = 3.11
    price: int = 4725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk09",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk09"] = Sniper_Mk09().to_data()


@dataclass
class Shotgun_Mk09:
    damage: int = 14
    penetration: float = 0.19
    recoil: float = 0.291
    fire_rate: float = 1.45
    magazine_size: int = 12
    reload_time: float = 2.41
    price: int = 1925

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk09",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk09"] = Shotgun_Mk09().to_data()


@dataclass
class Pistol_Mk10:
    damage: int = 30
    penetration: float = 0.40
    recoil: float = 0.110
    fire_rate: float = 5.00
    magazine_size: int = 12
    reload_time: float = 1.70
    price: int = 650

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk10",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk10"] = Pistol_Mk10().to_data()


@dataclass
class SMG_Mk10:
    damage: int = 23
    penetration: float = 0.30
    recoil: float = 0.190
    fire_rate: float = 10.50
    magazine_size: int = 30
    reload_time: float = 2.20
    price: int = 1450

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk10",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk10"] = SMG_Mk10().to_data()


@dataclass
class Rifle_Mk10:
    damage: int = 40
    penetration: float = 0.75
    recoil: float = 0.070
    fire_rate: float = 6.50
    magazine_size: int = 30
    reload_time: float = 2.50
    price: int = 2950

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk10",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk10"] = Rifle_Mk10().to_data()


@dataclass
class Sniper_Mk10:
    damage: int = 85
    penetration: float = 0.95
    recoil: float = 0.390
    fire_rate: float = 1.70
    magazine_size: int = 10
    reload_time: float = 3.10
    price: int = 4750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk10",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk10"] = Sniper_Mk10().to_data()


@dataclass
class Shotgun_Mk10:
    damage: int = 15
    penetration: float = 0.20
    recoil: float = 0.290
    fire_rate: float = 1.50
    magazine_size: int = 8
    reload_time: float = 2.40
    price: int = 1950

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk10",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk10"] = Shotgun_Mk10().to_data()


@dataclass
class Pistol_Mk11:
    damage: int = 30
    penetration: float = 0.41
    recoil: float = 0.109
    fire_rate: float = 5.05
    magazine_size: int = 13
    reload_time: float = 1.69
    price: int = 675

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk11",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk11"] = Pistol_Mk11().to_data()


@dataclass
class SMG_Mk11:
    damage: int = 23
    penetration: float = 0.31
    recoil: float = 0.189
    fire_rate: float = 10.55
    magazine_size: int = 31
    reload_time: float = 2.19
    price: int = 1475

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk11",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk11"] = SMG_Mk11().to_data()


@dataclass
class Rifle_Mk11:
    damage: int = 40
    penetration: float = 0.76
    recoil: float = 0.069
    fire_rate: float = 6.55
    magazine_size: int = 31
    reload_time: float = 2.49
    price: int = 2975

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk11",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk11"] = Rifle_Mk11().to_data()


@dataclass
class Sniper_Mk11:
    damage: int = 85
    penetration: float = 0.95
    recoil: float = 0.389
    fire_rate: float = 1.75
    magazine_size: int = 11
    reload_time: float = 3.09
    price: int = 4775

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk11",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk11"] = Sniper_Mk11().to_data()


@dataclass
class Shotgun_Mk11:
    damage: int = 15
    penetration: float = 0.21
    recoil: float = 0.289
    fire_rate: float = 1.55
    magazine_size: int = 9
    reload_time: float = 2.39
    price: int = 1975

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk11",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk11"] = Shotgun_Mk11().to_data()


@dataclass
class Pistol_Mk12:
    damage: int = 31
    penetration: float = 0.42
    recoil: float = 0.108
    fire_rate: float = 5.10
    magazine_size: int = 14
    reload_time: float = 1.68
    price: int = 700

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk12",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk12"] = Pistol_Mk12().to_data()


@dataclass
class SMG_Mk12:
    damage: int = 24
    penetration: float = 0.32
    recoil: float = 0.188
    fire_rate: float = 10.60
    magazine_size: int = 32
    reload_time: float = 2.18
    price: int = 1500

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk12",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk12"] = SMG_Mk12().to_data()


@dataclass
class Rifle_Mk12:
    damage: int = 41
    penetration: float = 0.77
    recoil: float = 0.068
    fire_rate: float = 6.60
    magazine_size: int = 32
    reload_time: float = 2.48
    price: int = 3000

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk12",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk12"] = Rifle_Mk12().to_data()


@dataclass
class Sniper_Mk12:
    damage: int = 86
    penetration: float = 0.95
    recoil: float = 0.388
    fire_rate: float = 1.80
    magazine_size: int = 12
    reload_time: float = 3.08
    price: int = 4800

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk12",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk12"] = Sniper_Mk12().to_data()


@dataclass
class Shotgun_Mk12:
    damage: int = 16
    penetration: float = 0.22
    recoil: float = 0.288
    fire_rate: float = 1.60
    magazine_size: int = 10
    reload_time: float = 2.38
    price: int = 2000

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk12",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk12"] = Shotgun_Mk12().to_data()


@dataclass
class Pistol_Mk13:
    damage: int = 31
    penetration: float = 0.43
    recoil: float = 0.107
    fire_rate: float = 5.15
    magazine_size: int = 15
    reload_time: float = 1.67
    price: int = 725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk13",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk13"] = Pistol_Mk13().to_data()


@dataclass
class SMG_Mk13:
    damage: int = 24
    penetration: float = 0.33
    recoil: float = 0.187
    fire_rate: float = 10.65
    magazine_size: int = 33
    reload_time: float = 2.17
    price: int = 1525

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk13",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk13"] = SMG_Mk13().to_data()


@dataclass
class Rifle_Mk13:
    damage: int = 41
    penetration: float = 0.78
    recoil: float = 0.067
    fire_rate: float = 6.65
    magazine_size: int = 33
    reload_time: float = 2.47
    price: int = 3025

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk13",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk13"] = Rifle_Mk13().to_data()


@dataclass
class Sniper_Mk13:
    damage: int = 86
    penetration: float = 0.95
    recoil: float = 0.387
    fire_rate: float = 1.85
    magazine_size: int = 13
    reload_time: float = 3.07
    price: int = 4825

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk13",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk13"] = Sniper_Mk13().to_data()


@dataclass
class Shotgun_Mk13:
    damage: int = 16
    penetration: float = 0.23
    recoil: float = 0.287
    fire_rate: float = 1.65
    magazine_size: int = 11
    reload_time: float = 2.37
    price: int = 2025

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk13",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk13"] = Shotgun_Mk13().to_data()


@dataclass
class Pistol_Mk14:
    damage: int = 32
    penetration: float = 0.44
    recoil: float = 0.106
    fire_rate: float = 5.20
    magazine_size: int = 16
    reload_time: float = 1.66
    price: int = 750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk14",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk14"] = Pistol_Mk14().to_data()


@dataclass
class SMG_Mk14:
    damage: int = 25
    penetration: float = 0.34
    recoil: float = 0.186
    fire_rate: float = 10.70
    magazine_size: int = 34
    reload_time: float = 2.16
    price: int = 1550

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk14",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk14"] = SMG_Mk14().to_data()


@dataclass
class Rifle_Mk14:
    damage: int = 42
    penetration: float = 0.79
    recoil: float = 0.066
    fire_rate: float = 6.70
    magazine_size: int = 34
    reload_time: float = 2.46
    price: int = 3050

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk14",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk14"] = Rifle_Mk14().to_data()


@dataclass
class Sniper_Mk14:
    damage: int = 87
    penetration: float = 0.95
    recoil: float = 0.386
    fire_rate: float = 1.90
    magazine_size: int = 14
    reload_time: float = 3.06
    price: int = 4850

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk14",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk14"] = Sniper_Mk14().to_data()


@dataclass
class Shotgun_Mk14:
    damage: int = 17
    penetration: float = 0.24
    recoil: float = 0.286
    fire_rate: float = 1.70
    magazine_size: int = 12
    reload_time: float = 2.36
    price: int = 2050

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk14",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk14"] = Shotgun_Mk14().to_data()


@dataclass
class Pistol_Mk15:
    damage: int = 32
    penetration: float = 0.45
    recoil: float = 0.105
    fire_rate: float = 5.25
    magazine_size: int = 12
    reload_time: float = 1.65
    price: int = 775

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk15",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk15"] = Pistol_Mk15().to_data()


@dataclass
class SMG_Mk15:
    damage: int = 25
    penetration: float = 0.35
    recoil: float = 0.185
    fire_rate: float = 10.75
    magazine_size: int = 30
    reload_time: float = 2.15
    price: int = 1575

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk15",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk15"] = SMG_Mk15().to_data()


@dataclass
class Rifle_Mk15:
    damage: int = 42
    penetration: float = 0.80
    recoil: float = 0.065
    fire_rate: float = 6.75
    magazine_size: int = 30
    reload_time: float = 2.45
    price: int = 3075

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk15",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk15"] = Rifle_Mk15().to_data()


@dataclass
class Sniper_Mk15:
    damage: int = 87
    penetration: float = 0.95
    recoil: float = 0.385
    fire_rate: float = 1.95
    magazine_size: int = 10
    reload_time: float = 3.05
    price: int = 4875

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk15",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk15"] = Sniper_Mk15().to_data()


@dataclass
class Shotgun_Mk15:
    damage: int = 17
    penetration: float = 0.25
    recoil: float = 0.285
    fire_rate: float = 1.75
    magazine_size: int = 8
    reload_time: float = 2.35
    price: int = 2075

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk15",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk15"] = Shotgun_Mk15().to_data()


@dataclass
class Pistol_Mk16:
    damage: int = 33
    penetration: float = 0.46
    recoil: float = 0.104
    fire_rate: float = 5.30
    magazine_size: int = 13
    reload_time: float = 1.64
    price: int = 800

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk16",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk16"] = Pistol_Mk16().to_data()


@dataclass
class SMG_Mk16:
    damage: int = 26
    penetration: float = 0.36
    recoil: float = 0.184
    fire_rate: float = 10.80
    magazine_size: int = 31
    reload_time: float = 2.14
    price: int = 1600

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk16",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk16"] = SMG_Mk16().to_data()


@dataclass
class Rifle_Mk16:
    damage: int = 43
    penetration: float = 0.81
    recoil: float = 0.064
    fire_rate: float = 6.80
    magazine_size: int = 31
    reload_time: float = 2.44
    price: int = 3100

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk16",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk16"] = Rifle_Mk16().to_data()


@dataclass
class Sniper_Mk16:
    damage: int = 88
    penetration: float = 0.95
    recoil: float = 0.384
    fire_rate: float = 2.00
    magazine_size: int = 11
    reload_time: float = 3.04
    price: int = 4900

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk16",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk16"] = Sniper_Mk16().to_data()


@dataclass
class Shotgun_Mk16:
    damage: int = 18
    penetration: float = 0.26
    recoil: float = 0.284
    fire_rate: float = 1.80
    magazine_size: int = 9
    reload_time: float = 2.34
    price: int = 2100

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk16",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk16"] = Shotgun_Mk16().to_data()


@dataclass
class Pistol_Mk17:
    damage: int = 33
    penetration: float = 0.47
    recoil: float = 0.103
    fire_rate: float = 5.35
    magazine_size: int = 14
    reload_time: float = 1.63
    price: int = 825

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk17",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk17"] = Pistol_Mk17().to_data()


@dataclass
class SMG_Mk17:
    damage: int = 26
    penetration: float = 0.37
    recoil: float = 0.183
    fire_rate: float = 10.85
    magazine_size: int = 32
    reload_time: float = 2.13
    price: int = 1625

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk17",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk17"] = SMG_Mk17().to_data()


@dataclass
class Rifle_Mk17:
    damage: int = 43
    penetration: float = 0.82
    recoil: float = 0.063
    fire_rate: float = 6.85
    magazine_size: int = 32
    reload_time: float = 2.43
    price: int = 3125

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk17",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk17"] = Rifle_Mk17().to_data()


@dataclass
class Sniper_Mk17:
    damage: int = 88
    penetration: float = 0.95
    recoil: float = 0.383
    fire_rate: float = 2.05
    magazine_size: int = 12
    reload_time: float = 3.03
    price: int = 4925

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk17",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk17"] = Sniper_Mk17().to_data()


@dataclass
class Shotgun_Mk17:
    damage: int = 18
    penetration: float = 0.27
    recoil: float = 0.283
    fire_rate: float = 1.85
    magazine_size: int = 10
    reload_time: float = 2.33
    price: int = 2125

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk17",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk17"] = Shotgun_Mk17().to_data()


@dataclass
class Pistol_Mk18:
    damage: int = 34
    penetration: float = 0.48
    recoil: float = 0.102
    fire_rate: float = 5.40
    magazine_size: int = 15
    reload_time: float = 1.62
    price: int = 850

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk18",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk18"] = Pistol_Mk18().to_data()


@dataclass
class SMG_Mk18:
    damage: int = 27
    penetration: float = 0.38
    recoil: float = 0.182
    fire_rate: float = 10.90
    magazine_size: int = 33
    reload_time: float = 2.12
    price: int = 1650

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk18",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk18"] = SMG_Mk18().to_data()


@dataclass
class Rifle_Mk18:
    damage: int = 44
    penetration: float = 0.83
    recoil: float = 0.062
    fire_rate: float = 6.90
    magazine_size: int = 33
    reload_time: float = 2.42
    price: int = 3150

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk18",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk18"] = Rifle_Mk18().to_data()


@dataclass
class Sniper_Mk18:
    damage: int = 89
    penetration: float = 0.95
    recoil: float = 0.382
    fire_rate: float = 2.10
    magazine_size: int = 13
    reload_time: float = 3.02
    price: int = 4950

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk18",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk18"] = Sniper_Mk18().to_data()


@dataclass
class Shotgun_Mk18:
    damage: int = 19
    penetration: float = 0.28
    recoil: float = 0.282
    fire_rate: float = 1.90
    magazine_size: int = 11
    reload_time: float = 2.32
    price: int = 2150

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk18",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk18"] = Shotgun_Mk18().to_data()


@dataclass
class Pistol_Mk19:
    damage: int = 34
    penetration: float = 0.49
    recoil: float = 0.101
    fire_rate: float = 5.45
    magazine_size: int = 16
    reload_time: float = 1.61
    price: int = 875

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk19",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk19"] = Pistol_Mk19().to_data()


@dataclass
class SMG_Mk19:
    damage: int = 27
    penetration: float = 0.39
    recoil: float = 0.181
    fire_rate: float = 10.95
    magazine_size: int = 34
    reload_time: float = 2.11
    price: int = 1675

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk19",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk19"] = SMG_Mk19().to_data()


@dataclass
class Rifle_Mk19:
    damage: int = 44
    penetration: float = 0.84
    recoil: float = 0.061
    fire_rate: float = 6.95
    magazine_size: int = 34
    reload_time: float = 2.41
    price: int = 3175

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk19",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk19"] = Rifle_Mk19().to_data()


@dataclass
class Sniper_Mk19:
    damage: int = 89
    penetration: float = 0.95
    recoil: float = 0.381
    fire_rate: float = 2.15
    magazine_size: int = 14
    reload_time: float = 3.01
    price: int = 4975

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk19",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk19"] = Sniper_Mk19().to_data()


@dataclass
class Shotgun_Mk19:
    damage: int = 19
    penetration: float = 0.29
    recoil: float = 0.281
    fire_rate: float = 1.95
    magazine_size: int = 12
    reload_time: float = 2.31
    price: int = 2175

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk19",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk19"] = Shotgun_Mk19().to_data()


@dataclass
class Pistol_Mk20:
    damage: int = 35
    penetration: float = 0.50
    recoil: float = 0.100
    fire_rate: float = 5.50
    magazine_size: int = 12
    reload_time: float = 1.60
    price: int = 900

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk20",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk20"] = Pistol_Mk20().to_data()


@dataclass
class SMG_Mk20:
    damage: int = 28
    penetration: float = 0.40
    recoil: float = 0.180
    fire_rate: float = 11.00
    magazine_size: int = 30
    reload_time: float = 2.10
    price: int = 1700

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk20",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk20"] = SMG_Mk20().to_data()


@dataclass
class Rifle_Mk20:
    damage: int = 45
    penetration: float = 0.85
    recoil: float = 0.060
    fire_rate: float = 7.00
    magazine_size: int = 30
    reload_time: float = 2.40
    price: int = 3200

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk20",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk20"] = Rifle_Mk20().to_data()


@dataclass
class Sniper_Mk20:
    damage: int = 90
    penetration: float = 0.95
    recoil: float = 0.380
    fire_rate: float = 2.20
    magazine_size: int = 10
    reload_time: float = 3.00
    price: int = 5000

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk20",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk20"] = Sniper_Mk20().to_data()


@dataclass
class Shotgun_Mk20:
    damage: int = 20
    penetration: float = 0.30
    recoil: float = 0.280
    fire_rate: float = 2.00
    magazine_size: int = 8
    reload_time: float = 2.30
    price: int = 2200

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk20",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk20"] = Shotgun_Mk20().to_data()


@dataclass
class Pistol_Mk21:
    damage: int = 35
    penetration: float = 0.51
    recoil: float = 0.099
    fire_rate: float = 5.55
    magazine_size: int = 13
    reload_time: float = 1.59
    price: int = 925

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk21",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk21"] = Pistol_Mk21().to_data()


@dataclass
class SMG_Mk21:
    damage: int = 28
    penetration: float = 0.41
    recoil: float = 0.179
    fire_rate: float = 11.05
    magazine_size: int = 31
    reload_time: float = 2.09
    price: int = 1725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk21",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk21"] = SMG_Mk21().to_data()


@dataclass
class Rifle_Mk21:
    damage: int = 45
    penetration: float = 0.86
    recoil: float = 0.059
    fire_rate: float = 7.05
    magazine_size: int = 31
    reload_time: float = 2.39
    price: int = 3225

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk21",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk21"] = Rifle_Mk21().to_data()


@dataclass
class Sniper_Mk21:
    damage: int = 90
    penetration: float = 0.95
    recoil: float = 0.379
    fire_rate: float = 2.25
    magazine_size: int = 11
    reload_time: float = 2.99
    price: int = 5025

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk21",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk21"] = Sniper_Mk21().to_data()


@dataclass
class Shotgun_Mk21:
    damage: int = 20
    penetration: float = 0.31
    recoil: float = 0.279
    fire_rate: float = 2.05
    magazine_size: int = 9
    reload_time: float = 2.29
    price: int = 2225

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk21",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk21"] = Shotgun_Mk21().to_data()


@dataclass
class Pistol_Mk22:
    damage: int = 36
    penetration: float = 0.52
    recoil: float = 0.098
    fire_rate: float = 5.60
    magazine_size: int = 14
    reload_time: float = 1.58
    price: int = 950

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk22",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk22"] = Pistol_Mk22().to_data()


@dataclass
class SMG_Mk22:
    damage: int = 29
    penetration: float = 0.42
    recoil: float = 0.178
    fire_rate: float = 11.10
    magazine_size: int = 32
    reload_time: float = 2.08
    price: int = 1750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk22",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk22"] = SMG_Mk22().to_data()


@dataclass
class Rifle_Mk22:
    damage: int = 46
    penetration: float = 0.87
    recoil: float = 0.058
    fire_rate: float = 7.10
    magazine_size: int = 32
    reload_time: float = 2.38
    price: int = 3250

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk22",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk22"] = Rifle_Mk22().to_data()


@dataclass
class Sniper_Mk22:
    damage: int = 91
    penetration: float = 0.95
    recoil: float = 0.378
    fire_rate: float = 2.30
    magazine_size: int = 12
    reload_time: float = 2.98
    price: int = 5050

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk22",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk22"] = Sniper_Mk22().to_data()


@dataclass
class Shotgun_Mk22:
    damage: int = 21
    penetration: float = 0.32
    recoil: float = 0.278
    fire_rate: float = 2.10
    magazine_size: int = 10
    reload_time: float = 2.28
    price: int = 2250

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk22",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk22"] = Shotgun_Mk22().to_data()


@dataclass
class Pistol_Mk23:
    damage: int = 36
    penetration: float = 0.53
    recoil: float = 0.097
    fire_rate: float = 5.65
    magazine_size: int = 15
    reload_time: float = 1.57
    price: int = 975

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk23",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk23"] = Pistol_Mk23().to_data()


@dataclass
class SMG_Mk23:
    damage: int = 29
    penetration: float = 0.43
    recoil: float = 0.177
    fire_rate: float = 11.15
    magazine_size: int = 33
    reload_time: float = 2.07
    price: int = 1775

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk23",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk23"] = SMG_Mk23().to_data()


@dataclass
class Rifle_Mk23:
    damage: int = 46
    penetration: float = 0.88
    recoil: float = 0.057
    fire_rate: float = 7.15
    magazine_size: int = 33
    reload_time: float = 2.37
    price: int = 3275

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk23",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk23"] = Rifle_Mk23().to_data()


@dataclass
class Sniper_Mk23:
    damage: int = 91
    penetration: float = 0.95
    recoil: float = 0.377
    fire_rate: float = 2.35
    magazine_size: int = 13
    reload_time: float = 2.97
    price: int = 5075

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk23",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk23"] = Sniper_Mk23().to_data()


@dataclass
class Shotgun_Mk23:
    damage: int = 21
    penetration: float = 0.33
    recoil: float = 0.277
    fire_rate: float = 2.15
    magazine_size: int = 11
    reload_time: float = 2.27
    price: int = 2275

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk23",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk23"] = Shotgun_Mk23().to_data()


@dataclass
class Pistol_Mk24:
    damage: int = 37
    penetration: float = 0.54
    recoil: float = 0.096
    fire_rate: float = 5.70
    magazine_size: int = 16
    reload_time: float = 1.56
    price: int = 1000

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk24",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk24"] = Pistol_Mk24().to_data()


@dataclass
class SMG_Mk24:
    damage: int = 30
    penetration: float = 0.44
    recoil: float = 0.176
    fire_rate: float = 11.20
    magazine_size: int = 34
    reload_time: float = 2.06
    price: int = 1800

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk24",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk24"] = SMG_Mk24().to_data()


@dataclass
class Rifle_Mk24:
    damage: int = 47
    penetration: float = 0.89
    recoil: float = 0.056
    fire_rate: float = 7.20
    magazine_size: int = 34
    reload_time: float = 2.36
    price: int = 3300

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk24",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk24"] = Rifle_Mk24().to_data()


@dataclass
class Sniper_Mk24:
    damage: int = 92
    penetration: float = 0.95
    recoil: float = 0.376
    fire_rate: float = 2.40
    magazine_size: int = 14
    reload_time: float = 2.96
    price: int = 5100

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk24",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk24"] = Sniper_Mk24().to_data()


@dataclass
class Shotgun_Mk24:
    damage: int = 22
    penetration: float = 0.34
    recoil: float = 0.276
    fire_rate: float = 2.20
    magazine_size: int = 12
    reload_time: float = 2.26
    price: int = 2300

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk24",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk24"] = Shotgun_Mk24().to_data()


@dataclass
class Pistol_Mk25:
    damage: int = 37
    penetration: float = 0.55
    recoil: float = 0.095
    fire_rate: float = 5.75
    magazine_size: int = 12
    reload_time: float = 1.55
    price: int = 1025

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk25",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk25"] = Pistol_Mk25().to_data()


@dataclass
class SMG_Mk25:
    damage: int = 30
    penetration: float = 0.45
    recoil: float = 0.175
    fire_rate: float = 11.25
    magazine_size: int = 30
    reload_time: float = 2.05
    price: int = 1825

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk25",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk25"] = SMG_Mk25().to_data()


@dataclass
class Rifle_Mk25:
    damage: int = 47
    penetration: float = 0.90
    recoil: float = 0.055
    fire_rate: float = 7.25
    magazine_size: int = 30
    reload_time: float = 2.35
    price: int = 3325

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk25",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk25"] = Rifle_Mk25().to_data()


@dataclass
class Sniper_Mk25:
    damage: int = 92
    penetration: float = 0.95
    recoil: float = 0.375
    fire_rate: float = 2.45
    magazine_size: int = 10
    reload_time: float = 2.95
    price: int = 5125

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk25",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk25"] = Sniper_Mk25().to_data()


@dataclass
class Shotgun_Mk25:
    damage: int = 22
    penetration: float = 0.35
    recoil: float = 0.275
    fire_rate: float = 2.25
    magazine_size: int = 8
    reload_time: float = 2.25
    price: int = 2325

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk25",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk25"] = Shotgun_Mk25().to_data()


@dataclass
class Pistol_Mk26:
    damage: int = 38
    penetration: float = 0.56
    recoil: float = 0.094
    fire_rate: float = 5.80
    magazine_size: int = 13
    reload_time: float = 1.54
    price: int = 1050

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk26",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk26"] = Pistol_Mk26().to_data()


@dataclass
class SMG_Mk26:
    damage: int = 31
    penetration: float = 0.46
    recoil: float = 0.174
    fire_rate: float = 11.30
    magazine_size: int = 31
    reload_time: float = 2.04
    price: int = 1850

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk26",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk26"] = SMG_Mk26().to_data()


@dataclass
class Rifle_Mk26:
    damage: int = 48
    penetration: float = 0.91
    recoil: float = 0.054
    fire_rate: float = 7.30
    magazine_size: int = 31
    reload_time: float = 2.34
    price: int = 3350

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk26",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk26"] = Rifle_Mk26().to_data()


@dataclass
class Sniper_Mk26:
    damage: int = 93
    penetration: float = 0.95
    recoil: float = 0.374
    fire_rate: float = 2.50
    magazine_size: int = 11
    reload_time: float = 2.94
    price: int = 5150

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk26",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk26"] = Sniper_Mk26().to_data()


@dataclass
class Shotgun_Mk26:
    damage: int = 23
    penetration: float = 0.36
    recoil: float = 0.274
    fire_rate: float = 2.30
    magazine_size: int = 9
    reload_time: float = 2.24
    price: int = 2350

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk26",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk26"] = Shotgun_Mk26().to_data()


@dataclass
class Pistol_Mk27:
    damage: int = 38
    penetration: float = 0.57
    recoil: float = 0.093
    fire_rate: float = 5.85
    magazine_size: int = 14
    reload_time: float = 1.53
    price: int = 1075

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk27",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk27"] = Pistol_Mk27().to_data()


@dataclass
class SMG_Mk27:
    damage: int = 31
    penetration: float = 0.47
    recoil: float = 0.173
    fire_rate: float = 11.35
    magazine_size: int = 32
    reload_time: float = 2.03
    price: int = 1875

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk27",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk27"] = SMG_Mk27().to_data()


@dataclass
class Rifle_Mk27:
    damage: int = 48
    penetration: float = 0.92
    recoil: float = 0.053
    fire_rate: float = 7.35
    magazine_size: int = 32
    reload_time: float = 2.33
    price: int = 3375

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk27",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk27"] = Rifle_Mk27().to_data()


@dataclass
class Sniper_Mk27:
    damage: int = 93
    penetration: float = 0.95
    recoil: float = 0.373
    fire_rate: float = 2.55
    magazine_size: int = 12
    reload_time: float = 2.93
    price: int = 5175

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk27",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk27"] = Sniper_Mk27().to_data()


@dataclass
class Shotgun_Mk27:
    damage: int = 23
    penetration: float = 0.37
    recoil: float = 0.273
    fire_rate: float = 2.35
    magazine_size: int = 10
    reload_time: float = 2.23
    price: int = 2375

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk27",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk27"] = Shotgun_Mk27().to_data()


@dataclass
class Pistol_Mk28:
    damage: int = 39
    penetration: float = 0.58
    recoil: float = 0.092
    fire_rate: float = 5.90
    magazine_size: int = 15
    reload_time: float = 1.52
    price: int = 1100

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk28",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk28"] = Pistol_Mk28().to_data()


@dataclass
class SMG_Mk28:
    damage: int = 32
    penetration: float = 0.48
    recoil: float = 0.172
    fire_rate: float = 11.40
    magazine_size: int = 33
    reload_time: float = 2.02
    price: int = 1900

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk28",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk28"] = SMG_Mk28().to_data()


@dataclass
class Rifle_Mk28:
    damage: int = 49
    penetration: float = 0.93
    recoil: float = 0.052
    fire_rate: float = 7.40
    magazine_size: int = 33
    reload_time: float = 2.32
    price: int = 3400

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk28",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk28"] = Rifle_Mk28().to_data()


@dataclass
class Sniper_Mk28:
    damage: int = 94
    penetration: float = 0.95
    recoil: float = 0.372
    fire_rate: float = 2.60
    magazine_size: int = 13
    reload_time: float = 2.92
    price: int = 5200

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk28",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk28"] = Sniper_Mk28().to_data()


@dataclass
class Shotgun_Mk28:
    damage: int = 24
    penetration: float = 0.38
    recoil: float = 0.272
    fire_rate: float = 2.40
    magazine_size: int = 11
    reload_time: float = 2.22
    price: int = 2400

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk28",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk28"] = Shotgun_Mk28().to_data()


@dataclass
class Pistol_Mk29:
    damage: int = 39
    penetration: float = 0.59
    recoil: float = 0.091
    fire_rate: float = 5.95
    magazine_size: int = 16
    reload_time: float = 1.51
    price: int = 1125

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk29",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk29"] = Pistol_Mk29().to_data()


@dataclass
class SMG_Mk29:
    damage: int = 32
    penetration: float = 0.49
    recoil: float = 0.171
    fire_rate: float = 11.45
    magazine_size: int = 34
    reload_time: float = 2.01
    price: int = 1925

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk29",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk29"] = SMG_Mk29().to_data()


@dataclass
class Rifle_Mk29:
    damage: int = 49
    penetration: float = 0.94
    recoil: float = 0.051
    fire_rate: float = 7.45
    magazine_size: int = 34
    reload_time: float = 2.31
    price: int = 3425

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk29",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk29"] = Rifle_Mk29().to_data()


@dataclass
class Sniper_Mk29:
    damage: int = 94
    penetration: float = 0.95
    recoil: float = 0.371
    fire_rate: float = 2.65
    magazine_size: int = 14
    reload_time: float = 2.91
    price: int = 5225

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk29",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk29"] = Sniper_Mk29().to_data()


@dataclass
class Shotgun_Mk29:
    damage: int = 24
    penetration: float = 0.39
    recoil: float = 0.271
    fire_rate: float = 2.45
    magazine_size: int = 12
    reload_time: float = 2.21
    price: int = 2425

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk29",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk29"] = Shotgun_Mk29().to_data()


@dataclass
class Pistol_Mk30:
    damage: int = 40
    penetration: float = 0.60
    recoil: float = 0.090
    fire_rate: float = 6.00
    magazine_size: int = 12
    reload_time: float = 1.50
    price: int = 1150

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk30",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk30"] = Pistol_Mk30().to_data()


@dataclass
class SMG_Mk30:
    damage: int = 33
    penetration: float = 0.50
    recoil: float = 0.170
    fire_rate: float = 11.50
    magazine_size: int = 30
    reload_time: float = 2.00
    price: int = 1950

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk30",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk30"] = SMG_Mk30().to_data()


@dataclass
class Rifle_Mk30:
    damage: int = 50
    penetration: float = 0.95
    recoil: float = 0.050
    fire_rate: float = 7.50
    magazine_size: int = 30
    reload_time: float = 2.30
    price: int = 3450

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk30",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk30"] = Rifle_Mk30().to_data()


@dataclass
class Sniper_Mk30:
    damage: int = 95
    penetration: float = 0.95
    recoil: float = 0.370
    fire_rate: float = 2.70
    magazine_size: int = 10
    reload_time: float = 2.90
    price: int = 5250

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk30",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk30"] = Sniper_Mk30().to_data()


@dataclass
class Shotgun_Mk30:
    damage: int = 25
    penetration: float = 0.40
    recoil: float = 0.270
    fire_rate: float = 2.50
    magazine_size: int = 8
    reload_time: float = 2.20
    price: int = 2450

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk30",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk30"] = Shotgun_Mk30().to_data()


@dataclass
class Pistol_Mk31:
    damage: int = 40
    penetration: float = 0.61
    recoil: float = 0.089
    fire_rate: float = 6.05
    magazine_size: int = 13
    reload_time: float = 1.49
    price: int = 1175

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk31",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk31"] = Pistol_Mk31().to_data()


@dataclass
class SMG_Mk31:
    damage: int = 33
    penetration: float = 0.51
    recoil: float = 0.169
    fire_rate: float = 11.55
    magazine_size: int = 31
    reload_time: float = 1.99
    price: int = 1975

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk31",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk31"] = SMG_Mk31().to_data()


@dataclass
class Rifle_Mk31:
    damage: int = 50
    penetration: float = 0.95
    recoil: float = 0.049
    fire_rate: float = 7.55
    magazine_size: int = 31
    reload_time: float = 2.29
    price: int = 3475

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk31",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk31"] = Rifle_Mk31().to_data()


@dataclass
class Sniper_Mk31:
    damage: int = 95
    penetration: float = 0.95
    recoil: float = 0.369
    fire_rate: float = 2.75
    magazine_size: int = 11
    reload_time: float = 2.89
    price: int = 5275

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk31",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk31"] = Sniper_Mk31().to_data()


@dataclass
class Shotgun_Mk31:
    damage: int = 25
    penetration: float = 0.41
    recoil: float = 0.269
    fire_rate: float = 2.55
    magazine_size: int = 9
    reload_time: float = 2.19
    price: int = 2475

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk31",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk31"] = Shotgun_Mk31().to_data()


@dataclass
class Pistol_Mk32:
    damage: int = 41
    penetration: float = 0.62
    recoil: float = 0.088
    fire_rate: float = 6.10
    magazine_size: int = 14
    reload_time: float = 1.48
    price: int = 1200

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk32",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk32"] = Pistol_Mk32().to_data()


@dataclass
class SMG_Mk32:
    damage: int = 34
    penetration: float = 0.52
    recoil: float = 0.168
    fire_rate: float = 11.60
    magazine_size: int = 32
    reload_time: float = 1.98
    price: int = 2000

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk32",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk32"] = SMG_Mk32().to_data()


@dataclass
class Rifle_Mk32:
    damage: int = 51
    penetration: float = 0.95
    recoil: float = 0.048
    fire_rate: float = 7.60
    magazine_size: int = 32
    reload_time: float = 2.28
    price: int = 3500

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk32",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk32"] = Rifle_Mk32().to_data()


@dataclass
class Sniper_Mk32:
    damage: int = 96
    penetration: float = 0.95
    recoil: float = 0.368
    fire_rate: float = 2.80
    magazine_size: int = 12
    reload_time: float = 2.88
    price: int = 5300

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk32",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk32"] = Sniper_Mk32().to_data()


@dataclass
class Shotgun_Mk32:
    damage: int = 26
    penetration: float = 0.42
    recoil: float = 0.268
    fire_rate: float = 2.60
    magazine_size: int = 10
    reload_time: float = 2.18
    price: int = 2500

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk32",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk32"] = Shotgun_Mk32().to_data()


@dataclass
class Pistol_Mk33:
    damage: int = 41
    penetration: float = 0.63
    recoil: float = 0.087
    fire_rate: float = 6.15
    magazine_size: int = 15
    reload_time: float = 1.47
    price: int = 1225

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk33",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk33"] = Pistol_Mk33().to_data()


@dataclass
class SMG_Mk33:
    damage: int = 34
    penetration: float = 0.53
    recoil: float = 0.167
    fire_rate: float = 11.65
    magazine_size: int = 33
    reload_time: float = 1.97
    price: int = 2025

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk33",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk33"] = SMG_Mk33().to_data()


@dataclass
class Rifle_Mk33:
    damage: int = 51
    penetration: float = 0.95
    recoil: float = 0.047
    fire_rate: float = 7.65
    magazine_size: int = 33
    reload_time: float = 2.27
    price: int = 3525

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk33",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk33"] = Rifle_Mk33().to_data()


@dataclass
class Sniper_Mk33:
    damage: int = 96
    penetration: float = 0.95
    recoil: float = 0.367
    fire_rate: float = 2.85
    magazine_size: int = 13
    reload_time: float = 2.87
    price: int = 5325

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk33",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk33"] = Sniper_Mk33().to_data()


@dataclass
class Shotgun_Mk33:
    damage: int = 26
    penetration: float = 0.43
    recoil: float = 0.267
    fire_rate: float = 2.65
    magazine_size: int = 11
    reload_time: float = 2.17
    price: int = 2525

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk33",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk33"] = Shotgun_Mk33().to_data()


@dataclass
class Pistol_Mk34:
    damage: int = 42
    penetration: float = 0.64
    recoil: float = 0.086
    fire_rate: float = 6.20
    magazine_size: int = 16
    reload_time: float = 1.46
    price: int = 1250

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk34",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk34"] = Pistol_Mk34().to_data()


@dataclass
class SMG_Mk34:
    damage: int = 35
    penetration: float = 0.54
    recoil: float = 0.166
    fire_rate: float = 11.70
    magazine_size: int = 34
    reload_time: float = 1.96
    price: int = 2050

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk34",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk34"] = SMG_Mk34().to_data()


@dataclass
class Rifle_Mk34:
    damage: int = 52
    penetration: float = 0.95
    recoil: float = 0.046
    fire_rate: float = 7.70
    magazine_size: int = 34
    reload_time: float = 2.26
    price: int = 3550

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk34",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk34"] = Rifle_Mk34().to_data()


@dataclass
class Sniper_Mk34:
    damage: int = 97
    penetration: float = 0.95
    recoil: float = 0.366
    fire_rate: float = 2.90
    magazine_size: int = 14
    reload_time: float = 2.86
    price: int = 5350

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk34",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk34"] = Sniper_Mk34().to_data()


@dataclass
class Shotgun_Mk34:
    damage: int = 27
    penetration: float = 0.44
    recoil: float = 0.266
    fire_rate: float = 2.70
    magazine_size: int = 12
    reload_time: float = 2.16
    price: int = 2550

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk34",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk34"] = Shotgun_Mk34().to_data()


@dataclass
class Pistol_Mk35:
    damage: int = 42
    penetration: float = 0.65
    recoil: float = 0.085
    fire_rate: float = 6.25
    magazine_size: int = 12
    reload_time: float = 1.45
    price: int = 1275

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk35",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk35"] = Pistol_Mk35().to_data()


@dataclass
class SMG_Mk35:
    damage: int = 35
    penetration: float = 0.55
    recoil: float = 0.165
    fire_rate: float = 11.75
    magazine_size: int = 30
    reload_time: float = 1.95
    price: int = 2075

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk35",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk35"] = SMG_Mk35().to_data()


@dataclass
class Rifle_Mk35:
    damage: int = 52
    penetration: float = 0.95
    recoil: float = 0.045
    fire_rate: float = 7.75
    magazine_size: int = 30
    reload_time: float = 2.25
    price: int = 3575

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk35",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk35"] = Rifle_Mk35().to_data()


@dataclass
class Sniper_Mk35:
    damage: int = 97
    penetration: float = 0.95
    recoil: float = 0.365
    fire_rate: float = 2.95
    magazine_size: int = 10
    reload_time: float = 2.85
    price: int = 5375

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk35",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk35"] = Sniper_Mk35().to_data()


@dataclass
class Shotgun_Mk35:
    damage: int = 27
    penetration: float = 0.45
    recoil: float = 0.265
    fire_rate: float = 2.75
    magazine_size: int = 8
    reload_time: float = 2.15
    price: int = 2575

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk35",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk35"] = Shotgun_Mk35().to_data()


@dataclass
class Pistol_Mk36:
    damage: int = 43
    penetration: float = 0.66
    recoil: float = 0.084
    fire_rate: float = 6.30
    magazine_size: int = 13
    reload_time: float = 1.44
    price: int = 1300

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk36",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk36"] = Pistol_Mk36().to_data()


@dataclass
class SMG_Mk36:
    damage: int = 36
    penetration: float = 0.56
    recoil: float = 0.164
    fire_rate: float = 11.80
    magazine_size: int = 31
    reload_time: float = 1.94
    price: int = 2100

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk36",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk36"] = SMG_Mk36().to_data()


@dataclass
class Rifle_Mk36:
    damage: int = 53
    penetration: float = 0.95
    recoil: float = 0.044
    fire_rate: float = 7.80
    magazine_size: int = 31
    reload_time: float = 2.24
    price: int = 3600

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk36",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk36"] = Rifle_Mk36().to_data()


@dataclass
class Sniper_Mk36:
    damage: int = 98
    penetration: float = 0.95
    recoil: float = 0.364
    fire_rate: float = 3.00
    magazine_size: int = 11
    reload_time: float = 2.84
    price: int = 5400

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk36",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk36"] = Sniper_Mk36().to_data()


@dataclass
class Shotgun_Mk36:
    damage: int = 28
    penetration: float = 0.46
    recoil: float = 0.264
    fire_rate: float = 2.80
    magazine_size: int = 9
    reload_time: float = 2.14
    price: int = 2600

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk36",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk36"] = Shotgun_Mk36().to_data()


@dataclass
class Pistol_Mk37:
    damage: int = 43
    penetration: float = 0.67
    recoil: float = 0.083
    fire_rate: float = 6.35
    magazine_size: int = 14
    reload_time: float = 1.43
    price: int = 1325

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk37",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk37"] = Pistol_Mk37().to_data()


@dataclass
class SMG_Mk37:
    damage: int = 36
    penetration: float = 0.57
    recoil: float = 0.163
    fire_rate: float = 11.85
    magazine_size: int = 32
    reload_time: float = 1.93
    price: int = 2125

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk37",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk37"] = SMG_Mk37().to_data()


@dataclass
class Rifle_Mk37:
    damage: int = 53
    penetration: float = 0.95
    recoil: float = 0.043
    fire_rate: float = 7.85
    magazine_size: int = 32
    reload_time: float = 2.23
    price: int = 3625

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk37",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk37"] = Rifle_Mk37().to_data()


@dataclass
class Sniper_Mk37:
    damage: int = 98
    penetration: float = 0.95
    recoil: float = 0.363
    fire_rate: float = 3.05
    magazine_size: int = 12
    reload_time: float = 2.83
    price: int = 5425

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk37",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk37"] = Sniper_Mk37().to_data()


@dataclass
class Shotgun_Mk37:
    damage: int = 28
    penetration: float = 0.47
    recoil: float = 0.263
    fire_rate: float = 2.85
    magazine_size: int = 10
    reload_time: float = 2.13
    price: int = 2625

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk37",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk37"] = Shotgun_Mk37().to_data()


@dataclass
class Pistol_Mk38:
    damage: int = 44
    penetration: float = 0.68
    recoil: float = 0.082
    fire_rate: float = 6.40
    magazine_size: int = 15
    reload_time: float = 1.42
    price: int = 1350

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk38",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk38"] = Pistol_Mk38().to_data()


@dataclass
class SMG_Mk38:
    damage: int = 37
    penetration: float = 0.58
    recoil: float = 0.162
    fire_rate: float = 11.90
    magazine_size: int = 33
    reload_time: float = 1.92
    price: int = 2150

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk38",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk38"] = SMG_Mk38().to_data()


@dataclass
class Rifle_Mk38:
    damage: int = 54
    penetration: float = 0.95
    recoil: float = 0.042
    fire_rate: float = 7.90
    magazine_size: int = 33
    reload_time: float = 2.22
    price: int = 3650

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk38",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk38"] = Rifle_Mk38().to_data()


@dataclass
class Sniper_Mk38:
    damage: int = 99
    penetration: float = 0.95
    recoil: float = 0.362
    fire_rate: float = 3.10
    magazine_size: int = 13
    reload_time: float = 2.82
    price: int = 5450

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk38",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk38"] = Sniper_Mk38().to_data()


@dataclass
class Shotgun_Mk38:
    damage: int = 29
    penetration: float = 0.48
    recoil: float = 0.262
    fire_rate: float = 2.90
    magazine_size: int = 11
    reload_time: float = 2.12
    price: int = 2650

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk38",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk38"] = Shotgun_Mk38().to_data()


@dataclass
class Pistol_Mk39:
    damage: int = 44
    penetration: float = 0.69
    recoil: float = 0.081
    fire_rate: float = 6.45
    magazine_size: int = 16
    reload_time: float = 1.41
    price: int = 1375

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk39",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk39"] = Pistol_Mk39().to_data()


@dataclass
class SMG_Mk39:
    damage: int = 37
    penetration: float = 0.59
    recoil: float = 0.161
    fire_rate: float = 11.95
    magazine_size: int = 34
    reload_time: float = 1.91
    price: int = 2175

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk39",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk39"] = SMG_Mk39().to_data()


@dataclass
class Rifle_Mk39:
    damage: int = 54
    penetration: float = 0.95
    recoil: float = 0.041
    fire_rate: float = 7.95
    magazine_size: int = 34
    reload_time: float = 2.21
    price: int = 3675

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk39",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk39"] = Rifle_Mk39().to_data()


@dataclass
class Sniper_Mk39:
    damage: int = 99
    penetration: float = 0.95
    recoil: float = 0.361
    fire_rate: float = 3.15
    magazine_size: int = 14
    reload_time: float = 2.81
    price: int = 5475

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk39",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk39"] = Sniper_Mk39().to_data()


@dataclass
class Shotgun_Mk39:
    damage: int = 29
    penetration: float = 0.49
    recoil: float = 0.261
    fire_rate: float = 2.95
    magazine_size: int = 12
    reload_time: float = 2.11
    price: int = 2675

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk39",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk39"] = Shotgun_Mk39().to_data()


@dataclass
class Pistol_Mk40:
    damage: int = 45
    penetration: float = 0.70
    recoil: float = 0.080
    fire_rate: float = 6.50
    magazine_size: int = 12
    reload_time: float = 1.40
    price: int = 1400

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk40",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk40"] = Pistol_Mk40().to_data()


@dataclass
class SMG_Mk40:
    damage: int = 38
    penetration: float = 0.60
    recoil: float = 0.160
    fire_rate: float = 12.00
    magazine_size: int = 30
    reload_time: float = 1.90
    price: int = 2200

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk40",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk40"] = SMG_Mk40().to_data()


@dataclass
class Rifle_Mk40:
    damage: int = 55
    penetration: float = 0.95
    recoil: float = 0.040
    fire_rate: float = 8.00
    magazine_size: int = 30
    reload_time: float = 2.20
    price: int = 3700

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk40",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk40"] = Rifle_Mk40().to_data()


@dataclass
class Sniper_Mk40:
    damage: int = 100
    penetration: float = 0.95
    recoil: float = 0.360
    fire_rate: float = 3.20
    magazine_size: int = 10
    reload_time: float = 2.80
    price: int = 5500

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk40",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk40"] = Sniper_Mk40().to_data()


@dataclass
class Shotgun_Mk40:
    damage: int = 30
    penetration: float = 0.50
    recoil: float = 0.260
    fire_rate: float = 3.00
    magazine_size: int = 8
    reload_time: float = 2.10
    price: int = 2700

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk40",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk40"] = Shotgun_Mk40().to_data()


@dataclass
class Pistol_Mk41:
    damage: int = 45
    penetration: float = 0.71
    recoil: float = 0.079
    fire_rate: float = 6.55
    magazine_size: int = 13
    reload_time: float = 1.39
    price: int = 1425

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk41",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk41"] = Pistol_Mk41().to_data()


@dataclass
class SMG_Mk41:
    damage: int = 38
    penetration: float = 0.61
    recoil: float = 0.159
    fire_rate: float = 12.05
    magazine_size: int = 31
    reload_time: float = 1.89
    price: int = 2225

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk41",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk41"] = SMG_Mk41().to_data()


@dataclass
class Rifle_Mk41:
    damage: int = 55
    penetration: float = 0.95
    recoil: float = 0.039
    fire_rate: float = 8.05
    magazine_size: int = 31
    reload_time: float = 2.19
    price: int = 3725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk41",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk41"] = Rifle_Mk41().to_data()


@dataclass
class Sniper_Mk41:
    damage: int = 100
    penetration: float = 0.95
    recoil: float = 0.359
    fire_rate: float = 3.25
    magazine_size: int = 11
    reload_time: float = 2.79
    price: int = 5525

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk41",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk41"] = Sniper_Mk41().to_data()


@dataclass
class Shotgun_Mk41:
    damage: int = 30
    penetration: float = 0.51
    recoil: float = 0.259
    fire_rate: float = 3.05
    magazine_size: int = 9
    reload_time: float = 2.09
    price: int = 2725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk41",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk41"] = Shotgun_Mk41().to_data()


@dataclass
class Pistol_Mk42:
    damage: int = 46
    penetration: float = 0.72
    recoil: float = 0.078
    fire_rate: float = 6.60
    magazine_size: int = 14
    reload_time: float = 1.38
    price: int = 1450

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk42",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk42"] = Pistol_Mk42().to_data()


@dataclass
class SMG_Mk42:
    damage: int = 39
    penetration: float = 0.62
    recoil: float = 0.158
    fire_rate: float = 12.10
    magazine_size: int = 32
    reload_time: float = 1.88
    price: int = 2250

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk42",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk42"] = SMG_Mk42().to_data()


@dataclass
class Rifle_Mk42:
    damage: int = 56
    penetration: float = 0.95
    recoil: float = 0.038
    fire_rate: float = 8.10
    magazine_size: int = 32
    reload_time: float = 2.18
    price: int = 3750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk42",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk42"] = Rifle_Mk42().to_data()


@dataclass
class Sniper_Mk42:
    damage: int = 101
    penetration: float = 0.95
    recoil: float = 0.358
    fire_rate: float = 3.30
    magazine_size: int = 12
    reload_time: float = 2.78
    price: int = 5550

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk42",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk42"] = Sniper_Mk42().to_data()


@dataclass
class Shotgun_Mk42:
    damage: int = 31
    penetration: float = 0.52
    recoil: float = 0.258
    fire_rate: float = 3.10
    magazine_size: int = 10
    reload_time: float = 2.08
    price: int = 2750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk42",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk42"] = Shotgun_Mk42().to_data()


@dataclass
class Pistol_Mk43:
    damage: int = 46
    penetration: float = 0.73
    recoil: float = 0.077
    fire_rate: float = 6.65
    magazine_size: int = 15
    reload_time: float = 1.37
    price: int = 1475

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk43",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk43"] = Pistol_Mk43().to_data()


@dataclass
class SMG_Mk43:
    damage: int = 39
    penetration: float = 0.63
    recoil: float = 0.157
    fire_rate: float = 12.15
    magazine_size: int = 33
    reload_time: float = 1.87
    price: int = 2275

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk43",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk43"] = SMG_Mk43().to_data()


@dataclass
class Rifle_Mk43:
    damage: int = 56
    penetration: float = 0.95
    recoil: float = 0.037
    fire_rate: float = 8.15
    magazine_size: int = 33
    reload_time: float = 2.17
    price: int = 3775

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk43",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk43"] = Rifle_Mk43().to_data()


@dataclass
class Sniper_Mk43:
    damage: int = 101
    penetration: float = 0.95
    recoil: float = 0.357
    fire_rate: float = 3.35
    magazine_size: int = 13
    reload_time: float = 2.77
    price: int = 5575

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk43",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk43"] = Sniper_Mk43().to_data()


@dataclass
class Shotgun_Mk43:
    damage: int = 31
    penetration: float = 0.53
    recoil: float = 0.257
    fire_rate: float = 3.15
    magazine_size: int = 11
    reload_time: float = 2.07
    price: int = 2775

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk43",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk43"] = Shotgun_Mk43().to_data()


@dataclass
class Pistol_Mk44:
    damage: int = 47
    penetration: float = 0.74
    recoil: float = 0.076
    fire_rate: float = 6.70
    magazine_size: int = 16
    reload_time: float = 1.36
    price: int = 1500

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk44",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk44"] = Pistol_Mk44().to_data()


@dataclass
class SMG_Mk44:
    damage: int = 40
    penetration: float = 0.64
    recoil: float = 0.156
    fire_rate: float = 12.20
    magazine_size: int = 34
    reload_time: float = 1.86
    price: int = 2300

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk44",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk44"] = SMG_Mk44().to_data()


@dataclass
class Rifle_Mk44:
    damage: int = 57
    penetration: float = 0.95
    recoil: float = 0.036
    fire_rate: float = 8.20
    magazine_size: int = 34
    reload_time: float = 2.16
    price: int = 3800

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk44",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk44"] = Rifle_Mk44().to_data()


@dataclass
class Sniper_Mk44:
    damage: int = 102
    penetration: float = 0.95
    recoil: float = 0.356
    fire_rate: float = 3.40
    magazine_size: int = 14
    reload_time: float = 2.76
    price: int = 5600

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk44",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk44"] = Sniper_Mk44().to_data()


@dataclass
class Shotgun_Mk44:
    damage: int = 32
    penetration: float = 0.54
    recoil: float = 0.256
    fire_rate: float = 3.20
    magazine_size: int = 12
    reload_time: float = 2.06
    price: int = 2800

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk44",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk44"] = Shotgun_Mk44().to_data()


@dataclass
class Pistol_Mk45:
    damage: int = 47
    penetration: float = 0.75
    recoil: float = 0.075
    fire_rate: float = 6.75
    magazine_size: int = 12
    reload_time: float = 1.35
    price: int = 1525

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk45",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk45"] = Pistol_Mk45().to_data()


@dataclass
class SMG_Mk45:
    damage: int = 40
    penetration: float = 0.65
    recoil: float = 0.155
    fire_rate: float = 12.25
    magazine_size: int = 30
    reload_time: float = 1.85
    price: int = 2325

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk45",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk45"] = SMG_Mk45().to_data()


@dataclass
class Rifle_Mk45:
    damage: int = 57
    penetration: float = 0.95
    recoil: float = 0.035
    fire_rate: float = 8.25
    magazine_size: int = 30
    reload_time: float = 2.15
    price: int = 3825

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk45",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk45"] = Rifle_Mk45().to_data()


@dataclass
class Sniper_Mk45:
    damage: int = 102
    penetration: float = 0.95
    recoil: float = 0.355
    fire_rate: float = 3.45
    magazine_size: int = 10
    reload_time: float = 2.75
    price: int = 5625

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk45",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk45"] = Sniper_Mk45().to_data()


@dataclass
class Shotgun_Mk45:
    damage: int = 32
    penetration: float = 0.55
    recoil: float = 0.255
    fire_rate: float = 3.25
    magazine_size: int = 8
    reload_time: float = 2.05
    price: int = 2825

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk45",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk45"] = Shotgun_Mk45().to_data()


@dataclass
class Pistol_Mk46:
    damage: int = 48
    penetration: float = 0.76
    recoil: float = 0.074
    fire_rate: float = 6.80
    magazine_size: int = 13
    reload_time: float = 1.34
    price: int = 1550

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk46",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk46"] = Pistol_Mk46().to_data()


@dataclass
class SMG_Mk46:
    damage: int = 41
    penetration: float = 0.66
    recoil: float = 0.154
    fire_rate: float = 12.30
    magazine_size: int = 31
    reload_time: float = 1.84
    price: int = 2350

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk46",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk46"] = SMG_Mk46().to_data()


@dataclass
class Rifle_Mk46:
    damage: int = 58
    penetration: float = 0.95
    recoil: float = 0.034
    fire_rate: float = 8.30
    magazine_size: int = 31
    reload_time: float = 2.14
    price: int = 3850

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk46",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk46"] = Rifle_Mk46().to_data()


@dataclass
class Sniper_Mk46:
    damage: int = 103
    penetration: float = 0.95
    recoil: float = 0.354
    fire_rate: float = 3.50
    magazine_size: int = 11
    reload_time: float = 2.74
    price: int = 5650

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk46",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk46"] = Sniper_Mk46().to_data()


@dataclass
class Shotgun_Mk46:
    damage: int = 33
    penetration: float = 0.56
    recoil: float = 0.254
    fire_rate: float = 3.30
    magazine_size: int = 9
    reload_time: float = 2.04
    price: int = 2850

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk46",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk46"] = Shotgun_Mk46().to_data()


@dataclass
class Pistol_Mk47:
    damage: int = 48
    penetration: float = 0.77
    recoil: float = 0.073
    fire_rate: float = 6.85
    magazine_size: int = 14
    reload_time: float = 1.33
    price: int = 1575

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk47",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk47"] = Pistol_Mk47().to_data()


@dataclass
class SMG_Mk47:
    damage: int = 41
    penetration: float = 0.67
    recoil: float = 0.153
    fire_rate: float = 12.35
    magazine_size: int = 32
    reload_time: float = 1.83
    price: int = 2375

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk47",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk47"] = SMG_Mk47().to_data()


@dataclass
class Rifle_Mk47:
    damage: int = 58
    penetration: float = 0.95
    recoil: float = 0.033
    fire_rate: float = 8.35
    magazine_size: int = 32
    reload_time: float = 2.13
    price: int = 3875

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk47",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk47"] = Rifle_Mk47().to_data()


@dataclass
class Sniper_Mk47:
    damage: int = 103
    penetration: float = 0.95
    recoil: float = 0.353
    fire_rate: float = 3.55
    magazine_size: int = 12
    reload_time: float = 2.73
    price: int = 5675

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk47",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk47"] = Sniper_Mk47().to_data()


@dataclass
class Shotgun_Mk47:
    damage: int = 33
    penetration: float = 0.57
    recoil: float = 0.253
    fire_rate: float = 3.35
    magazine_size: int = 10
    reload_time: float = 2.03
    price: int = 2875

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk47",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk47"] = Shotgun_Mk47().to_data()


@dataclass
class Pistol_Mk48:
    damage: int = 49
    penetration: float = 0.78
    recoil: float = 0.072
    fire_rate: float = 6.90
    magazine_size: int = 15
    reload_time: float = 1.32
    price: int = 1600

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk48",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk48"] = Pistol_Mk48().to_data()


@dataclass
class SMG_Mk48:
    damage: int = 42
    penetration: float = 0.68
    recoil: float = 0.152
    fire_rate: float = 12.40
    magazine_size: int = 33
    reload_time: float = 1.82
    price: int = 2400

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk48",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk48"] = SMG_Mk48().to_data()


@dataclass
class Rifle_Mk48:
    damage: int = 59
    penetration: float = 0.95
    recoil: float = 0.032
    fire_rate: float = 8.40
    magazine_size: int = 33
    reload_time: float = 2.12
    price: int = 3900

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk48",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk48"] = Rifle_Mk48().to_data()


@dataclass
class Sniper_Mk48:
    damage: int = 104
    penetration: float = 0.95
    recoil: float = 0.352
    fire_rate: float = 3.60
    magazine_size: int = 13
    reload_time: float = 2.72
    price: int = 5700

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk48",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk48"] = Sniper_Mk48().to_data()


@dataclass
class Shotgun_Mk48:
    damage: int = 34
    penetration: float = 0.58
    recoil: float = 0.252
    fire_rate: float = 3.40
    magazine_size: int = 11
    reload_time: float = 2.02
    price: int = 2900

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk48",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk48"] = Shotgun_Mk48().to_data()


@dataclass
class Pistol_Mk49:
    damage: int = 49
    penetration: float = 0.79
    recoil: float = 0.071
    fire_rate: float = 6.95
    magazine_size: int = 16
    reload_time: float = 1.31
    price: int = 1625

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk49",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk49"] = Pistol_Mk49().to_data()


@dataclass
class SMG_Mk49:
    damage: int = 42
    penetration: float = 0.69
    recoil: float = 0.151
    fire_rate: float = 12.45
    magazine_size: int = 34
    reload_time: float = 1.81
    price: int = 2425

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk49",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk49"] = SMG_Mk49().to_data()


@dataclass
class Rifle_Mk49:
    damage: int = 59
    penetration: float = 0.95
    recoil: float = 0.031
    fire_rate: float = 8.45
    magazine_size: int = 34
    reload_time: float = 2.11
    price: int = 3925

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk49",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk49"] = Rifle_Mk49().to_data()


@dataclass
class Sniper_Mk49:
    damage: int = 104
    penetration: float = 0.95
    recoil: float = 0.351
    fire_rate: float = 3.65
    magazine_size: int = 14
    reload_time: float = 2.71
    price: int = 5725

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk49",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk49"] = Sniper_Mk49().to_data()


@dataclass
class Shotgun_Mk49:
    damage: int = 34
    penetration: float = 0.59
    recoil: float = 0.251
    fire_rate: float = 3.45
    magazine_size: int = 12
    reload_time: float = 2.01
    price: int = 2925

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk49",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk49"] = Shotgun_Mk49().to_data()


@dataclass
class Pistol_Mk50:
    damage: int = 50
    penetration: float = 0.80
    recoil: float = 0.070
    fire_rate: float = 7.00
    magazine_size: int = 12
    reload_time: float = 1.30
    price: int = 1650

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="pistol_mk50",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["pistol_mk50"] = Pistol_Mk50().to_data()


@dataclass
class SMG_Mk50:
    damage: int = 43
    penetration: float = 0.70
    recoil: float = 0.150
    fire_rate: float = 12.50
    magazine_size: int = 30
    reload_time: float = 1.80
    price: int = 2450

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="smg_mk50",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["smg_mk50"] = SMG_Mk50().to_data()


@dataclass
class Rifle_Mk50:
    damage: int = 60
    penetration: float = 0.95
    recoil: float = 0.030
    fire_rate: float = 8.50
    magazine_size: int = 30
    reload_time: float = 2.10
    price: int = 3950

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="rifle_mk50",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["rifle_mk50"] = Rifle_Mk50().to_data()


@dataclass
class Sniper_Mk50:
    damage: int = 105
    penetration: float = 0.95
    recoil: float = 0.350
    fire_rate: float = 3.70
    magazine_size: int = 10
    reload_time: float = 2.70
    price: int = 5750

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="sniper_mk50",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["sniper_mk50"] = Sniper_Mk50().to_data()


@dataclass
class Shotgun_Mk50:
    damage: int = 35
    penetration: float = 0.60
    recoil: float = 0.250
    fire_rate: float = 3.50
    magazine_size: int = 8
    reload_time: float = 2.00
    price: int = 2950

    def to_data(self) -> WeaponData:
        return WeaponData(
            name="shotgun_mk50",
            damage=self.damage,
            penetration=self.penetration,
            recoil=self.recoil,
            fire_rate=self.fire_rate,
            magazine_size=self.magazine_size,
            reload_time=self.reload_time,
            price=self.price,
        )

CATALOGUE["shotgun_mk50"] = Shotgun_Mk50().to_data()
