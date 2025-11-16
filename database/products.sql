-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2025 at 06:50 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `local_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `description`, `image`, `category`) VALUES
(1, 'Shirt 1', '499.00', 'Cotton casual shirt', '/images/tshirt.jpg', 'Shirts'),
(2, 'Shirt 2', '599.00', 'Formal slim-fit shirt', '/images/shirt2.jpg', 'Shirts'),
(3, 'Shoe 1', '999.00', 'Running shoes with great comfort', '/images/shoes1.jpg', 'Shoes'),
(4, 'Shoe 2', '1299.00', 'Stylish leather shoes', '/images/shoes2.jpg', 'Shoes'),
(5, 'Watch 1', '799.00', 'Classic analog watch', '/images/watch1.jpg', 'Accessories'),
(6, 'Bag 1', '699.00', 'Stylish backpack for daily use', '/images/bag1.jpg', 'Bags'),
(7, 'Shirt 3', '699.00', 'Checked flannel shirt', '/images/shirt3.jpg', 'Shirts'),
(8, 'Shoe 3', '899.00', 'Canvas sneakers for men', '/images/shoes3.jpg', 'Shoes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
