import matplotlib.pyplot as plt

labels = ['Electronics', 'Clothing', 'Home Decor', 'Books']
sizes = [35, 25, 20, 20]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
explode = (0.1, 0, 0, 0)  

plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=140)

plt.axis('equal')

plt.title('Sales Distribution in Different Categories')

plt.show()
