# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CarControllerParams:
  def __init__(self, CP):
    if CP.carFingerprint == CAR.IMPREZA_2020:
      self.STEER_MAX = 1439
    else:
      self.STEER_MAX = 2047
    self.STEER_STEP = 2                # how often we update the steer cmd
    self.STEER_DELTA_UP = 50           # torque increase per refresh, 0.8s to max
    self.STEER_DELTA_DOWN = 70         # torque decrease per refresh
    self.STEER_DRIVER_ALLOWANCE = 60   # allowed driver torque before start limiting
    self.STEER_DRIVER_MULTIPLIER = 10  # weight driver torque heavily
    self.STEER_DRIVER_FACTOR = 1       # from dbc

class CAR:
  ASCENT = "SUBARU ASCENT LIMITED 2019"
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  IMPREZA_2020 = "SUBARU IMPREZA SPORT 2020"
  CROSSTREK_2020H = "SUBARU CROSSTREK LIMITED 2020 HYBRID"
  FORESTER = "SUBARU FORESTER 2019"
  FORESTER_PREGLOBAL = "SUBARU FORESTER 2017 - 2018"
  LEGACY_PREGLOBAL = "SUBARU LEGACY 2015 - 2018"
  LEVORG_PREGLOBAL = "SUBARU LEVORG 2016"
  OUTBACK = "SUBARU OUTBACK 2020"
  OUTBACK_PREGLOBAL = "SUBARU OUTBACK 2015 - 2017"
  OUTBACK_PREGLOBAL_2018 = "SUBARU OUTBACK 2018 - 2019"
  WRX_PREGLOBAL = "SUBARU WRX 2018"

FINGERPRINTS = {
  CAR.IMPREZA_2020: [{
  # SUBARU CROSSTREK SPORT 2020
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 282: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 803: 8, 805: 8, 808: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1617: 8, 1632: 8, 1650: 8, 1677: 8, 1697: 8, 1722: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8, 1968: 8, 1976: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # IMPREZA 2020
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 282: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 801: 8, 802: 8, 803: 8, 805: 8, 808: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  }],
  CAR.CROSSTREK_2020H: [{
  # CROSSTREK HYBRID 2020
    2: 8, 64: 8, 175: 8, 280: 8, 281: 8, 290: 8, 295: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 327: 3, 344: 8, 505: 8, 544: 8, 552: 8, 554: 8, 557: 8, 577: 8, 580: 8, 600: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 839: 8, 865: 8, 877: 8, 912: 8, 915: 8, 940: 8, 945: 8, 956: 8, 1031: 8, 1614: 8, 1617: 8, 1632: 8, 1657: 8, 1658: 8, 1677: 8, 1722: 8, 1750: 8, 1786: 5, 1787: 5, 1788: 8, 1813: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8,
  }],
  CAR.FORESTER: [{
  # FORESTER 2019-20
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 282: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 803: 8, 805: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 961: 8, 984: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1651: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1698: 8, 1722: 8, 1743: 8, 1759: 8, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  }],
  CAR.OUTBACK_PREGLOBAL: [{
  # OUTBACK PREMIUM 2.5i 2015
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 346: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5, 1882: 8, 2015: 8, 2016: 8, 2024: 8, 604: 8, 885: 8, 1788: 8, 316: 8, 1614: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1743: 8, 1785: 5, 1787: 5
  },
  # OUTBACK PREMIUM 3.6i 2015
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1779: 8, 1786: 5
  },
  # OUTBACK LIMITED 2.5i 2018
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1736: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  }],
  CAR.OUTBACK_PREGLOBAL_2018: [{
  # OUTBACK LIMITED 3.6R 2019
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 886: 2, 977: 8, 1614: 8, 1632: 8, 1657: 8, 1658: 8, 1672: 8, 1736: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1862: 8, 1870: 8, 1920: 8, 1927: 8, 1928: 8, 1935: 8, 1968: 8, 1976: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.FORESTER_PREGLOBAL: [{
  # FORESTER PREMIUM 2.5i 2017
    2: 8, 112: 8, 117: 8, 128: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 340: 7, 342: 8, 352: 8, 353: 8, 354: 8, 355: 8, 356: 8, 554: 8, 604: 8, 640: 8, 641: 8, 642: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 886: 1, 888: 8, 977: 8, 1398: 8, 1632: 8, 1743: 8, 1744: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1882: 8, 1895: 8, 1903: 8, 1986: 8, 1994: 8, 2015: 8, 2016: 8, 2024: 8, 644:8, 890:8, 1736:8
  }],
  CAR.LEGACY_PREGLOBAL: [{
  # LEGACY 2.5i 2017
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1632: 8, 1640: 8, 1736: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 644: 8
  },
  # LEGACY 2018
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1743: 8, 1745: 8, 1778: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # LEGACY 2018
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  }],
}

