from datetime import datetime
from pathlib import Path

def gerar_relatorio(path_metrics="ml/metrics.txt", saida="docs/relatorio.md"):
    Path("docs").mkdir(exist_ok=True)
    agora = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        metrics = Path(path_metrics).read_text(encoding="utf-8")
    except Exception:
        metrics = "(metrics.txt não encontrado)"

    md = f"""# Relatório de Execução — Sprint 3

**Data/Hora:** {agora}

## Métricas (classification_report)


## Imagens
- Matriz de Confusão: [docs/matriz_confusao.png](matriz_confusao.png)
- Dispersão: [docs/scatter.png](scatter.png)
"""
    Path(saida).write_text(md, encoding="utf-8")
