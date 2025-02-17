---

# Calculadora de IMC
<img src="https://memes.memedrop.io/production/Dk613ekq8ymR/source.gif" alt="Yokuso" width="1050" height="auto"/>

Este projeto implementa uma calculadora de Índice de Massa Corporal (IMC) utilizando a biblioteca Tkinter, com uma interface gráfica simples. O programa permite ao usuário inserir seu nome, peso e altura, calcular o IMC e salvar os dados em um arquivo de texto.

## Autores
- Pedro Arthur
- Emanuel Rodrigues
- Miguel Sthevão

## Instalação

Para rodar o projeto em seu computador, siga os seguintes passos:

1. Clone o repositório:
    ```bash
    git clone https://github.com/Pedro-Arthur13/Calculadora-de-imc.git
    ```

2. Navegue até a pasta do projeto:
    ```bash
    cd Calculadora-de-imc
    ```

3. Verifique se o Python 3.x está instalado em seu computador. Caso não tenha, instale-o a partir de [python.org](https://www.python.org/downloads/).

4. Instale a biblioteca Tkinter (se necessário). Em sistemas baseados em Debian/Ubuntu, você pode instalar Tkinter com:
    ```bash
    sudo apt-get install python3-tk
    ```

5. Execute o código:
    ```bash
    python3 imc_calculadora.py
    ```

## Como Usar

1. Abra a aplicação.
2. Preencha seu **Nome**, **Peso** (em kg) e **Altura** (em metros) nos campos correspondentes.
3. Clique no botão **Calcular** para calcular seu IMC.
4. O IMC será exibido abaixo, junto com uma mensagem indicando o resultado.
5. As informações inseridas serão salvas em um arquivo de texto com o nome formatado de acordo com o nome informado (ex: `Pedro_Arthur_Info.txt`).

## Funcionalidades

- **Cálculo do IMC:** O IMC é calculado com a fórmula: IMC = peso/altura^2
- **Validação de Entrada:** O programa verifica se o peso e a altura são valores positivos e se são números válidos.
- **Alteração de Tema:** Você pode alternar entre o **Modo Claro** e o **Modo Escuro** clicando no botão de alternância no canto superior direito.
- **Salvar Dados:** Os dados (Nome, Peso, Altura, IMC) são salvos em um arquivo de texto.

## Exceções Tratadas

- **NegativeValueError:** Caso o peso ou altura sejam menores ou iguais a zero, uma exceção personalizada será gerada, exibindo uma mensagem de erro.
- **ValueError:** Caso o peso ou a altura não sejam números válidos, uma exceção será gerada, indicando que as entradas precisam ser numéricas.


---

