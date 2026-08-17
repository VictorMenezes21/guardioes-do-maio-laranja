"""
Arquivo: orientacoes_e_campanha.py
Projeto: MINI-GAME — Maio Laranja (Pique ECA)
Responsável original: Isabela Evellyn Lança Martins
Função do arquivo: exibir informações sobre a campanha e orientações de prevenção.

Ajuste feito na integração:
- Mantivemos os textos originais e as mensagens mais bonitas do arquivo enviado pelo grupo.
- Apenas acrescentamos limpeza de tela e pausa para funcionar bem junto com o main.py.
"""

# Importa funções auxiliares para organizar a exibição no terminal.
from utilitarios import limpar_tela


def mostrar_orientacoes():
    """Mostra orientações importantes para crianças, adolescentes, pais e responsáveis."""

    # Limpa a tela para a leitura ficar mais confortável.
    limpar_tela()

    print(f"\n{'=' * 60}")
    print("🛡️ ORIENTAÇÕES IMPORTANTES 🛡️".center(60))
    print(f"{'=' * 60}")

    print("""
👦👧 CRIANÇAS E ADOLESCENTES TÊM DIREITO À PROTEÇÃO!

• Seu corpo é seu e ninguém pode tocar em você sem sua permissão.

• Caso alguém faça você se sentir desconfortável,
  com medo ou ameaçado, procure ajuda imediatamente.

• Nunca guarde segredos que causem tristeza,
  medo ou insegurança.

• Converse com pais, responsáveis, professores
  ou outro adulto de confiança.

• Na internet, nunca compartilhe informações pessoais
  com desconhecidos.

• Se presenciar alguma situação suspeita,
  denuncie. Sua atitude pode proteger uma vida.

• Lembre-se: pedir ajuda é um ato de coragem.

🧡 Você não está sozinho(a)!
🧡 Sempre existe alguém disposto a ajudar.
          
============================================================

👨‍👩‍👧 ORIENTAÇÕES PARA PAIS E RESPONSÁVEIS

• Mantenha diálogo constante com seus filhos.

• Demonstre interesse pela rotina, amizades
  e atividades realizadas por eles.

• Oriente sobre segurança na internet e redes sociais.

• Observe mudanças repentinas de comportamento,
  isolamento, medo excessivo ou queda no rendimento escolar.

• Ensine que o corpo possui limites e que ninguém
  pode ultrapassá-los.

• Escute sem julgar e acolha qualquer relato
  de desconforto ou violência.

• Conheça os canais oficiais de denúncia.

• Em caso de suspeita, não ignore os sinais.
  Procure ajuda especializada imediatamente.

============================================================

🧡 PROTEGER É UM ATO DE AMOR.
          
🛡️ Seja um Guardião da Infância.
🛡️ Sua atitude pode fazer a diferença.

        """)
    
    print("=" * 60)
    input("\nPressione ENTER para voltar ao menu...")


def mostrar_campanha():
    """Mostra informações sobre a campanha Maio Laranja."""

    # Limpa a tela para a leitura ficar mais confortável.
    limpar_tela()

    print(f"\n{'=' * 60}")
    print("🧡 CAMPANHA MAIO LARANJA 🧡".center(60))
    print(f"{'=' * 60}")

    print("""
🌼 O QUE É O MAIO LARANJA?

O Maio Laranja é uma campanha nacional de conscientização
 e combate ao abuso e à exploração sexual de crianças e adolescentes.

📅 O dia 18 de maio foi escolhido como o
Dia Nacional de Combate ao Abuso e à Exploração Sexual
de Crianças e Adolescentes.

🎯 OBJETIVOS DA CAMPANHA

• Informar a população sobre o tema.
• Incentivar a prevenção.
• Estimular denúncias.
• Fortalecer a rede de proteção.
• Garantir os direitos das crianças e adolescentes.

🛡️ Toda criança merece crescer com segurança,
respeito e dignidade.
          
============================================================

💡 A conscientização é a principal ferramenta de prevenção.

🧡 Denuncie.
🧡 Oriente.
🧡 Proteja.

Juntos podemos construir um ambiente mais seguro
para crianças e adolescentes.

🌻 Seja parte dessa causa.
🌻 Seja um Guardião da Infância.
          
        """)
    
    print("=" * 60)
    input("\nPressione ENTER para voltar ao menu...")


# Este bloco permite testar este arquivo separadamente.
if __name__ == "__main__":
    while True:
        print("\n=== TESTE ORIENTAÇÕES ===")
        print("1 - Campanha")
        print("2 - Orientações")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            mostrar_campanha()

        elif opcao == "2":
            mostrar_orientacoes()

        elif opcao == "3":
            break
