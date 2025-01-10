-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 09 Jan 2025 pada 15.50
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_project_uas`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_barang`
--

CREATE TABLE `data_barang` (
  `id` int(11) NOT NULL,
  `kode` varchar(255) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `qty` int(11) NOT NULL,
  `harga` int(11) DEFAULT NULL,
  `total` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `data_barang`
--

INSERT INTO `data_barang` (`id`, `kode`, `nama`, `qty`, `harga`, `total`) VALUES
(1, 'LTP', 'ACER', 100, 9999999, '999999900'),
(2, 'LTP', 'Laptop Asus', 5, 7600000, '76000000'),
(5, 'MS', 'Mouse', 100, 255000, '25500000'),
(6, 'LTP', 'Laptop Hp', 12, 5400000, '64800000'),
(7, 'HVS', 'Kertas HVS', 100, 500, '50000'),
(10, 'LTP', 'Laptop Asus', 19, 5000000, '60000000'),
(11, 'LTP', 'Laptop Hp', 50, 10000000, '10000000'),
(12, 'HVS', 'Kertas HVS', 90, 100, '10000'),
(13, 'LTP', 'Laptop Lenovo Thinkpad', 100, 5999000, '599900000'),
(14, 'LTP ', 'Laptop Hp', 90, 8999999, '809999910'),
(16, 'PL', 'Pulpen Gel', 19, 2000, '200000'),
(19, 'KTS', 'Kertas A4', 10, 100, '10000');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `pass` text NOT NULL,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `username`, `pass`, `role`) VALUES
('ADM1', 'admin', 'radar', 'Admin'),
('ADM2', 'arka', 'arka*123nuri', 'Admin'),
('US2', 'rani', 'rani*90', 'User');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `data_barang`
--
ALTER TABLE `data_barang`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `data_barang`
--
ALTER TABLE `data_barang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
