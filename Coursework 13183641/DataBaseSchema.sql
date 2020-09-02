-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: coursework2-13183641
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `isbn` varchar(45) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `publisher` varchar(45) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`isbn`),
  UNIQUE KEY `isbn_UNIQUE` (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('0192839705','Mrs Dalloway','Woolf, Virginia','Oxford World Classics',2000,'Novel'),('03004056','The discovery of mankind : Atlantic encounters in the age of Columbus / ','Abulafia, David.','Atlantic Books',2008,'Gardening'),('0415226643','The psychology of being happy','Argyle, Michael','Routledge',2001,'Self-Help'),('0500232121','The heyday of salon painting : masterpieces of bourgeois realism','Čelebonović, Aleksa.','Thames and Hudson,',1974,'Art'),('0805500003','New ideas for the XX Century','Clarke, Michael','Oxford University Press',1901,'Art'),('0824017781','Six discourses on the miracles of Our Saviour ; and, Defences of his discourses, 1727-1730','Woolston, Thomas','Garland Publishing',1887,'Philosophy'),('0953886670','Translations from the Russian','Woolf, Virginia','Virginia Woolf Society of Great Britain',2017,'Novel'),('1854106554','The garden : a history in landscape and art','Pizzoni, Filippo.','Aurum Press',1999,'Gardening'),('1912038532','The happy hypocrite : a fairy tale for tired men ','Beerbohn Max','John Lane, the Bodley Head',1905,'Novel'),('9780191751035','The Oxford handbook of happiness','David, Susan','Oxford University Press',2013,'Self-Help');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrowed`
--

DROP TABLE IF EXISTS `borrowed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrowed` (
  `memberNo` int NOT NULL,
  `isbn` varchar(45) NOT NULL,
  `borroweddate` date NOT NULL,
  `duedate` date NOT NULL,
  PRIMARY KEY (`memberNo`,`isbn`,`borroweddate`,`duedate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrowed`
--

LOCK TABLES `borrowed` WRITE;
/*!40000 ALTER TABLE `borrowed` DISABLE KEYS */;
INSERT INTO `borrowed` VALUES (1,'03004056','2002-03-20','2005-03-20'),(1,'0415226643','2011-05-05','2011-05-15'),(1,'9780191751035','2000-01-10','2000-01-20'),(1,'9780191751035','2019-01-12','2019-01-22'),(2,'03004056','2001-09-09','2001-09-19'),(2,'0415226643','2004-04-10','2004-04-20'),(2,'0500232121','2020-09-09','2020-09-19'),(2,'0953886670','2020-02-02','2020-02-12'),(2,'9780191751035','2005-08-08','2005-08-18'),(3,'03004056','2012-12-12','2012-12-22'),(3,'0500232121','2003-05-05','2003-05-14'),(3,'1912038532','2016-10-20','2016-10-30'),(4,'03004056','2008-01-20','2008-01-30'),(4,'0500232121','2018-03-03','2018-03-13'),(4,'9780191751035','2015-03-03','2015-03-13'),(5,'03004056','2019-01-01','2019-01-11'),(5,'0500232121','2007-05-05','2007-05-05'),(6,'03004056','2007-05-05','2007-05-15'),(6,'0415226643','2005-03-18','2005-03-28'),(6,'0415226643','2019-05-05','2019-05-15'),(6,'0953886670','1995-09-09','1995-09-19'),(7,'0500232121','1998-08-08','1998-08-18'),(7,'0953886670','2019-08-08','2019-08-18'),(7,'9780191751035','2017-09-09','2017-09-19'),(8,'0953886670','2020-01-01','2020-01-11');
/*!40000 ALTER TABLE `borrowed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `memberNo` int unsigned NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`memberNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1,'David Copperfield','32'),(2,'Boris Johnson','55'),(3,'John McDonalds','24'),(4,'Jane Doe','83'),(5,'Peter Sands','41'),(6,'John Muir','92'),(7,'Sandra Williamson','34'),(8,'Sadiq Khan Jr','14');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-16 17:32:19
