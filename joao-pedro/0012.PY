class ControleMarmitas:
    def __init__(self):
        self.estoque = {
            'arroz': 0,    
            'feijao': 0,   
            'carne': 0,    
            'salada': 0    
        }
        
        self.porcao_por_marmita = {
            'arroz': 100,
            'feijao': 50,
            'carne': 25,
            'salada': 10
        }
    
    def adicionar_estoque(self, ingrediente, quantidade):
        """Adiciona quantidade ao estoque do ingrediente especificado"""
        if ingrediente in self.estoque:
            self.estoque[ingrediente] += quantidade
            print(f"Adicionado {quantidade}g de {ingrediente}. Estoque atual: {self.estoque[ingrediente]}g")
        else:
            print("Ingrediente inválido!")
    
    def verificar_estoque(self):
        """Mostra o estoque atual de todos os ingredientes"""
        print("\n=== ESTOQUE ATUAL ===")
        for ingrediente, quantidade in self.estoque.items():
            print(f"{ingrediente.capitalize()}: {quantidade}g")
    
    def calcular_marmitas_possiveis(self):
        """Calcula quantas marmitas podem ser feitas com o estoque atual"""
        marmitas_possiveis = []
        for ingrediente, quantidade in self.estoque.items():
            if self.porcao_por_marmita[ingrediente] > 0:
                marmitas = quantidade // self.porcao_por_marmita[ingrediente]
                marmitas_possiveis.append(marmitas)
        
        if not marmitas_possiveis:
            return 0
        return min(marmitas_possiveis)
    
    def vender_marmita(self, quantidade):
        """Registra a venda de uma quantidade de marmitas"""
        marmitas_possiveis = self.calcular_marmitas_possiveis()
        
        if quantidade <= 0:
            print("Quantidade inválida!")
            return False
            
        if quantidade > marmitas_possiveis:
            print(f"Não há ingredientes suficientes. Só é possível fazer {marmitas_possiveis} marmita(s).")
            return False
        
        for ingrediente in self.estoque:
            self.estoque[ingrediente] -= self.porcao_por_marmita[ingrediente] * quantidade
        
        print(f"\n✅ {quantidade} marmita(s) vendida(s) com sucesso!")
        print(f"Marmitas restantes possíveis: {self.calcular_marmitas_possiveis()}")
        return True

def menu():
    print("\n=== CONTROLE DE MARMITAS ===")
    print("1. Adicionar ingredientes ao estoque")
    print("2. Ver estoque atual")
    print("3. Vender marmita(s)")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    sistema = ControleMarmitas()

    while True:
        opcao = menu()
        
        if opcao == '1':
            print("\n=== ADICIONAR AO ESTOQUE ===")
            print("1. Arroz (100g por marmita)")
            print("2. Feijão (50g por marmita)")
            print("3. Carne (25g por marmita)")
            print("4. Salada (10g por marmita)")
            escolha = input("Escolha o ingrediente (ou 0 para voltar): ")
            
            if escolha == '0':
                continue
                
            ingredientes = ['arroz', 'feijao', 'carne', 'salada']
            try:
                if escolha in ['1', '2', '3', '4']:
                    quantidade = float(input(f"Quantos gramas de {ingredientes[int(escolha)-1]} deseja adicionar? "))
                    sistema.adicionar_estoque(ingredientes[int(escolha)-1], quantidade)
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, insira um número válido.")
                
        elif opcao == '2':
            sistema.verificar_estoque()
            print(f"\nMarmitas possíveis de fazer: {sistema.calcular_marmitas_possiveis()}")
            
        elif opcao == '3':
            try:
                quantidade = int(input("Quantas marmitas deseja vender? "))
                sistema.vender_marmita(quantidade)
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
                
        elif opcao == '4':
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    print("=== SISTEMA DE CONTROLE DE MARMITAS ===")
    print("Bem-vindo ao sistema de controle de marmitas!")
    main()