import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def carregar_dados(caminho="data/dados.csv", n=400, seed=42):
    """Lê data/dados.csv (target na coluna 'target'); se não existir, gera sintético."""
    os.makedirs("data", exist_ok=True)

    if os.path.exists(caminho):
        df = pd.read_csv(caminho)
        X = df.drop(columns=["target"]).values
        y = df["target"].values
        print(f"Dados carregados de {caminho} -> {df.shape}")
        return X, y

    X, y = make_classification(
        n_samples=n, n_features=3, n_informative=3, n_redundant=0,
        n_classes=2, random_state=seed
    )
    cols = ["feat_1", "feat_2", "feat_3"]
    pd.DataFrame(np.c_[X, y], columns=cols + ["target"]).to_csv(caminho, index=False)
    print(f"Dados sintéticos gerados e salvos em {caminho}")
    return X, y

def treinar_modelo(dados):
    X, y = dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )
    modelo = LogisticRegression(solver="liblinear", random_state=42)
    modelo.fit(X_train, y_train)
    return modelo, X_test, y_test

def avaliar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    relatorio = classification_report(y_test, y_pred, digits=4)
    cm = confusion_matrix(y_test, y_pred)
    print("\nMétricas de Classificação:\n", relatorio)
    print("Matriz de Confusão:\n", cm)
    return relatorio, cm

def salvar_metricas(texto, caminho="ml/metrics.txt"):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)

def plotar_matriz_confusao(cm, caminho="docs/matriz_confusao.png"):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    plt.figure()
    plt.imshow(cm, cmap="Blues")
    plt.title("Matriz de Confusão")
    plt.xlabel("Predito")
    plt.ylabel("Real")
    for (i, j), v in np.ndenumerate(cm):
        plt.text(j, i, str(v), ha="center", va="center")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()

def plotar_scatter(X, y, caminho="docs/scatter.png"):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.title("Dispersão (duas primeiras features)")
    plt.xlabel("feat_1")
    plt.ylabel("feat_2")
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()
