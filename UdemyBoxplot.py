import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    num_ale = random.randint(0,30)
    vetor.append(num_ale)

plt.boxplot(vetor)
plt.title("BoxPlot")
plt.show()