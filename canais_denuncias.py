"""
Arquivo: canais_denuncias.py
Projeto: MINI-GAME — Maio Laranja (Pique ECA)
Responsável original: Jeniffer Thalya Ferreira do Nascimento
Função do arquivo: exibir canais de denúncia e apoio.

Ajuste feito na integração:
- Mantivemos o visual e as mensagens originais do grupo.
- Apenas colocamos limpeza de tela para funcionar melhor dentro do menu principal.
"""

# Importa função auxiliar para limpar a tela antes de exibir os canais.
from utilitarios import limpar_tela


def get_canais_de_denuncia():
    """Retorna uma lista com os canais de denúncia cadastrados."""

    canais = [
        {
            "nome": "Disque 100",
            "numero": "0800 55 0140",
            "funcao": "Denúncia anônima de abuso sexual, maus-tratos e exploração",
            "disponibilidade": "24h, todos os dias"
        },
        {
            "nome": "Polícia Militar",
            "numero": "190",
            "funcao": "Emergência policial",
            "disponibilidade": "24h, todos os dias"
        },
        {
            "nome": "Conselho Tutelar",
            "numero": "Consulte sua cidade",
            "funcao": "Proteção e orientação à criança",
            "disponibilidade": "Horário comercial"
        },
        {
            "nome": "Ligue 180",
            "numero": "180",
            "funcao": "Atendimento à mulher e a criança",
            "disponibilidade": "24h, todos os dias"
        },
        {
            "nome": "Samu",
            "numero":"192",
            "funcao":"Emergência médica",
            "disponibilidade":"24h, todos os dias"
        }
    ]
    return canais


def mostrar_menu_denuncia():
    """Mostra os canais de denúncia na tela."""

    # Limpa a tela para os canais aparecerem organizados.
    limpar_tela()

    canais = get_canais_de_denuncia()
    
    print("\n" + "=" * 50)
    print("🛑 CANAIS OFICIAIS DE DENÚNCIA 🛑")
    print("=" * 50)
    print("Anote os canais abaixo:\n")
    
    for i, canal in enumerate(canais, 1):
        print(f"{i}. {canal['nome']} ")
        print(f"📞 Contato: {canal['numero']}")
        print(f"📝 Função: {canal['funcao']}")
        print(f"⏰ Disponibilidade: {canal['disponibilidade']}\n")
    
    print("=" * 50)
    input("Pressione ENTER para continuar!")


# Este bloco permite testar este arquivo separadamente.
if __name__ == "__main__":
    mostrar_menu_denuncia()
