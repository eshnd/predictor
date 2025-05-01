import math
import random

datapoints = [ # features, output, reward
    [1, 2, 7, 13, 18],
    [2, 5, 11, 17, 19],
    [7, 6, 12, 14, 21]
]

input_features = [8, 9, 14] # features

def narwhal(input_features, datapoints_old): 
    datapoints = datapoints_old
    combined = []
    for th in datapoints:
        combined += th
    combined += input_features
    maxc = max(th)
    minc = min(th)

    for j in range(len(datapoints)):
        for i in range(len(datapoints[j])):
            datapoints[j][i] = (datapoints[j][i] - minc) / (maxc - minc)
    for i in range(len(input_features)):
        input_features[i] = (input_features[i] - minc) / (maxc - minc)
    
    closest_points = []

    for point in datapoints:
        to_sqrt = 0

        for i in range(len(input_features)):
            to_sqrt += pow((input_features[i] - point[i]), 2)
        
        distance = math.sqrt(to_sqrt)
        closest_points.append([point, distance])
    
    def by_distance(x):
        return x[1]

    closest_points.sort(key=by_distance)
    first_closest = closest_points[0][0]
    second_closest = closest_points[1][0]

    for i in range(len(first_closest)):
        if first_closest[i] == second_closest[i]:
            first_closest[i] *= 0.99999

    new_point = [[input_features[0]]]

    for i in range(len(input_features) - 1):
        a = input_features[i+1]

        while i >= 0:
            slope = (first_closest[i+1] - second_closest[i+1]) / (first_closest[i] - second_closest[i])
            a = (a - (first_closest[i+1] - (slope * first_closest[i])))/slope
            i -= 1

        new_point.append([a])

    for j in range(len(new_point)):
        for i in range(len(first_closest) - 1):
            slope = (first_closest[i+1] - second_closest[i+1]) / (first_closest[i] - second_closest[i])
            new_point[j].append((slope * new_point[j][i]) + (first_closest[i+1] - (slope * first_closest[i])))
    
    closest_points = []

    for point in new_point:
        to_sqrt = 0

        for i in range(len(input_features)):
            to_sqrt += pow((input_features[i] - point[i]), 2)
        
        distance = math.sqrt(to_sqrt)
        closest_points.append([point, distance])

    closest_points.sort(key=by_distance)
    preoutput = closest_points[0][0]

    if preoutput[-1] < first_closest[-1]:
        preoutput[-2] = preoutput[-2]*.7 + first_closest[-2]*.3
    elif preoutput[-1] < second_closest[-1]:
        preoutput[-2] = preoutput[-2]*.7 + second_closest[-2]*.3

    avgreward = 0
    for thing in datapoints:
        avgreward += thing[-1]
    avgreward /= len(datapoints)

    experiment = 1 + (random.randint(-int((100 - avgreward)/2), int((100-avgreward)/2))/500)

    for i in range(len(preoutput)):
        preoutput[i] = (preoutput[i] * (maxc - minc)) + minc
    
    output = preoutput[-2] * experiment

    return output
