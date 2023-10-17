import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

mapeamento = {
        0:  'Maçã 🍎',
        1:  'Banana 🍌',
        2:  'Vigna mungo',
        3:  'Grão-de-bico',
        4:  'Coco 🥥',
        5:  'Café ☕',
        6:  'Algodão',
        7:  'Uva 🍇',
        8:  'Juta 🧶',
        9:  'Feijão Roxo',
        10: 'Lentilha',
        11: 'Milho 🌽',
        12: 'Manga 🥭',
        13: 'Vigna aconitifolia',
        14: 'Vigna radiata',
        15: 'Melão 🍈',
        16: 'Laranja 🍊',
        17: 'Mamão',
        18: 'Guandu',
        19: 'Romã',
        20: 'Arroz 🍚',
        21: 'Melancia 🍉'
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

def Avaliar_DecisionTree(model ,x_validation, y_validation):
    predictions = model.predict(x_validation)
    accuracy = accuracy_score(y_validation, predictions)
    report = classification_report(y_validation, predictions)
    return accuracy, report

def Recomendar(dados_usuario):
    scaler = StandardScaler()
    data_frame_dados = pd.DataFrame([dados_usuario])

    file_path = 'content\\crop_recommendation.csv'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, file_path)

    dataset = Carregar_Dataset(dataset_path)

    dataset_encoded = Encoder_Y(dataset)

    x_train, x_validation, y_train, y_validation = dividir_conjunto_de_dados(dataset)

    x_train_scaled, x_validation_scaled = Normalizar_dados(x_train, x_validation)

    Treino_Modelo = Treinar_DecisionTree(x_train_scaled, y_train)

    data_frame_dados.columns = x_train.columns
    scaler.fit(x_train)
    dados_scaled = scaler.transform(data_frame_dados)
    recomendacao = Treino_Modelo.predict(dados_scaled)
    resultado_recomendacao = mapeamento[recomendacao[0]]
    
    return resultado_recomendacao

def relatorio():
    Recomendar()
    print("")
    print("                     Precisão:",accuracy, '\n')
    print(report)

if __name__ == '__main__':

    #Aqui estou carregando meu dataset que esta na pasta 'content'
    #usei o import os para encontrar o dataset sem precisar colocar o diretorio manualmente
    file_path = 'content\\crop_recommendation.csv'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, file_path)
    dataset = Carregar_Dataset(dataset_path)

    #print(dataset)
    #input('')

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

    #print(dataset_encoded.head(30))
    #input('')

    #Aqui estou mostrando a prcisão do meu modelo e tambem exibindo um relatorio de treinamento de cada 'label'
    accuracy, report = Avaliar_DecisionTree(Treino_Modelo, x_validation_scaled, y_validation)

    #print('\n', "            Precisao DecisionTree: ", accuracy, '\n')
    #print("                             Relatorio", '\n')
    #print(report)]

    relatorio()


    
    

