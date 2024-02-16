#IMPORTANDO PACOTES
import analise
from dash import Dash, html, dash_table


#INICIALIZANDO O APP (Dash constructor)
app = Dash(__name__)

#LAYOYT DO APP
app.layout = html.Div([
    html.Div(children='Meu Primeiro app com Dados'),
    dash_table.DataTable(data=janeiro_df.to_dict('records'), page_size=10)
])

#RODANDO O APP
if __name__ == '__main__':
    app.run(debug=True)
