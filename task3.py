import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

def task3(name):
    data = pd.read_csv(name)
    data['Agency'].value_counts(sort=True).plot(kind='bar')
    plt.show()


task3('NYC_Jobs.csv')
#Вивести назви агентств та кількість вакансій, які вони
#подали. Використовуючи бібліотеку Matplotlib відобразити отримані дані
#у вигляді стовпцеві діаграми