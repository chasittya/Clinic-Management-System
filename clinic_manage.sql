-- Table `users` for authentication
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `FName` VARCHAR(255),
  `LName` VARCHAR(255),
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` ENUM('patient', 'staff', 'admin') NOT NULL DEFAULT 'patient', 
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW()
) ENGINE = InnoDB;

-- Table `patients`
CREATE TABLE IF NOT EXISTS `patients` (
  `patientID` INT AUTO_INCREMENT PRIMARY KEY,
  `userID` INT,
  `FName` VARCHAR(255),
  `LName` VARCHAR(255),
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
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `userID` INT,
  `FName` VARCHAR(255),
  `LName` VARCHAR(255),
  `scontact_info` VARCHAR(255),
  FOREIGN KEY (`userID`) REFERENCES `users`(`id`)
) ENGINE=InnoDB;

-- Table `admin`
CREATE TABLE IF NOT EXISTS `admin` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
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
  FOREIGN KEY (`staffID`) REFERENCES `staff` (`id`),
  FOREIGN KEY (`patientID`) REFERENCES `patients`(`patientID`)
) ENGINE=InnoDB;


