-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: spot_project
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number` varchar(255) NOT NULL,
  `attraction_id` bigint NOT NULL,
  `attraction_name` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL,
  `price` int NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  `user_phone` varchar(255) NOT NULL,
  `status` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `attraction_id` (`attraction_id`),
  KEY `user_email` (`user_email`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`attraction_id`) REFERENCES `taipei_spots` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`user_email`) REFERENCES `user` (`email`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'1649140378-1',5,'北投圖書館','2022-04-21','afternoon',2500,'abby','abby@abby','0912345678',0),(2,'1649140496-1',5,'北投圖書館','2022-04-21','afternoon',2500,'abby','abby@abby','0912345678',0),(3,'1649141311-1',5,'北投圖書館','2022-04-21','afternoon',2500,'abby','abby@abby','0912345678',1),(4,'1649141454-1',5,'北投圖書館','2022-04-21','afternoon',2500,'abby','abby@abby','0912345678',1),(5,'1649143166-1',10,'南港山系-象山親山步道','2022-04-28','afternoon',2500,'abby','abby@abby','0912345678',1),(6,'1649143227-1',3,'士林官邸','2022-04-21','afternoon',2500,'abby','abby@abby','0912345678',1),(7,'1649143867-3',3,'士林官邸','2022-04-14','afternoon',2500,'test','test@test','0999999999',1),(8,'1649143946-3',10,'南港山系-象山親山步道','2022-04-13','afternoon',2500,'test','test@test','0999999999',1),(9,'1649155823-1',3,'士林官邸','2022-04-21','afternoon',2500,'abby','abby@abby','0955555555',1),(10,'1649156017-1',12,'行天宮','2022-04-19','afternoon',2500,'abby','abby@abby','0922222222',1),(11,'1649156212-1',12,'行天宮','2022-04-19','afternoon',2500,'abby','abby@abby','0922222222',0),(12,'1649156361-1',7,'關渡、金色水岸、八里左岸自行車道','2022-04-26','afternoon',2500,'abby','abby@abby','0912345678',0),(13,'1649156391-1',7,'關渡、金色水岸、八里左岸自行車道','2022-04-26','afternoon',2500,'abby','abby@abby','0912345678',0),(14,'1649156454-1',7,'關渡、金色水岸、八里左岸自行車道','2022-04-26','afternoon',2500,'abby','abby@abby','0912345678',0),(15,'1649156487-1',7,'關渡、金色水岸、八里左岸自行車道','2022-04-26','afternoon',2500,'abby','abby@abby','0912345678',0),(16,'1649156503-1',7,'關渡、金色水岸、八里左岸自行車道','2022-04-26','afternoon',2500,'abby','abby@abby','0912345678',1),(17,'1649157780-1',12,'行天宮','2022-04-27','afternoon',2500,'abby','abby@abby','0912345678',1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-05 19:26:07
