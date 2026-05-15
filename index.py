python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the SAIFI dataset
data = pd.read_csv('SAIFI.csv')

def plot_saifi_trends(data):
    # Convert Year column to datetime
    data['Year'] = pd.to_datetime(data['Year'], format='%Y')

    # Set Year as index
    data.set_index('Year', inplace=True)

    # Plot SAIFI trends
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x=data.index, y='SAIFI', marker='o')
    plt.title('Annual SAIFI (System Average Interruption Frequency Index) Trends (2013-2025)')
    plt.xlabel('Year')
    plt.ylabel('SAIFI (Interruptions per Customer)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_saifi_trends(data)
