# dictionaries are used to store key-value pairs

phone_numbers = {'aakash':'99099010','hemanth':'023290342','siddhanth':'4303242423'}

print(phone_numbers['aakash'])

phone_numbers['vishal'] = '12431421431'
phone_numbers['aakash'] = '1232321'

print(phone_numbers)

for name in phone_numbers:
    print('name: ',name,', phone_no: ',phone_numbers[name])

#hash table usins list or array to store the key-value pairs
