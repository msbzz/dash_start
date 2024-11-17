# Importando as bibliotecas necessárias
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

# Função 1: Calcular o total de vendas
def calcular_total_vendas():
    return df["Vendas"].sum()

# Função 2: Criar um gráfico de barras
def criar_grafico_barras(metrica_selecionada):
    return px.bar(
        df,
        x="Mês",
        y=metrica_selecionada,
        title=f"{metrica_selecionada} Mensais (Gráfico de Barras)",
        color="Mês",
    )

# Layout da aplicação
app.layout = html.Div([
    html.H1("Dashboard Interativo - Vendas e Lucros"),
    
    # Exibição do total de vendas
    html.Div(id='total-vendas', style={'margin-bottom': '20px'}),

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

    # Botão para alternar o tipo de gráfico
    dcc.RadioItems(
        id='tipo-grafico',
        options=[
            {'label': 'Gráfico de Linhas', 'value': 'linha'},
            {'label': 'Gráfico de Barras', 'value': 'barra'},
        ],
        value='linha',
        style={'margin-top': '20px'}
    ),

    # Gráfico interativo
    dcc.Graph(id='grafico-interativo'),
])

# Callback para atualizar o total de vendas
@app.callback(
    Output('total-vendas', 'children'),
    Input('dropdown-metrica', 'value')
)
def atualizar_total_vendas(metrica_selecionada):
    if metrica_selecionada == "Vendas":
        total = calcular_total_vendas()
        return f"Total de Vendas: R$ {total}"
    return "Total de Lucro não calculado."

# Callback para atualizar o gráfico
@app.callback(
    Output('grafico-interativo', 'figure'),
    [Input('dropdown-metrica', 'value'),
     Input('tipo-grafico', 'value')]
)
def atualizar_grafico(metrica_selecionada, tipo_grafico):
    if tipo_grafico == 'linha':
        # Gráfico de linha
        return px.line(
            df,
            x='Mês',
            y=metrica_selecionada,
            title=f'{metrica_selecionada} Mensais (Gráfico de Linha)',
            markers=True
        )
    elif tipo_grafico == 'barra':
        # Chama a função para criar um gráfico de barras
        return criar_grafico_barras(metrica_selecionada)

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True,port=8052)
