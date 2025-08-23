from ml import modelo_sensores as ms

def main():
    print("Iniciando Sprint 3 - Hermes Reply")

    # 1) Carregar dados (gera data/dados.csv se não existir)
    X, y = ms.carregar_dados()

    # 2) Treinar modelo
    modelo, X_test, y_test = ms.treinar_modelo((X, y))

    # 3) Avaliar modelo
    relatorio, cm = ms.avaliar_modelo(modelo, X_test, y_test)

    # 4) Persistir resultados
    ms.salvar_metricas(relatorio, "ml/metrics.txt")
    ms.plotar_matriz_confusao(cm, "docs/matriz_confusao.png")
    ms.plotar_scatter(X_test, y_test, "docs/scatter.png")

    print("\nExecução concluída.")
    print("• Métricas: ml/metrics.txt")
    print("• Gráficos: docs/matriz_confusao.png e docs/scatter.png")

if __name__ == "__main__":
    main()
