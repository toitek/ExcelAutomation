import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/advertising.csv")
print(df.info())


# Create a scatter plot of TV and sales
plt.scatter(df['TV'], df['Sales'])
plt.xlabel('TV Advertising Spend')
plt.ylabel('Sales')
plt.show()