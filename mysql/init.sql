CREATE TABLE ciudades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    temperatura FLOAT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO ciudades(nombre, temperatura)
VALUES
('Medellin', 24),
('Bogota', 18),
('Cali', 30);