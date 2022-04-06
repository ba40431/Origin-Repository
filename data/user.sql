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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'abby','abby@abby','$2b$12$YKTGD/f3Q0AbF8eCcGJxKuk7LAphGUio8JWOJmIXnyZ3YWfQl4AB.'),(3,'test','test@test','$2b$12$PXm0HRFZ8TPT8pAJxmQ54e4wqHG1.EQQglW6yRbmmsCskiXe9zFkK'),(4,'kiki','kiki@kiki','$2b$12$6KgLWrP4/8qY6LnFq27dU.yhvTQdz/ohjrYKimYmV7UQFmpoAYyya'),(5,'aaron','aaron@aaron','$2b$12$ACEtuE5swSjxWgxQtEdj1.pHVImvzMPR54pg4t1JIUuCX2NXYvV9K'),(6,'蘋果','apple@apple','$2b$12$p4R4IL3lDwbVH/S1s6M57.jROFTPRZmBkV5UCAosmjQ/kjkmgofui'),(7,'莉莎','lisa@lisa','$2b$12$SsIDGjkPz0tUnvqwuIqeGOHhc4UfZaZQ8a0xZbIvI8MWIvaywHULi'),(8,'cat','cat@cat','$2b$12$O/wev/99cg0JGr0ZwCrG1O4XeyLrj.udY5LnfLgjcFvF5/hmzM93u'),(9,'dog','dog@dog','$2b$12$1thPCumYmu4GEQEccNuhvekIt8i.mjm3yUnKlFYmRjlsYyB9ETJeu'),(12,'abc','abc@abc','$2b$12$OsFFJQWJLdMqEFkl8Dhv3uZnpCTrLH4kQ9/LtQiDTR9oT3.lYe.Yu'),(13,'test','test@test','test'),(14,'test','test@test','test'),(15,'艾莉絲','alice@alice','$2b$12$q2IuNmx5GHrkm.PHE3D1OOXdpwzYfAFxITS4AiQ.icdnwMJletgQ6'),(16,'Apple','apple@apple.com','$2b$12$WPCbrZLnWWw3xnXphjvjSuKyNxHrcEVIkVKLMCBok2SAeOfI2OiWO'),(17,'test1','test1@test1','$2b$12$fpk2rBk8QL9XlK76EL.9QuWordPnK9sgy9tSBZ0hdZBS7eP9/S912'),(18,'test2','test2@test2','$2b$12$XP5Ms7p5rD9rPRGSHpLyxuUx.9YDGVae8Qs4gPGfzEV3FfTcQAwOW');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-05 19:25:25
