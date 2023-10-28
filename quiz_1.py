import pandas as pd
import matplotlib.pyplot as plt

#chavtvirtot faili
file_path = "C:/Applications/survey_results_public.csv"
df = pd.read_csv(file_path)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


columns = ["YearsCode", "Country", "DevType"]
subset_df = df[columns]
#aq vayenebt index-acias
df.set_index('Country', inplace=True)

#filtris dayeneba
#virchevt iset developerebs romlebsac 5 wlianze meti stazhi aqvt da arian fullstackebi
filtered_data = subset_df[(subset_df['YearsCode' > 5] & subset_df['DevType'].str.contains('full-stack'))]

filtered_data.loc['YearsCode'].head(50)

#sortireba qveynis, asakis da developeris tipis mixedvit
df[['Country', 'DevType', 'Age']].head(100)

#statistikis gamotvla
mean_value = df['Column2'].mean()
std_deviation = df['Column2'].std()
median_value = df['Column2'].median()
min_value = df['Column2'].min()
max_value = df['Column2'].max()

print(f"Mean: {mean_value}")
print(f"Standard Deviation: {std_deviation}")
print(f"Median: {median_value}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")

#chartis daxatva 
bar_data = df['Category'].value_counts()
bar_data.plot(kind='bar')
plt.title('Bar Chart')
plt.xlabel('YearsCode')
plt.ylabel('Age')
plt.show()

line_data = df.groupby('Year')['Value'].mean()
line_data.plot(kind='line')
plt.title('Line Chart')
plt.xlabel('YearsCode')
plt.ylabel('Age')
plt.show()







