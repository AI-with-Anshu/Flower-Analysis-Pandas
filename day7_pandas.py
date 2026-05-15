import pandas as pd
import matplotlib.pyplot as plt

data = {
    'name': ['Rose','Sunflower','Lotus','Rose','Sunflower','Lotus','Rose','Sunflower','Lotus'],
    'petal_length': [1.4, 3.5, 4.2, 1.5, 3.8, 4.5, 1.3, 3.6, 4.1],
    'color': ['Red','Yellow','Pink','Red','Yellow','Pink','Red','Yellow','Pink'],
    'price': [50, 30, 70, 55, 35, 75, 48, 32, 68],
    'beautiful': [True, True, True, True, False, True, True, True, False]
}

df = pd.DataFrame(data)

print("=== Full Table ===")
print(df)
print("\n=== First 3 rows ===")
print(df.head(3))
print("\n=== Shape ===")
print(df.shape)
print("\n=== Info ===")
print(df.info())
print("\n=== Statistics ===")
print(df.describe())
print("\n=== Only Rose ===")
print(df[df['name'] == 'Rose'])
print("\n=== Price greater than 50 ===")
print(df[df['price'] > 50])
print("\n=== Sort according to price ===")
print(df.sort_values('price', ascending=False))
print("\n=== Average price of every flower ===")
print(df.groupby('name')['price'].mean())
print("\n=== Most expensive flower ===")
print(df.loc[df['price'].idxmax()])

df['price_per_cm'] = df['price'] / df['petal_length']
print("\n=== Price per cm ===")
print(df[['name','price','petal_length','price_per_cm']].head())
print("\n=== Missing values ===")
print(df.isnull().sum())

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
avg_price = df.groupby('name')['price'].mean()
axes[0].bar(avg_price.index, avg_price.values, color=['#E53E3E','#D97706','#16A34A'])
axes[0].set_title("Average Price per Flower")
axes[0].set_ylabel("Price (Rs)")
axes[0].set_xlabel("Flower Name")

for name, color in zip(['Rose','Sunflower','Lotus'], ['#E53E3E','#D97706','#16A34A']):
    subset = df[df['name'] == name]
    axes[1].scatter(subset['petal_length'], subset['price'], label=name, color=color, s=100)

axes[1].set_title("Petal Length vs Price")
axes[1].set_xlabel("Petal Length (cm)")
axes[1].set_ylabel("Price (Rs)")
axes[1].legend()

plt.tight_layout()
plt.savefig("day7_results.png", dpi=150)
plt.show()
print("Figure saved!")