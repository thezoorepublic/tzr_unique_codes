import random

class Allotment(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count

characters = 'CDFHJKLMNPRTXZ3479'
code_length = 7
seed = 100

total = len(characters)**7
print total/1566797

allotments = [        
    Allotment('primary-1',712180),
    Allotment('primary-2',712180),
    Allotment('spare', 142436),
    Allotment('testing', 1000)
]

#    Allotment('codes',19320000),
#    Allotment('telephone', 10000),
#    Allotment('testing', 1000)

def generate_unique_codes(characters, code_length, number_of_codes, seed):
    random.seed(seed)
    codes = set()
    while True:
        s = ''.join(random.choice(characters) for i in range(code_length))
        codes.add(s) 
        if len(codes) >= number_of_codes:
            return list(codes)

def split_codes(unique_codes, allotments):
    for allotment in allotments:
        allotment.codes = unique_codes[0:allotment.count]
        del unique_codes[0:allotment.count]

total = sum([allotment.count for allotment in allotments])
codes = generate_unique_codes(characters, code_length, total, seed)
codes = split_codes(codes, allotments)

codes_done = {}
for allotment in allotments:
    file = open(allotment.name+'.csv', 'w')
    file.write('code\n')
    for code in allotment.codes:
        file.write('%s\n' % (code))
        assert not code in codes_done
        codes_done[code] = True
