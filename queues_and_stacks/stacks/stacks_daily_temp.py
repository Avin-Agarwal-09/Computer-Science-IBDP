#Given an array of integers temperatures represents the daily temperatures, 
#return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

def daily_temps(temps):
    n = len(temps)
    results = [0] * n
    stack = []
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            previous_index = stack.pop()
            results[previous_index] = i - previous_index
        stack.append(i)
    return results

temps = [1,0,10,5,2,3,4,20]
print(daily_temps(temps))