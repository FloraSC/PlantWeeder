CREATE TABLE IF NOT EXISTS native_plants (
  id PRIMARY KEY AUTO_INCREMENT,
  scientific_name TEXT UNIQUE NOT NULL,
  common_name TEXT,
  description MEDIUMTEXT,
  url TEXT
)

CREATE TABLE IF NOT EXISTS native_plants_location (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  scientific_name TEXT,
  latituce INT(11) NOT NULL,
  longitude INT(11) NOT NULL,
  image_url TEXT,
  fk_npl_scientific_name FOREIGN KEY (scientific_name) REFERENCES native_plants(scientific_name)
)
