import charts
import read_csv
import utils
data = read_csv.read_csv('./world_population.csv')
print('Select a chart to display ')
print('1 for bar chart, population of a country of your choice')
print('2 for pie chart of South America population by country')
print('3 for pie chart of the world population by country')

choice = int(input('-->'))
while choice != 1 and choice != 2 and choice != 3:
  print('Wrong number, try again')
  print('Select a chart to display ')
  print('1 for bar chart, population of a country of your choice')
  print('2 for pie chart of South America population by country')
  print('3 for pie chart of the world population by country')
  choice = int(input('-->'))

def barchart(data):
  country = input('Type country -->>')
  print('Generating chart...')
  country_dic = utils.population_by_country(country, data)
  res = country_dic[0]
  years, pop = utils.get_pop_by_country(res)
  charts.generate_barchart(country, years, pop)
  
def data_for_pie(data):
  print('Generating chart...')
  #data->[{}, {}, ..., {}]
  data2 = {data['Country/Territory']:data['World Population Percentage']
          for data in data}
  #print(data2)
  c_names = list(data2.keys())
  percentages = list(data2.values())
  percentages_int = []
  for i in percentages:
    percentages_int.append(float(i))
  charts.generate_piechart(c_names, percentages_int)

def piechart_p(data):
  print('Generating chart...')
  data = list(filter(lambda k: k['Continent'] == 'South America', data))
  countries = list(map(lambda k: k['Country/Territory'], data))
  porcen = list(map(lambda k: k['World Population Percentage'], data))
  charts.generate_piechart(countries, porcen)

if __name__ == '__main__':
  if choice == 1:
    barchart(data)
  elif choice == 2:
    piechart_p(data)
  else:
    data_for_pie(data)