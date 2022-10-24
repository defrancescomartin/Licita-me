-- **************************** SqlDBM: MySQL ***************************
-- *** Generated for LicitaMe, v1 by 4437@holbertonstudents.com **
-- Script that creates the MySQL server user licitame if not exists and grant al privileges.

CREATE DATABASE IF NOT EXISTS `LicitaMeDB`;
CREATE USER IF NOT EXISTS 'licitame'@'localhost' IDENTIFIED BY 'Password-2022';
GRANT ALL PRIVILEGES ON LicitaMeDB . * TO 'licitame'@'localhost';
GRANT SELECT ON performance_schema . * TO 'licitame'@'localhost';

-- ************************************** `LicitaMeDB`.`Company`

CREATE TABLE `LicitaMeDB`.`Company`
(
 `CompanyId`   int NOT NULL AUTO_INCREMENT ,
 `CompanyName` varchar(45) NOT NULL ,
 `RUT`         varchar(12) NOT NULL ,
 `RSocial`     varchar(45) NULL ,
 `Address`     varchar(45) NULL ,
 `State`       varchar(45) NULL ,
 `City`        varchar(45) NULL ,
 `Phone`       varchar(20) NULL ,
 `CreationDate`     datetime DEFAULT CURRENT_TIMESTAMP ,
 `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,

PRIMARY KEY (`CompanyId`)
);

-- ************************************** `LicitaMeDB`.`User`

CREATE TABLE `LicitaMeDB`.`User`
(
 `id`               int NOT NULL AUTO_INCREMENT ,
 `CompanyId`        int NOT NULL ,
 `CustomerName`     varchar(25) NOT NULL ,
 `Phone`            varchar(20) NULL ,
 `Email`            varchar(45) NULL ,
 `Birthdate`        date NULL ,
 `Address`          varchar(45) NULL ,
 `State`            varchar(45) NULL ,
 `City`             varchar(45) NULL ,
 `Password`         varchar(80) NOT NULL ,
 `CreationDate`     datetime DEFAULT CURRENT_TIMESTAMP ,
 `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,

PRIMARY KEY (`id`),
KEY `FK_2` (`CompanyId`),
CONSTRAINT `FK_1` FOREIGN KEY `FK_2` (`CompanyId`) REFERENCES `LicitaMeDB`.`Company` (`CompanyId`)
);

-- ************************************** `LicitaMeDB`.`Request`

CREATE TABLE `LicitaMeDB`.`Request`
(
 `RequestId`      int NOT NULL AUTO_INCREMENT ,
 `id`             int NOT NULL ,
 `CompanyId`      int NOT NULL ,
 `FileId`         varchar(10) NULL ,
 `StartingDate`   date NULL ,
 `FinishDate`     date NULL ,
 `Category`       varchar(45) NULL ,
 `Description`    mediumtext NULL ,
 `Title`          varchar(45) NULL ,
 `StatusCode`     int NULL ,
 `CreationDate`     datetime DEFAULT CURRENT_TIMESTAMP ,
 `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,

PRIMARY KEY (`RequestId`),
KEY `FK_2` (`CompanyId`),
CONSTRAINT `FK_2` FOREIGN KEY `FK_2` (`CompanyId`) REFERENCES `LicitaMeDB`.`Company` (`CompanyId`),
KEY `FK_3` (`id`),
CONSTRAINT `FK_5` FOREIGN KEY `FK_3` (`id`) REFERENCES `LicitaMeDB`.`User` (`id`)
);

-- ************************************** `LicitaMeDB`.`Bid`

CREATE TABLE `LicitaMeDB`.`Bid`
(
 `BidId`        int NOT NULL AUTO_INCREMENT ,
 `BidNumber`    varchar(10) NOT NULL ,
 `id`           int NOT NULL ,
 `RequestId`    int NULL ,
 `CompanyId`    int NOT NULL ,
 `TotalAmount`  decimal(12,2) NULL ,
 `StartingDate` date NULL ,
 `FinishDate`   date NULL ,
 `Category`     varchar(45) NULL ,
 `FileId`       varchar(10) NULL ,
 `CurrencyCode` int NULL ,
 `StatusCode`   int NULL ,
 `CreationDate`     datetime DEFAULT CURRENT_TIMESTAMP ,
 `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,

PRIMARY KEY (`BidId`),
KEY `FK_2` (`CompanyId`),
CONSTRAINT `FK_3` FOREIGN KEY `FK_2` (`CompanyId`) REFERENCES `LicitaMeDB`.`Company` (`CompanyId`),
KEY `FK_3` (`RequestId`),
CONSTRAINT `FK_4` FOREIGN KEY `FK_3` (`RequestId`) REFERENCES `LicitaMeDB`.`Request` (`RequestId`),
KEY `FK_4` (`id`),
CONSTRAINT `FK_6` FOREIGN KEY `FK_4` (`id`) REFERENCES `LicitaMeDB`.`User` (`id`)
);
