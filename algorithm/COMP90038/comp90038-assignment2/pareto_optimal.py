from __future__ import print_function

point = [
    (1, 11), (2, 1), (2, 6), (4, 3), (4, 8), (5,10),
    (6, 6), (8, 7), (10, 4), (11, 2)
]
#(11, 4), (11, 7), (11, 10), (11, 11), (12, 11)

X = []
Y = []

sorted(point, key=lambda x: x[0])
print(point[0])
temp_point = point[len(point) - 1]
y_max = temp_point[1]
pareto_optimal = []
pareto_optimal.append(temp_point)
for i in range(len(point) - 2, -1, -1):
    test_point = point[i]
    print(i)
    if test_point[1] >= y_max:
        pareto_optimal.append(test_point)
        y_max = test_point[1]

print(pareto_optimal)

"""
// find a set of pareto optimals point of S
// Input : S, a finite set of n distinct point P1(x1, y1), P2(x2, y2), ..., Pn(xn, yn)
//         S is an 2 dimensional array -> [[x1, y1],[x2,y2], ..., [xn, yn]]
// Output: a set of pareto optimal point
function FIND_PARETO_OPTIMAL(S)
  sorted_s <- QUICK_SORT(S[x]) // sort point by x-axis
  len <- length(S)
  pareto_optimal <- [] // initiate empty array
  pareto_optimal.push(sorted_s[len - 1]) // put last element (highest x-axis value)
  y_max <- sorted_s[len - 1][1] // store y-axis from highest x-axis point

  for len - 2 to 0 do
      // compare max y-axis with the selected point y-axis
      if point[i][1] > y_max then 
          pareto_optimal.push(point)
          y_max = point[y]

   return pareto_optimal
"""

"""
QuickSort will take O(n log n) and last comparison will running n times, so overall complexity will be O(n log n)
"""

