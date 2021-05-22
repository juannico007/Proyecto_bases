import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from python import Connection
import sentencias as sql
import unidecode
from urllib.request import urlopen
import json
import plotly.graph_objects as go

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    counties = json.load(response)

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#analisis 1
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.analisis1(), con.connection)
con.closeConnection()
df = pd.DataFrame(query, columns=["departamento", "numero_casos"])

#graficas

figBaranalisis1 = px.bar(df.head(20), x="departamento", y="numero_casos", title = "Barras Verticales Analisis 1")

figBarHanalisis1 = px.bar(df.head(25), y="departamento", x="numero_casos", orientation = 'h', title = "Barras Horizontales Analisis 1")

figpieanalisis1 = px.pie(df.head(25), values = "numero_casos", names = "departamento", title = "Pie Analisis 1")

figlineanalisis1 = px.line(df, x="departamento", y="numero_casos", title='Line Analisis 1')

locs = []
y = []
for i in range(len(df)-1):
    dep = df.loc[i, 'departamento']
    if dep == "Nariño":
        locs.append(dep.upper())
    elif dep == "BOGOTÁ D. C.":
        locs.append("SANTAFE DE BOGOTA D.C")
    else:
        locs.append(unidecode.unidecode(dep.upper()))
    y.append(df.loc[i, 'numero_casos'])

for loc in counties['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']

figmapanalisis1 = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=locs,
                    z=y,
                    colorscale=["#FFD700","#800000"],
                    colorbar_title="Casos"))

figmapanalisis1.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328})

#analisis 2
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.analisis2(), con.connection)
con.closeConnection()
df = pd.DataFrame(query, columns=["grupo", "numero_casos"])

#graficas 

figBaranalisis2 = px.bar(df.head(20), x="grupo", y="numero_casos", title = "Barras Verticales Analisis 2")

figBarHanalisis2 = px.bar(df.head(25), y="grupo", x="numero_casos", orientation = 'h', title = "Barras Horizontales Analisis 2")

figpieanalisis2 = px.pie(df.head(25), values = "numero_casos", names = "grupo", title = "Pie Analisis 2")

figlineanalisis2 = px.line(df, x="grupo", y="numero_casos", title='Line Analisis 2')

#analisis 3
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.analisis3(), con.connection)
con.closeConnection()
df = pd.DataFrame(query, columns=["etapa", "numero_casos"])

#graficas 

figBaranalisis3 = px.bar(df.head(20), x="etapa", y="numero_casos", title = "Barras Verticales Analisis 3")

figBarHanalisis3 = px.bar(df.head(25), y="etapa", x="numero_casos", orientation = 'h', title = "Barras Horizontales Analisis 3")

figpieanalisis3 = px.pie(df.head(25), values = "numero_casos", names = "etapa", title = "Pie Analisis 3")

figlineanalisis3 = px.line(df, x="etapa", y="numero_casos", title='Line Analisis 3')

#analisis 4
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.analisis4(), con.connection)
con.closeConnection()
df = pd.DataFrame(query, columns=["genero" , "condena", "numero_casos"])

#graficas 

figBaranalisis4 = px.bar(df.head(20), x= "genero", y="numero_casos", color = "condena", title = "Barras Verticales Analisis 4")

figBarHanalisis4 = px.bar(df.head(25), y= "genero", x="numero_casos", color = "condena", orientation = 'h', title = "Barras Horizontales Analisis 4")

figpieanalisis4 = px.pie(df.head(25), values = "numero_casos", names = "genero", title = "Pie Analisis 4")

figlineanalisis4 = px.line(df, x= "genero", y="numero_casos", title='Line Analisis 4')



# Layout
app.layout = html.Div(children=[
    html.H1(children='Analisis conteo de victimas'),

    html.H2(children = 'Analisis1'),
    dcc.Graph(
        id='Barras Verticales 1',
        figure=figBaranalisis1
    ),
    dcc.Graph(
        id='Barras Horizontales 1',
        figure=figBarHanalisis1
    ),
    dcc.Graph(
        id='Pie 1',
        figure=figpieanalisis1
    ),
    dcc.Graph(
        id='Lineas 1',
        figure=figlineanalisis1
    ),
    dcc.Graph(
        id='Mapa 1',
        figure=figmapanalisis1
    ),
   
    html.H3(children = 'Analisis2'),
    dcc.Graph(
        id='Barras Verticales 2',
        figure=figBaranalisis2
    ),
    dcc.Graph(
        id='Barras Horizontales 2',
        figure=figBarHanalisis2
    ),
    dcc.Graph(
        id='Pie 2',
        figure=figpieanalisis2
    ),
    dcc.Graph(
        id='Lineas 2',
        figure=figlineanalisis2
    ),
    
    html.H4(children = 'Analisis3'),
    dcc.Graph(
        id='Barras Verticales 3',
        figure=figBaranalisis3
    ),
    dcc.Graph(
        id='Barras Horizontales 3',
        figure=figBarHanalisis3
    ),
    dcc.Graph(
        id='Pie 3',
        figure=figpieanalisis3
    ),
    dcc.Graph(
        id='Lineas 3',
        figure=figlineanalisis3
    ),

    html.H5(children = 'Analisis4'),
    dcc.Graph(
        id='Barras Verticales 4',
        figure=figBaranalisis4
    ),
    dcc.Graph(
        id='Barras Horizontales 4',
        figure=figBarHanalisis4
    ),
    dcc.Graph(
        id='Pie 4',
        figure=figpieanalisis4
    ),
    dcc.Graph(
        id='Lineas 4',
        figure=figlineanalisis4
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
