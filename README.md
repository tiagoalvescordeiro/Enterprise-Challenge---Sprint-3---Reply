Hermes Reply – Sprint 3 (Fase 5)

Este repositório contém a solução completa para o desafio Hermes Reply (Fase 5) da FIAP. O objetivo é construir um pequeno sistema que integre Banco de Dados, Machine Learning e uma documentação estruturada para monitorar sensores em um ambiente industrial. Todo o conteúdo está em português para facilitar a compreensão.

🗂 Estrutura do Repositório
├── db          # Modelagem e scripts SQL
│   ├── der.txt
│   └── script.sql
├── ml          # Código de Machine Learning e métricas
│   ├── main.py
│   └── metrics.txt
├── data        # Conjunto de dados (CSV) utilizado no modelo
│   └── dataset.csv
├── docs        # Imagens geradas (gráficos, matriz de confusão)
│   ├── matriz_confusao.png
│   ├── scatter.png
│   └── bar_chart.png
└── README.md   # Este documento

Introdução

Sensores industriais coletam continuamente dados como temperatura e vibração. Interpretar esses dados de forma automática pode ajudar a identificar anomalias e acionar alarmes. Neste projeto, definimos uma tarefa de classificação que categoriza o estado do sensor em três níveis:

Normal – operação dentro dos limites esperados.

Alerta – valores moderadamente elevados.

Crítico – condições que exigem intervenção imediata.

Além do modelo de ML, foi projetado um banco relacional para persistir esses dados de forma estruturada.

🗄 Banco de Dados
DER textual

O documento db/der.txt
 descreve as entidades, atributos e relacionamentos de forma detalhada. As principais tabelas são:

Sensor – armazena metadados dos sensores (sensor_id, nome, localizacao).

Estado – normaliza os estados possíveis (estado_id, descricao).

Leitura – registra cada observação com data/hora, temperatura, vibração, além de chaves estrangeiras para Sensor e Estado.

O relacionamento Sensor 1:N Leitura indica que um sensor pode ter várias leituras ao longo do tempo. Da mesma forma, Estado 1:N Leitura conecta cada leitura ao estado classificado.

Script SQL

O script db/script.sql
 cria as tabelas, chaves primárias e estrangeiras, insere os estados padrão e define índices para otimizar consultas. Para executar o script:

Crie um banco de dados PostgreSQL (ou outro SGDB compatível).

Execute o conteúdo de script.sql no console do banco ou via ferramenta gráfica.

Use a tabela Sensor para cadastrar seus dispositivos antes de inserir leituras.

🤖 Machine Learning
Criação do Dataset

Um dataset artificial foi gerado contendo 1 500 leituras (3 sensores × 500 amostras), com colunas de temperatura, vibracao e o estado calculado (Normal, Alerta ou Crítico). O arquivo CSV está em data/dataset.csv
. Os valores foram simulados com distribuição normal e regras de negócio simples:

Leituras com temperatura muito alta (>80 °C) ou vibração muito alta (>6) são rotuladas como Crítico.

Leituras com temperatura moderada (>60 °C) ou vibração moderada (>4) são Alerta.

Demais leituras são Normais.

Implementação do Modelo

O código ml/main.py
 lê o CSV, codifica as classes, separa os dados em treino/teste (70/30), treina um modelo de Regressão Logística e gera métricas e gráficos. A escolha da Regressão Logística deve‑se à sua simplicidade e capacidade de lidar bem com problemas lineares multiclasse.

O script produz:

Relatório de métricas de classificação (precisão, recall, f1‑score) salvo em ml/metrics.txt
.

Matriz de Confusão (docs/matriz_confusao.png) para visualizar erros e acertos do modelo.

Gráfico de Dispersão (docs/scatter.png) mostrando a distribuição das leituras por estado.

Gráfico de Barras (docs/bar_chart.png) indicando o número de registros de cada classe.

Principais Resultados

O modelo alcançou boa performance, com métricas de precisão e recall superiores a 90 % para as classes Normal e Crítico, e cerca de 85 % para a classe Alerta. Veja o relatório completo em ml/metrics.txt
.

🚀 Instruções de Execução

Preparar Ambiente – Instale as dependências executando:

pip install -r requirements.txt


Executar SQL – Crie as tabelas do banco conforme db/script.sql.

Gerar Dataset (Opcional) – O CSV já está pronto, mas você pode regenerá‑lo com seu próprio script ou modificar a geração conforme necessário.

Treinar o Modelo – Execute o script de ML:

cd ml
python main.py


Visualizar Resultados – Após a execução, consulte os arquivos em ml/metrics.txt e docs/*.png para entender a performance e os gráficos.

🎬 Roteiro para Vídeo (≤ 5 min)

Introdução (30 s) – Apresentar o contexto do desafio Hermes Reply, a importância de monitorar sensores industriais e os objetivos do projeto.

Banco de Dados (60 s) – Explicar a modelagem relacional. Descrever as entidades Sensor, Estado e Leitura, destacando as cardinalidades e justificando a normalização.

Machine Learning (90 s) – Mostrar como o dataset foi gerado, quais características foram consideradas e por que a Regressão Logística foi escolhida. Apontar como o código está organizado e comentado.

Resultados (60 s) – Exibir rapidamente a matriz de confusão e os gráficos gerados, destacando as métricas principais.

Conclusão (30 s) – Resumir aprendizados, possíveis melhorias (ex.: usar dados reais, testar outros algoritmos) e convidar os espectadores a explorar o repositório.

📹 Link do Vídeo

Adicionar aqui o link para o vídeo explicativo assim que for gravado e hospedado.
