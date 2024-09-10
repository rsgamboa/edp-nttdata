def analise_vendas(vendas):
    # Total de vendas, média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas) if vendas else 0
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Entrada usuario 
    entrada = input()
    # Lista de entrada:
    vendas = list(map(int, entrada.split(',')))
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))