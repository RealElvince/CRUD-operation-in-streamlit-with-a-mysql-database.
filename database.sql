CREATE DATABASE crud_streamlit;

USE crud_streamlit;

CREATE TABLE users(
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone_number VARCHAR(50),
  email VARCHAR(50)
  
);
