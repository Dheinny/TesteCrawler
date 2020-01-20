--
-- Banco de dados: `app_crawler`
--
CREATE DATABASE IF NOT EXISTS `app_crawler`;
USE `app_crawler`;

CREATE TABLE eventos(
	id INT(7) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome_evento VARCHAR(50),
    nome_local VARCHAR(50),
    cidade_local VARCHAR(30),
    descricao LONGTEXT,
    data_evento DATE,
    dia_semana VARCHAR(10),
    hora_evento TIME,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE tipo_tickets (
  id INT(7) UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
  id_eventos INT(7) UNSIGNED NOT NULL,
  tipo_ticket VARCHAR(20) DEFAULT NULL,
  valor_ticket DECIMAL(6,2) DEFAULT NULL,
  taxa_ticket DECIMAL(5,2) DEFAULT NULL,
  FOREIGN KEY (id_eventos)
        REFERENCES eventos(id)
        ON DELETE CASCADE
);
