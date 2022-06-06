# Price Predictor

Projeto tenta estipular a precificação de uma entrada no Airbnb com base em um modelo preditivo, <br>
usando um dataset retirado de: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro <br>

**Linguagem utilizada:** Python<br>
**Principais bibliotecas utilizadas:** Pandas, Matplotlib, Seaborn e Scikit-learn.

## Importação e tratamento inicial
Os dados estavam em múltiplos arquivos, então fez-se necessária a utilização de um iterador<br>
para leitura de todos eles, já adicionando colunas referentes ao mês e ano nos quais as entradas<br>
foram adicionadas ao Airbnb.<br>
Depois, fiz uma limpeza simples e visual das colunas que não eram relevantes para o estudo<br>
a fim de ficar com os dados aparentemente relevantes, a saber:<br>
- host_is_superhost;
- host_listings_count;
- latitude e longitude;
- property_type;
- room_type;
- accommodates;
- bathrooms;
- bedrooms;
- beds;
- bed_type;
- amenities;
- price;
- guests_included;
- extra_people;
- minimum_nights;
- maximum_nights;
- number_of_reviews;
- instant_bookable;
- is_business_travel_ready;
- cancellation_policy;
- year; e
- month.

Após o tratamento de colunas, verifiquei a quantidade de linhas que possuíam algum valor NaN.<br>
Por ser um valor muito pequeno comparado ao volume de dados disponível, decidi por eliminar<br>
tais linhas.

Depois, foi necessário transformar os valores das colunas "price" e "extra_people" para o<br>
tipo float32, para isso, precisava remover os marcadores de milhar e o $.

Por fim, utilizando as bibliotecas Seaborn e Matplotlib, criei um Heatmap para verificar<br>
se haviam valores com alta correlação que também poderiam ser desconsiderados na análise.<br>
Não havendo ocorrências gritantes, decidi por manter como estava.

Com isso, o tratamento inicial dos dados foi finalizado.

## Tratamento fino (Coluna a coluna)
Nesta etapa, analisei todas as colunas para, primeiro, verificar a relevancia da mesma para<br>
o projeto final e, também, para remover valores discrepantes (outliers) presentes.

Um exemplo de coluna removida foi a "host_listings_count", visto que ele pode gerar uma má<br>
interpretação do modelo, visto que haviam muitos valores discrepantes dos demais, devido<br>
à quantidade de quartos de hoteis anunciados no Airbnb. Assim, considerei prudente remover<br>
a coluna em vez de remover todos os valores que seriam considerados "outliers".

Ao início (no momento do carregamento do Dataset), eu possuía 902210 linhas em meu Dataset.<br>
No final do tratamento, havia 653774 linhas. Um pouco mais de 1/4 dos dados foi desconsiderado<br>
para o modelo final ser o mais preciso possível, sem incorrer em overfitting.

## Treinamento do Modelo:
**Modelos utilizados:**
- RandomForest;
- LinearRegression; e
- ExtraTrees.

**Métricas utilizadas:**
- R²; e
- MSE (Mean Squared Error).


**Melhor resultado:**
- ExtraTrees

**Métricas:**
- R²: 96.91%
- MSE: 46.09

## Conclusões
Com um resultado satisfatório de aproximadamente 97% de precisão, considerei desnecessario<br>
realizar novos tratamentos para polir o modelo. Acredito que o mesmo é uma fonte fidedigna<br>
para consulta de valores para usuários que desejem anunciar seus logradouros no Airbnb do<br>
Rio de Janeiro.

## Deploy
Ao final do arquivo existe a criação do arquivo .joblib para utilização no deploy, que está<br>
implementado em um outro arquivo. A saber, Deploy.py.<br>
O arquivo "data.csv" refere-se ao Dataset após o processo de tratamento.
