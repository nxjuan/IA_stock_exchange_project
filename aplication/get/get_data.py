import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf


# Função para obter os dados de uma semana atrás até hoje usando yfinance
def get_stock_data(symbol):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # Baixar os dados usando yfinance
    df = yf.download(symbol, start=start_date, end=end_date, interval="1m")
    
    return df