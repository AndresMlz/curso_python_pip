import matplotlib.pyplot as plt

def generate_barchart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_piechart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['W', 'L', 'B']
  values = [40, 40, 20]
  #generate_barchart(labels, values)
  generate_piechart(labels, values)