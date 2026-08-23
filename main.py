# ==============================================================================
# SISTEMA DE GESTÃO - COFFEE SHOPS TIA ROSA
# Disciplina: Desenvolvimento de Sistema em Python
# ==============================================================================

# Cardápio organizado por categorias
cardapio = {
    "Bebidas": {
        1: {"nome": "Café Coado Artesanal", "preco": 6.00, "ingredientes": "Grãos selecionados, água filtrada"},
        2: {"nome": "Cappuccino Tradicional", "preco": 10.50, "ingredientes": "Café expresso, leite vaporizado, cacau, canela"}
    },
    "Comidas": {
        3: {"nome": "Pão de Queijo Mineiro", "preco": 5.00, "ingredientes": "Polvilho, queijo canastra, ovos, leite"},
        4: {"nome": "Bolo de Cenoura c/ Choco", "preco": 8.00, "ingredientes": "Cenoura, farinha, açúcar, cobertura de cacau"}
    }
}

clientes = {}  # Estrutura: {cpf: {"nome": str, "pontos": int}}
pedidos = []   # Estrutura: [{"id": int, "cliente": str, "itens": list, "total": float}]

def buscar_item_por_id(item_id):
    """Busca um item no cardápio pelo seu ID numérico."""
    for categoria, itens in cardapio.items():
        if item_id in itens:
            return itens[item_id]
    return None

def exibir_menu_principal():
    print("\n" + "="*50)
    print("        ☕ COFFEE SHOPS TIA ROSA - GESTÃO ☕        ")
    print("="*50)
    print("  [1] Consultar Cardápio")
    print("  [2] Cadastrar Cliente (Programa de Fidelidade)")
    print("  [3] Registrar Novo Pedido")
    print("  [4] Relatório de Vendas Diárias")
    print("  [0] Sair")
    print("="*50)

def consultar_cardapio():
    print("\n" + "="*60)
    print(f"{'CARDÁPIO DIGITAL':^60}")
    print("="*60)
    
    for categoria, itens in cardapio.items():
        print(f"\n--- {categoria.upper()} ---")
        print(f"{'ID':<4} | {'Item':<28} | {'Preço':<10}")
        print("-" * 60)
        for item_id, info in itens.items():
            print(f"[{item_id}]  | {info['nome']:<28} | R$ {info['preco']:>6.2f}")
            print(f"      └ Ingredientes: {info['ingredientes']}")
    print("="*60)

def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTE ---")
    cpf = input("Digite o CPF do cliente (apenas números): ").strip()
    if cpf in clientes:
        print(f"\n⚠️ Cliente já cadastrado: {clientes[cpf]['nome']} | Pontos acumulados: {clientes[cpf]['pontos']}")
        return
    
    nome = input("Digite o nome completo do cliente: ").strip()
    clientes[cpf] = {"nome": nome, "pontos": 0}
    print(f"\n✅ Cliente '{nome}' cadastrado com sucesso no Programa de Fidelidade!")

def registrar_pedido():
    print("\n--- NOVO PEDIDO ---")
    cpf = input("Informe o CPF do cliente (ou aperte ENTER para Consumidor Final): ").strip()
    
    nome_cliente = "Consumidor Final"
    if cpf in clientes:
        nome_cliente = clientes[cpf]['nome']
        print(f"Cliente identificado: {nome_cliente}")
    elif cpf:
        print("⚠️ CPF não encontrado. O pedido será registrado como Consumidor Final.")

    itens_pedido = []
    total_pedido = 0.0

    consultar_cardapio()

    while True:
        try:
            opcao = int(input("\nDigite o ID do item para adicionar (ou 0 para FINALIZAR): "))
            if opcao == 0:
                break
            
            item = buscar_item_por_id(opcao)
            if item:
                itens_pedido.append(item['nome'])
                total_pedido += item['preco']
                print(f"  └ ✅ {item['nome']} adicionado ao carrinho! (Subtotal: R$ {total_pedido:.2f})")
            else:
                print("  └ ❌ ID inválido. Escolha um número presente no cardápio.")
        except ValueError:
            print("  └ ❌ Entrada inválida! Digite apenas números.")

    if itens_pedido:
        id_pedido = len(pedidos) + 1
        pedidos.append({
            "id": id_pedido,
            "cliente": nome_cliente,
            "itens": itens_pedido,
            "total": total_pedido
        })
        
        # Sistema de Pontuação: R$ 10,00 = 1 ponto
        if cpf in clientes:
            pontos_ganhos = int(total_pedido // 10)
            clientes[cpf]['pontos'] += pontos_ganhos

        print("\n" + "="*45)
        print(f"      RESUMO DO PEDIDO #{id_pedido}")
        print("="*45)
        print(f"Cliente: {nome_cliente}")
        print("Itens solicitados:")
        for i, item in enumerate(itens_pedido, 1):
            print(f"  {i}. {item}")
        print("-" * 45)
        print(f"TOTAL A PAGAR: R$ {total_pedido:.2f}")
        if cpf in clientes:
            print(f"Pontos acumulados nesta compra: +{int(total_pedido // 10)}")
        print("="*45)
    else:
        print("\nNenhum item foi selecionado. Pedido cancelado.")

def relatorio_vendas():
    print("\n" + "="*50)
    print(f"{'RELATÓRIO DE VENDAS DIÁRIAS':^50}")
    print("="*50)
    
    if not pedidos:
        print("Nenhuma venda registrada até o momento.")
        return

    faturamento_total = 0.0
    print(f"{'ID':<5} | {'Cliente':<25} | {'Total':<10}")
    print("-" * 50)
    for p in pedidos:
        print(f"{p['id']:<5} | {p['cliente']:<25} | R$ {p['total']:>6.2f}")
        faturamento_total += p['total']
    
    print("-" * 50)
    print(f"Total de Pedidos Realizados: {len(pedidos)}")
    print(f"Faturamento Total do Dia:    R$ {faturamento_total:.2f}")
    print("="*50)

def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            consultar_cardapio()
        elif opcao == '2':
            cadastrar_cliente()
        elif opcao == '3':
            registrar_pedido()
        elif opcao == '4':
            relatorio_vendas()
        elif opcao == '0':
            print("\nEncerrando o sistema Coffee Shops Tia Rosa... Até logo! ☕")
            break
        else:
            print("\nOpção inválida! Selecione um número do menu.")

if __name__ == "__main__":
    main()
