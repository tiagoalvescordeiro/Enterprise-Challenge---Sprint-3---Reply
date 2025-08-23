import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def gerar_dados(caminho_csv='data/sensores.csv', n_sensors=6, n_per_sensor=500, seed=42):
    """Gera dados sintéticos de sensores e salva em CSV."""
    np.random.seed(seed)
    rows = []
    for sensor_id in range(1, n_sensors + 1):
        temp = np.random.normal(70 + sensor_id * 2, 10, n_per_sensor)
        vib = np.random.normal(5 + sensor_id * 0.5, 2, n_per_sensor)
        for t, v in zip(temp, vib):
            if t < 75 and v < 6:
                estado = 'Normal'
            elif (75 <= t < 90) or (6 <= v < 9):
                estado = 'Alerta'
            else:
                estado = 'Crítico'
            rows.append({
                'id_sensor': sensor_id,
                'temperatura': round(float(t), 2),
                'vibracao': round(float(v), 2),
                'estado': estado
            })
    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)
    df.to_csv(caminho_csv, index=False)
    return df

def carregar_dados(caminho_csv='data/sensores.csv'):
    """Carrega o CSV de sensores. Se não existir, gera novos dados."""
    if not os.path.exists(caminho_csv):
        df = gerar_dados(caminho_csv)
    else:
        df = pd.read_csv(caminho_csv)
    return df

def treinar_modelo(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    return modelo, X_test, y_test

def avaliar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, digits=4)
    cm = confusion_matrix(y_test, y_pred, labels=modelo.classes_)
    return acc, report, cm

def salvar_metrics(acc, report, caminho='ml/metrics.txt'):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w') as f:
        f.write(f'Accuracy: {acc:.4f}\n')
        f.write(report)

def plotar_matriz_confusao(cm, labels, caminho='docs/matriz_confusao.png'):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    plt.figure()
    plt.imshow(cm, interpolation='nearest')
    plt.title('Matriz de Confusão')
    plt.xlabel('Previsto')
    plt.ylabel('Real')
    plt.xticks(range(len(labels)), labels, rotation=45)
    plt.yticks(range(len(labels)), labels)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j], ha='center', va='center')
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()

def plotar_scatter(df, caminho='docs/scatter.png'):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    plt.figure()
    class_to_int = {c: i for i, c in enumerate(df['estado'].unique())}
    colors = [class_to_int[c] for c in df['estado']]
    plt.scatter(df['temperatura'], df['vibracao'], c=colors)
    plt.title('Dispersão das leituras de sensores')
    plt.xlabel('Temperatura')
    plt.ylabel('Vibração')
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()

def main():
    df = carregar_dados()
    X = df[['temperatura', 'vibracao']]
    y = df['estado']
    modelo, X_test, y_test = treinar_modelo(X, y)
    acc, report, cm = avaliar_modelo(modelo, X_test, y_test)
    salvar_metrics(acc, report)
    plotar_matriz_confusao(cm, modelo.classes_)
    plotar_scatter(df)
    print(f'Accuracy: {acc:.4f}')

if __name__ == '__main__':
    main()
