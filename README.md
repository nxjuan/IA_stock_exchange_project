# IA_stock_exchange_project

# b3fileparser

A função dessa biblioteca é fazer o parser do arquivo com cotações históricas da B3, disponíveis em https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/

## Instalação

Instalação pode ser feita via pip

```
pip install b3fileparser
```

## Exemplo 1

```python
from b3fileparser.b3parser import B3Parser


parser = B3Parser.create_parser(engine='pandas')
dados_b3 = parser.read_b3_file('COTAHIST_A2023.TXT')
dados_b3
```

