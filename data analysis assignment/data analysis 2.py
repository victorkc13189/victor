import matplotlib.pyplot as plt
import pandas as pd

data={
    'sex': ['Male', 'Male', 'Male', 'Male', 'Male','Male', 'Male', 'Male',
            'Male', 'Male', 'Female', 'Female', 'Female', 'Female',
            'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Breath Holding Time': [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27,
                            59.09, 51.15, 58.32, 22.22, 30.57, 17.47, 22.39,
                            26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    'Height': [184, 182, 180, 191, 189, 181, 180, 170, 176, 185, 175, 158,
               166, 175, 160, 165, 166, 170, 170, 172]
}

df = pd.DataFrame(data)
plt.figure(figsize=(12, 6))

plt.subplot( 1, 2 ,1)
plt.hist(df['Breath Holding Time'], bins=10, color='pink', edgecolor='black', alpha=0.7)
plt.title('Histogram of Breath Holding Times')
plt.xlabel('Breath Holding Time')
plt.ylabel('Height')

plt.subplot(1, 2, 2)

plt.scatter(df[df['sex']== 'Male']['Breath Holding Time'],
            [0] * sum(df['sex']== 'Male'),
            color='green', label='Male', alpha=0.5)


plt.scatter(df[df['sex'] == 'Female']['Breath Holding Time'],
            [1] *sum(df['sex'] == 'Female'),
                     color='blue', label='Female', alpha=0.5)

plt.title('Side-by-Side Dot Plot Of Breath Holding Times by Sex')
plt.yticks( [0, 1],['Male', 'Female'] )
plt.xlabel('Breath Holding Time (seconds')
plt.legend()

plt.tight_layout()
plt.show()
