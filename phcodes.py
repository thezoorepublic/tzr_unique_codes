import random,os

class Allotment(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count

characters = 'CDFHJKLMNPRTXZ3479'
code_length = 9
seed = 100
codecsv_heading='code'
file_type='.csv'
excludes_filename='excludes.csv'
allotments = [        
    Allotment('newwinning',71820),
    Allotment('newlosing',7980),
    Allotment('newspare', 7980),
    Allotment('newtest', 200),
    Allotment('newcustomersupport', 5000)
]


def generate_unique_codes(characters, code_length, number_of_codes, seed):
    random.seed(seed)
    all_codes = set()
    excludes=set()
    if os.path.exists(f'{excludes_filename}'):  # for topping up codes, anything in exclude.txt will be excluded
        print("Using excludes file")
        with open(f'{excludes_filename}', 'r+') as fp:
            rows = fp.read().split('\n')
            for row in rows:
                if row == '': continue
                excludes.add(row.strip())
                all_codes.add(row.strip())
    total_possible_codes= len(characters)**code_length-len(excludes)
    #Sense Check
    print(f"{total_possible_codes}/{number_of_codes}={total_possible_codes / number_of_codes}")
    if total_possible_codes / number_of_codes < 10:
        print(
            f"{total_possible_codes}/{number_of_codes}={total_possible_codes / number_of_codes}Are you sure you want to do this? That's not enough codes")

    while True:
        s = ''.join(random.choice(characters) for i in range(code_length))
        all_codes.add(s)
        if len(all_codes)-len(excludes) >= number_of_codes:
            codes=list(all_codes.difference(excludes))
            return codes

def split_codes(unique_codes, allotments):
    for allotment in allotments:
        allotment.codes = unique_codes[0:allotment.count]
        del unique_codes[0:allotment.count]

def generate():
    total = sum([allotment.count for allotment in allotments])
    codes = generate_unique_codes(characters, code_length, total, seed)
    codes = split_codes(codes, allotments)

    codes_done = {}
    for allotment in allotments:
        file = open(allotment.name+file_type, 'w')
        file.write(f'{codecsv_heading}\n')
        for code in allotment.codes:
            file.write(f"{code}\n")
            if code not in codes_done:
                codes_done[code] = True
            else:
                print("Hmm... this used to be an assert not thing but I changed it, did I break something?")
        file.close()

def split_to_groups(file_name=None):
    """Splits code into groups with one code being the 'master' for each group"""
    file_name=f"{allotments[0].name}{file_type}"
    book_length = 1200
    number_of_books=2600
    header_text="Cover_Code,Coupon_Code"
    code_list = []
    with open(file_name,'r') as code_import:
        code_import=[code.split()[0] for code in code_import]
        for code in code_import:
            if code!=codecsv_heading:
                code_list.append(code)
    #Sense check
    if len(code_list)<book_length*number_of_books+number_of_books:
        #checks if the there are enough codes for all vouches + all grouping codes for the book labels
        print ("Something is wrong, you don't have enough codes for the promo")

    more_spares= open(f'more-spares{file_type}', 'w') #just in case - this shouldn't be used

    with open(f'code_list{file_type}','w') as code_list_export:
        code_list_export.write(f"{header_text}\n")
        for i,code in enumerate(code_list):
            if i<number_of_books*book_length+number_of_books:
                if i==0 or (i)%(book_length+1)==0:
                    code_list_export.write(f"{code},\n")
                else:
                    code_list_export.write(f",{code}\n")
            else:
                code_list_export.close()
                more_spares.write(f"{code}\n")
    more_spares.close()

def split_to_multiple_files(input_file,file_length=None):
    book_length = 1200
    number_of_books = 2600
    original_file_length=number_of_books*book_length+number_of_books #plus the header line
    alt_book_size=int((original_file_length - number_of_books)/book_length/10)
    book_size=int(number_of_books/10)
    print (alt_book_size)
    print (book_size)
    if not file_length:
        file_length=book_size*book_length+book_size #plus the header line -
    smallfile = None
    file_name= open(input_file,'r')
    for count,line in enumerate(file_name):
        if count ==0:
            small_filename = f"small_file{count + file_length}.csv"
            smallfile = open(small_filename, 'w')
        if (count)  % file_length ==0:
            if smallfile:
                smallfile.close()
            small_filename=f"small_file{count+file_length}.csv"
            smallfile=open(small_filename,'w')
        if smallfile:
            if count % file_length==0 or count==0:
                smallfile.write('Cover_Code,Coupon_Code\n')
            smallfile.write(line)

def combine_files(export_name,*files):
    combined_file=open(export_name,'w')
    for filename in files:
        readfile=open(filename,'r')
        for line in readfile:
            combined_file.write(line)
        readfile.close()
    combined_file.close()



if __name__ == "__main__":
    # pass
    # os.chdir('944')
    # combine_files("excludes.csv",'Archive/codes-primary.csv','codes-spare.csv','codes-testandcustomerservice.csv')
    # split_to_multiple_files('code_list.csv')
    # split_to_groups('small_file240000.csv')
    generate()
    # split_to_groups()