from analysis import load_data, average_humidity, total_rainfall, average_moving, cleandata, heighest_temp, lowest_temp
from visualization import plot_chart


df = load_data()

avg_humidity = average_humidity(df)
print("Average Humidity:", avg_humidity)

total = total_rainfall(df)
print("Total Rainfall:", total)

hig_val = heighest_temp(df)
print("Highest Temp = ", hig_val)

low_tem = lowest_temp(df)
print("Lowest Temp = ", low_tem)

df = average_moving(df)
print(df.head(7))

plot_chart(df)
