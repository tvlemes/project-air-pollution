/*
File: raw_air_pollution.py
Author: Thiago Vilarinho Lemes
Date: 2023-05-13
e-mail: contatothiagolemes@gmail.com
Description: This file is part of the Big Data project to assess air pollution.

Project: Air Pollution
*/
DROP TABLE IF EXISTS air_pollution;
CREATE TABLE IF NOT EXISTS air_pollution(ID SERIAL PRIMARY KEY, CO FLOAT, NO FLOAT, NO2 FLOAT, O3 FLOAT, SO2 FLOAT, PM2_5 FLOAT, PM10 FLOAT, NH3 FLOAT, DATE_PERIOD TIMESTAMP, DATE_DAY INT, DATE_MONTH INT, DATE_YEAR INT, NAME_MONTH VARCHAR(10), DATE_HOUR INT);