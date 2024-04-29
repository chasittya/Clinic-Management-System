
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `clinic_manage` DEFAULT CHARACTER SET utf8 ;
USE `clinic_manage` ;

-- Table `users` for authentication
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` VARCHAR(10) NOT NULL DEFAULT 'patient', 
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW()
) ENGINE = InnoDB;


-- Table `patients`
CREATE TABLE IF NOT EXISTS `patients` (
  `patientID` INT AUTO_INCREMENT PRIMARY KEY,
  `userID` INT,
  `FName` VARCHAR(255),
  `LName` VARCHAR(255),
  `role`  VARCHAR(50),
  `SSN` VARCHAR(255),
  `birthday` DATE,
  `gender` CHAR(1),
  `contactPhone` VARCHAR(255),
  `medicalHistory` TEXT,
  `notes` TEXT,
  FOREIGN KEY (`userID`) REFERENCES `users`(`id`)
) ENGINE=InnoDB;



-- Table `staff`
CREATE TABLE IF NOT EXISTS `staff` (
  `staffID` INT AUTO_INCREMENT PRIMARY KEY,
  `userID` INT,
  `FName` VARCHAR(255),
  `LName` VARCHAR(255),
  `scontact_info` VARCHAR(255),
  FOREIGN KEY (`userID`) REFERENCES `users`(`id`)
) ENGINE=InnoDB;

-- Table `admin`
CREATE TABLE IF NOT EXISTS `admin` (
  `adminID` INT AUTO_INCREMENT PRIMARY KEY,
  `userID` INT,
  `FName` VARCHAR(255),
  `LName` VARCHAR(255),
  `scontact_info` VARCHAR(255),
  FOREIGN KEY (`userID`) REFERENCES `users`(`id`)
) ENGINE=InnoDB;

-- Table `appointments`
CREATE TABLE IF NOT EXISTS `appointments` (
  `appointmentID` INT AUTO_INCREMENT PRIMARY KEY,
  `patientID` INT,
  `staffID` INT,
  `appointment_datetime` DATETIME,
  FOREIGN KEY (`staffID`) REFERENCES `staff` (`patientID`),
  FOREIGN KEY (`patientID`) REFERENCES `patients`(`patientID`)
) ENGINE=InnoDB;

-- Reset SQL mode and foreign key checks
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
