import DAN

ServerIP = '140.113.199.199'   #=None:AutoSearch, or ='IP':Connect to this IP

def profile_init():
    DAN.profile['dm_name']='Lamp'
    DAN.profile['d_name']='Lamp.'+DAN.get_mac_addr()[-4:]


def odf():  # int only
    return [
        ('Luminance', 0, 'Luminance'),
    ]


def idf():
    return [
     #  ('PIN1', float),
     #  ('PIN2', int),
     #  ('PIN3', str),
    ]
