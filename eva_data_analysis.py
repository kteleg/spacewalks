import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='utf-8')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

eva_df = pd.read_json(input_file, convert_dates=['date'])
eva_df['eva'] = eva_df['eva'].astype(float)

# Remove rows with missing values
eva_df.dropna(axis=0, inplace=True)

# Sort the DataFrame by the 'date' column in ascending order
eva_df.sort_values('date', inplace=True)
eva_df.to_csv(output_file, index=False)

# Convert 'duration' column (in HH:MM format) to total hours as a float
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
# Calculate cumulative time spent in space over the years
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()