import DAN

#ServerURL='https://DomainName'# for secure connection
ServerURL='http://IP:9999'     # for non-secure connection
Comm_interval = 10 # unit:second

def profile_init():
    DAN.profile['dm_name']='SwitchSet'
    DAN.profile['d_name']='Set' #DAN.get_mac_addr()[-4:]

def odf():  # int only
    return [
	('Switch-O1', 0, 'Switch-O1'),
        ('Switch-O2', 0, 'Switch-O2'),
        ('Switch-O3', 0, 'Switch-O3'),
        ('Switch-O4', 0, 'Switch-O4'),
        ('Switch-O5', 0, 'Switch-O5'),
        ('Switch-O6', 0, 'Switch-O6'),
        ('Switch-O7', 0, 'Switch-O7'),
        ('Switch-O8', 0, 'Switch-O8'),
        ('Switch-O9', 0, 'Switch-O9'),
        ('Switch-O10', 0, 'Switch-O10'),
    ]

def idf():
    return [
       ('Humidity', int),
       #('A1', int),
       #('A2', int),
       #('A3', int),
       #('A4', int),
       #('A5', int),
    ]
