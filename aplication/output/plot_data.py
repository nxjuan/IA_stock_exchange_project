import matplotlib.pyplot as plt

# Função para plotar gráfico de linha
def plot_stock_data(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Preço de Fechamento')
    plt.title('B3SA3 - Preço por Hora (Última Semana)')
    plt.xlabel('Data e Hora')
    plt.ylabel('Preço de Fechamento (R$)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()