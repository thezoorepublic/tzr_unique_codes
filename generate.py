#!/usr/bin/env python
# generate.py
#
#

import random
import os
def lazy_write(filename, outlist):
    print('Writing %d codes to %s' % (len(outlist), filename))
    with open(filename, 'w') as outfile:
        outfile.write('\r'.join(outlist))
        outfile.write('\r')
def generate():
    INCLUDED_CHARACTERS='CDFHJKLMNPRTXZ3479' #Avoids ambiguous characters and vowels
    CODE_LENGTH=9
    ADDITIONAL = 2600
    PRIMARY = 3120000+ADDITIONAL
    TEST = 5200
    SPARE=312000

    NUMBER_OF_CODES=PRIMARY+TEST+SPARE
    SPLIT=True #Splits the codes generated into Primary, Test and Spare


    POOL = (len(INCLUDED_CHARACTERS)**CODE_LENGTH)
    SANITY = POOL/NUMBER_OF_CODES
    print(POOL, SANITY)
    if SANITY < 10:
        print('ooooh, are you sure?')


    excludes = set()
    all_codes = set()
    if os.path.exists('exclude.txt'): #for topping up codes, anythign in exclude.txt will be excluded
        print("Using excludes file")
        with open('exclude.txt', 'rU+') as fp:
            rows = fp.read().split('\n')
            for row in rows:
                if row == '': continue
                excludes.add(row.strip())
                all_codes.add(row.strip())


    random.seed(1)
    while True:
        s = ''.join(random.choice(INCLUDED_CHARACTERS) for i in range(CODE_LENGTH))
        all_codes.add(s)
        if len(all_codes) - len(excludes) >= NUMBER_OF_CODES:
            break



    codes = list(all_codes.difference(excludes))

    if not SPLIT:
        lazy_write('codes-all.txt', codes)

    if SPLIT:
        primary = codes[0:PRIMARY]
        test = codes[PRIMARY:PRIMARY + TEST]
        spare = codes[PRIMARY+TEST:]
        lazy_write('codes-primary.csv', primary)
        lazy_write('codes-test.csv', test)
        lazy_write('codes-spare.csv', spare)
def lazy_write(filename, outlist):
    print('Writing %d codes to %s' % (len(outlist), filename))
    with open(filename, 'w') as outfile:
        outfile.write('\r'.join(outlist))
        outfile.write('\r')

def split_to_groups():
    """Splits code into groups with one code being the 'master' for each group"""
    book_length = 1200
    number_of_books=2600
    header_text="Cover_Code,Coupon_Code"
    code_list = []
    with open('codes-primary.csv','r') as code_import:
        for in_code in code_import:
            code_list.append(in_code.split()[0])

    if len(code_list)<book_length*number_of_books+number_of_books:
        #checks if the there are enough codes for all vouches + all grouping codes for the book labels
        print ("Something is wrong, you don't have enough codes for the promo")
    more_spares= open('more-spares.csv', 'w')
    with open('code_list.csv','w') as code_list_export:
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

if __name__ == '__main__':
    # generate()
    split_to_groups()