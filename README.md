# Versão em Português
# Previsão de Rotatividade de Clientes
![GitHub](https://img.shields.io/github/license/willianadb/gold_purification_prediction)
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
  - [README_en.md](https://github.com/willianadb/telecom_customer_churn_prediction/blob/main/docs/README_en.md): Documentação do projeto em inglês.
  - [README_pt.md](https://github.com/willianadb/telecom_customer_churn_prediction/blob/main/docs/README_pt.md): Documentação do projeto em português (você está aqui).
  
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
- Bibliotecas: `pandas`, `numpy`, `sklearn`, `xgboost`, `lightgbm`, `matplotlib`, `seaborn`, `joblib`, entre outras (veja [`requirements.txt`](https://github.com/willianadb/telecom_customer_churn_prediction/blob/main/requirements.txt)).

## 🧑‍💼 Autor
Este projeto foi desenvolvido por **Willian Albuquerque**, cientista de dados e especialista em aprendizado de máquina. Estou disponível para consultas e projetos relacionados ao tema.

# English version
# Customer Churn Prediction
![GitHub](https://img.shields.io/github/license/willianadb/gold_purification_prediction)

## 📄 Project Description
This project aims to predict customer churn for a telecommunications company using machine learning techniques. Accurately identifying customers likely to cancel services allows the company to implement proactive strategies to retain customers and improve satisfaction.

The work was developed in two versions: Portuguese and English, aiming to reach an international audience. The project includes an exploratory data analysis, the application of various predictive models, and hyperparameter tuning to achieve the best performance.

## 📂 Project Structure
- `data/`: Directory containing raw and processed data.
  - `raw/`: Original data files.
  - `processed/`: Data after preprocessing.
- `notebooks/`: Jupyter Notebooks containing analysis, modeling, and evaluation.
  - `portuguese/`: Notebook version in Portuguese.
  - `english/`: Notebook version in English.
- `scripts/`: Python scripts for data preprocessing, training, and model evaluation.
  - `portuguese/`
  - `english/`
- `models/`: Trained models saved for future use.
  - `portuguese/`
  - `english/`
- `docs/`:
  - [README_en.md](https://github.com/willianadb/telecom_customer_churn_prediction/blob/main/docs/README_en.md): Project documentation in English (you are here).
  - [README_pt.md](https://github.com/willianadb/telecom_customer_churn_prediction/blob/main/docs/README_pt.md): Project documentation in Portuguese.
  
## 📊 Exploratory Data Analysis
Exploratory Data Analysis (EDA) was performed to better understand the data and identify patterns that may influence customer churn. Some of the analyses included:
- Distribution of categorical and numerical variables.
- Correlation analysis to identify significant relationships between variables.
- Study of the distribution of customers who canceled and retained the service.

## ⚙️ Preprocessing
The `preprocess_data.py` script performs the following data preparation steps:
- Conversion of column names to `snake_case` format.
- Merging multiple data files (`contract.csv`, `personal.csv`, `internet.csv`, `phone.csv`).
- Handling of missing values.
- Encoding of categorical variables using One-Hot Encoding.
- Normalization of numerical variables.
- Creation of the target variable and relevant new features.

## 🧠 Predictive Modeling
Several machine learning models were trained and evaluated, including:
- Logistic Regression.
- Decision Trees.
- Random Forest.
- Gradient Boosting.
- XGBoost.
- LightGBM.

### 🛠️ Hyperparameter Tuning
The most promising models were **XGBoost**, which achieved an AUC-ROC of 0.9113 **without the need for hyperparameter tuning**, followed by the tuned Gradient Boosting with an AUC-ROC of 0.902170. Hyperparameter tuning was performed using `RandomizedSearchCV` and `GridSearchCV`.

## 📈 Evaluation and Results
The best model selected was **XGBoost**, achieving an AUC-ROC of 0.9113. Evaluation metrics, such as accuracy, precision, recall, and f1-score, were analyzed for each model, highlighting the effectiveness of the final model.

## 🚀 Next Steps and Final Considerations
- **Production Deployment:** The model is ready to be deployed in production for real-time churn prediction.
- **Monitoring:** Continuous monitoring of the model's performance with new data is suggested.
- **Future Adjustments:** Further hyperparameter tuning and feature engineering can be performed to improve the model's performance.

## 📂 How to Run the Project
1. Clone this repository: `git clone https://github.com/willianadb/telecom_customer_churn_prediction.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Navigate to the `notebooks` folder and run the desired version (`portuguese` or `english`). It is recommended to start with the Exploratory Data Analysis (`EDA`) before proceeding to modeling.
4. The preprocessing and modeling scripts can be found in the `scripts` folder.

## 📋 Requirements
- Python 3.x
- Libraries: `pandas`, `numpy`, `sklearn`, `xgboost`, `lightgbm`, `matplotlib`, `seaborn`, `joblib`, among others (see [`requirements.txt`](https://github.com/willianadb/telecom_customer_churn_prediction/blob/main/requirements.txt)).

## 🧑‍💼 Author
This project was developed by **Willian Albuquerque**, a data scientist and machine learning specialist. I am available for consultations and projects related to this topic.
