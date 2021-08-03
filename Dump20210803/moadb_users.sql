-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: moadb
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `SummonerName` varchar(30) NOT NULL,
  `RankTier` varchar(15) DEFAULT NULL,
  `MainPosition` varchar(10) DEFAULT NULL,
  `totalgame` int DEFAULT NULL,
  `wins` int DEFAULT NULL,
  `loss` int DEFAULT NULL,
  `red_wins` int DEFAULT NULL,
  `red_loss` int DEFAULT NULL,
  `blue_wins` int DEFAULT NULL,
  `blue_loss` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'suppresser','Platinum','Jungle',NULL,0,0,0,0,0,0),(2,'dragonjin','Gold','Top',NULL,0,0,0,0,0,0),(3,'bluecrime','Unranked','Top',NULL,0,0,0,0,0,0),(4,'lincon9','Bronze','Jungle',NULL,0,0,0,0,0,0),(5,'churchhistory','Platinum','Support',NULL,0,0,0,0,0,0),(6,'oys4410','Gold','Top',NULL,0,0,0,0,0,0),(7,'gpoh508','Gold','Any',NULL,0,0,0,0,0,0),(8,'flearce','Platinum','Mid',NULL,0,0,0,0,0,0),(9,'dami bbo','Gold','ADC',NULL,0,0,0,0,0,0),(10,'enblanc','Gold','ADC',NULL,0,0,0,0,0,0),(11,'geon yeong kim','Gold','Mid',NULL,0,0,0,0,0,0),(12,'dudungappearance','Platinum','Jungle',NULL,0,0,0,0,0,0),(13,'illucky7','Silver','Mid',NULL,0,0,0,0,0,0),(14,'jyproot','Gold','ADC',NULL,0,0,0,0,0,0),(15,'cherry bear','Diamond','Top',NULL,0,0,0,0,0,0),(16,'feeblesticks','Diamond','Jungle',NULL,0,0,0,0,0,0),(17,'ettlia','Gold','Top',NULL,0,0,0,0,0,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-03 17:11:45
