CREATE DATABASE IF NOT EXISTS streaming;
USE streaming;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(255),
    url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    video_id INT NOT NULL,
    date_watched TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (video_id) REFERENCES videos(id)
);

CREATE TABLE IF NOT EXISTS log_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    acao VARCHAR(50),
    data_evento DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS log_videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    video_id INT,
    acao VARCHAR(50),
    data_evento DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Auditoria: os triggers populam as tabelas de log e a view unifica tudo para leitura/relatório


DROP TRIGGER IF EXISTS trg_usuario_criado;
DROP TRIGGER IF EXISTS trg_usuario_deletado;
DROP TRIGGER IF EXISTS trg_video_criado;
DROP TRIGGER IF EXISTS trg_video_deletado;

DELIMITER //

CREATE TRIGGER trg_usuario_criado
AFTER INSERT
ON users
FOR EACH ROW
BEGIN
    INSERT INTO log_usuarios (
        usuario_id,
        acao
    )
    VALUES (
        NEW.id,
        'USUARIO_CRIADO'
    );
END//

CREATE TRIGGER trg_usuario_deletado
AFTER DELETE
ON users
FOR EACH ROW
BEGIN
    INSERT INTO log_usuarios (
        usuario_id,
        acao
    )
    VALUES (
        OLD.id,
        'USUARIO_DELETADO'
    );
END//

CREATE TRIGGER trg_video_criado
AFTER INSERT
ON videos
FOR EACH ROW
BEGIN
    INSERT INTO log_videos (
        video_id,
        acao
    )
    VALUES (
        NEW.id,
        'VIDEO_CRIADO'
    );
END//

CREATE TRIGGER trg_video_deletado
AFTER DELETE
ON videos
FOR EACH ROW
BEGIN
    INSERT INTO log_videos (
        video_id,
        acao
    )
    VALUES (
        OLD.id,
        'VIDEO_DELETADO'
    );
END//

DELIMITER ;


CREATE OR REPLACE VIEW vw_auditoria AS
SELECT 'USUARIO' AS tipo, usuario_id AS referencia_id, acao, data_evento
FROM log_usuarios
UNION ALL
SELECT 'VIDEO' AS tipo, video_id AS referencia_id, acao, data_evento
FROM log_videos;
