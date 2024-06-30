-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-06-2024 a las 13:56:38
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hackad`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `campaigns`
--

CREATE TABLE `campaigns` (
  `id` smallint(6) NOT NULL,
  `customer_id` smallint(6) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `campaigns`
--

INSERT INTO `campaigns` (`id`, `customer_id`, `name`) VALUES
(1, 1, 'Upton Group'),
(2, 1, 'Roob, Hudson and Rippin'),
(3, 1, 'McCullough, Rempel and Larson'),
(4, 1, 'Lang and Sons'),
(5, 2, 'Ruecker, Hand and Haley');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers`
--

CREATE TABLE `customers` (
  `id` smallint(6) NOT NULL,
  `first_name` varchar(64) DEFAULT NULL,
  `last_name` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `customers`
--

INSERT INTO `customers` (`id`, `first_name`, `last_name`) VALUES
(1, 'Whitney', 'Ferrero'),
(2, 'Dickie', 'Romera');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `events`
--

CREATE TABLE `events` (
  `dt` varchar(19) DEFAULT NULL,
  `campaign_id` smallint(6) DEFAULT NULL,
  `status` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `events`
--

INSERT INTO `events` (`dt`, `campaign_id`, `status`) VALUES
('2021-12-02 13:52:00', 1, 'failure'),
('2021-12-02 08:17:48', 2, 'failure'),
('2021-12-02 08:18:17', 2, 'failure'),
('2021-12-01 11:55:32', 3, 'failure'),
('2021-12-01 06:53:16', 4, 'failure'),
('2021-12-02 04:51:09', 4, 'failure'),
('2021-12-01 06:34:04', 5, 'failure'),
('2021-12-02 03:21:18', 5, 'failure'),
('2021-12-01 03:18:24', 5, 'failure'),
('2021-12-02 15:32:37', 1, 'success'),
('2021-12-01 04:23:20', 1, 'success'),
('2021-12-02 06:53:24', 1, 'success'),
('2021-12-02 08:01:02', 2, 'success'),
('2021-12-01 15:57:19', 2, 'success'),
('2021-12-02 16:14:34', 3, 'success'),
('2021-12-02 21:56:38', 3, 'success'),
('2021-12-01 05:54:43', 4, 'success'),
('2021-12-02 17:56:45', 4, 'success'),
('2021-12-02 11:56:50', 4, 'success'),
('2021-12-02 06:08:20', 5, 'success');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `campaigns`
--
ALTER TABLE `campaigns`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indices de la tabla `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `events`
--
ALTER TABLE `events`
  ADD KEY `campaign_id` (`campaign_id`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `campaigns`
--
ALTER TABLE `campaigns`
  ADD CONSTRAINT `campaigns_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

--
-- Filtros para la tabla `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `events_ibfk_1` FOREIGN KEY (`campaign_id`) REFERENCES `campaigns` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
