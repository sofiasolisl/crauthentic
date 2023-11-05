CREATE DATABASE  IF NOT EXISTS `crauthentic` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `crauthentic`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: crauthentic
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `cellphone` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Sofia','Solis Loaiciga','sofis64@gmail.com',87055124,'2023-11-01 16:14:12','2023-11-05 11:52:44'),(2,'Pablo','Fallas Florian','pafaflo18@gmail.com',87055124,'2023-11-04 21:53:05','2023-11-04 22:05:50');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `id` int NOT NULL,
  `location` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'Airport Daniel Oduber (Liberia)','2023-10-30 13:54:20','2023-10-30 13:54:20'),(2,'Papagayo','2023-10-30 13:54:40','2023-10-30 13:54:40'),(3,'Flamingo','2023-10-30 13:54:53','2023-10-30 13:54:53'),(4,'Rincon de la Vieja','2023-10-30 13:55:22','2023-10-30 13:55:22'),(5,'La Fortuna','2023-10-30 13:55:38','2023-10-30 13:55:38'),(6,'Aeropuerto Juan Santamaria','2023-10-30 13:56:14','2023-10-30 13:56:14');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL,
  `pickup_details` varchar(255) DEFAULT NULL,
  `dropoff_details` varchar(255) DEFAULT NULL,
  `passengers` int DEFAULT NULL,
  `suitcases` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `hour` time DEFAULT NULL,
  `prices_idprices` int NOT NULL,
  `prices_routes_id` int NOT NULL,
  `customers_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`prices_idprices`,`prices_routes_id`,`customers_id`),
  KEY `fk_orders_prices1_idx` (`prices_idprices`,`prices_routes_id`),
  KEY `fk_orders_customers1_idx` (`customers_id`),
  CONSTRAINT `fk_orders_customers1` FOREIGN KEY (`customers_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `fk_orders_prices1` FOREIGN KEY (`prices_idprices`, `prices_routes_id`) REFERENCES `prices` (`id`, `route_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'hola','hola',1,1,'2023-11-08','21:47:00',1,1,1,'2023-11-04 21:48:14','2023-11-04 21:48:14'),(2,'hola','hola',1,1,'2023-11-08','21:47:00',1,1,1,'2023-11-04 21:49:06','2023-11-04 21:49:06'),(3,'hola','hola',1,1,'2023-11-08','21:47:00',1,1,1,'2023-11-04 21:49:25','2023-11-04 21:49:25'),(4,'hola','hola',1,1,'2023-11-08','21:47:00',1,1,1,'2023-11-04 21:50:47','2023-11-04 21:50:47'),(5,'hola','hola',1,1,'2023-11-28','21:52:00',2,2,2,'2023-11-04 21:53:17','2023-11-04 21:53:17'),(6,'hola','hola',1,1,'2023-11-09','22:10:00',1,1,2,'2023-11-04 22:06:00','2023-11-04 22:06:00'),(7,'hola','hola',1,1,'2023-11-06','23:52:00',1,1,1,'2023-11-05 11:53:24','2023-11-05 11:53:24'),(8,'hola','hola',1,1,'2023-11-06','23:52:00',1,1,1,'2023-11-05 12:05:01','2023-11-05 12:05:01'),(9,'hola','hola',1,1,'2023-11-06','23:52:00',1,1,1,'2023-11-05 12:05:25','2023-11-05 12:05:25');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prices`
--

DROP TABLE IF EXISTS `prices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prices` (
  `id` int NOT NULL,
  `price` int DEFAULT NULL,
  `route_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`route_id`),
  KEY `fk_prices_routes1_idx` (`route_id`),
  CONSTRAINT `fk_prices_routes1` FOREIGN KEY (`route_id`) REFERENCES `routes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prices`
--

LOCK TABLES `prices` WRITE;
/*!40000 ALTER TABLE `prices` DISABLE KEYS */;
INSERT INTO `prices` VALUES (1,40,1,'2023-10-30 14:10:22','2023-10-30 14:10:22'),(2,50,2,'2023-10-30 14:10:57','2023-10-30 14:10:57'),(3,50,3,'2023-10-30 14:11:07','2023-10-30 14:11:07'),(4,60,4,'2023-10-30 14:11:33','2023-10-30 14:11:33'),(5,70,5,'2023-10-30 14:12:25','2023-10-30 14:12:25'),(6,40,6,'2023-10-30 14:12:36','2023-10-30 14:12:36'),(7,50,7,'2023-10-30 14:12:42','2023-10-30 14:12:42'),(8,50,8,'2023-10-30 14:12:51','2023-10-30 14:12:51'),(9,60,9,'2023-10-30 14:13:41','2023-10-30 14:13:41'),(10,70,10,'2023-10-30 14:13:50','2023-10-30 14:13:50');
/*!40000 ALTER TABLE `prices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routes`
--

DROP TABLE IF EXISTS `routes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `routes` (
  `id` int NOT NULL,
  `duration` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `from_location_id` int NOT NULL,
  `to_location_id` int NOT NULL,
  PRIMARY KEY (`id`,`from_location_id`,`to_location_id`),
  KEY `fk_routes_locations1_idx` (`from_location_id`),
  KEY `fk_routes_locations2_idx` (`to_location_id`),
  CONSTRAINT `fk_routes_locations1` FOREIGN KEY (`from_location_id`) REFERENCES `locations` (`id`),
  CONSTRAINT `fk_routes_locations2` FOREIGN KEY (`to_location_id`) REFERENCES `locations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routes`
--

LOCK TABLES `routes` WRITE;
/*!40000 ALTER TABLE `routes` DISABLE KEYS */;
INSERT INTO `routes` VALUES (1,1,'2023-10-30 13:57:23','2023-10-30 13:57:23',1,2),(2,2,'2023-10-30 13:58:18','2023-10-30 13:58:18',1,3),(3,1,'2023-10-30 13:58:43','2023-10-30 13:58:43',1,4),(4,3,'2023-10-30 13:59:00','2023-10-30 13:59:00',1,5),(5,4,'2023-10-30 13:59:36','2023-10-30 13:59:36',1,6),(6,4,'2023-10-30 14:00:07','2023-10-30 14:00:07',6,1),(7,3,'2023-10-30 14:00:37','2023-10-30 14:00:37',5,1),(8,1,'2023-10-30 14:00:47','2023-10-30 14:00:47',4,1),(9,2,'2023-10-30 14:00:58','2023-10-30 14:00:58',3,1),(10,1,'2023-10-30 14:01:16','2023-10-30 14:01:16',2,1);
/*!40000 ALTER TABLE `routes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-05 12:23:22
