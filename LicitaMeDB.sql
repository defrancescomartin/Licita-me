-- MySQL dump 10.13  Distrib 5.7.39, for Linux (x86_64)
--
-- Host: localhost    Database: LicitaMeDB
-- ------------------------------------------------------
-- Server version	5.7.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Bid`
--

DROP TABLE IF EXISTS `Bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bid` (
  `BidId` int(11) NOT NULL,
  `BidNumber` varchar(10) NOT NULL,
  `RequestId` int(11) NOT NULL,
  `CompanyId` int(11) NOT NULL,
  `CreationDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `TotalAmount` decimal(12,2) NOT NULL,
  `StartingDate` date NOT NULL,
  `FinishDate` date NOT NULL,
  `Category` varchar(45) NOT NULL,
  `FileId` varchar(10) NOT NULL,
  PRIMARY KEY (`BidId`),
  KEY `FK_2` (`CompanyId`),
  KEY `FK_3` (`RequestId`),
  CONSTRAINT `FK_3` FOREIGN KEY (`CompanyId`) REFERENCES `Company` (`CompanyId`),
  CONSTRAINT `FK_4` FOREIGN KEY (`RequestId`) REFERENCES `Request` (`RequestId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bid`
--

LOCK TABLES `Bid` WRITE;
/*!40000 ALTER TABLE `Bid` DISABLE KEYS */;
/*!40000 ALTER TABLE `Bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Company`
--

DROP TABLE IF EXISTS `Company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Company` (
  `CompanyId` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyName` varchar(45) NOT NULL,
  `RUT` int(11) NOT NULL,
  `RSocial` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `State` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `CreationDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`CompanyId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Company`
--

LOCK TABLES `Company` WRITE;
/*!40000 ALTER TABLE `Company` DISABLE KEYS */;
INSERT INTO `Company` VALUES (1,'Holberton inc',0,'','','','','','2022-10-15 07:03:11','2022-10-15 07:03:11');
/*!40000 ALTER TABLE `Company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Request`
--

DROP TABLE IF EXISTS `Request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Request` (
  `RequestId` int(11) NOT NULL AUTO_INCREMENT,
  `RequestNumber` varchar(10) NOT NULL,
  `CompanyId` int(11) NOT NULL,
  `CreationDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `CurrencyCode` int(11) NOT NULL,
  `StaringDate` date NOT NULL,
  `FinishDate` date NOT NULL,
  `Category` varchar(45) NOT NULL,
  `Description` mediumtext NOT NULL,
  `Title` varchar(45) NOT NULL,
  `StatusCode` int(11) NOT NULL,
  PRIMARY KEY (`RequestId`),
  KEY `FK_2` (`CompanyId`),
  CONSTRAINT `FK_2` FOREIGN KEY (`CompanyId`) REFERENCES `Company` (`CompanyId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Request`
--

LOCK TABLES `Request` WRITE;
/*!40000 ALTER TABLE `Request` DISABLE KEYS */;
/*!40000 ALTER TABLE `Request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `UserId` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyId` int(11) NOT NULL,
  `CustomerName` varchar(20) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `CreationDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `ModificationDate` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Email` varchar(45) NOT NULL,
  `Birthdate` date NOT NULL,
  `Address` varchar(45) NOT NULL,
  `State` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `Password` varchar(80) NOT NULL,
  PRIMARY KEY (`UserId`),
  KEY `FK_2` (`CompanyId`),
  CONSTRAINT `FK_1` FOREIGN KEY (`CompanyId`) REFERENCES `Company` (`CompanyId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (3,1,'Holberton','','2022-10-15 07:06:50','2022-10-15 07:06:50','','0000-00-00','','','','');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-15  8:13:34
