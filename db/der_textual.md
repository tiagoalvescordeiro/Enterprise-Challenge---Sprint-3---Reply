# Modelo Relacional (DER Textual)

Este documento descreve as entidades e relacionamentos do banco de dados proposto para monitoramento de sensores e manutenção de equipamentos em uma linha de produção.

## Entidades

### **Sensor**
- **id_sensor** (PK): identificador único do sensor.
- **tipo**: tipo de sensor (temperatura, vibração, pressão etc.).
- **localizacao**: local onde o sensor está instalado (linha de produção, setor, máquina etc.).
- **descricao**: descrição adicional do sensor.
- **id_equipamento** (FK → Equipamento.id_equipamento): equipamento ao qual o sensor está associado.

### **Leitura**
- **id_leitura** (PK): identificador único da leitura.
- **id_sensor** (FK → Sensor.id_sensor): sensor que gerou a leitura.
- **timestamp**: data e hora da leitura.
- **valor**: valor numérico da leitura.
- **unidade**: unidade de medida (°C, mm/s², bar etc.).

### **Equipamento**
- **id_equipamento** (PK): identificador único do equipamento.
- **nome**: nome ou código do equipamento.
- **descricao**: descrição do equipamento.
- **setor**: setor ou linha em que o equipamento opera.

### **Manutencao**
- **id_manutencao** (PK): identificador único do registro de manutenção.
- **id_equipamento** (FK → Equipamento.id_equipamento): equipamento que recebeu a manutenção.
- **data_inicio**: data de início da manutenção.
- **data_fim**: data de término da manutenção (pode ser nula se em andamento).
- **descricao**: descrição da intervenção realizada.

### **Alerta**
- **id_alerta** (PK): identificador único do alerta.
- **id_leitura** (FK → Leitura.id_leitura): leitura que originou o alerta.
- **nivel**: nível de alerta (Normal, Alerta ou Crítico).
- **mensagem**: mensagem descritiva do alerta.

## Relacionamentos e Cardinalidades

- **Equipamento–Sensor**: Um equipamento pode possuir **vários sensores** (1:N). Cada sensor está associado a um equipamento.
- **Sensor–Leitura**: Um sensor gera **muitas leituras** ao longo do tempo (1:N). Cada leitura pertence a um único sensor.
- **Leitura–Alerta**: Uma leitura pode gerar **nenhum ou um** alerta (0:1). Um alerta sempre está associado a exatamente uma leitura.
- **Equipamento–Manutencao**: Um equipamento pode ter **múltiplas manutenções** registradas (1:N). Cada manutenção refere-se a um equipamento.

## Justificativa

- O modelo segue os princípios de normalização para evitar redundância de dados.
- Chaves estrangeiras garantem a integridade referencial entre as tabelas.
- Tipos de dados são escolhidos conforme as necessidades (por exemplo, `DECIMAL` para valores de sensores e `TIMESTAMP` para registros de tempo).
