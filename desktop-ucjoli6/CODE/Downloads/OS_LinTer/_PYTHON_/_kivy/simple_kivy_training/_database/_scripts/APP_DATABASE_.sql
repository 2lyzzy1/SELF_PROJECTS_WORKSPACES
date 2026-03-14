CREATE DATABASE usenv_;

USE usenv_;

-- self.QUERY

CREATE TABLE user_(
  userID INT NOT NULL AUTOINCREMENT PRIMARY KEY,
  lastName VARCHAR(50) NOT NULL,
  firstName VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  birthDate DATE,
  birthPlace VARCHAR(100) NOT NULL,
  residencePlace VARCHAR(100) NOT NULL,
  job_ VARCHAR(50) NOT NULL,
  height INT NOT NULL,
  weigth INT NOT NULL,
  morphology VARCHAR(200),
  defects VARCHAR(200),
  isTerrian VARCHAR(25),
);

INSERT INTO TABLE user_
  (lastName, firstName, age, birthDate, birthPlace, residencePlace, job_, height, weigth, morphology, defects, isTerrian)
VALUES
  (),
  (),
  (),

-- DEAD ZONE
--DELETE TABLE user_;
--DROP DATABASE usenv_;
