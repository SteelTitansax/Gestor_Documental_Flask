-- MySQL Script generated by MySQL Workbench
-- sáb 12 mar 2022 14:40:43
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Gestor_Documental
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Gestor_Documental
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Gestor_Documental` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `Gestor_Documental` ;

-- -----------------------------------------------------
-- Table `Gestor_Documental`.`contacts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`contacts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fullname` VARCHAR(255) NULL DEFAULT NULL,
  `phone` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `Gestor_Documental`.`Sala`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`Sala` (
  `idsala` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(255) NULL,
  `Tamaño` VARCHAR(255) NULL,
  `Fecha` VARCHAR(255) NULL,
  PRIMARY KEY (`idsala`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestor_Documental`.`Documentos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`Documentos` (
  `idDocumentos` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(255) NULL,
  `Tipo` VARCHAR(255) NULL,
  `Tag` VARCHAR(255) NULL,
  PRIMARY KEY (`idDocumentos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestor_Documental`.`Desarrollador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`Desarrollador` (
  `idDesarrollador` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(255) NULL,
  `Area` VARCHAR(255) NULL,
  `Rango` VARCHAR(255) NULL,
  `idDocumento` INT NULL,
  `idSala` INT NULL,
  PRIMARY KEY (`idDesarrollador`),
  INDEX `idDocumento_idx` (`idDocumento` ASC) VISIBLE,
  INDEX `idSala_idx` (`idSala` ASC) VISIBLE,
  CONSTRAINT `idDocumento`
    FOREIGN KEY (`idDocumento`)
    REFERENCES `Gestor_Documental`.`Documentos` (`idDocumentos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSala`
    FOREIGN KEY (`idSala`)
    REFERENCES `Gestor_Documental`.`Sala` (`idsala`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestor_Documental`.`Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`Material` (
  `idMaterial` INT NOT NULL AUTO_INCREMENT,
  `Tipo` VARCHAR(255) NULL,
  `Modelo` VARCHAR(255) NULL,
  `IdDesarrollador` INT NULL,
  PRIMARY KEY (`idMaterial`),
  INDEX `fk_Material_1_idx` (`IdDesarrollador` ASC) VISIBLE,
  CONSTRAINT `fk_Material_1`
    FOREIGN KEY (`IdDesarrollador`)
    REFERENCES `Gestor_Documental`.`Desarrollador` (`idDesarrollador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestor_Documental`.`ProjectManager`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`ProjectManager` (
  `idProjectManager` INT NOT NULL AUTO_INCREMENT,
  `Tipo` VARCHAR(255) NULL,
  `Area` VARCHAR(255) NULL,
  `Rango` VARCHAR(255) NULL,
  `idDesarrollador` INT NULL,
  PRIMARY KEY (`idProjectManager`),
  INDEX `idDesarrollador_idx` (`idDesarrollador` ASC) VISIBLE,
  CONSTRAINT `idDesarrollador`
    FOREIGN KEY (`idDesarrollador`)
    REFERENCES `Gestor_Documental`.`Desarrollador` (`idDesarrollador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestor_Documental`.`Repositorios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`Repositorios` (
  `idRepositorios` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(255) NULL,
  PRIMARY KEY (`idRepositorios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestor_Documental`.`Dev:Repo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestor_Documental`.`Dev:Repo` (
  `idRepositoriosDevRepo` INT NULL,
  `IdDesarrolladorDevRepo` INT NULL,
  INDEX `idRepositorio_idx` (`idRepositoriosDevRepo` ASC) VISIBLE,
  INDEX `idDesarrollador_idx` (`IdDesarrolladorDevRepo` ASC) VISIBLE,
  CONSTRAINT `idDesarrolladorDevRepo`
    FOREIGN KEY (`IdDesarrolladorDevRepo`)
    REFERENCES `Gestor_Documental`.`Desarrollador` (`idDesarrollador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idRepositorioDevRepo`
    FOREIGN KEY (`idRepositoriosDevRepo`)
    REFERENCES `Gestor_Documental`.`Repositorios` (`idRepositorios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
