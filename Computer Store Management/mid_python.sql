-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 16, 2021 lúc 02:24 PM
-- Phiên bản máy phục vụ: 10.4.18-MariaDB
-- Phiên bản PHP: 7.4.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `mid_python`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `name` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `bought` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `amount` int(11) NOT NULL,
  `date` date NOT NULL,
  `contact` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `customer`
--

INSERT INTO `customer` (`id`, `name`, `bought`, `amount`, `date`, `contact`) VALUES
(1, 'Kimberly C Wagner', 'Mainboard ASUS PRIME Z390-P', 4, '2021-01-02', 32975871),
(2, 'Joan G Smith', 'Mainboard MSI Z590-A PRO', 8, '2021-01-05', 16678098),
(3, 'John D McCann', 'Bàn phím cơ Logitech G613', 7, '2021-01-07', 82685619),
(4, 'Shirley J Clevenger', 'Bàn phím Logitech G512 GX RGB', 3, '2021-01-20', 53309176),
(5, 'Jessica W Hill', 'Gaming Laptop ASUS ROG Zephyrus G14 GA401IV-BR9N6', 1, '2021-01-23', 34306504),
(6, 'Kelli D Munoz', 'Ổ CỨNG SSD SAMSUNG 980 PRO 1TB', 5, '2021-01-25', 6390314),
(7, 'Jason A Blackmon', 'Nguồn CoolerMaster V750 SFX', 4, '2021-01-29', 74851886),
(8, 'Louise D Burns', 'Ổ cứng SSD Samsung 870 Evo ', 23, '2021-02-02', 15570488),
(9, 'Earline K Serrano', 'Card Màn Hình ASUS GeForce GTX 1050Ti 4GB', 1, '2021-02-03', 91432463),
(10, 'James E Amos', 'Mainboard MSI MAG B460 TOMAHAWK ', 9, '2021-02-08', 50063396),
(11, 'Raymond J Newton', 'Nguồn CoolerMaster V750 SFX', 6, '2021-02-09', 84230499),
(12, 'Christopher C Wise', 'Bàn phím cơ Logitech G813 LIGHTSYNC RGB', 5, '2021-02-17', 85085528),
(13, 'Richard L Nichols', 'Mainboard ASUS ROG STRIX B460', 6, '2021-02-21', 79121663),
(14, 'Kevin S Jackson', 'CPU Intel Core i7-10700F', 5, '2021-02-24', 76544182),
(15, 'Debbie A Wiseman', 'VGA-Card màn hình LEADTEK NVIDIA Quadro P1000', 3, '2021-03-10', 54352441),
(16, 'Larry M Blanton', 'Nguồn CORSAIR SF600', 11, '2021-03-14', 38015977),
(17, 'Bruce M Mizell', 'Màn hình LG 27MP59G ', 2, '2021-03-17', 10115337),
(18, 'Belinda P Gardner', 'CPU Intel Core i9-9900K', 6, '2021-03-20', 71071687),
(19, 'Edward G Machado', 'CPU Intel Core i3-10105', 3, '2021-03-27', 75320643),
(20, 'Patricia W Pagan', 'Nguồn GIGABYTE AORUS', 5, '2021-03-28', 57305410),
(21, 'Ralph H Hanes', 'Bàn phím Logitech G610 Orion', 5, '2021-04-07', 82722314),
(22, 'Elinor D Foster', 'Laptop Asus Vivobook X509JP-EJ013T', 4, '2021-04-08', 27112301),
(23, 'Evangeline J Moore', 'Ổ cứng SSD Samsung 860 EVO ', 22, '2021-04-11', 79234518),
(24, 'Maud T Caldwell', 'Nguồn Corsair RM750x White', 6, '2021-04-20', 10970867),
(25, 'Jimmy C Wheat', 'Màn hình máy tính LG 29WN600-W', 4, '2021-04-25', 86469859),
(26, 'Steven B Hardin', 'Laptop ASUS Vivobook X415JA-EK259T', 5, '2020-01-30', 8078888),
(27, 'Steven C Wagner', 'Card Đồ Họa VGA GIGABYTE GeForce RTX 3090 GAMING OC', 3, '2020-01-31', 17814444),
(28, 'Beatrice J Brown', 'CPU Intel Core i5-8600K', 4, '2020-02-10', 91766610),
(29, 'Jessica H Williams', 'Mainboard ASUS TUF GAMING B560M-PLUS ', 7, '2020-02-13', 80593003),
(30, 'Robert E Polito', 'Màn hình Dell P2719H', 2, '2020-02-28', 50542198),
(31, 'Jason E McGovern', 'Ổ cứng SSD Samsung 980 PRO 500GB', 11, '2020-03-24', 77492934),
(32, 'Javier J Haddad', 'Card Màn Hình Asus Dual Geforce RTX 3060 12G', 2, '2020-03-29', 22541356),
(33, 'Jackie R Dosch', 'Màn hình LCD Samsung LC27R500FHEXXV ', 3, '2020-04-01', 51454186),
(34, 'Cynthia K Spence', 'VGA-Card màn hình GIGABYTE GeForce RTX™ 2060 OC', 3, '2020-04-16', 52353647),
(35, 'Don M Beauregard', 'Laptop ASUS Expertbook (Laptop dành cho doanh nghiệp)', 3, '2020-06-29', 19808527),
(36, 'Warren L Hunsberger', 'Laptop Asus VivoBook TM420UA-EC022T', 1, '2020-07-09', 85208683),
(37, 'Kelly M Sanches', 'Ổ cứng SSD NVMe Gen4 Seagate Firecuda 520', 5, '2021-01-17', 15425028),
(38, 'Shannon S Hamilton', 'Bàn phím cơ Logitech G913 TKL', 4, '2021-02-05', 6160774),
(39, 'Victoria W Diaz', 'Màn hình LCD SAMSUNG LF24T350', 1, '2021-02-13', 98393752),
(40, 'Alyssa F Keck', 'CPU Intel Core i7-10700', 7, '2021-04-13', 81399264);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `amount` int(11) NOT NULL,
  `price` bigint(11) NOT NULL,
  `information` varchar(225) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `product`