FW_VERSIONS = {
  CAR.ASCENT: {
    # 2019 Ascent - UDM / @Adminiuga
    # 2019 Ascent - UDM / @tvo
    # 2019 Ascent - UDM / @RCoaster
    # 2021 Ascent - UDM / @Sandy
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa5 \x19\x02\x00',
      b'\xa5 !\002\000',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x85\xc0\xd0\x00',
      b'\005\xc0\xd0\000',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xb9\x1f@ \x10',
      b'\000\000e~\037@ \'',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbb,\xa0t\a',
      b'\xf1\x82\xbb,\xa0t\x87',
      b'\xf1\x82\xbb,\xa0t\a',
      b'\xf1\x82\xd9,\xa0@\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x00\xfe\xf7\x00\x00',
      b'\001\xfe\xf9\000\000',
    ],
  },
  CAR.IMPREZA: {
    # 2018 Crosstrek - EDM / @martinl
    # 2018 Impreza - ADM / @Michael
    # 2019 Impreza Premium - UDM / @hitoryu2001
    # 2018 Crosstrek Limited - UDM / @Joey
    # 2017 Impreza - UDM / @Frye
    # 2018 Crosstrek - UDM / @rwalsh3
    # 2018 Crosstrek - UDM / @pemerick07
    # 2018 Crosstrek - UDM / @rwalsh3 (new engine fw)
    # 2019 Crosstrek - UDM / @Nooks Cranny
    # 2019 Impreza - UDM / @cheesypotato
    # 2019 Impreza - UDM / @dbzx6r
    # 2018 Impreza Sport - UDM / @gking
    # 2019 Crosstrek Limited - UDM / @cellfreak
    # 2019 Impreza Limited - UDM / @boros
    # 2017 Impreza - UDM / @Fidel
    # 2018 Crosstrek - UDM / @dnewstat
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x7a\x94\x3f\x90\x00',
      b'\xa2 \x185\x00',
      b'\xa2 \x193\x00',
      b'z\x94.\x90\x00',
      b'z\x94\b\x90\x01',
      b'\xa2 \x19`\x00',
      b'z\x94\f\x90\001',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x7a\xc0\x0c\x00',
      b'z\xc0\b\x00',
      b'\x8a\xc0\x00\x00',
      b'z\xc0\x04\x00',
      b'z\xc0\x00\x00',
      b'\x8a\xc0\x10\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xb5\x1f@ \x0e',
      b'\x00\x00d\xdc\x1f@ \x0e',
      b'\x00\x00e\x1c\x1f@ \x14',
      b'\x00\x00d)\x1f@ \a',
      b'\x00\x00e+\x1f@ \x14',
      b'\000\000e+\000\000\000\000',
      b'\000\000dd\037@ \016',
      b'\000\000e\002\037@ \024',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xaa\x61\x66\x73\x07',
      b'\xbeacr\a',
      b'\xc5!`r\a',
      b'\xaa!ds\a',
      b'\xaa!`u\a',
      b'\xaa!dq\a',
      b'\xaa!dt\a',
      b'\xc5!dr\a',
      b'\xc5!ar\a',
      b'\xbe!as\a',
      b'\xc5!ds\a',
      b'\xc5!`s\a',
      b'\xaa!au\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe3\xe5\x46\x31\x00',
      b'\xe4\xe5\x061\x00',
      b'\xe5\xf5\x04\x00\x00',
      b'\xe3\xf5G\x00\x00',
      b'\xe3\xf5\a\x00\x00',
      b'\xe3\xf5C\x00\x00',
      b'\xe5\xf5B\x00\x00',
      b'\xe5\xf5$\000\000',
      b'\xe4\xf5\a\000\000',
      b'\xe3\xf5F\000\000',
    ],
  },
  CAR.IMPREZA_2020: {
    # 2020 Impreza Sport - UDM @CrispinFlowerday
    # 2020 Impreza Hatchback Premium - UDM @davidvatz
    # 2020 Impreza Hatchback - UDM @GPT-3
    # 2020 Impreza Premium - UDM @KeetsScrimalittle
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa2 \0314\000',
      b'\xa2 \0313\000',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9a\xc0\000\000',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\000\000eb\037@ \"',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xca!ap\a',
      b'\xca!`p\a',
      b'\xca!`0\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe6\xf5\004\000\000',
      b'\xe6\xf5$\000\000',
    ],
  },
  CAR.CROSSTREK_2020H: {
    # 2020 Crosstrek Hybrid UDM / @revity
    # 2020 Crosstrek Hybrid UDM / @Dave32
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa2 \x19e\x01',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9a\xc2\x01\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00el\x1f@ #',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xd7!`@\x07',
      b'\xd7!`p\a',
    ],
  },
  CAR.FORESTER: {
    # 2021 Subaru Forester - UDM / @gotham
    # 2019 Subaru Forester - UDM / @clockenessmnstr
    # 2020 Subaru Forester - UDM / @TH156UY
    # 2021 Subaru Forester - UDM / @umby24
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa3 \030\024\000',
      b'\xa3  \024\000',
      b'\xa3 \031\024\000',
      b'\xa3  \024\001',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x8d\xc0\004\000',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\000\000e!\037@ \021',
      b'\000\000e\x97\037@ 0',
      b'\000\000e`\037@  ',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb6\"`A\a',
      b'\xcf"`0\a',
      b'\xcb\"`@\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\032\xf6B0\000',
      b'\032\xf6F`\000',
      b'\032\xf6b`\000',
    ],
  },
  CAR.FORESTER_PREGLOBAL: {
    # 2018 Subaru Forester 2.5i Touring - UDM / @Oreo
    # 2018 Subaru Forester 2.5 Limited - Canada / @litobro
    # 2017 Subaru Forester UDM / @hitoryu2001
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x7d\x97\x14\x40',
    ],
    (Ecu.eps, 0x746, None): [
      b'}\xc0\x10\x00',
      b'm\xc0\x10\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00\x64\x35\x1f\x40\x20\x09',
      b'\x00\x00c\xe9\x1f@ \x03',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xba"@p\a',
      b'\xa7)\xa0q\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xdc\xf2\x60\x60\x00',
      b'\xdc\xf2@`\x00',
      b'\xda\xfd\xe0\x80\x00',
    ],
  },
  CAR.LEGACY_PREGLOBAL: {
    # 2018 Subaru Legacy 2.5i Premium - UDM / @kram322
    # 2016 Subaru Legacy - UDM / @nort
    # 2015 Subaru Legacy 3.6R Limited / @chrissantamaria
    # 2017 Subaru Legacy 2.5i Sport / @bonnysonnyandclyde
    # 2015 Subaru Legacy Premium 2.5i / @Wanting.RA1N
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x8b\x97D\x00',
      b'k\x97D\x00',
      b'[\xba\xc4\x03',
      b'{\x97D\x00',
      b'[\x97D\000',
    ],
    (Ecu.eps, 0x746, None): [
      b'{\xb0\x00\x00',
      b'[\xb0\x00\x01',
      b'K\xb0\x00\x01',
      b'k\xb0\x00\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00df\x1f@ \n',
      b'\x00\x00c\xb7\x1f@\x10\x16',
      b'\x00\x00c\x94\x1f@\x10\x08',
      b'\x00\x00c\xec\x1f@ \x04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb5\"@p\a',
      b'\xab*@r\a',
      b'\xa0+@p\x07',
      b'\xb4"@0\x07',
      b'\xa0"@q\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbc\xf2\x00\x81\x00',
      b'\xbe\xf2\x00p\x00',
      b'\xbf\xfb\xc0\x80\x00',
      b'\xbd\xf2\x00`\x00',
      b'\xbf\xf2\000\x80\000',
    ],
  },
  CAR.LEVORG_PREGLOBAL: {
     # 2016 Subaru Levorg / @jpgnz
     # Ecu, addr, subaddr: ROM ID
     (Ecu.esp, 0x7b0, None): [
       b'j\x9c\x92\002'
     ],
     (Ecu.eps, 0x746, None): [
       b'Z\xb0\000\000'
     ],
     (Ecu.fwdCamera, 0x787, None): [
       b'\000\000c\xd3\000\000\000\000',
     ],
     (Ecu.engine, 0x7e0, None): [
       b'\xf1\x82\xa6\000\xa1t\a'
     ],
     (Ecu.transmission, 0x7e1, None): [
       b'\xcb\xd9\000p\000'
     ],
  },
  CAR.OUTBACK: {
    # 2020 Outback 2.4 XT Limited - UDM / @KingChalupa
    # 2020 Outback 2.5i Premium - UDM / @ursubpar
    # 2021 Outback / @Frye - FL
    # 2020 Outback 2.4 Touring XT  - UDM / @chrissantamaria
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa1  \x06\x01',
      b'\xa1  \a\x00',
      b'\xa1  \b\001',
      b'\xa1  \x06\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x9b\xc0\x10\x00',
      b'\x9b\xc0\x20\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00eJ\x00\x1f@ \x19\x00',
      b'\000\000e\x80\000\037@ \031\000',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbc,\xa0q\x07',
      b'\xbc\"`@\a',
      b'\xde"`0\a',
      b'\xf1\x82\xbc,\xa0q\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xa5\xfe\xf7@\x00',
      b'\xa5\xf6D@\x00',
      b'\xa5\xfe\xf6@\x00',
    ],
  },
  CAR.OUTBACK_PREGLOBAL: {
    # 2017 Outback Limited 3.6r - UDM / @Anthony
    # 2016 Outback Limited 2.5 - UDM / @aeiro
    # 2015 Outback Limited 2.5 - ADM / @Bugsy
    # 2015 Outback Premium 3.6i - UDM / @aidrive
    # 2016 Outback Premium 2.5 - UDM / @Troy
    # 2017 Subaru Outback 2.5 - UDM / @chewbaru
    # 2017 Subaru Outback - UDM / @the3seashells
    # 2016 Outback Premium 2.5i - UDM / @G-Wood
    # 2016 Outback 3.6R - UDM / @KingSlayer
    # 2017 Outback Limited 2.5i / @laksdjf
    # 2015 Outback 3.6R - UDM / @bitwaster
    # 2015 Outback - UDM / @chk_null
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'{\x9a\xac\x00',
      b'k\x97\xac\x00',
      b'\x5b\xf7\xbc\x03',
      b'[\xf7\xac\x03',
      b'{\x97\xac\x00',
      b'k\x9a\xac\000',
      b'[\xba\xac\x03',
      b'[\xf7\xac\000',
    ],
    (Ecu.eps, 0x746, None): [
      b'k\xb0\x00\x00',
      b'[\xb0\x00\x00',
      b'\x4b\xb0\x00\x02',
      b'K\xb0\x00\x00',
      b'{\xb0\x00\x01',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00c\xec\x1f@ \x04',
      b'\x00\x00c\xd1\x1f@\x10\x17',
      b'\xf1\x00\xf0\xe0\x0e',
      b'\x00\x00c\x94\x00\x00\x00\x00',
      b'\x00\x00c\x94\x1f@\x10\b',
      b'\x00\x00c\xb7\x1f@\x10\x16',
      b'\000\000c\x90\037@\020\016',
      b'\x00\x00c\xec\x37@\x04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb4+@p\a',
      b'\xab\"@@\a',
      b'\xa0\x62\x41\x71\x07',
      b'\xa0*@q\a',
      b'\xab*@@\a',
      b'\xb4"@0\a',
      b'\xb4"@p\a',
      b'\xab"@s\a',
      b'\xab+@@\a',
      b'\xb4"@r\a',
      b'\xa0+@@\x07'
      b'\xa0\"@\x80\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbd\xfb\xe0\x80\x00',
      b'\xbe\xf2@\x80\x00',
      b'\xbf\xe2\x40\x80\x00',
      b'\xbf\xf2@\x80\x00',
      b'\xbe\xf2@p\x00',
      b'\xbd\xf2@`\x00',
      b'\xbd\xf2@\x81\000',
      b'\xbe\xfb\xe0p\000',
      b'\xbf\xfb\xe0b\x00',
    ],
  },
  # Outback with reversed driver torque signal
  CAR.OUTBACK_PREGLOBAL_2018: {
    # 2018 Outback Premium 2.5i - UDM / @zhoux260
    # 2018 Outback 3.6r UDM / @mirroregami
    # 2018 Outback 2.5i Premium UDM / @dirkmm
    # 2019 Outback UDM / @Valhalla
    # 2018 Outback 2.5 / @haak
    # 2018 Outback 3.6r USDM / @Scripty_
    # 2018 Subaru Outback 2.0d - ADM / @Richo
    # 2019 Outback 2.5i Premium / @Z-dawg Swizzlepants
    # 2019 Outback Touring 3.6R / @danyo
    # 2019 Outback - UDM / @Steven C
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x8b\x97\xac\x00',
      b'\x8b\x9a\xac\x00',
      b'\x9b\x97\xac\x00',
      b'\x8b\x97\xbc\x00',
      b'\x8b\x99\xac\x00',
      b'\x9b\x9a\xac\000',
      b'\x9b\x97\xbe\x10',
    ],
    (Ecu.eps, 0x746, None): [
      b'{\xb0\x00\x00',
      b'{\xb0\x00\x01',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00df\x1f@ \n',
      b'\x00\x00d\xfe\x1f@ \x15',
      b'\x00\x00d\x95\x00\x00\x00\x00',
      b'\x00\x00d\x95\x1f@ \x0f',
      b'\x00\x00d\xfe\x00\x00\x00\x00',
      b'\x00\x00e\x19\x1f@ \x15',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xb5"@p\a',
      b'\xb5+@@\a',
      b'\xb5"@P\a',
      b'\xc4"@0\a',
      b'\xb5b@1\x07',
      b'\xb5q\xe0@\a',
      b'\xc4+@0\a',
      b'\xc4b@p\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xbc\xf2@\x81\x00',
      b'\xbc\xfb\xe0\x80\x00',
      b'\xbc\xf2@\x80\x00',
      b'\xbb\xf2@`\x00',
      b'\xbc\xe2@\x80\x00',
      b'\xbc\xfb\xe0`\x00',
      b'\xbc\xaf\xe0`\x00',
      b'\xbb\xfb\xe0`\000',
    ],
  },
  CAR.WRX_PREGLOBAL: {
    # 2018 Subaru WRX / @cferra
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x8a\x95R\x01'
    ],
    (Ecu.eps, 0x746, None): [
      b'z\xb0\x00\x00'
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xae\x1f@ \r'
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x82\xb2)\xa0P\x97'
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xcd\xfd\xd0\x80\x00'
    ],
  },
}


