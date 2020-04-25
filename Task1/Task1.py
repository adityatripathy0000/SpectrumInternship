import numpy as np
import matplotlib.pyplot as plt
scores = {"Day 1": 100, "Day 2": 108, "Day 3":112, "Day 4":115, "Day 5":150,
          "Day 6":178, "Day 7": 143, "Day 8": 132, "Day 9":190, "Day 10": 235,
          "Day 11":253, "Day 12": 298, "Day 13": 328, "Day 14":390, "Day 15": 257,
          "Day 16":288, "Day 17": 393, "Day 18": 425, "Day 19":458, "Day 20": 450,
          "Day 21":473, "Day 22": 333, "Day 23": 452, "Day 24":490, "Day 25": 495,
          "Day 26":488, "Day 27": 543, "Day 28": 532, "Day 29":590, "Day 30": 605}

#Array containing values of scores dictionary
Scores = np.array(list(scores.values()))

#Array containing values from 1 to 30
Days = np.array(range(1, 31))

#Visualise Scores vs Days {x-axis : Scores, y-axis : Days}
plt.scatter(Scores, Days, color='red')
plt.plot(Scores, Days, color= 'blue')
plt.title('Scores Vs. Days')
plt.xlabel('Scores')
plt.ylabel('Days')
plt.show()

#Visualise Scores Vs Days  {x-axis : Days, y-axis : Scores}
plt.scatter(Days, Scores, color='red')
plt.plot(Days, Scores, color= 'blue')
plt.title('Scores Vs. Days')
plt.xlabel('Days')
plt.ylabel('Scores')
plt.show()

#Mean, Median, Min, Max of Billy's Scores
print('Mean : {}'.format(np.mean(Scores)))
print('Median : {}'.format(np.median(Scores)))
print('Min : {}'.format(np.min(Scores)))
print('Max : {}'.format(np.max(Scores)))