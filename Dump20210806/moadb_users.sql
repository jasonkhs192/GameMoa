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
  `win_rate` varchar(10) DEFAULT NULL,
  `totalgame` int DEFAULT NULL,
  `wins` int DEFAULT NULL,
  `loss` int DEFAULT NULL,
  `red_wins` int DEFAULT NULL,
  `red_loss` int DEFAULT NULL,
  `blue_wins` int DEFAULT NULL,
  `blue_loss` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'suppresser','Platinum','Jungle','77.78',18,14,4,4,2,10,2),(2,'dragonjin','Gold','Top','52.38',21,11,10,5,5,6,5),(3,'bluecrime','Unranked','Top','0.00',3,0,3,0,2,0,1),(4,'lincon9','Bronze','Jungle','44.83',29,13,16,3,15,10,1),(5,'churchhistory','Platinum','Support','51.61',31,16,15,5,11,11,4),(6,'oys4410','Gold','Top','55.00',20,11,9,3,7,8,2),(7,'gpoh508','Gold','Any','75.00',4,3,1,1,1,2,0),(8,'flearce','Platinum','Mid','41.38',29,12,17,2,13,10,4),(9,'dami bbo','Gold','ADC','50.00',12,6,6,2,4,4,2),(10,'enblanc','Gold','ADC','57.58',33,19,14,6,10,13,4),(11,'geon yeong kim','Gold','Mid','56.25',16,9,7,2,4,7,3),(12,'dudungappearance','Platinum','Jungle','20.00',5,1,4,1,2,0,2),(13,'illucky7','Silver','Mid','33.33',9,3,6,1,2,2,4),(14,'jyproot','Gold','ADC','0.00',1,0,1,0,0,0,1),(15,'cherry bear','Diamond','Top','53.85',13,7,6,2,6,5,0),(16,'feeblesticks','Diamond','Jungle','40.00',5,2,3,1,1,1,2),(17,'ettlia','Gold','Top','43.48',23,10,13,6,7,4,6),(18,'kaka0talk','Diamond','Jungle','None',0,0,0,0,0,0,0),(19,'jimmya92','Silver','Support','40.00',5,2,3,0,3,2,0),(20,'artbeatproject','Gold','Any','0.00',4,0,4,0,4,0,0),(21,'ssagajirungji','Gold','Support','25.00',4,1,3,1,1,0,2),(22,'bulldone','Unranked','Any','100.00',2,2,0,0,0,2,0),(23,'labslave','Silver','ADC','57.14',7,4,3,0,3,4,0),(24,'peterpapa','Bronze','ADC','0.00',2,0,2,0,2,0,0),(25,'kaykuva','Unranked','ADC','50.00',4,2,2,1,0,1,2),(26,'yellopanda','Bronze','Top','50.00',6,3,3,1,2,2,1),(27,'vananarang','Platinum','Jungle','50.00',18,9,9,3,5,6,4),(28,'research big guy','Platinum','Top','0.00',1,0,1,0,0,0,1),(29,'villma','Unranked','Any','None',0,0,0,0,0,0,0),(30,'vvookie','Gold','Mid','66.67',3,2,1,1,1,1,0),(31,'monbreak','Silver','Any','33.33',3,1,2,1,0,0,2),(32,'tomato and sugar','Unranked','Any','50.00',2,1,1,0,1,1,0),(33,'cb billma','Master','Mid','100.00',2,2,0,2,0,0,0),(34,'ohdidyoudothat','Unranked','Any','0.00',2,0,2,0,2,0,0),(35,'kat4','Grand Master','Mid','0.00',1,0,1,0,1,0,0),(36,'asdfaa','Unranked','Jungle','66.67',3,2,1,1,1,1,0),(37,'jun ki min','Gold','Mid','50.00',4,2,2,0,2,2,0);
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

-- Dump completed on 2021-08-06 16:51:27
