from IA_stock_exchange_project.aplication.get.get_data import get_stock_data
from IA_stock_exchange_project.aplication.output.plot_data import plot_stock_data


# Símbolo para B3SA3

symbol = "B3SA3.SA"  # Símbolo correto para yfinance

# Obtenha os dados
df = get_stock_data(symbol)

# Verifique se os dados foram obtidos com sucesso antes de tentar plotar
if df is not None and not df.empty:
    # Gere o gráfico
    plot_stock_data(df)
else:
    print("Não foi possível obter os dados do ativo.")
