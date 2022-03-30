from curses import color_content
from load_data import demand_driven_aggregate_cost_results, demand_driven_aggregate_geotype_cost, demand_driven_municipality_capacity_results, supply_driven_analysis_results
import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide")
st.title('5G infrastructure Analysis')


@st.cache
def load_data(data):
    if data == "ddagc":
      df_list= demand_driven_aggregate_geotype_cost()
    elif data == "ddmcr":
      df_list = demand_driven_municipality_capacity_results()
    elif data == "ddacr":
      df_list = demand_driven_aggregate_cost_results()
    elif data == "sdar":
      df_list = supply_driven_analysis_results()
    return df_list


selection = st.sidebar.radio(
     "Show analysis based on ",
     ('Capacity Margin by Scenario',
     'Costs Per Square Kilometer by Geotype', 
     'Aggregate cost by Geotype', 
     'Scenario-wise investment cost',
     'Maximum average capacity per user'
     ))

if selection == 'Costs Per Square Kilometer by Geotype':
      df_list = load_data("ddagc")

      fig = make_subplots(rows=3, cols=3, shared_yaxes=True, shared_xaxes=True,
                    subplot_titles=("Hybrid","Small Cells", "Spectrum Integration"),
                   horizontal_spacing = 0.05,
                   vertical_spacing= 0.05)
      i = 0
      for col in range(1,4):
          for row in range(1,4):
              df = df_list[i]
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['RAN.macro']/df['area_km2'], 
                                  name='Macro RAN',
                                  hovertemplate = 'Macro RAN<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="green"),
                                  legendgroup="Macro RAN",
                                  text=((df['RAN.macro']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  showlegend=True if i==0 else False
                            ), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['backhaul.macro']/df['area_km2'], 
                                  name='Macro Backhaul',
                                  hovertemplate = 'Macro Backhaul<br>Geo Type: %{x}<br>Cost:%{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="red"),
                                  legendgroup="Macro Backhaul",
                                  text=((df['backhaul.macro']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['civil.works.macro']/df['area_km2'], 
                                  name='Macro Civil Works',
                                  hovertemplate = 'Macro Civil Works<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="yellow"),
                                  legendgroup="Macro Civil Works",
                                  text=((df['civil.works.macro']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['RAN.small.cells']/df['area_km2'], 
                                  name='Small Cells RAN',
                                  hovertemplate = 'Small Cells RAN<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="orange"),
                                  legendgroup="Small Cells RAN",
                                  text=((df['RAN.small.cells']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['civil.works.small']/df['area_km2'], 
                                  name='Small Civil Works',
                                  hovertemplate = 'Small Civil Works<br>Geo Type: %{x}<br>Cost:%{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="blue"),
                                  legendgroup="Small Civil Works",
                                  text=((df['civil.works.small']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              i+=1

      fig.update_yaxes(range=[0, 1.05])
      fig.update_xaxes(title_text="Geotype", row=3, col=1)
      fig.update_xaxes(title_text="Geotype", row=3, col=2)
      fig.update_xaxes(title_text="Geotype", row=3, col=3)
      fig.update_yaxes(title_text="Investment Cost(Million €) <br>Scenario 1", row=1, col=1)
      fig.update_yaxes(title_text="Investment Cost(Million €) <br>Scenario 2", row=2, col=1)
      fig.update_yaxes(title_text="Investment Cost(Million €) <br>Scenario 3", row=3, col=1)
      fig.update_layout(height=900, width=1000, title_text="Costs Per Square Kilometer by Geotype", barmode='stack')
      st.plotly_chart(fig)
elif selection == 'Aggregate cost by Geotype':
      df_list = load_data("ddagc")
      
      fig = make_subplots(rows=3, cols=3, shared_yaxes=True, shared_xaxes=True,
                          subplot_titles=("Hybrid","Small Cells", "Spectrum Integration"),
                        
                        horizontal_spacing = 0.05,
                        vertical_spacing= 0.05)
      i = 0
      for col in range(1,4):
          for row in range(1,4):
              df = df_list[i]
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['RAN.macro'], 
                                  name='Macro RAN',
                                  text=((df['RAN.macro']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  hovertemplate = 'Macro RAN<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="green"),
                                  legendgroup="Macro RAN",
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['backhaul.macro'], 
                                  name='Macro Backhaul',
                                  text=((df['backhaul.macro']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  hovertemplate = 'Macro Backhaul<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="red"),
                                  legendgroup="Macro Backhaul",
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['civil.works.macro'], 
                                  name='Macro Civil Works',
                                  text=((df['civil.works.macro']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  hovertemplate = 'Macro Civil Works<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="yellow"),
                                  legendgroup="Macro Civil Works",
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['RAN.small.cells'], 
                                  name='Small Cells RAN',
                                  text=((df['RAN.small.cells']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  hovertemplate = 'Small Cells RAN<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="orange"),
                                  legendgroup="Small Cells RAN",
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              fig.add_trace(go.Bar(x=df['geotype'], 
                                  y=df['civil.works.small'], 
                                  name='Small Civil Works',
                                  text=((df['civil.works.small']/df['cost'])*100).apply(lambda x: '{0:1.2f}%'.format(x)),  
                                  hovertemplate = 'Small Civil Works<br>Geo Type: %{x}<br>Cost: %{y:.2f} Million €<br>Investment:%{text}<extra></extra>',
                                  marker = dict(color="blue"),
                                  legendgroup="Small Civil Works",
                                  showlegend=True if i==0 else False), 
                            row=row, col=col)
              i+=1

      fig.update_yaxes(range=[0, 800])
      fig.update_xaxes(title_text="Geotype", row=3, col=1)
      fig.update_xaxes(title_text="Geotype", row=3, col=2)
      fig.update_xaxes(title_text="Geotype", row=3, col=3)
      fig.update_yaxes(title_text="Investment Cost(Million €) <br>Scenario 1", row=1, col=1)
      fig.update_yaxes(title_text="Investment Cost(Million €) <br>Scenario 2", row=2, col=1)
      fig.update_yaxes(title_text="Investment Cost(Million €) <br>Scenario 3", row=3, col=1)
      fig.update_layout(height=900, width=1000, title_text="Aggregate cost by Geotype", barmode='stack')
      st.plotly_chart(fig)
elif selection == 'Capacity Margin by Scenario':
      ddmcr, cities = load_data("ddmcr")
      strategy = st.sidebar.selectbox("Select Strategy", ddmcr['strategy'].unique())
      scenario = st.sidebar.selectbox("Select Scenario", ddmcr['scenario'].unique())
      df = ddmcr[(ddmcr['strategy']==strategy) & (ddmcr['scenario']==scenario)]
      fig = px.choropleth(
        df,
        locations="id",
        geojson=cities,
        color="capacity_margin",
        hover_name="municipalities",
        hover_data= {'capacity_margin':True, 'id':False},
        title=f"Capacity Margin for {strategy} {scenario}",
        color_continuous_scale=px.colors.diverging.RdYlGn,
        range_color=[-100, 100]
        )
      fig.update_geos(fitbounds="locations", visible=False)
      fig.update_layout(height=800, width=900)
      fig.update_coloraxes(colorbar_title="Capacity Margin<br>  (Gbps)", cmid=0)
      st.plotly_chart(fig)
elif selection == 'Scenario-wise investment cost':
    df = load_data("ddacr")
    fig = px.bar(df, x="scenario", y="cost", color="strategy",
                text_auto=True
                                  )
    fig.update_yaxes(title_text="Total Cost (Euros)")                                
    fig.update_layout(height=600, width=950, title_text="Scenario-wise investment cost", xaxis={'categoryorder':'total descending'})
    
    st.plotly_chart(fig)
elif selection == 'Maximum average capacity per user':
    df_all, df_limited = load_data('sdar')
    fig = make_subplots(rows=1, cols=2, shared_yaxes=True, 
                        subplot_titles=("All available spectrum","Limited spectrum"))

    fig.add_trace(
        go.Bar(x=df_all.index,
        y=df_all['max_user_demand_lte_mbps_km2'],
              name= "4G", legendgroup="4G",
              marker = dict(color="red"),
              text=round(df_all['max_user_demand_lte_mbps_km2']),
              hovertemplate = '4G<br>Geo Type: %{x}<br>Capacity: %{y:d} Mbps<br><extra></extra>'
                                  ),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(x=df_all.index,
        y=df_all['max_user_demand_5g_mbps_km2'],
              name= "5G", legendgroup="5G",
              marker = dict(color="blue"),
              text=round(df_all['max_user_demand_5g_mbps_km2']),
              hovertemplate = '5G<br>Geo Type: %{x}<br>Capacity: %{y:d} Mbps<br><extra></extra>'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=df_limited.index,
        y=df_limited['max_user_demand_lte_mbps_km2'],
              name= "4G", legendgroup="4G", showlegend=False,
              marker = dict(color="red"),
              text=round(df_limited['max_user_demand_lte_mbps_km2']),
              hovertemplate = '4G<br>Geo Type: %{x}<br>Capacity: %{y:d} Mbps<br><extra></extra>'),
        row=1, col=2
    )
    fig.add_trace(
        go.Bar(x=df_limited.index,
        y=df_limited['max_user_demand_5g_mbps_km2'],
              name= "5G", legendgroup="5G", showlegend=False,
              marker = dict(color="blue"),
              text=round(df_limited['max_user_demand_5g_mbps_km2']),
              hovertemplate = '5G<br>Geo Type: %{x}<br>Capacity: %{y:d} Mbps<br><extra></extra>'),
        row=1, col=2
    )
    
    fig.update_xaxes(title_text="Geotype", row=1, col=1)
    fig.update_xaxes(title_text="Geotype", row=1, col=2)
    fig.update_yaxes(title_text="Capacity (Mbps per User)", row=1, col=1)
    fig.update_layout(height=600, width=950, title_text="Maximum average capacity per user", barmode='stack')
    st.plotly_chart(fig)
else:
     st.sidebar.write("Please select an option from above.")

