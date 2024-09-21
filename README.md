
```markdown
@sidneylcarneiro/calculadora-customtkinter
# Calculadora com CustomTkinter

Uma calculadora gráfica com interface personalizada usando a biblioteca [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). Este projeto permite a personalização das cores da calculadora, persistindo a configuração de tema entre as execuções. A calculadora suporta operações aritméticas básicas e tem funções como copiar o resultado e inverter o sinal dos números.

## Captura de Tela
![Captura de Tela]([./screenshots/screenshot.png](https://github.com/sidneylcarneiro/calculadora-customtkinter/blob/main/screenshots/screenshot.png))

## Funcionalidades

- **Operações matemáticas básicas**: Adição, subtração, multiplicação, divisão, potência.
- **Manipulação de sinais**: Inversão de sinais positivos e negativos.
- **Cálculo de porcentagem**: Realiza cálculos com porcentagem.
- **Personalização de cores**: Permite alterar o esquema de cores da interface.
- **Limite de caracteres no display**: O display permite até 25 caracteres.
- **Entrada por teclado**: Suporte a teclas como `Enter`, `Backspace`, e `Esc` para operações rápidas.
- **Copiar para área de transferência**: Função para copiar o resultado da operação para a área de transferência.

## Pré-requisitos

Antes de começar, certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

Além disso, você precisa instalar a biblioteca `customtkinter`. Para isso, execute o comando abaixo:

```bash
pip install customtkinter
```

## Instalação

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/@sidneylcarneiro/calculadora-customtkinter.git
   ```

2. Entre no diretório do projeto:

   ```bash
   cd calculadora-customtkinter
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
   > Se houver um arquivo `requirements.txt` para futuras dependências. Caso contrário, o único pré-requisito é o `customtkinter`.

## Como Usar

1. Execute o arquivo `main.py` para iniciar a calculadora:

   ```bash
   python main.py
   ```

2. A interface da calculadora aparecerá e você poderá utilizar o mouse ou o teclado para realizar operações matemáticas.


---

## Esquemas de Cores

A calculadora permite a customização de cores por meio de um menu que pode ser acessado ao clicar no botão `Ξ`. Selecione a cor de sua preferência, e a escolha será salva para a próxima vez que o programa for executado.

As opções de cores disponíveis são:

| Identificador | Screenshot |
|---------------|------------|
| **Branco**    | [Captura de Tela](./screenshots/white.png) |
| **Verde**     | [Captura de Tela](./screenshots/green.png) |
| **Azul**      | [Captura de Tela](./screenshots/blue.png) |
| **Preto**     | [Captura de Tela](./screenshots/black.png) |
| **Vermelho**  | [Captura de Tela](./screenshots/red.png) |
| **Roxo**      | [Captura de Tela](./screenshots/purple.png) |
| **Laranja**   | [Captura de Tela](./screenshots/orange.png) |
| **Cinza**     | [Captura de Tela](./screenshots/gray.png) |

---

## Contribuição

Se desejar contribuir com este projeto, sinta-se à vontade para abrir um *pull request* ou relatar problemas na aba de *issues*.

## Licença

Este projeto está licenciado sob a licença MIT. 
```
