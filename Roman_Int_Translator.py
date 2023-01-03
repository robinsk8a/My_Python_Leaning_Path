#This is a challenge from https://www.codewars.com/ where I needed to do code that alow me to translate natural numbers to roman numbers and the other wey around.
#Here you can find more solutions https://www.codewars.com/users/robinsk8a/completed_solutions


roman_number= {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

key_list = list(roman_number.keys())
val_list = list(roman_number.values())


def getrom_by_val(arr, value):
    arr.append(key_list[val_list.index(value)])
    

class RomanNumerals:
    
    def to_roman(val):
        if 0 < val < 4000:
            roman = [] 
            count_dig = len(str(val))

            for dig in str(val):
                count_dig -= 1
                pls_zero = ("0" * count_dig)
                digpls= (dig + pls_zero)
                if dig == "4" or dig == "9":
                    intdig = int(str(int(dig) + 1)   + pls_zero)
                    posdig = str(int(dig) + 1)
                    getrom_by_val(roman, int("1" + pls_zero))
                    getrom_by_val(roman, intdig)
                    val -= int(dig + pls_zero)
                else:
                    for key in reversed(roman_number):
                        while 0 < int(digpls) >= roman_number[key]:
                            roman.append(key)
                            digpls = int(digpls) -  roman_number[key]
                        
  
            return "".join(roman)

            
            

    def from_roman(roman_num):
        number_list = []
        for let in roman_num:
            number_list.append(roman_number[let])
        for i in range(0, len(number_list)-1):
            if number_list[i + 1] > number_list[i]:
                number_list[i+1] = number_list[i+1] - number_list[i]
                number_list[i] = 0
        return sum(number_list)
    
    
    
print(RomanNumerals.to_roman(146))
print(RomanNumerals.to_roman(1280))
print(RomanNumerals.to_roman(249))
print(RomanNumerals.to_roman(3782))
print(RomanNumerals.to_roman(4900))
print(RomanNumerals.to_roman(2040))

print(RomanNumerals.from_roman("CCXLVI"))
print(RomanNumerals.from_roman("MMMDCCLXXXII"))
print(RomanNumerals.from_roman("IV"))
