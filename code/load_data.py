import pandas as pd
import json

def demand_driven_aggregate_geotype_cost():
  ddagc = pd.read_csv("data/demand_driven_aggregate_geotype_cost.csv")
  df_list = []
  df_list.append(ddagc[(ddagc['strategy']=='Hybrid') & (ddagc['scenario']=='Scenario 1 (30 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Hybrid') & (ddagc['scenario']=='Scenario 2 (100 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Hybrid') & (ddagc['scenario']=='Scenario 3 (300 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Small Cells') & (ddagc['scenario']=='Scenario 1 (30 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Small Cells') & (ddagc['scenario']=='Scenario 2 (100 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Small Cells') & (ddagc['scenario']=='Scenario 3 (300 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Spectrum Integration') & (ddagc['scenario']=='Scenario 1 (30 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Spectrum Integration') & (ddagc['scenario']=='Scenario 2 (100 Mbps)')])
  df_list.append(ddagc[(ddagc['strategy']=='Spectrum Integration') & (ddagc['scenario']=='Scenario 3 (300 Mbps)')])
  return df_list

def demand_driven_municipality_capacity_results():
  ddmcr = pd.read_csv("data/demand_driven_municipality_capacity_results.csv")
  cities = json.load(open("data/townships.geojson", "r"))
  temp_code = {
      'Bergen (L.)':'0893',
      'Bergen (NH.)':'0373',
      'Dantumadiel':'1891',
      'Ferwerderadiel':'1722',
      'De Fryske Marren':'1921',
      'Groningen':'0014',
      'Hengelo':'0164',
      'Littenseradiel':'0140',
      'Menameradiel':'1908',
      'Sudwest-Fryslan':'1900',
      'Tytsjerksteradiel':'0737',
      'Utrecht':'0344',
  }
  city_code= {}
  for m in cities['features']:
      m["id"] = m["properties"]["code"]
      city_code[m['properties']['name']] = m['properties']['code']
  ddmcr['id']= ddmcr['municipalities'].apply(add_id)
  def add_id(x):
    if x in city_code.keys():
        return city_code[x]  
    elif x.split(',')[-1] in city_code.keys():
        return city_code[x.split(',')[-1]]
    elif x in temp_code:
        return temp_code[x]
    else:
        print(x)
        return 0

  return ddmcr, cities

def filter_data_for_map(data, scenario, strategy):
  data[(data['strategy']=='Hybrid') & (data['scenario']=='Scenario 1 (30 Mbps)')]

