# Iniciando em Dash

Este guia apresenta as ideias discutidas e adotadas para criar um projeto utilizando o framework Dash, com o objetivo de construir aplicativos interativos e painéis de controle para visualização de dados. Ele é indicado para iniciantes e profissionais que desejam aprender a configurar e trabalhar com Dash de forma simples e organizada.

---

## O que é o Dash?
Dash é um **framework open-source** criado pela **Plotly**, utilizado para desenvolver **aplicações web interativas** com foco em visualização de dados. Ele é amplamente utilizado para criar dashboards e aplicações analíticas com uma interface amigável, sem a necessidade de conhecimento profundo em desenvolvimento web.

- **Baseado em:** Python (backend com Flask e frontend com React.js).
- **Principais aplicações:**
  - Dashboards interativos.
  - Visualizações de dados dinâmicas.
  - Aplicações para análise de dados e relatórios.

---

## Requisitos para Começar

1. **Python Instalado:** Certifique-se de que o Python está instalado em sua máquina.
2. **Ambiente Virtual (opcional, mas recomendado):**
   - Crie um ambiente virtual para isolar as dependências do projeto:
     ```bash
     python -m venv env
     ```
   - Ative o ambiente virtual:
     - Windows: `.     - Windows: `.\env\Scripts\activate`
     - Linux/Mac: `source env/bin/activate`
3. **Instale as Dependências:**
   - Instale as bibliotecas necessárias para o projeto:
     ```bash
     pip install dash plotly pandas
     ```

---

## Criando o Projeto Dash

1. **Estrutura Básica do Projeto:**
   Crie um arquivo `app.py` com o seguinte exemplo básico:

   ```python
   import dash
   from dash import dcc, html
   from dash.dependencies import Input, Output
   import plotly.express as px
   import pandas as pd

   # Criando uma aplicação Dash
   app = dash.Dash(__name__)

   # Dados de exemplo
   data = {
       "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"],
       "Vendas": [1000, 1500, 1200, 1700, 1600],
       "Lucro": [400, 500, 300, 600, 550],
   }
   df = pd.DataFrame(data)

   # Layout da aplicação
   app.layout = html.Div([
       html.H1("Dashboard Interativo - Vendas e Lucros"),
       dcc.Dropdown(
           id='dropdown-metrica',
           options=[
               {'label': 'Vendas', 'value': 'Vendas'},
               {'label': 'Lucro', 'value': 'Lucro'},
           ],
           value='Vendas',  # Valor padrão
           style={'width': '50%'}
       ),
       dcc.Graph(id='grafico-interativo'),
   ])

   # Callback para atualizar o gráfico
   @app.callback(
       Output('grafico-interativo', 'figure'),
       [Input('dropdown-metrica', 'value')]
   )
   def atualizar_grafico(metrica_selecionada):
       fig = px.line(
           df, x='Mês', y=metrica_selecionada, title=f'{metrica_selecionada} Mensais', markers=True
       )
       return fig

   # Executar o servidor
   if __name__ == '__main__':
       app.run_server(debug=True)
   ```

2. **Executando o Projeto:**
   Salve o arquivo como `app.py` e execute o seguinte comando no terminal:
   ```bash
   python app.py
   ```

   Acesse o navegador no endereço exibido (geralmente, `http://127.0.0.1:8050`).

---

## Gerenciando Dependências

1. **Criando o arquivo `requirements.txt`:**
   Use o comando para gerar uma lista de dependências do projeto:
   ```bash
   pip freeze > requirements.txt
   ```

2. **Reutilizando o arquivo `requirements.txt`:**
   Para recriar o ambiente em outra máquina ou reconfigurar o projeto, use:
   ```bash
   pip install -r requirements.txt
   ```

---

## Benefícios do Dash
- **Simplicidade:** Crie aplicações web usando apenas Python.
- **Flexibilidade:** Suporte a layouts dinâmicos e interações complexas.
- **Aplicabilidade:** Ideal para cientistas de dados, analistas e engenheiros de software.

---

## Considerações Finais
Este projeto introdutório é um ponto de partida para explorar as capacidades do Dash. Com ele, você pode criar dashboards mais complexos, integrar dados de APIs e adicionar mais interatividade conforme a necessidade.

 

