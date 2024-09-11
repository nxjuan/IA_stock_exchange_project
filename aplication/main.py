from get.get_data import get_stock_data
from output.plot_data import plot_stock_data

def main():
    # Símbolo para B3SA3

    symbol = "B3SA3.SA"  # Símbolo correto para yfinance

    # Obtenha os dados
    df = get_stock_data(symbol)
    df = df[df.index.dayofweek < 5]  # Remover finais de semana
    df = df.between_time('09:00', '17:30') # Filtrar para o horário de 9:00 até 17:30
    df

    # Verifique se os dados foram obtidos com sucesso antes de tentar plotar
    if df is not None and not df.empty:
        # Gere o gráfico
        plot_stock_data(df)
    else:
        print("Não foi possível obter os dados do ativo.")





if __name__ == "__main__":
    main()  