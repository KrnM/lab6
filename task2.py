import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)


def task2(name):
    data = pd.read_csv(name)
    print(data[:10])
    print(data['Agency'][:10])
    print(data[['Agency', 'Business Title', 'Work Location 1']])



task2('NYC_Jobs.csv')
#Вивести перші 10 записів датасету. Вивести значення
#стовпця “Agency” для перших десяти записів. Вивести значення стовпців
#“Agency”, “Business Title” та “Work Location 1” для всіх записів датасету.
