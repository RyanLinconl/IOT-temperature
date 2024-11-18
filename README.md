# IoT Temperature Monitoring Dashboard

Este projeto é um sistema de monitoramento de temperaturas baseado em dados coletados de dispositivos IoT. O objetivo principal é fornecer insights sobre as leituras de temperatura, como a média de temperatura por dispositivo, leituras por hora do dia e variações de temperatura máxima e mínima.

O projeto inclui uma interface de dashboard interativa que permite visualizar esses dados de forma clara e intuitiva. Ele foi desenvolvido utilizando Python, PostgreSQL, Streamlit e Plotly.

---

## 📸 Capturas de Tela do Dashboard

### Leituras por Hora do Dia

![Leituras por Hora](https://imgur.com/grEd0dX)

Esta visualização exibe a variação das temperaturas ao longo do dia, agrupadas por hora. Ela permite identificar padrões de temperatura em intervalos de tempo específicos.

### Média de Temperatura por Dispositivo

![Média de Temperatura](https://imgur.com/ucjVJdl)

Esta visualização mostra a média de temperatura por dispositivo, permitindo uma análise comparativa entre diferentes dispositivos ou ambientes.

### Temperatura Máxima e Mínima por Dia

![Temperatura Máxima e Mínima](https://imgur.com/AZBbqVR)

Esta visualização exibe a temperatura máxima e mínima registrada por dia, fornecendo uma visão geral da variação de temperatura ao longo do tempo.

---

## 📈 Insights Obtidos dos Dados
A partir das visualizações geradas, podemos obter os seguintes insights:

Leituras por Hora: A visualização de leituras por hora pode indicar padrões de variação de temperatura ao longo do dia, como quedas ou aumentos de temperatura em horários específicos. Isso pode ser útil para otimizar a operação dos dispositivos, como sistemas de aquecimento ou refrigeração.

Média de Temperatura por Dispositivo: Ao analisar a média de temperatura por dispositivo, podemos identificar dispositivos que estão registrando temperaturas mais altas ou mais baixas, o que pode indicar falhas, necessidade de ajustes ou até mesmo padrões específicos de cada ambiente.

Temperatura Máxima e Mínima: A análise das temperaturas máximas e mínimas permite identificar variações extremas e possíveis anomalias. Isso é útil para monitorar condições críticas, como superaquecimento ou resfriamento excessivo, que podem danificar equipamentos ou afetar o ambiente.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Streamlit**: Framework utilizado para criar o dashboard interativo.
- **Plotly**: Biblioteca para criar gráficos interativos.
- **PostgreSQL**: Banco de dados utilizado para armazenar as leituras de temperatura.
- **SQLAlchemy**: ORM utilizado para interagir com o banco de dados no Python.
- **Pandas**: Biblioteca utilizada para processamento e limpeza de dados.

---

## 🔧 Configuração e Execução

### 1. Clonando o Repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
