import matplotlib.pyplot as plt

def generate_piechart():
    labels = ['A', 'B', 'C']
    values = [152, 84, 31]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()