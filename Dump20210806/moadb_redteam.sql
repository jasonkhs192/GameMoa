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
-- Table structure for table `redteam`
--

DROP TABLE IF EXISTS `redteam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `redteam` (
  `id` int NOT NULL AUTO_INCREMENT,
  `top` varchar(20) DEFAULT NULL,
  `jungle` varchar(20) DEFAULT NULL,
  `mid` varchar(20) DEFAULT NULL,
  `adc` varchar(20) DEFAULT NULL,
  `support` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `redteam`
--

LOCK TABLES `redteam` WRITE;
/*!40000 ALTER TABLE `redteam` DISABLE KEYS */;
INSERT INTO `redteam` VALUES (1,'bluecrime','lincon9','flearce','enblanc','churchhistory'),(2,'dragonjin','suppresser','gpoh508','dami bbo','oys4410'),(3,'bluecrime','dragonjin','flearce','dami bbo','gpoh508'),(4,'dragonjin','oys4410','flearce','enblanc','churchhistory'),(5,'ettlia','lincon9','cb billma','enblanc','churchhistory'),(6,'cherry bear','lincon9','flearce','ettlia','oys4410'),(7,'feeblesticks','dudungappearance','cherry bear','dami bbo','ssagajirungji'),(8,'lincon9','suppresser','cherry bear','enblanc','flearce'),(9,'oys4410','artbeatproject','ohdidyoudothat','enblanc','jimmya92'),(10,'ettlia','artbeatproject','ohdidyoudothat','dami bbo','ssagajirungji'),(11,'artbeatproject','dudungappearance','dragonjin','ettlia','flearce'),(12,'lincon9','dudungappearance','kat4','jimmya92','ettlia'),(13,'ettlia','suppresser','flearce','peterpapa','churchhistory'),(14,'lincon9','feeblesticks','dragonjin','peterpapa','vvookie'),(15,'ettlia','dragonjin','vvookie','enblanc','churchhistory'),(16,'artbeatproject','lincon9','flearce','labslave','churchhistory'),(17,'yellopanda','flearce','geon yeong kim','enblanc','churchhistory'),(18,'lincon9','vananarang','cherry bear','labslave','oys4410'),(19,'yellopanda','asdfaa','geon yeong kim','vananarang','oys4410'),(20,'yellopanda','asdfaa','geon yeong kim','vananarang','oys4410'),(21,'ettlia','flearce','illucky7','enblanc','churchhistory'),(22,'lincon9','illucky7','geon yeong kim','enblanc','churchhistory'),(23,'ettlia','dragonjin','vananarang','kaykuva','monbreak'),(24,'lincon9','illucky7','geon yeong kim','enblanc','churchhistory'),(25,'dragonjin','suppresser','geon yeong kim','enblanc','churchhistory'),(26,'ettlia','lincon9','flearce','vananarang','oys4410'),(27,'dragonjin','lincon9','tomato and sugar','enblanc','churchhistory'),(28,'ettlia','dragonjin','flearce','vananarang','oys4410'),(29,'cherry bear','lincon9','flearce','vananarang','oys4410'),(30,'dragonjin','suppresser','ettlia','vananarang','oys4410'),(31,'cherry bear','lincon9','flearce','enblanc','churchhistory'),(32,'labslave','suppresser','cherry bear','dami bbo','jimmya92'),(33,'lincon9','flearce','jun ki min','enblanc','churchhistory'),(34,'lincon9','cherry bear','jun ki min','enblanc','churchhistory'),(35,'ettlia','lincon9','flearce','dami bbo','vananarang');
/*!40000 ALTER TABLE `redteam` ENABLE KEYS */;
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
