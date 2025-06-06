import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r"Students Social Media Addiction.csv") #copy the path of the csv file 
print("Missing values:\n", df.isnull().sum())

# 1. Addiction Score vs. Avg Daily Usage
plt.figure()
sns.scatterplot(data=df, x='Avg_Daily_Usage_Hours', y='Addicted_Score', hue='Gender', palette='coolwarm')
plt.title("Addicted Score vs. Daily Social Media Usage")
plt.xlabel("Avg Daily Usage (Hours)")
plt.ylabel("Addicted Score")
plt.tight_layout()

# 2. Addiction Score by Gender
plt.figure()
sns.boxplot(x='Gender', y='Addicted_Score', data=df, palette='Set2')
plt.title("Addiction Score Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Addicted Score")
plt.tight_layout()

# 3. Mental Health Score vs. Addiction Score
plt.figure()
sns.regplot(data=df, x='Addicted_Score', y='Mental_Health_Score', scatter_kws={'alpha':0.5}, line_kws={"color": "red"})
plt.title("Mental Health vs. Addiction Score")
plt.xlabel("Addicted Score")
plt.ylabel("Mental Health Score")
plt.tight_layout()

# 4. Sleep Hours vs. Addiction Score
plt.figure()
sns.violinplot(data=df, x='Affects_Academic_Performance', y='Sleep_Hours_Per_Night', palette='pastel')
plt.title("Sleep Hours by Academic Impact of Social Media")
plt.xlabel("Affects Academic Performance")
plt.ylabel("Sleep Hours per Night")
plt.tight_layout()

# 5. Most Used Platform vs. Average Usage Hours
plt.figure()
sns.barplot(data=df, x='Most_Used_Platform', y='Avg_Daily_Usage_Hours', estimator=np.mean, palette='muted')
plt.title("Average Daily Usage by Social Media Platform")
plt.xlabel("Most Used Platform")
plt.ylabel("Avg Daily Usage (Hours)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
