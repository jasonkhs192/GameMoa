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
-- Table structure for table `blueteam`
--

DROP TABLE IF EXISTS `blueteam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blueteam` (
  `id` int NOT NULL AUTO_INCREMENT,
  `top` varchar(20) DEFAULT NULL,
  `jungle` varchar(20) DEFAULT NULL,
  `mid` varchar(20) DEFAULT NULL,
  `adc` varchar(20) DEFAULT NULL,
  `support` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blueteam`
--

LOCK TABLES `blueteam` WRITE;
/*!40000 ALTER TABLE `blueteam` DISABLE KEYS */;
INSERT INTO `blueteam` VALUES (1,'dragonjin','suppresser','gpoh508','dami bbo','oys4410'),(2,'bluecrime','lincon9','flearce','enblanc','churchhistory'),(3,'oys4410','lincon9','suppresser','enblanc','churchhistory'),(4,'bulldone','suppresser','gpoh508','dami bbo','geon yeong kim'),(5,'research big guy','dudungappearance','flearce','jyproot','illucky7'),(6,'dudungappearance','feeblesticks','illucky7','dami bbo','ssagajirungji'),(7,'dragonjin','lincon9','suppresser','enblanc','churchhistory'),(8,'ettlia','feeblesticks','illucky7','dragonjin','churchhistory'),(9,'ettlia','flearce','geon yeong kim','dami bbo','ssagajirungji'),(10,'oys4410','flearce','geon yeong kim','enblanc','jimmya92'),(11,'lincon9','suppresser','bulldone','enblanc','churchhistory'),(12,'dragonjin','suppresser','flearce','labslave','feeblesticks'),(13,'dragonjin','lincon9','geon yeong kim','enblanc','vvookie'),(14,'ettlia','suppresser','flearce','enblanc','churchhistory'),(15,'lincon9','flearce','geon yeong kim','kaykuva','oys4410'),(16,'yellopanda','vananarang','geon yeong kim','enblanc','oys4410'),(17,'cherry bear','lincon9','vananarang','labslave','oys4410'),(18,'yellopanda','flearce','geon yeong kim','enblanc','churchhistory'),(19,'ettlia','flearce','illucky7','enblanc','churchhistory'),(20,'ettlia','flearce','illucky7','enblanc','churchhistory'),(21,'yellopanda','asdfaa','geon yeong kim','vananarang','oys4410'),(22,'ettlia','dragonjin','vananarang','kaykuva','monbreak'),(23,'lincon9','illucky7','geon yeong kim','enblanc','churchhistory'),(24,'ettlia','dragonjin','vananarang','kaykuva','monbreak'),(25,'ettlia','lincon9','flearce','vananarang','oys4410'),(26,'dragonjin','suppresser','geon yeong kim','enblanc','churchhistory'),(27,'cherry bear','suppresser','flearce','vananarang','oys4410'),(28,'dragonjin','suppresser','tomato and sugar','enblanc','churchhistory'),(29,'cherry bear','lincon9','flearce','enblanc','churchhistory'),(30,'dragonjin','suppresser','ettlia','vananarang','oys4410'),(31,'lincon9','vananarang','jun ki min','enblanc','churchhistory'),(32,'labslave','suppresser','cherry bear','dami bbo','jimmya92'),(33,'labslave','flearce','ettlia','vananarang','dami bbo'),(34,'cherry bear','dragonjin','jun ki min','enblanc','churchhistory');
/*!40000 ALTER TABLE `blueteam` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-04 17:13:46
