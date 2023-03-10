
# how to create the following nested list ???
'''
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

'''

# initialize
matrix = []

for i in range(5): # -> index = 0 to 4, 取不到5

    # Append an empty sublist inside the list
    matrix.append([]) # 确定append的数据结构

    for j in range(5):
        matrix[i].append(j)

print(matrix)


# same output with the following code
matrix = [[j for j in range(5)] for i in range(5)] # [[里面一层循环] 外面一层循环]

print(matrix)



''' Example of loop a nestedlist'''

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

flatten_planets = []

for sublist in planets:
    for planet in sublist:

        if len(planet) < 6:
            flatten_planets.append(planet)


print(flatten_planets)