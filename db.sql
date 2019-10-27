DROP TABLE IF EXISTS native_plants_location;
DROP TABLE IF EXISTS native_plants;

CREATE TABLE IF NOT EXISTS native_plants (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  scientific_name VARCHAR(256) UNIQUE NOT NULL,
  common_name VARCHAR(256),
  description VARCHAR(2048),
  url VARCHAR(512)
);

CREATE TABLE IF NOT EXISTS native_plants_location (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  scientific_name VARCHAR(256),
  latitude INT(11) NOT NULL,
  longitude INT(11) NOT NULL,
  image_url VARCHAR(512),
  FOREIGN KEY (scientific_name) REFERENCES native_plants(scientific_name)
);
