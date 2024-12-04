import pandas as pd
import matplotlib.pyplot as plt


data ={
    'Music': [304, 257, 174, 214,69,
              317, 387, 47, 157, 0, 332, 308,
              317, 286, 236, 299, 206, 278, 188, 43,
              0, 0, 0, 0, 0],
    'No Music':[292, 270, 47, 288, 324,
                292, 364, 316, 287, 75,
                282, 149, 274, 319, 213, 3,
                324, 2, 128, 219, 94,
                164, 0, 0, 0]
}

df= pd.DataFrame(data)

plt.figure(figsize=(12, 6))

plt.subplot( 1, 2, 1)
plt.hist(df['Music'],  bins=10, color='purple', alpha=0.7, edgecolor='black')
plt.title(' Music')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)


plt.subplot(1, 2, 2)
plt.hist(df['No Music'], bins=10, color='red', alpha=0.7, edgecolor='black')
plt.title('No Music')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot( 1, 2, 1)
plt.scatter(df['Music'], [0] *len(df['Music']), color='purple', alpha=0.7, edgecolor='black')
plt.title('Music')
plt.yticks([])
plt.xlabel('Growth')
plt.axhline(0,color='black', lw=0.5 )


plt.subplot(1, 2, 2)
plt.scatter(df['No Music'], [0] * len(df['No Music']), color='red', alpha=0.7, edgecolors='black')
plt.title('No Music')
plt.yticks()
plt.xlabel('Growth')
plt.axhline(0, color='black',lw=0.5)

plt.tight_layout()
plt.show()