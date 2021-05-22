import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from python import Connection
import sentencias as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

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

#figmapanalisis1 = px.choropleth(df, locations = "departamento", scope = "Colombia", color = "numero_casos", color_continuous_scale = ["#99ccff","#ff3333"])

#analisis 2
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.analisis2(), con.connection)
con.closeConnection()
df = pd.DataFrame(query, columns=["grupo", "numero_casos"])
print(df)

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
df = pd.DataFrame(query, columns=["Genero", "Condena", "numero_casos"])

#graficas 

figBaranalisis4 = px.bar(df.head(20), x="Genero", y="numero_casos", title = "Barras Verticales Analisis 4")

figBarHanalisis4 = px.bar(df.head(25), y="Genero", x="numero_casos", orientation = 'h', title = "Barras Horizontales Analisis 4")

figpieanalisis4 = px.pie(df.head(25), values = "numero_casos", names = "Genero", title = "Pie Analisis 4")

figlineanalisis4 = px.line(df, x="Genero", y="numero_casos", title='Line Analisis 4')


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
    # dcc.Graph(
    #     id='Mapa',
    #     figure=figBarCasesAMRO
    # ),
   
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
    
    html.H2(children = 'Analisis3'),
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
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
