import math

def calcular_compra_tinta(area):
    # Calcula litros necessários com 10% de folga
    litros = math.ceil((area / 6) * 1.1)
    
    # Opção 1: Apenas latas de 18 litros
    latas = math.ceil(litros / 18)
    preco_latas = latas * 80
    
    # Opção 2: Apenas galões de 3,6 litros
    galoes = math.ceil(litros / 3.6)
    preco_galoes = galoes * 25
    
    # Opção 3: Mistura de latas e galões
    latas_mista = math.floor(litros / 18)
    galoes_mista = math.ceil((litros - (latas_mista * 18)) / 3.6)
    preco_misto = (latas_mista * 80) + (galoes_mista * 25)
    
    return litros, latas, preco_latas, galoes, preco_galoes, latas_mista, galoes_mista, preco_misto

def main():
    try:
        # Solicita a área a ser pintada
        area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
        
        # Obtém os resultados da compra de tinta
        litros, latas, preco_latas, galoes, preco_galoes, latas_mista, galoes_mista, preco_misto = calcular_compra_tinta(area)
        
        # Apresenta os resultados
        print(f"\nÁrea a ser pintada: {area} m²")
        print(f"Litros de tinta necessários (com 10% de folga): {litros}")
        
        print("\nOpções de Compra:")
        print(f"1. Apenas latas de 18 litros:")
        print(f"   Latas: {latas}")
        print(f"   Preço total: R$ {preco_latas:.2f}")
        
        print(f"\n2. Apenas galões de 3,6 litros:")
        print(f"   Galões: {galoes}")
        print(f"   Preço total: R$ {preco_galoes:.2f}")
        
        print(f"\n3. Mistura de latas e galões:")
        print(f"   Latas de 18 litros: {latas_mista}")
        print(f"   Galões de 3,6 litros: {galoes_mista}")
        print(f"   Preço total: R$ {preco_misto:.2f}")
    
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido para a área.")

if __name__ == "__main__":
    main()