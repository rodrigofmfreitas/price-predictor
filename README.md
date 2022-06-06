# Price Predictor

Projeto tenta estipular a precificação de uma entrada no Airbnb com base em um modelo preditivo, <br>
usando um dataset retirado de: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro <br>

**Linguagem utilizada:** Python
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

