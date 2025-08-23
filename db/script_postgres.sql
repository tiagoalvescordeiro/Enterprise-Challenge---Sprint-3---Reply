-- DDL para criação das tabelas em PostgreSQL
CREATE TABLE IF NOT EXISTS Equipamento (
    id_equipamento SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    setor VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Sensor (
    id_sensor SERIAL PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    localizacao VARCHAR(100),
    descricao TEXT,
    id_equipamento INTEGER NOT NULL,
    FOREIGN KEY (id_equipamento) REFERENCES Equipamento(id_equipamento)
);

CREATE TABLE IF NOT EXISTS Leitura (
    id_leitura BIGSERIAL PRIMARY KEY,
    id_sensor INTEGER NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    unidade VARCHAR(20),
    FOREIGN KEY (id_sensor) REFERENCES Sensor(id_sensor)
);

CREATE TABLE IF NOT EXISTS Alerta (
    id_alerta SERIAL PRIMARY KEY,
    id_leitura BIGINT NOT NULL,
    nivel VARCHAR(10) NOT NULL CHECK (nivel IN ('Normal','Alerta','Crítico')),
    mensagem TEXT,
    FOREIGN KEY (id_leitura) REFERENCES Leitura(id_leitura)
);

CREATE TABLE IF NOT EXISTS Manutencao (
    id_manutencao SERIAL PRIMARY KEY,
    id_equipamento INTEGER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE,
    descricao TEXT,
    FOREIGN KEY (id_equipamento) REFERENCES Equipamento(id_equipamento)
);

-- Índices opcionais para melhorar consultas frequentes
CREATE INDEX IF NOT EXISTS idx_sensor_tipo ON Sensor(tipo);
CREATE INDEX IF NOT EXISTS idx_leitura_sensor ON Leitura(id_sensor);
CREATE INDEX IF NOT EXISTS idx_manutencao_equipamento ON Manutencao(id_equipamento);
