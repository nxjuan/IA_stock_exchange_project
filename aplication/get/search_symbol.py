import yfinance as yf

def find_stock_symbol(query):
    # Tentar buscar o símbolo diretamente
    try:
        stock = yf.Ticker(query)
        # Verificar se há dados históricos, o que indica que o símbolo é válido
        hist = stock.history(period="1d")
        if not hist.empty:
            return query, stock.info['longName']
    except Exception as e:
        pass

    # Se não encontrou nada, sugerir possíveis símbolos relacionados
    print("O símbolo exato não foi encontrado. Tentando sugerir símbolos similares...")

    # Buscar símbolos que contenham a string fornecida
    search_results = yf.utils.get_tickers(query)
    if search_results:
        print("Sugestões de símbolos:")
        for result in search_results[:5]:  # Mostrar apenas os 5 primeiros resultados
            try:
                stock = yf.Ticker(result)
                hist = stock.history(period="1d")
                if not hist.empty:
                    print(f"{result}: {stock.info['longName']}")
            except Exception as e:
                pass
        return None
    else:
        print("Nenhuma correspondência encontrada.")
        return None

def main():
    # Receber o nome ou símbolo da ação do usuário
    query = input("Digite o nome ou símbolo da ação: ").strip().upper()

    # Tentar encontrar o símbolo
    result = find_stock_symbol(query)

    if result:
        symbol, long_name = result
        print(f"\nAção encontrada!\nSímbolo: {symbol}\nNome: {long_name}")
    else:
        print("\nNão foi possível encontrar uma correspondência exata.")

if __name__ == "__main__":
    main()
