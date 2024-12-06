def calcular_download(tamanho, velocidade):
    # Converte MB para Mb e calcula tempo em minutos
    return round((tamanho * 8) / velocidade / 60, 2)

def main():
    try:
        tamanho = float(input("Digite o tamanho do arquivo em MB: "))
        velocidade = float(input("Digite a velocidade da internet em Mbps: "))
        
        tempo = calcular_download(tamanho, velocidade)
        
        print(f"\nTempo de download: {tempo} minutos")
    
    except ValueError:
        print("Erro: Digite valores numéricos válidos.")

if __name__ == "__main__":
    main()