# 📊 Sistema de Pesquisa de Satisfação - TudoWeb

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)](https://github.com/)
[![Licença](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 🎯 Sobre o Projeto

Desenvolvido para a empresa de marketing *TudoWeb*, este programa em **Python** tem como objetivo automatizar a coleta e a análise de uma pesquisa de opinião sobre o atendimento ao cliente, registrando o retorno de múltiplos entrevistados de forma estruturada e eficiente.

---

## 📋 Regras de Negócio e Funcionalidades

O sistema aplica os seguintes conceitos de programação:

* **Estrutura de Repetição:** Utiliza um laço (`for`) para automatizar a coleta iterativa dos dados de acordo com a quantidade de entrevistados estipulada.
* **Coleta de Dados Completos:** Solicita o nome, a idade e a avaliação de satisfação individual de cada participante.
* **Validação por Estruturas de Decisão:** Processa as notas informadas (`1: EXCELENTE`, `2: BOM`, `3: RUIM`) utilizando condicionais (`if`, `elif`, `else`) para garantir a contagem correta dos votos.
* **Relatório Estatístico Final:** Exibe um resumo consolidado com o total de entrevistados e as quantidades exatas de respostas nas categorias **EXCELENTE** e **RUIM**.

---

## ⚙️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Conceitos aplicados:** Estruturas de repetição (`for`), estruturas condicionais (`if`, `elif`, `else`), tratamento de exceções (`try/except`) e manipulação de contadores.

---

## 🚀 Como Executar o Programa

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo de código-fonte da agenda.
3. Abra o terminal na pasta onde o arquivo está salvo e execute o seguinte comando:

```bash
python pesquisa_opiniao_tudoweb.py