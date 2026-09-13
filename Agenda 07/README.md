# 💧 Sistema de Classificação de Consumo de Água

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)](https://github.com/)
[![Licença](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 🎯 Sobre o Projeto

Desenvolvido para a campanha de conscientização ambiental de uma companhia de saneamento fictícia, este programa em **Python** tem como objetivo automatizar a classificação do perfil de consumo de água dos imóveis com base no tipo de residência e na quantidade gasta mensalmente (em $m^3$), emitindo alertas e orientações educativas aos moradores.

---

## 📋 Regras de Negócio Implementadas

O sistema aplica as seguintes condicionais para a tomada de decisão:

* **Comercial:** Exibe a mensagem *"Tarifa comercial aplicada – consulte o plano corporativo."*
* **Apartamento com consumo < 10 $m^3$:** Exibe *"Consumo econômico – excelente controle de água!"*
* **Apartamento (qualquer consumo) ou Casa com consumo $\le$ 25 $m^3$:** Exibe *"Consumo moderado – dentro do padrão residencial."*
* **Demais casos (Consumo excessivo):** Exibe *"Consumo excessivo – adote medidas de economia e verifique vazamentos."*

---

## ⚙️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Conceitos aplicados:** Estruturas condicionais (`if`, `elif`, `else`), operadores lógicos, tratamento de exceções (`try/except`) e validação de dados de entrada.

---

## 🚀 Como Executar o Programa

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `app.py`.
3. Abra o terminal na pasta onde o arquivo está salvo e execute o seguinte comando:

```bash
python app.py
