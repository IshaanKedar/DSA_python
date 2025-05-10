'''You're in charge of selecting a football (soccer) team from a large pool of players.
Each player has a cost, and a rating. You have a limited budget. What is the highest total rating of a team that fits within your budget. Assume that there's no minimum or maximum team size.'''


t0 = {
    'input':{
        'capacity':165,'weights':[23,31,29,44,53,38,63,85,89,82],
        'profits':[92,57,49,68,69,43,67,84,87,72]
    },
    'output':309
    }
t1 = {
    'input':{
        'capacity':3,'weights':[4,5,6],
        'profits':[1,2,3]
    },
    'output':0
    }


t2 = {
    'input':{
        'capacity':4,'weights':[4,5,1],
        'profits':[1,2,3]
    },
    'output':3
    }

knaptests = [t0,t1,t2]
def max_profit_recursive(weights, profits, capacity, idx = 0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx]+max_profit_recursive(weights, profits, capacity-weights[idx], idx+1)
        return max(option1,option2)
    
print(max_profit_recursive(t0['input']['weights'],t0['input']['profits'],t0['input']['capacity'])==t0['output'])

from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(max_profit_recursive,knaptests)