--

INSERT INTO `product` (`id`, `name`, `amount`, `price`, `information`) VALUES
(1, 'CPU Intel Core i5-8600K', 34, 7300000, '3.6GHz Turbo Up To 4.3GHz, 6 nhân 6 luồng, 9MB Cache'),
(2, 'CPU Intel Core i9-9900K', 12, 9690000, '3.60GHz Turbo Up To 5.00GHz, 8 Nhân 16 Luồng, 16M Cache'),
(3, 'CPU Intel Core i3-10105', 78, 4290000, '3.7GHz turbo up to 4.4Ghz, 4 nhân 8 luồng, 6MB Cache'),
(4, 'CPU Intel Core i7-10700F', 10, 7490000, '3.8GHz turbo up to 5.1GHz, 8 nhân 16 luồng, 16MB Cache'),
(5, 'CPU Intel Core i7-10700', 40, 8390000, '2.90GHz Turbo Up To 4.80GHz, 8 Nhân 16 Luồng'),
(6, 'Card Đồ Họa VGA GIGABYTE GeForce RTX 3090 GAMING OC', 8, 72990000, '24GB GDDR6X, 384-bit, HDMI +DP, 2x8-pin'),
(7, 'Card Màn Hình ASUS GeForce GTX 1050Ti 4GB', 9, 3090000, 'NVIDIA Geforce/ 4Gb/ DDR5/ 128 Bits'),
(8, 'Card Màn Hình Asus Dual Geforce RTX 3060 12G', 11, 21990000, 'NVIDIA GeForce RTX 30 Series, 12GB GDDR6, GDDR6, 256-bit, GeForce RTX 3060'),
(9, 'VGA-Card màn hình GIGABYTE GeForce RTX™ 2060 OC', 9, 15390000, '6GB GDDR6, 192 bits, HDMI +DP'),
(10, 'VGA-Card màn hình LEADTEK NVIDIA Quadro P1000', 24, 8290000, ' 4GB GDDR5, 128-bits, PCI Express 3.0 x16'),
(11, 'Bàn phím Logitech G512 GX RGB', 12, 2190000, 'Switch: GX Brown (Tactile)/ GX Red (Linear), Non-Clicky, RGB Backlighting, Aluminum Backplate'),
(12, 'Bàn phím cơ Logitech G813 LIGHTSYNC RGB', 12, 3490000, 'Switch: CLICKY/TACTILE /LINEAR, LIGHTSYNC RGB, aluminium case'),
(13, 'Bàn phím cơ Logitech G913 TKL', 8, 3990000, 'Lightspeed Wireless, LED RGB '),
(14, 'Bàn phím cơ Logitech G613', 67, 1790000, 'Wireless, sử dụng công tắc cơ khí Romer-G '),
(15, 'Bàn phím Logitech G610 Orion', 52, 1740000, 'Switch:	Cherry MX Blue switch, Kích thước:153 x 443.5 x 34.3 mm'),
(16, 'Laptop Asus Vivobook X509JP-EJ013T', 10, 18790000, 'CPU: Intel Core i5, RAM: 4GB DDR4, Ổ đĩa cứng: 512GB, VGA: NVIDIA GEFORCE MX330 2GB GDDR5'),
(17, 'Gaming Laptop ASUS ROG Zephyrus G14 GA401IV-BR9N6', 19, 49876295, 'Processor 3.0 GHz, 6GB GDDR6, 8GB DDR4 SO-DIMM, 1TB M.2 NVMe™ PCIe® 3.0 SSD'),
(18, 'Laptop Asus VivoBook TM420UA-EC022T', 46, 20788986, 'R5 5500U/8GB RAM/512GB SSD/14 FHD Touch/Win10/Xoay/Đen'),
(19, 'Laptop ASUS Vivobook X415JA-EK259T', 14, 18000000, 'Intel Core i5-1035G1 (1.0 Ghz, 6 MB)/ RAM 4GB DDR4/ 512GB SSD/ Intel UHD Graphics/ WL+BT'),
(20, 'Laptop ASUS Expertbook (Laptop dành cho doanh nghiệp)', 10, 17864957, 'SSD 512GB, HDD 1TB, 14inch, 1.23kg, 18.5mm'),
(21, 'Mainboard ASUS ROG STRIX B460', 32, 3790000, 'Intel B460, Socket 1200, m-ATX, 4 khe Ram DDR4'),
(22, 'Mainboard ASUS PRIME Z390-P', 20, 5490000, 'Intel Z390, Socket 1151, ATX, 4 khe RAM DDR4'),
(23, 'Mainboard ASUS TUF GAMING B560M-PLUS ', 24, 3690000, 'Intel B560, Socket 1200, m-ATX, 4 khe Ram DDR4'),
(24, 'Mainboard MSI Z590-A PRO', 60, 4890000, 'Intel Z590, Socket 1200, ATX, 4 khe Ram DDR4'),
(25, 'Mainboard MSI MAG B460 TOMAHAWK ', 40, 3490000, 'Intel B460, Socket 1200, ATX, 4 khe RAM DDR4'),
(26, 'Màn hình LG 27MP59G ', 38, 4250000, '27 inch/FHD/LED/IPS/250cd/m²/DP+HDMI+VGA/75Hz/1ms'),
(27, 'Màn hình LCD SAMSUNG LF24T350', 8, 3768000, '1920 x 1080/IPS/75Hz/5 ms/FreeSync'),
(28, 'Màn hình máy tính LG 29WN600-W', 67, 5990000, '29inch IPS 75Hz AMD FreeSync™ HDR 29WN600-W'),
(29, 'Màn hình LCD Samsung LC27R500FHEXXV ', 50, 5749000, '26.9 inch/FHD/3000:1/1800R/hỗ trợ AMD FreeSync'),
(30, 'Màn hình Dell P2719H', 58, 5490000, '27 inch/FHD/LED/IPS/DP/HDMI+VGA/250cd/m²/60Hz/5ms'),
(31, 'Nguồn GIGABYTE AORUS', 63, 3650000, 'P850W - 850W - 80 Plus Gold - Full Modular'),
(32, 'Nguồn Cooler Master V1000 Platinum', 27, 6290000, '1000W – 80 Plus Platinum – Full Modular'),
(33, 'Nguồn CORSAIR SF600', 57, 3500000, '600W - 80 Plus Platinum - Full Modular'),
(34, 'Nguồn CoolerMaster V750 SFX', 87, 3790000, '750W - 80 Plus Gold - Full Modular'),
(35, 'Nguồn Corsair RM750x White', 76, 3550000, '750W - 80 Plus Gold - Full Modular'),
(36, 'Ổ cứng SSD Samsung 860 EVO ', 69, 4090000, '1TB, Sata III 6Gbit/s, 2.5\"'),
(37, 'Ổ cứng SSD Samsung 980 PRO 500GB', 67, 3990000, 'M.2 2280, PCIe Gen4.0 x4, NVMe1.3c, 500GB'),
(38, 'Ổ cứng SSD Samsung 870 Evo ', 42, 4290000, '1TB, 2.5-Inch, Sata III 6Gbit/s'),
(39, 'Ổ cứng SSD NVMe Gen4 Seagate Firecuda 520', 70, 4290000, '500GB, PCIe Gen 4.0x4, 3D TLC, M.2 2280-D'),
(40, 'Ổ CỨNG SSD SAMSUNG 980 PRO 1TB', 52, 3990000, '1TB, 1GB LPDDR4, PCIe Gen 4.0x4, NVMe 1.3c,  Samsung Elpis Controller, Samsung Magician Software');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `name` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `dob` date NOT NULL,
  `contact` bigint(11) NOT NULL,
  `job` varchar(225) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `staff`
--

INSERT INTO `staff` (`id`, `name`, `dob`, `contact`, `job`) VALUES
(1, 'Clyde R Poe', '1996-01-08', 5785130, 'Manager'),
(2, 'Hoàng Hữu Huy', '2001-10-01', 909112324, 'Computers Salesperson'),
(3, 'Marcel H Hardman', '1999-05-29', 656638973, 'Customer Service Advisor'),
(4, 'Thomas I Young', '1995-11-11', 438270178, 'Computer Technician'),
(5, 'Sondra M Doyle', '1997-12-09', 335882908, 'Computers Salesperson'),
(6, 'Andrew V Pendergrass', '2000-07-16', 311423163, 'Clerk'),
(7, 'Kevin P McDonald', '1994-01-15', 424292925, 'Computer Technician'),
(8, 'Suzanne B Spencer', '1998-02-15', 163791288, 'Computers Salesperson'),
(9, 'Josephine J Luna', '1999-03-18', 512318692, 'Customer Service Advisor'),
(10, 'Phạm Hoàng Việt', '2001-02-03', 9771223471, 'Computer Technician');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Chỉ mục cho bảng `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT cho bảng `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