STEER_THRESHOLD = {
  CAR.ASCENT: 80,
  CAR.IMPREZA: 80,
  CAR.IMPREZA_2020: 80,
  CAR.CROSSTREK_2020H: 80,
  CAR.FORESTER: 80,
  CAR.FORESTER_PREGLOBAL: 75,
  CAR.LEGACY_PREGLOBAL: 75,
  CAR.LEVORG_PREGLOBAL: 75,
  CAR.OUTBACK: 80,
  CAR.OUTBACK_PREGLOBAL: 75,
  CAR.OUTBACK_PREGLOBAL_2018: 75,
  CAR.WRX_PREGLOBAL: 75,
}

DBC = {
  CAR.ASCENT: dbc_dict('subaru_global_2017_generated', None),
  CAR.IMPREZA: dbc_dict('subaru_global_2017_generated', None),
  CAR.IMPREZA_2020: dbc_dict('subaru_global_2017_generated', None),
  CAR.CROSSTREK_2020H: dbc_dict('subaru_global_2020_hybrid_generated', None),
  CAR.FORESTER: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
  CAR.LEGACY_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.LEVORG_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
  CAR.OUTBACK: dbc_dict('subaru_global_2017_generated', None),
  CAR.OUTBACK_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK_PREGLOBAL_2018: dbc_dict('subaru_outback_2019_generated', None),
  CAR.WRX_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
}

PREGLOBAL_CARS = [CAR.FORESTER_PREGLOBAL, CAR.LEGACY_PREGLOBAL, CAR.LEVORG_PREGLOBAL, CAR.OUTBACK_PREGLOBAL, CAR.OUTBACK_PREGLOBAL_2018, CAR.WRX_PREGLOBAL]
GLOBAL_CARS_SNG = [CAR.ASCENT, CAR.IMPREZA, CAR.IMPREZA_2020, CAR.FORESTER]
SUBARU_WMI = ['JF1', 'JF2', '4S3', '4S4']
