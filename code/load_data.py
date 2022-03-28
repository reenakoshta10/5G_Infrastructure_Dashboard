import pandas as pd
import json
import locale

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
  def add_id(x):
    if x in city_code.keys():
        return city_code[x]  
    elif x.split(',')[-1] in city_code.keys():
        return city_code[x.split(',')[-1]]
    elif x in temp_code:
        return temp_code[x]
    else:
        return 0
  for m in cities['features']:
      m["id"] = m["properties"]["code"]
      city_code[m['properties']['name']] = m['properties']['code']
  ddmcr['id']= ddmcr['municipalities'].apply(add_id)
  
  return ddmcr, cities

def convert_str_to_float(num):
    num = num.replace(" ","")
    if num[0]=="-" and len(num)==1:
        return 0
    elif num[0]=="-":
        num = num[1:]
        return int(num.replace(',','')) * (-1)
    else:
        return int(num.replace(',',''))

def demand_driven_aggregate_cost_results():
  ddacr = pd.read_csv("data/demand_driven_aggregate_cost_results.csv")
  ddacr['cost']= ddacr['cost'].apply(convert_str_to_float)
  return ddacr

def supply_driven_analysis_results():
  sdar = pd.read_csv("data/supply_driven_analysis_results.csv", index_col=0)
  df_all= sdar[sdar['spectrum_availability']== 'All'].groupby('geotype')[["max_user_demand_lte_mbps_km2", "max_user_demand_5g_mbps_km2"]].mean()
  df_limited= sdar[sdar['spectrum_availability']== 'Limited'].groupby('geotype')[["max_user_demand_lte_mbps_km2", "max_user_demand_5g_mbps_km2"]].mean()
  return df_all, df_limited