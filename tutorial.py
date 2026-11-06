# Tkinter é a biblioteca padrão do Python para criar interfaces gráficas de usuário (GUI). Ela fornece uma interface para o toolkit Tcl/Tk, que consiste na linguagem de script Tcl (criada em 1988) e no toolkit gráfico Tk (desenvolvido a partir de 1991), ambos projetados originalmente para a construção de interfaces gráficas multiplataforma.
#
# Já vem instalado na maioria das distribuições Python;
# Permite criar aplicações gráficas com poucas linhas de código;
# Funciona em Windows, Linux e macOS sem modificações;
# Grande variedade de widgets prontos (botões, caixas de texto, menus);
# Integração nativa com Python e compatibilidade com outras bibliotecas.
#
# 01. Importar o módulo Tkinter: O primeiro passo é importar a biblioteca no seu código Python. Essa etapa permite acessar todas as classes e funções necessárias para criar sua interface gráfica.
# import tkinter as tk
#
# 02. Criar a janela principal: A janela principal é o container no qual todos os elementos da sua aplicação serão exibidos. Você cria essa janela instanciando a classe Tk.
# janela = tk.Tk()
# janela.title("Base fundo branco")

# 03. Adicionar widgets à janela: Widgets são os componentes gráficos da sua interface, como botões, rótulos, caixas de texto e menus. Cada widget precisa ser criado e então posicionado na janela usando um gerenciador de layout.
# rotulo = tk.Label(janela, text="Olá, Tkinter!")
# rotulo.pack()
#
# 04. Iniciar o loop principal: O loop principal mantém a aplicação rodando e responsiva às ações do usuário. Sem ele, a janela seria criada e fechada imediatamente. Esse método fica aguardando eventos como cliques, digitação e movimentos do mouse, atualizando a interface conforme necessário até que o usuário feche a janela.
# janela.mainloop()
#
# Essa estrutura é a base de qualquer aplicação Tkinter. A partir dela, você pode criar interfaces muito mais complexas combinando diferentes widgets, gerenciadores de layout e eventos de interação.