import numpy as np
import pandas as pd
import sklearn as sk
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

def Carregar_Dataset(path):
    dataset = pd.read_csv(path)
    dataset.head(30)
    return dataset

def Encoder_Y(dataset):
    Label_encoder = LabelEncoder()
    encoded_Y = Label_encoder.fit_transform(dataset['label'])
    dataset['label'] = encoded_Y
    return dataset

def dividir_conjunto_de_dados(dataset):
    x = dataset.iloc[:, :-1]
    y = dataset['label']
    x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_validation, y_train, y_validation

def Normalizar_dados(x_train, x_validation):
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_validation_scaled = scaler.transform(x_validation)
    return x_train_scaled, x_validation_scaled

def Treinar_DecisionTree(x_train, y_train):
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    return model

def Avaliar_DecisionTree(model, x_validation, y_validation):
    predictions = model.predict(x_validation)
    accuracy = accuracy_score(y_validation, predictions)
    report = classification_report(y_validation, predictions)
    return accuracy, report


if __name__ == '__main__':

    #Aqui estou carregando meu dataset que esta na pasta 'content'
    #usei o import os para encontrar o dataset sem precisar colocar o diretorio manualmente
    file_path = 'content\\crop_recommendation.csv'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, file_path)
    dataset = Carregar_Dataset(dataset_path)

    print(dataset)
    input('')

    #Chamado da funcao Encoder para transformar a coluna dado 'label' em numeros,
    #que é nessecario dependendo do modelo de machine learning, pois meu modelo nao é capaz de compreender strings
    dataset_encoded = Encoder_Y(dataset)
    
    #Desempacotando as variaveis da funcao dividir_conjunto_de_dados 
    #x_train - São os dados que uso para treinar o modelo
    #y_train - Basicamente é o 'label' o resultado da recomendacão e o y_train que ira dizer qual planta o usuario deve plantar
    #x_validation - É um template que servirá para validar se o treinamento dos dados x_train estao corretos
    # y_validation - É a template para validar o dado 'label' 
    x_train, x_validation, y_train, y_validation = dividir_conjunto_de_dados(dataset)

    #Pre processamento usando a normalizacao de dados
    x_train_scaled, x_validation_scaled = Normalizar_dados(x_train, x_validation)

    #Aqui estou dando os valores para o modelo da machine learning, note que estou usando a normalzação no x
    Treino_Modelo = Treinar_DecisionTree(x_train_scaled, y_train)

    #Aqui estou mostrando a prcisão do meu modelo e tambem exibindo um relatorio de treinamento de cada 'label'
    accuracy, report = Avaliar_DecisionTree(Treino_Modelo, x_validation_scaled, y_validation)

    print(dataset_encoded.head(30))
    input('')
    print('\n', "            Precisao DecisionTree: ", accuracy, '\n')
    print("                             Relatorio", '\n')
    print(report)
    input('')



