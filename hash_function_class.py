max_hash_table_size = 4096


    




data_list = [None]*4096

for item in data_list:
    assert item == None

#hashing function converts no numeric data types to numbers to be used as list indices
def get_index(Data_list,a_string):
    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result+= a_number

    list_index = result % len(data_list)
    return list_index

# #insert
# data_list[get_index(data_list,'hemanth')] = ('hemanth','989983494')

# #retreive
# idx = get_index(data_list,'hemanth')
# key,value = data_list[idx]
# print(key,value)

# #list comprehension

# pairs = [kv[0] for kv in data_list if kv is not None]
# print(pairs)

#creating class for this
class hashtable:
    def __init__(self, max_size = max_hash_table_size):
        self.data_list = [None] * max_size

    def insert(self,key,value):
        idx = get_index(self.data_list,key)
        self.data_list[idx] = (key,value)

    def find(self,key):
        idx = get_index(self.data_list,key)
        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            key,value = kv
            return value
        
    def update(self,key,value):
        idx = get_index(self.data_list,key)
        self.data_list[idx] = (key,value)

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
    
basic_table = hashtable(max_size=1024)

basic_table.insert('aakash','234234242')
basic_table.insert('hemanth','909090909')

print(basic_table.find('hemanth'))

basic_table.update('aakash','333333')

print(basic_table.list_all())

#handling collisions (linear probing)



def get_valid_index(data_list, key):
    idx = get_index(data_list,key)

    while True:
        kv = data_list[idx]

        if kv == None:
            return idx
        k,v = kv
        if k == key:
            return idx
        idx+=1

        if idx == len(data_list):
            idx = 0

class probinghashtable:
    def __init__(self, max_size = max_hash_table_size):
        self.data_list = [None] * max_size

    def insert(self,key,value):
        idx = get_valid_index(self.data_list,key)
        self.data_list[idx] = (key,value)

    def find(self,key):
        idx = get_valid_index(self.data_list,key)
        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            key,value = kv
            return value
        
    def update(self,key,value):
        idx = get_valid_index(self.data_list,key)
        self.data_list[idx] = (key,value)

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
    
probing_table = probinghashtable()
probing_table.insert('listen','99')

print(probing_table.find('listen'))

probing_table.insert('silent',200)

print(probing_table.find('listen'))
print(probing_table.find('silent'))

probing_table.insert('listen',101)

print(probing_table.find('listen') == 101)

print(probing_table.list_all())
