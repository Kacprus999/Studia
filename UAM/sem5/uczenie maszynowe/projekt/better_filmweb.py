import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
import re


def data_preprocessing():
    data = pd.read_csv("imdb/title_rating_data.tsv", sep='\t')      # dane z ocenami filmów
    data.drop(data[data["numVotes"] <100].index, inplace = True)     # usunięcie danych zawierających mniej niż 100 ocen

    df1 = pd.read_csv("imdb/title_basic_data.tsv", sep='\t', usecols=['tconst','isAdult','startYear','genres'])      # dane z informacjami o filmach
    df1[['genre_1','genre_2','genre_3']] = df1['genres'].str.split(',', expand=True)       # podzielenie kolumny genres na 3 i jej usunięcie
    df1.drop(columns=['genres'],inplace=True)

    data = data.merge(df1)    # złączenie 2 pierwszych dataframeów

    df2 = pd.read_csv("imdb/title_principals_data.tsv", sep='\t', usecols = ['tconst', 'nconst','category'])       # wczytanie danych z obsadą
    df2['nconst'] = df2['nconst'].astype("category").cat.codes
    df2.drop(columns=['category'],inplace=True)
    df2['nconst'] = df2['nconst'].apply(str)
    df2 = df2.groupby('tconst')['nconst'].apply(','.join).reset_index()     # polaczenie danych z wielu wierszy w 1 w kolumnie ncons
    df2[['crew_1','crew_2','crew_3','crew_4','crew_5','crew_6','crew_7','crew_8','crew_9','crew_10']] = df2["nconst"].str.split(',',expand=True)    # podzielenie kolumny nconst na 10 osob
    df2.drop(columns=['nconst'],inplace=True)
    data = data.merge(df2)      # dolaczenie 3 dataframe do glownego

    print(data)
    data.to_csv('processed_data.csv',index=False)    # zapisanie danych preprocessed dataframe do pliku

def postprocessing():
    data = pd.read_csv('processed_data.csv', sep=',')
    data.drop(columns=['tconst'],inplace=True)
    data.dropna(subset=['genre_1'])
    data.drop(columns=['crew_7','crew_8','crew_9','crew_10'],inplace=True)
    data.drop(columns=['crew_6','crew_5','crew_4','crew_3','crew_2','crew_1'],inplace=True)
    # data.drop(columns=["genre_1",'genre_2','genre_3'],inplace=True)
    # data['genre_1'] = data['genre_1'].replace(r'\\N','0',regex=True)
    data['startYear'] = data['startYear'].replace(r'\\N','0',regex=True)
    data.drop(data[data["startYear"] =="0"].index, inplace = True)
    data.drop(data[data["genre_1"] == "0"].index, inplace = True)

    data = pd.get_dummies(data, columns=['genre_1','genre_2','genre_3'])
    # print(data)
    data.to_csv('postprocessed_data.csv',index=False)    # zapisanie danych preprocessed dataframe do pliku


FEATURES = ['numVotes', 'isAdult', 'startYear', 'genre_1_Action', 'genre_1_Adult',
       'genre_1_Adventure', 'genre_1_Animation', 'genre_1_Biography',
       'genre_1_Comedy', 'genre_1_Crime', 'genre_1_Documentary',
       'genre_1_Drama', 'genre_1_Family', 'genre_1_Fantasy',
       'genre_1_Film-Noir', 'genre_1_Game-Show', 'genre_1_History',
       'genre_1_Horror', 'genre_1_Music', 'genre_1_Musical', 'genre_1_Mystery',
       'genre_1_News', 'genre_1_Reality-TV', 'genre_1_Romance',
       'genre_1_Sci-Fi', 'genre_1_Short', 'genre_1_Sport', 'genre_1_Talk-Show',
       'genre_1_Thriller', 'genre_1_War', 'genre_1_Western', 'genre_2_Adult',
       'genre_2_Adventure', 'genre_2_Animation', 'genre_2_Biography',
       'genre_2_Comedy', 'genre_2_Crime', 'genre_2_Documentary',
       'genre_2_Drama', 'genre_2_Family', 'genre_2_Fantasy',
       'genre_2_Film-Noir', 'genre_2_Game-Show', 'genre_2_History',
       'genre_2_Horror', 'genre_2_Music', 'genre_2_Musical', 'genre_2_Mystery',
       'genre_2_News', 'genre_2_Reality-TV', 'genre_2_Romance',
       'genre_2_Sci-Fi', 'genre_2_Short', 'genre_2_Sport', 'genre_2_Talk-Show',
       'genre_2_Thriller', 'genre_2_War', 'genre_2_Western',
       'genre_3_Adventure', 'genre_3_Animation', 'genre_3_Biography',
       'genre_3_Comedy', 'genre_3_Crime', 'genre_3_Documentary',
       'genre_3_Drama', 'genre_3_Family', 'genre_3_Fantasy',
       'genre_3_Film-Noir', 'genre_3_Game-Show', 'genre_3_History',
       'genre_3_Horror', 'genre_3_Music', 'genre_3_Musical', 'genre_3_Mystery',
       'genre_3_News', 'genre_3_Reality-TV', 'genre_3_Romance',
       'genre_3_Sci-Fi', 'genre_3_Short', 'genre_3_Sport', 'genre_3_Talk-Show',
       'genre_3_Thriller', 'genre_3_War', 'genre_3_Western']

# data_preprocessing()
# postprocessing()
data = pd.read_csv('postprocessed_data.csv', sep=',')
data = data.fillna(0)

columns = data.columns[1:]                  #wszystkie kolumny oprocz Rating
# print(columns)
data = data[FEATURES + ["averageRating"]]        #wybór cech


# podział danych na zbiory uczący i testowy
data_train, data_test = train_test_split(data, test_size=0.2)

# uczenie modelu
y_train = pd.DataFrame(data_train["averageRating"])
x_train = pd.DataFrame(data_train[FEATURES])

data_mean = data["averageRating"].mean()
print(f"Mean from all avg rating: {data_mean}")

model = LinearRegression()  # definicja modelu
model.fit(x_train, y_train.values.ravel(order='C'))  # dopasowanie modelu

# Predykcja wyników dla danych testowych
y_expected = pd.DataFrame(data_test["averageRating"])
x_test = pd.DataFrame(data_test[FEATURES])
y_predicted = model.predict(x_test)  # predykcja wyników na podstawie modelu

# print(np.full(len(y_expected), data_mean))

mse = mean_squared_error(y_expected, np.full(len(y_expected),data_mean), squared = False)
print(f"Mean squared error from expected and all data: {mse}")

score2 = model.score(x_test, y_expected)
score = mean_squared_error(y_expected, y_predicted,squared = False)

# print(f"Mean train: {np.mean(y_train)}")
# print(f"Mean expected: {np.mean(y_expected)}")
# print(f"Mean predicted: {np.mean(y_predicted)}")

print(f"Model score: {score}")
print(f"Model score2: {score2}")
# print(y_predicted[:10])  # Pierwsze 10 wynikow