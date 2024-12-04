import matplotlib.pyplot as plt

categories = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
values = [0.28, 0.18, 0.08, 0.28, 0.18]

plt.barh(categories, values, color='green')

plt.title('Barchart')
plt.xlabel('Proportion of Total')
plt.ylabel('categories')

plt.show()
