
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np


df = pd.read_csv(r"D:\tamilanskills\project7\traffic_management_dataset.csv")


print("Dataset Shape:", df.shape)
print("Columns:", df.columns)
print("Missing Values:\n", df.isnull().sum())


df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day_name()


plt.figure(figsize=(12,6))
sns.lineplot(x="hour", y="traffic_volume", data=df, estimator="mean", ci=None)
plt.title("Average Traffic Volume by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Traffic Volume")
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(x="day", y="traffic_volume", data=df, order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
plt.title("Traffic Volume by Day of Week")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12,6))
sns.barplot(x="weather_condition", y="traffic_volume", data=df)
plt.title("Traffic Volume vs Weather Condition")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(x="accident_reported", y="avg_vehicle_speed", data=df)
plt.title("Impact of Accidents on Vehicle Speed")
plt.xlabel("Accident Reported (0=No, 1=Yes)")
plt.ylabel("Average Vehicle Speed")
plt.show()


X = df[["hour"]]
y = df["traffic_volume"]

model = LinearRegression()
model.fit(X, y)


hours = np.array(range(24)).reshape(-1, 1)
predicted_volume = model.predict(hours)

plt.figure(figsize=(12,6))
plt.plot(hours, predicted_volume, marker="o", label="Predicted")
plt.title("Predicted Traffic Volume by Hour (Regression)")
plt.xlabel("Hour of Day")
plt.ylabel("Traffic Volume")
plt.legend()
plt.grid(True)
plt.show()
