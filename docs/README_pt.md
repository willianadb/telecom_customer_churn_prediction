# Projeto de Previsão de Rotatividade de Clientes

## 📄 Descrição do Projeto
Este projeto tem como objetivo prever a rotatividade de clientes de uma empresa de telecomunicações, utilizando técnicas de aprendizado de máquina. A identificação precisa dos clientes propensos a cancelar os serviços permite que a empresa implemente estratégias proativas para reter clientes e aumentar a satisfação.

O trabalho foi desenvolvido em duas versões: português e inglês, visando alcançar um público internacional. O projeto inclui uma análise exploratória dos dados, a aplicação de vários modelos preditivos, e o ajuste de hiperparâmetros para obter a melhor performance.

## 📂 Estrutura do Projeto
- `data/`: Diretório contendo os dados brutos e processados.
  - `raw/`: Arquivos de dados originais.
  - `processed/`: Dados após o pré-processamento.
- `notebooks/`: Notebooks Jupyter contendo a análise, modelagem e avaliação.
  - `portuguese/`: Versão do notebook em português.
  - `english/`: Versão do notebook em inglês.
- `scripts/`: Scripts Python para pré-processamento, treinamento e avaliação dos modelos.
  - `portuguese/`
  - `english/`
- `models/`: Modelos treinados salvos para uso futuro.
  - `portuguese/`
  - `english/`
- `docs/`:
  - [README_en.md](docs/README_en.md): Documentação do projeto em inglês.
  - [README_pt.md](docs/README_pt.md): Documentação do projeto em português (você está aqui).
  
## 📊 Análise Exploratória
A análise exploratória (EDA) foi realizada para entender melhor os dados e identificar padrões que podem influenciar a rotatividade dos clientes. Algumas das análises incluídas:
- Distribuição das variáveis categóricas e numéricas.
- Análise de correlação para identificar relações significativas entre as variáveis.
- Estudo da distribuição de clientes que cancelaram e mantiveram o serviço.

## ⚙️ Pré-Processamento
O script `preprocess_data.py` executa as seguintes etapas de preparação dos dados:
- Conversão de nomes de colunas para o formato `snake_case`.
- Mesclagem de múltiplos arquivos de dados (`contract.csv`, `personal.csv`, `internet.csv`, `phone.csv`).
- Tratamento de valores ausentes.
- Codificação de variáveis categóricas usando One-Hot Encoding.
- Normalização de variáveis numéricas.
- Criação da variável alvo e de novas features relevantes.

## 🧠 Modelagem Preditiva
Foram treinados e avaliados vários modelos de aprendizado de máquina, incluindo:
- Regressão Logística.
- Árvores de Decisão.
- Random Forest.
- Gradient Boosting.
- XGBoost.
- LightGBM.

### 🛠️ Ajuste de Hiperparâmetros
Os modelos mais promissores foram o **XGBoost** que atingiu a AUC-ROC de 0.9113  **sem necessidade de ajustes nos hiperparâmetros** seguido do Gradient Boosting ajustado	com AUC-ROC de 0.902170, onde passou por ajustes de hiperparâmetros utilizando `RandomizedSearchCV` e `GridSearchCV`.

## 📈 Avaliação e Resultados
O melhor modelo selecionado foi o **XGBoost**, alcançando uma AUC-ROC de 0.9113.  As métricas de avaliação, como acurácia, precisão, recall e f1-score, foram analisadas para cada modelo, destacando a eficácia do modelo final.

## 🚀 Próximos Passos e Considerações Finais
- **Implementação em Produção:** O modelo está pronto para ser implementado em produção para prever a rotatividade em tempo real.
- **Monitoramento:** Sugere-se o monitoramento contínuo do modelo para avaliar sua performance com novos dados.
- **Ajustes Futuros:** Ajustes adicionais nos hiperparâmetros e na engenharia de features podem ser realizados para melhorar ainda mais o desempenho do modelo.

## 📂 Como Executar o Projeto
1. Clone este repositório: `git clone https://github.com/willianadb/telecom_customer_churn_prediction.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Navegue até a pasta `notebooks` e execute a versão desejada (`portuguese` ou `english`). É recomendável começar pela análise exploratória (`EDA`) antes de seguir para a modelagem.
4. Os scripts de pré-processamento e modelagem podem ser encontrados na pasta `scripts`.

## 📋 Requisitos
- Python 3.x
- Bibliotecas: `pandas`, `numpy`, `sklearn`, `xgboost`, `lightgbm`, `matplotlib`, `seaborn`, `joblib`, entre outras (veja `requirements.txt`).

## 🧑‍💼 Autor
Este projeto foi desenvolvido por **Willian Albuquerque**, cientista de dados e especialista em aprendizado de máquina. Estou disponível para consultas e projetos relacionados ao tema.

---

### Observações
O projeto foi estruturado seguindo boas práticas de ciência de dados, visando a publicação no GitHub. Feedbacks são bem-vindos!
