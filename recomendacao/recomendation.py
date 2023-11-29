import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

mapeamento = {
        0:  'Maçã',
        1:  'Banana',
        2:  'Feijão Roxo',
        3:  'Grão-de-bico',
        4:  'Coco',
        5:  'Café',
        6:  'Algodão',
        7:  'Uva',
        8:  'Juta',
        9:  'Feijão preto',
        10: 'Lentilha',
        11: 'Milho',
        12: 'Manga',
        13: 'Feijão',
        14: 'Vigna radiata',
        15: 'Melão',
        16: 'Laranja',
        17: 'Mamão',
        18: 'Guandu',
        19: 'Romã',
        20: 'Arroz',
        21: 'Melancia'
    }


def Carregar_Dataset(path):
    dataset = pd.read_csv(path)
    dataset.head(30)
    return dataset

def Encoder_Y(dataset): 
    Label_encoder = LabelEncoder()
    encoded_Y = Label_encoder.fit_transform(dataset['label'])
    dataset['label'] = encoded_Y
    return dataset

def dividir_conjunto_de_dados(dataset, estado_de_aleatoriedade, tamanho_teste):
    x = dataset.iloc[:, :-1]
    y = dataset['label']
    x_treino, x_validacao, y_treino, y_validacao = train_test_split(x, y, random_state=estado_de_aleatoriedade, test_size=tamanho_teste)
    return x_treino, x_validacao, y_treino, y_validacao

def Normalizar_dados(x_treino, x_validacao):
    scaler = StandardScaler()
    x_treino_normalizado = scaler.fit_transform(x_treino)
    x_validacao_normalizado = scaler.transform(x_validacao)
    return x_treino_normalizado, x_validacao_normalizado

def Treinar_Modelo(x_treino, y_treino, modelo):
    model = modelo.fit(x_treino, y_treino)
    return model

def Avaliar_Modelo(model ,x_validacao, y_validacao):
    predictions = model.predict(x_validacao)
    accuracy = accuracy_score(y_validacao, predictions)
    report = classification_report(y_validacao, predictions)
    print(accuracy)
    print(report)

def Recomendar(dados_usuario, model, random_st, test_s):
    scaler = StandardScaler()
    data_frame_dados = pd.DataFrame([dados_usuario])

    file_path = 'content//crop_recommendation.csv'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, file_path)

    dataset = Carregar_Dataset(dataset_path)

    dataset_encoded = Encoder_Y(dataset)

    x_treino, x_validacao, y_treino, y_validacao = dividir_conjunto_de_dados(dataset, random_st, test_s)

    x_treino_normalizado, x_validacao_normalizado = Normalizar_dados(x_treino, x_validacao)

    Treino_Modelo = Treinar_Modelo(x_treino_normalizado, y_treino, model)

    data_frame_dados.columns = x_treino.columns
    scaler.fit(x_treino)
    dados_scaled = scaler.transform(data_frame_dados)
    recomendacao = Treino_Modelo.predict(dados_scaled)
    resultado_recomendacao = mapeamento[recomendacao[0]]

    Avaliar_Modelo(Treino_Modelo,x_validacao_normalizado, y_validacao)

    
    return resultado_recomendacao



    
    

