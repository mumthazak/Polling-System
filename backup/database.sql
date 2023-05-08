/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - polling_system
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`polling_system` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `polling_system`;

/*Table structure for table `booths` */

DROP TABLE IF EXISTS `booths`;

CREATE TABLE `booths` (
  `booth_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `district_id` int(11) DEFAULT NULL,
  `booth` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booth_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `booths` */

insert  into `booths`(`booth_id`,`login_id`,`district_id`,`booth`) values (1,4,1,'kumbalam'),(3,6,1,'fortkochi');

/*Table structure for table `candidates` */

DROP TABLE IF EXISTS `candidates`;

CREATE TABLE `candidates` (
  `candidate_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `election_id` int(11) DEFAULT NULL,
  `district_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `candidate_status` varchar(100) DEFAULT NULL,
  `aadhar` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`candidate_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `candidates` */

insert  into `candidates`(`candidate_id`,`login_id`,`election_id`,`district_id`,`first_name`,`last_name`,`age`,`dob`,`place`,`city`,`state`,`phone`,`email`,`candidate_status`,`aadhar`) values (1,14,1,1,'Rithik','Sunil','20','2000-05-02','edakochi','ernakulam','kerala','9876543210','rithik@gmail.com','accepted',NULL),(2,15,1,1,'Ayisha','Nezrin','20','2000-04-25','kakkanad','ernakulam','kerala','7865432109','ayish@gmail.com','accepted',NULL),(3,16,1,1,'Arya','Chandran','20','2000-02-28','vytilla','ernakulam','kerala','7865322190','arya@gmail.com','accepted',NULL),(4,20,1,1,'sai','ak','25','1995-03-12','palakkad','KOCHI','ammancovil','09539369854','jinugiridharan99@gmail.com','pending',NULL);

/*Table structure for table `districts` */

DROP TABLE IF EXISTS `districts`;

CREATE TABLE `districts` (
  `district_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`district_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `districts` */

insert  into `districts`(`district_id`,`login_id`,`district`) values (1,2,'Ernakulam'),(2,3,'Alappuzha');

/*Table structure for table `elections` */

DROP TABLE IF EXISTS `elections`;

CREATE TABLE `elections` (
  `election_id` int(11) NOT NULL AUTO_INCREMENT,
  `body` varchar(100) DEFAULT NULL,
  `election_date` varchar(100) DEFAULT NULL,
  `declared_on` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`election_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `elections` */

insert  into `elections`(`election_id`,`body`,`election_date`,`declared_on`,`status`) values (1,'legislative assembly','2021-04-23','2021-03-23','completed');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `login_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`login_type`) values (1,'admin','admin','admin'),(2,'ernakulam','ekm','district'),(3,'alapuzha','alapuzha','district'),(4,'kumbalam','kumbalam','booth'),(6,'fortkochi','fortkochi','booth'),(7,'18UCAP6914','michu','voter'),(8,'18UCAP6936','sanjana','voter'),(9,'18UCAP6941','aleena','voter'),(10,'18UCAP6943','gopika','voter'),(11,'18UCAP6929','jisma','voter'),(13,'18UCAP6934','nimra','voter'),(14,'18UCAP6942','rithik','candidate'),(15,'18UCAP6932','ayisha','candidate'),(16,'18UCAP6907','arya','candidate'),(19,'voter5','voter5','voter'),(20,'candii','candii','pending'),(21,'aaa','aaa','voter_pending'),(22,'dsfh','sdf','voter_pending'),(23,'anfhn','asgjhf','voter_pending');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) DEFAULT NULL,
  `total_vote` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`result_id`,`candidate_id`,`total_vote`) values (1,1,3),(2,2,2),(3,3,1);

/*Table structure for table `vote` */

DROP TABLE IF EXISTS `vote`;

CREATE TABLE `vote` (
  `vote_id` int(11) NOT NULL AUTO_INCREMENT,
  `vote_time` varchar(100) DEFAULT NULL,
  `voter_id` int(11) DEFAULT NULL,
  `candidate_id` int(11) DEFAULT NULL,
  `hash_value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vote_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `vote` */

insert  into `vote`(`vote_id`,`vote_time`,`voter_id`,`candidate_id`,`hash_value`) values (1,'2021-04-17 22:24:28',1,1,'99d068d846a04c8a18b57e60f88e62e1b9796389607593ea5086b4a3'),(2,'2021-04-17 22:26:35',2,2,'34413fcaf5aaabea36f7f08219e0d209672cd2166851afb7b1dd2871'),(3,'2021-04-17 22:27:06',3,3,'184cff583b89ec94f8ba9c1a4c076ef32f83076723124f39c659dcb0'),(4,'2021-04-17 22:27:27',4,1,'6b3d1a3c9de3fdfa7592a7bbd6facf1b8abd683914775c230b7cd47d'),(5,'2021-04-17 22:27:49',7,1,'542355ca8627b0273c96404268964936ac30d3646c6d2ee942611c6f'),(6,'2021-04-17 22:28:16',5,2,'647200a65c1cc448ef706c7a23c3d764f10bcd1ccd389b00ab267020');

/*Table structure for table `voters` */

DROP TABLE IF EXISTS `voters`;

CREATE TABLE `voters` (
  `voter_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `booth_id` int(11) DEFAULT NULL,
  `election_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `aadhar` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`voter_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `voters` */

insert  into `voters`(`voter_id`,`login_id`,`booth_id`,`election_id`,`first_name`,`last_name`,`age`,`dob`,`place`,`city`,`state`,`phone`,`email`,`aadhar`) values (1,7,1,1,'Nafeesath','Missriyya','21','2000-02-08','Kumbalam','ernakulam','kerala','9633987654','michushihab@gmail.com',NULL),(2,8,1,1,'sanjana','Jose','20','2000-11-11','cherthala','ernakulam','kerala','9876234561','sanjanajose@gmail.com',NULL),(3,9,3,1,'Aleena','Antony','20','2000-11-28','fort kochi','ernakulam','kerala','9876765434','aleena@gmail.com',NULL),(4,10,3,1,'Gopika','Anil','20','2000-10-27','fort kochi','ernakulam','kerala','7896054321','gopika@gmail.com',NULL),(5,11,1,1,'Jisma','Wilson','20','2000-10-04','Thevara','ernakulam','kerala','9876123450','jisma@gmail.com',NULL),(7,13,3,1,'Nimra','Azeez','20','2000-05-17','fort kochi','ernakulam','kerala','9876231450','nimra@gmail.com',NULL),(10,19,1,1,'JINU','G','22','1997-02-07','ekm','Pattambi','Kerala','09539367332','jinugiridharan29@gmail.com',NULL),(11,21,1,1,'JINU','G','25','1994-10-12','pkd','Pattambi','Kerala','09539367332','jinugiridharan29@gmail.com',NULL),(12,22,1,1,'JINU','G','25','1993-12-10','ekm','Pattambi','Kerala','09539367332','jinugiridharan29@gmail.com','123456789122'),(13,23,1,1,'JINU','G','25','1996-10-12','thrissur','Pattambi','Kerala','09539367332','jinugiridharan29@gmail.com','123654754123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
