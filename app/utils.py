def clear_data(x):
  print('~~~~~~~~')
  target_keys = ['2022 Population', '2020 Population', 
                 '2015 Population', '2010 Population', 
                 '2000 Population', '1990 Population', 
                 '1980 Population', '1970 Population']
  new_data = data[x]
  print(new_data)
  print('~~~~~~~~')
  graph_data={z:int(new_data[z]) for z in new_data if z in
              target_keys}
  print(graph_data)
  print(graph_data['2022 Population'])
  print(type(graph_data['2022 Population']))

def data_for_pie(data):
  #data->[{}, {}, {}, ...]
  data2 = {data['Country/Territory']:data['World Population Percentage']
          for data in data}
  print(data2)

def get_pop_by_country(country_dic):
  country = {
    '2022': int(country_dic['2022 Population']),
    '2020': int(country_dic['2020 Population']),
    '2015': int(country_dic['2015 Population']),
    '2010': int(country_dic['2010 Population']),
    '2000': int(country_dic['2000 Population']),
    '1990': int(country_dic['1990 Population']),
    '1980': int(country_dic['1980 Population']),
    '1970': int(country_dic['1970 Population'])    
  }
  years = country.keys()
  pop = country.values()
  return years, pop

def population_by_country(country, data):
  result = list(filter(lambda x: x['Country/Territory'] == country, data))
  return result
