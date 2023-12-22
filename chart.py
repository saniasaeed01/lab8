import matplotlib.pyplot as plt
import pandas as pd

csv_filename = "dataset.csv"
df = pd.read_csv(csv_filename)

names = df['Name']
ages = df['Age']

salaries = df['Salary']

plt.bar(names, salaries, color='blue')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary Distribution')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()