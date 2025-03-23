'''Alice has some cards with numbers written on them. She arranges
the cards in decreasing order, and lays them out face down in a sequence on a
table. She challenges Bob to pick out the card containing a given number by
turning over as few cards as possible. Write a function to help Bob locate the card.'''

def locate_card(cards,query):  #brute force solution (linear search)(O(n))
    position = 0
    print('cards:',cards)
    print('query:', query)

    while position < len(cards):
        print('position:', position)
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
    return -1

def locate_cards2(cards,query):  #optimal solution (binary search) keep in mind list is in decreasing order
    lo, hi = 0 , len(cards)-1
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]

        print("lo:", lo,"hi", hi, "mid", mid, ", mid_number:", mid_number)
        result = test_location(cards,query,mid)

        if result == 'found':
            return mid
        elif result ==  'left':
            hi = mid -1
        elif result == 'right':
            lo = mid+1

    return -1

def test_location(cards, query,mid):
    mid_number = cards[mid]
    print("mid: ", mid,", mid_number:", mid_number)
    if mid_number == query:
        if mid-1>=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number <query:
        return 'left'
    else:
        return 'right'


test = {'input':{'cards':[13,11,10,7,4,3,1,0],'query':7},'output':3}  # test case stored as dictionary
#print(locate_card(test['input']['cards'], test['input']['query']) == test['output'])

tests = []
tests.append(test)
tests.append({'input':{'cards':[13,11,10,7,4,3,1,0],'query':1},'output': 6})
tests.append({'input':{'cards':[4,2,1,-1],'query':4},'output': 0})
tests.append({'input':{'cards':[3,-1,-9,-127],'query':-127},'output': 3})
tests.append({'input':{'cards':[6],'query':6},'output': 0})
tests.append({'input':{'cards':[9,7,5,2,-9],'query':4},'output': -1})
tests.append({'input':{'cards':[],'query':1},'output': -1})
tests.append({'input':{'cards':[8,6,6,6,6,6,3,2,2,2,2,0,0,0],'query':3},'output': 6})
tests.append({'input':{'cards':[8,6,6,6,6,6,3,2,2,2,2,0,0,0],'query':6},'output': 1})

result = locate_card(test['input']['cards'], test['input']['query'])
#print(result)

from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases
#evaluate_test_case(locate_card,test)
#evaluate_test_cases(locate_card,tests)


cards6 = tests[6]['input']['cards']
query6 = tests[6]['input']['query']

#print(locate_card(cards6,query6))
#evaluate_test_cases(locate_card,tests)

#evaluate_test_cases(locate_cards2,tests)
evaluate_test_cases(locate_cards2,tests)


