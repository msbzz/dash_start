import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Criando uma aplicação Dash
app = dash.Dash(__name__)

# Criando um DataFrame de exemplo
data = {
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"],
    "Vendas": [1000, 1500, 1200, 1700, 1600],
    "Lucro": [400, 500, 300, 600, 550],
}
df = pd.DataFrame(data)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Dashboard Interativo - Vendas e Lucros"),
    
    # Dropdown para seleção de métrica
    dcc.Dropdown(
        id='dropdown-metrica',
        options=[
            {'label': 'Vendas', 'value': 'Vendas'},
            {'label': 'Lucro', 'value': 'Lucro'},
        ],
        value='Vendas',  # Valor padrão
        style={'width': '50%'}
    ),
    
    # Gráfico interativo
    dcc.Graph(id='grafico-interativo'),
])

# Callback para atualizar o gráfico com base na métrica selecionada
@app.callback(
    Output('grafico-interativo', 'figure'),
    [Input('dropdown-metrica', 'value')]
)
def atualizar_grafico(metrica_selecionada):
    # Criando o gráfico com base na métrica selecionada
    fig = px.line(
        df,
        x='Mês',
        y=metrica_selecionada,
        title=f'{metrica_selecionada} Mensais',
        markers=True
    )
    return fig

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)