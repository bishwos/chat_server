-- phpMyAdmin SQL Dump
-- version 5.2.0-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 25, 2022 at 06:31 PM
-- Server version: 10.9.4-MariaDB
-- PHP Version: 7.4.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `p2`
--

-- --------------------------------------------------------

--
-- Table structure for table `target`
--

CREATE TABLE `target` (
  `service` char(4) DEFAULT NULL,
  `device` char(40) NOT NULL,
  `channel` char(40) NOT NULL DEFAULT '',
  `domain` varchar(253) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `node` char(12) DEFAULT NULL,
  `secret` char(24) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `target`
--
ALTER TABLE `target`
  ADD PRIMARY KEY (`device`,`channel`),
  ADD KEY `nodeDomain` (`node`,`domain`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
