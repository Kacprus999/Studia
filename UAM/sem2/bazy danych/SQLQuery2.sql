-- Kolokwium przyk³adowe 2

--USE master;
--DROP DATABASE Klinika;
--GO

--CREATE DATABASE Klinika;
--GO

--USE Klinika;
--GO

--------- USUÑ TABELE ---------

DROP TABLE IF EXISTS Wizyty;
DROP TABLE IF EXISTS Lekarze;
DROP TABLE IF EXISTS Pacjenci;

--------- CREATE - UTWÓRZ TABELE I POWI¥ZANIA ----------

CREATE TABLE Lekarze
(
    id_lekarza     INT PRIMARY KEY,
    nazwisko       VARCHAR(30),
    imie           VARCHAR(30),
    specjalnosc    VARCHAR(30),
    data_urodzenia DATETIME,
    nip            VARCHAR(13),
    pesel          VARCHAR(11)
);

CREATE TABLE Pacjenci
(
    id_pacjenta    INT PRIMARY KEY,
    nazwisko       VARCHAR(30),
    imie           VARCHAR(30),
    pesel          VARCHAR(11),
    data_urodzenia DATETIME
);

CREATE TABLE Wizyty
(
    lekarz      INT REFERENCES Lekarze(id_lekarza),
    pacjent     INT REFERENCES Pacjenci(id_pacjenta),
    koszt       MONEY,
    data_wizyty DATETIME
);

GO

---------- INSERT - WSTAW DANE ----------

INSERT INTO Lekarze VALUES
(23, 'Kadaj',       'Monika',     'laryngolog',   '1965-03-16', '879-122-69-94', '65031687654'),
(25, 'Kordylewski', 'Michal',     'nefrolog',     '1970-01-13', '567-098-55-66', '70011345567'),
(26, 'Lewandowska', 'Sylwia',     'urolog',       '1955-04-22', '444-567-87-65', '55042256786'),
(28, 'Maslowski',   'Michal',     'okulista',     '1956-10-19', '345-667-56-65', '56101988766'),
(29, 'Olejnik',     'Jacek',      'pediatra',     '1960-07-23', '887-667-56-66', '60072388766'),
(30, 'Silakowska',  'Magdalena',  'nefrolog',     '1959-11-25', '899-008-56-33', '59112599088'),
(31, 'Reks',        'Pawel',      'pediatra',     '1971-09-26', '776-562-09-05', '71092699876'),
(33, 'Tucholska',   'Katarzyna',  'laryngolog',   '1970-11-11', '876-555-09-33', '70111133456'),
(34, 'Nowak',       'Anna',       'nefrolog',     '1970-04-12', '877-222-34-56', '70041245678'),
(36, 'Dybowski',    'Daniel',     'ortopeda',     '1954-02-18', '556-877-90-67', '54021833455'),
(38, 'Boniecki',    'Pawel',      'alergolog',    '1950-05-09', '566-978-87-01', '50050956677'),
(39, 'Celmer',      'Rados³aw',   'dermatolog',   '1946-08-23', '657-879-65-88', '46082399875'),
(41, 'Czapiewski',  'Jakub',      'laryngolog',   '1967-08-09', '234-986-99-44', '67080997756'),
(42, 'Dybowski',    'Michal',     'nefrolog',     '1966-05-29', '456-787-56-91', '66052988755'),
(45, 'Jackowska',   'Agnieszka',  'chirurg',      '1970-11-05', '876-456-98-12', '70110565723'),
(49, 'Krajewska',   'Malgorzata', 'neurolog',     '1977-06-06', '456-987-75-33', '77060688543'),
(50, 'Poznanski',   'Maciej',     'kardiolog',    '1972-08-18', '546-978-34-98', '72081877653'),
(51, 'Kowalik',     'Szymon',     'ortopeda',     '1955-09-05', '546-787-76-44', '55090587622'),
(52, 'Marciniak',   'Krzysztof',  'reumatolog',   '1956-10-10', '876-089-34-76', '56101098724'),
(53, 'Zakowska',    'Grazyna',    'okulista',     '1967-09-06', '345-968-87-55', '67090656683'),
(55, 'Gawronski',   'Piotr',      'laryngolog',   '1969-10-27', '887-988-67-54', '69102777544'),
(60, 'Jaworska',    'Karolina',   'chirurg',      '1968-04-02', '456-997-87-23', '68040276503'),
(61, 'Olszewska',   'Anna',       'nefrolog',     '1954-07-03', '445-987-77-34', '54070376501'),
(64, 'Stefanowicz', 'Grzegorz',   'internista',   '1955-10-27', '657-098-67-55', '55102744582'),
(65, 'Witkowski',   'Karol',      'onkolog',      '1965-08-04', '567-987-88-66', '65080487296'),
(67, 'Belczynska',  'Marta',      'internista',   '1973-08-26', '345-878-87-34', '73082679300'),
(69, 'Mruk',        'Agata',      'endokrynolog', '1968-03-08', '867-456-34-55', '68030899823'),
(70, 'Gruszka',     'Marcin',     'internista',   '1971-02-02', '768-873-67-44', '71020265499'),
(71, 'Rydz',        'Adam',       'laryngolog',   '1972-07-26', '334-678-98-30', '72072674961'),
(72, 'Damian',      'Iwona',      'dermatolog',   '1954-09-23', '456-098-67-01', '54092365792');

INSERT INTO Pacjenci VALUES
(100, 'Kowal',         'Waldemar',   '01211309876', '2001-1-13'),
(110, 'Cyrankowska',   'Ilona',      '06281498876', '2006-8-14'),
(111, 'Imbierowicz',   'Hanna',      '64040456673', '1964-4-4'),
(121, 'Karlowski',     'Henryk',     '55090933455', '1955-9-9'),
(122, 'Nowakowska',    'Joanna',     '73050512356', '1973-5-5'),
(124, 'Witkowski',     'Hubert',     '88030422354', '1988-3-4'),
(135, 'Walentowicz',   'Kinga',      '02250987765', '2002-5-9'),
(147, 'Gumowska',      'Dorota',     '65092490065', '1965-9-24'),
(155, 'Duch',          'Alicja',     '06231299954', '2006-3-12'),
(160, 'Misz',          'Borys',      '77121098855', '1977-12-10'),
(161, 'Barski',        'Karol',      '99021766543', '1999-2-17'),
(163, 'Bartkowiak',    'Bartlomiej', '07210376599', '2007-1-3'),
(164, 'Benetkiewicz',  'Piotr',      '01260988555', '2001-6-9'),
(165, 'Ciborski',      'Maciej',     '57091566457', '1957-9-15'),
(166, 'Gesicki',       'Radoslaw',   '00222709836', '2000-2-27'),
(170, 'Grajkowska',    'Monika',     '06271109823', '2006-7-11'),
(172, 'Juszczyk',      'Adela',      '99100996548', '1999-10-9'),
(173, 'Kolasinski',    'Karol',      '98090433765', '1998-9-4'),
(180, 'Kosicka',       'Kamila',     '03212099545', '2003-1-20'),
(181, 'Kupinski',      'Jakub',      '78061600987', '1978-6-16'),
(184, 'Lajzer',        'Michal',     '77092566487', '1977-9-25'),
(189, 'Lipinski',      'Artur',      '02281902345', '2002-8-19'),
(191, 'Malkowski',     'Adam',       '75082822376', '1975-8-28'),
(192, 'Noch',          'Przemyslaw', '99111590976', '1999-11-15'),
(193, 'Nowicka',       'Karolina',   '06231744366', '2006-3-17'),
(197, 'Pawlak',        'Justyna',    '01250577856', '2001-5-5'),
(198, 'Pawlowski',     'Jaroslaw',   '80062465987', '1980-6-24'),
(200, 'Plaskowski',    'Jacek',      '56070476895', '1956-7-4'),
(204, 'Ruminski',      'Krzysztof',  '99101010987', '1999-10-10'),
(205, 'Szalewski',     'Wojciech',   '99111987656', '1999-11-19'),
(207, 'Szewczyk',      'Maciej',     '99092776545', '1999-9-27'),
(208, 'Wadowska',      'Agnieszka',  '04262908766', '2004-6-29'),
(209, 'Waga',          'Emilia',     '95052768598', '1995-5-27'),
(212, 'Wilkonska',     'Marta',      '83070576855', '1983-7-5'),
(213, 'Bojanowska',    'Magdalena',  '71022675598', '1971-2-26'),
(216, 'Czyza',         'Pawel',      '06281233456', '2006-8-12'),
(226, 'Grabania',      'Malgorzata', '99040554586', '1999-4-5'),
(227, 'Kadajska',      'Monika',     '05272799043', '2005-7-27'),
(231, 'Becmer',        'Wojciech',   '99032778655', '1999-3-27'),
(233, 'Biernacka',     'Izabela',    '58073022657', '1958-7-30'),
(235, 'Blaszkiewicz',  'Marcin',     '04280999856', '2004-8-9'),
(236, 'Boladz',        'Artur',      '73022098768', '1973-2-20'),
(238, 'Ciecharowska',  'Ilona',      '65082890067', '1965-8-28'),
(241, 'Cyrankowska',   'Monika',     '03272809866', '2003-7-28'),
(243, 'Dankowski',     'Daniel',     '06291477654', '2006-9-14'),
(244, 'Draszczyk',     'Alicja',     '99030778645', '1999-3-7'),
(245, 'Duszynska',     'Joanna',     '66032685097', '1966-3-26'),
(246, 'Gumowska',      'Anna',       '59092098756', '1959-9-20'),
(247, 'Imbierowicz',   'Joanna',     '05272555476', '2005-7-25'),
(248, 'Kaminska',      'Jolanta',    '04221987656', '2004-2-19'),
(249, 'Karlowski',     'Radoslaw',   '80070324576', '1980-7-3'),
(252, 'Koronska',      'Sylwia',     '99122889704', '1999-12-28'),
(253, 'lukaszewska',   'Katarzyna',  '03271788923', '2003-7-17'),
(255, 'Modlinska',     'Agnieszka',  '06260192845', '2006-6-1'),
(257, 'Polarek',       'Mariola',    '53070987966', '1953-7-9'),
(258, 'Ottka',         'Piotr',      '49072987556', '1949-7-29'),
(262, 'Pieczatowski',  'Witold',     '04282277655', '2004-8-22'),
(263, 'Trawinska',     'Monika',     '07220899876', '2007-2-8'),
(264, 'Smoczynska',    'Karolina',   '99040112365', '1999-4-1'),
(266, 'Walentowicz',   'Hanna',      '00290122345', '2000-9-1'),
(271, 'Winiarska',     'Kinga',      '83072768895', '1983-7-27'),
(272, 'Walasz',        'Mariusz',    '93032265788', '1993-3-22'),
(273, 'Wojciechowska', 'Katarzyna',  '01230688765', '2001-3-6'),
(274, 'Wolski',        'Marek',      '99022009768', '1999-2-20'),
(276, 'Zawadzka',      'Monika',     '97012657489', '1997-1-26'),
(283, 'Wronikowska',   'Magdalena',  '06240488976', '2006-4-4'),
(284, 'Andracki',      'Bartosz',    '95082336577', '1995-8-23'),
(285, 'Bednarczyk',    'Lukasz',     '05210786955', '2005-1-7'),
(286, 'Bogdan',        'Dawid',      '99101889765', '1999-10-18'),
(288, 'Janas',         'Marcin',     '99072987699', '1999-7-29'),
(290, 'Januszkiewicz', 'Szymon',     '04241477685', '2004-4-14'),
(291, 'Kaznowska',     'Agnieszka',  '47032598077', '1947-3-25'),
(292, 'Korda',         'Dawid',      '88122685903', '1988-12-26'),
(295, 'Kosicki',       'Pawel',      '06250799087', '2006-5-7'),
(296, 'Krankowska',    'Justyna',    '99052009768', '1999-5-20'),
(299, 'Kurasz',        'Malgorzata', '80072765543', '1980-7-27'),
(300, 'Miler',         'Beata',      '99012776588', '1999-1-27'),
(301, 'Nielepiec',     'Tomasz',     '02222678854', '2002-2-26'),
(303, 'Pietrzak',      'Iwona',      '76103098067', '1976-10-30'),
(306, 'Pirogowski',    'Piotr',      '06220488795', '2006-2-4'),
(307, 'Romanska',      'Monika',     '73082776855', '1973-8-27'),
(308, 'Sankiewicz',    'Przemyslaw', '99100445677', '1999-10-4'),
(309, 'Sibilak',       'Izabela',    '70120675809', '1970-12-6'),
(311, 'Siemiatkowska', 'Anna',       '00210188976', '2000-1-1'),
(313, 'Sowinska',      'Dorota',     '88012087966', '1988-1-20'),
(314, 'Srubka',        'Marta',      '03292376544', '2003-9-23'),
(316, 'Waruszewska',   'Agnieszka',  '81102454687', '1981-10-24'),
(317, 'Wichrowska',    'Malgorzata', '01212799822', '2001-1-27'),
(318, 'Wilczek',       'Agata',      '95082778956', '1995-8-27'),
(319, 'Wiorowska',     'Agnieszka',  '04292148765', '2004-9-21'),
(401, 'Wirowski',      'Marcin',     '90112238495', '1990-11-22'),
(403, 'Wozniak',       'Szymon',     '99123009458', '1999-12-30'),
(404, 'Zielinski',     'Tomasz',     '49060987956', '1949-6-9'),
(405, 'Zygarska',      'Joanna',     '07220799825', '2007-2-7'),
(408, 'Ostrowski',     'Grzegorz',   '01241990654', '2001-4-19'),
(409, 'Rutkowska',     'Karolina',   '96022675877', '1996-2-26'),
(411, 'Jeziorski',     'Adrian',     '99021774658', '1999-2-17'),
(412, 'Zabielska',     'Kamila',     '03260688934', '2003-6-6'),
(415, 'Borowiec',      'Dorota',     '07230899833', '2007-3-8'),
(416, 'Rawski',        'Mariusz',    '98062657877', '1998-6-26'),
(418, 'Borowski',      'Andrzej',    '92031487655', '1992-3-14'),
(420, 'Kandulska',     'Eugenia',    '91052687765', '1991-5-26');

INSERT INTO Wizyty VALUES
(23, 124,  58.20, '2006-12-13'),
(23, 172, 125.60, '2006-1-25'),
(23, 191,  21.60, '2006-2-1'),
(23, 191, 116.80, '2006-9-26'),
(23, 207, 131.10, '2006-9-25'),
(23, 252,  38.70, '2006-3-6'),
(23, 272, 137.00, '2006-10-26'),
(23, 272, 147.70, '2007-2-13'),
(23, 291,  62.80, '2006-1-9'),
(23, 291,  75.70, '2006-6-6'),
(23, 416, 154.10, '2006-1-7'),
(25, 100, 156.90, '2006-8-4'),
(25, 135, 111.50, '2006-9-24'),
(25, 135, 186.30, '2007-4-7'),
(25, 248,  24.90, '2006-5-26'),
(26, 238, 189.40, '2006-8-2'),
(26, 238, 151.90, '2007-3-12'),
(26, 249, 174.50, '2006-10-19'),
(26, 401, 140.80, '2006-4-9'),
(28, 111, 172.70, '2006-2-3'),
(28, 161, 161.10, '2006-10-15'),
(28, 209,  29.20, '2007-4-1'),
(28, 246,  23.20, '2006-7-17'),
(28, 246, 183.00, '2006-9-27'),
(28, 252,  50.80, '2007-2-10'),
(28, 313,  93.10, '2006-10-27'),
(29, 170, 100.30, '2007-2-15'),
(29, 241,  31.70, '2007-1-25'),
(29, 253, 119.60, '2006-8-28'),
(29, 283, 131.80, '2006-12-4'),
(29, 306,  90.90, '2007-2-14'),
(29, 311,  18.50, '2006-12-29'),
(29, 311, 177.20, '2007-2-4'),
(29, 317,  34.60, '2007-4-1'),
(29, 319, 132.00, '2006-1-28'),
(30, 164,  28.50, '2006-11-10'),
(30, 255, 109.10, '2007-2-3'),
(30, 273,  13.20, '2006-7-26'),
(31, 100,  98.40, '2006-3-26'),
(31, 100, 102.70, '2006-8-12'),
(31, 100, 172.90, '2007-4-29'),
(31, 110,  17.10, '2006-12-8'),
(31, 110,  51.00, '2007-3-29'),
(31, 216, 124.20, '2007-2-24'),
(31, 273,  40.10, '2006-1-27'),
(31, 301, 121.70, '2006-6-6'),
(31, 301,  53.90, '2006-12-6'),
(31, 415, 190.00, '2007-4-10'),
(33, 111,  61.40, '2006-1-23'),
(33, 155, 165.00, '2006-11-11'),
(33, 166, 185.90, '2006-9-13'),
(33, 180, 172.40, '2006-7-8'),
(33, 262, 125.20, '2006-9-3'),
(33, 314,  78.10, '2006-7-8'),
(33, 314, 176.60, '2007-1-20'),
(33, 405, 150.00, '2007-3-24'),
(34, 110, 159.00, '2007-2-20'),
(34, 170, 170.20, '2007-1-18'),
(34, 170, 179.60, '2007-3-4'),
(34, 197, 167.70, '2006-7-26'),
(34, 262, 170.80, '2006-1-24'),
(34, 262, 161.00, '2006-4-10'),
(34, 262, 169.30, '2006-10-20'),
(34, 415,  87.40, '2007-4-15'),
(36, 160,  95.00, '2006-12-29'),
(36, 172, 129.10, '2006-10-10'),
(36, 204,  71.30, '2006-7-7'),
(36, 213, 124.30, '2006-12-7'),
(36, 213, 100.10, '2007-3-26'),
(36, 257, 200.90, '2006-10-29'),
(36, 286,  36.70, '2006-9-7'),
(36, 286,  99.70, '2006-12-9'),
(36, 307,  86.80, '2006-12-5'),
(38, 122,  27.80, '2006-10-19'),
(38, 164, 152.90, '2006-10-26'),
(38, 241, 196.00, '2006-10-11'),
(38, 241, 119.30, '2006-12-1'),
(38, 247,  90.40, '2006-2-26'),
(38, 263,  23.90, '2007-4-20'),
(38, 303,  85.60, '2006-7-5'),
(38, 309, 146.20, '2006-4-26'),
(38, 314, 122.20, '2007-8-6'),
(39, 147,  85.00, '2007-1-29'),
(39, 205, 145.50, '2006-1-29'),
(39, 205, 142.50, '2006-3-13'),
(39, 205, 119.20, '2006-6-14'),
(39, 286,  76.10, '2007-3-3'),
(39, 299,  56.90, '2006-2-3'),
(39, 299, 114.90, '2006-4-5'),
(39, 420,  38.70, '2001-1-22'),
(41, 198,  25.40, '2006-9-5'),
(41, 200,  98.50, '2006-9-24'),
(41, 200,  62.80, '2007-1-20'),
(41, 212,  75.70, '2006-9-18'),
(41, 231,  21.00, '2006-3-12'),
(41, 231,  28.90, '2006-5-24'),
(41, 231,  49.10, '2007-1-25'),
(41, 284,  34.20, '2006-11-11'),
(41, 292, 180.70, '2006-10-24'),
(41, 296,  65.40, '2007-2-10'),
(42, 166,  42.60, '2007-3-27'),
(42, 193, 200.70, '2007-1-24'),
(42, 285, 142.20, '2006-9-11'),
(45, 121, 135.10, '2006-10-24'),
(45, 122, 135.30, '2006-11-20'),
(45, 165, 121.20, '2006-10-18'),
(45, 204,  16.70, '2006-9-26'),
(45, 207, 168.70, '2006-11-23'),
(45, 258, 165.90, '2006-11-3'),
(45, 271,  57.70, '2006-2-1'),
(45, 288,  74.70, '2006-4-9'),
(45, 409, 195.90, '2007-1-24'),
(49, 163,  79.70, '2007-3-12'),
(49, 193,  74.50, '2007-2-13'),
(49, 227,  19.40, '2006-10-20'),
(49, 408, 125.80, '2006-9-3'),
(50, 227,  40.70, '2006-2-3'),
(50, 227,  41.20, '2006-11-21'),
(50, 290,  97.50, '2006-11-12'),
(50, 405, 123.30, '2007-3-28'),
(50, 412, 185.50, '2006-7-7'),
(51, 135, 160.70, '2007-2-26'),
(51, 189, 111.80, '2007-1-3'),
(51, 295,  59.50, '2007-2-12'),
(52, 121,  29.00, '2006-9-14'),
(52, 121,  35.60, '2007-3-13'),
(52, 226,  21.60, '2006-10-10'),
(52, 245,  36.30, '2006-9-2'),
(52, 284, 142.50, '2007-2-12'),
(52, 411, 184.60, '2006-11-23'),
(53, 155,  81.20, '2007-2-19'),
(53, 208,  25.50, '2006-3-18'),
(53, 212,  10.20, '2007-2-11'),
(53, 235, 124.30, '2006-10-22'),
(53, 266, 121.20, '2006-12-25'),
(53, 301, 178.20, '2006-10-24'),
(55, 205, 116.20, '2007-3-8'),
(55, 213, 101.50, '2006-4-2'),
(55, 264, 141.20, '2006-3-4'),
(55, 271, 127.50, '2007-2-15'),
(55, 303, 123.70, '2006-9-7'),
(60, 173, 196.40, '2007-3-24'),
(60, 184, 145.30, '2007-9-12'),
(60, 200, 124.60, '2006-9-8'),
(60, 209,  71.70, '2006-9-25'),
(60, 209, 160.00, '2006-11-29'),
(60, 226,  74.50, '2006-4-20'),
(60, 226, 164.30, '2006-9-21'),
(60, 231,  74.50, '2007-2-3'),
(60, 286,  21.50, '2007-1-25'),
(60, 299,  52.20, '2006-5-13'),
(61, 180, 121.80, '2006-10-20'),
(61, 208, 138.40, '2006-7-8'),
(61, 208,  14.20, '2007-1-25'),
(61, 243, 165.70, '2006-12-28'),
(61, 266,  98.80, '2006-9-16'),
(61, 319,  79.50, '2006-9-3'),
(61, 319, 107.10, '2006-11-9'),
(64, 160,  88.90, '2007-2-3'),
(64, 181,  15.50, '2006-10-12'),
(64, 184,  18.00, '2006-3-8'),
(64, 401, 200.30, '2006-12-7'),
(64, 401, 135.30, '2007-3-12'),
(65, 181,  83.90, '2006-2-10'),
(65, 181,  20.10, '2006-9-24'),
(65, 181, 158.40, '2007-2-12'),
(65, 192, 187.10, '2007-2-9'),
(65, 244, 140.50, '2006-10-24'),
(65, 291,  32.40, '2006-10-18'),
(65, 300,  17.50, '2001-11-24'),
(65, 316,  89.40, '2006-10-11'),
(65, 403,  81.50, '2003-12-12'),
(65, 418,  74.50, '2000-6-23'),
(67, 147,  80.30, '2007-2-8'),
(67, 236, 182.50, '2007-3-16'),
(67, 257, 193.60, '2006-5-5'),
(67, 257, 132.00, '2006-12-22'),
(69, 165,  57.70, '2007-3-30'),
(69, 236, 157.80, '2006-9-26'),
(69, 292, 177.30, '2006-1-4'),
(69, 316, 179.20, '2006-10-27'),
(69, 316, 105.90, '2007-2-13'),
(70, 124, 172.30, '2006-1-25'),
(70, 124,  71.60, '2006-10-9'),
(70, 245,  57.40, '2006-11-4'),
(70, 272,  90.30, '2006-10-24'),
(70, 308, 102.40, '2007-1-7'),
(71, 161, 154.10, '2006-4-8'),
(71, 161,  39.10, '2006-8-15'),
(71, 233,  12.90, '2006-12-3'),
(71, 238,  62.40, '2006-9-4'),
(71, 258, 144.20, '2006-10-19'),
(71, 274,  72.70, '2006-1-23'),
(71, 313,  86.30, '2006-12-3'),
(71, 404,  55.20, '2007-3-12'),
(72, 173, 102.60, '2006-9-2'),
(72, 173,  71.80, '2006-10-28'),
(72, 191, 192.10, '2006-10-12'),
(72, 198, 193.30, '2006-10-19'),
(72, 233, 152.00, '2006-7-6'),
(72, 233, 150.80, '2006-10-2'),
(72, 246,  97.60, '2006-7-10'),
(72, 249,  39.60, '2006-7-6'),
(72, 249,  41.50, '2006-8-23'),
(72, 249,  87.10, '2006-9-28'),
(72, 276, 196.70, '2007-5-12'),
(72, 288,  93.90, '2006-10-30'),
(72, 309,  76.70, '2006-9-28'),
(72, 309,  25.60, '2007-2-16'),
(72, 404, 166.70, '2006-8-28'),
(72, 409,  15.10, '2006-8-3'),
(72, 416, 188.50, '2007-1-25');

------------ SELECT ------------

SELECT * FROM Lekarze;
SELECT * FROM Pacjenci;
SELECT * FROM Wizyty;

-- Pytanie 1
-- ZnajdŸ lekarzy (pediatrów lub internistów), którzy 22 marca 2020 r. mieli powy¿ej 50 lat. Wyniki posortuj po dacie urodzenia.

SELECT nazwisko, imie, specjalnosc, data_urodzenia
FROM Lekarze
WHERE DATEDIFF(year, data_urodzenia, '2020-03-22') > 50
	  AND (specjalnosc = 'internista' OR specjalnosc = 'pediatra')
ORDER BY data_urodzenia;

-- Pytanie 2
-- Podaj daty wszystkich wizyt z 2006 roku realizowanych u Maslowskiego. Wyniki posortuj po dacie wizyty.
-- U¿yj z³¹czenia tabel.

SELECT data_wizyty
FROM Wizyty W
	 JOIN Lekarze L
		  ON W.lekarz = L.id_lekarza
WHERE L.nazwisko = 'Maslowski'
	  AND W.data_wizyty LIKE '%2006%'
ORDER BY W.data_wizyty;

-- Pytanie 3
-- Podaj nazwiska i specjalnoœci wszystkich lekarzy, u których leczy³ siê Witkowski. Wyniki posortuj po nazwiskach.
-- U¿yj z³¹czenia tabel.

SELECT DISTINCT L.nazwisko, L.specjalnosc
FROM Lekarze L
	 JOIN Wizyty W
		  ON L.id_lekarza = W.lekarz
	 JOIN Pacjenci P
		  ON W.pacjent = P.id_pacjenta
WHERE P.nazwisko = 'Witkowski'
ORDER BY L.nazwisko;

-- Pytanie 4
-- Podaj nazwiska lekarzy tej samej specjalnoœci co Stefanowicz. Wyniki posortuj po nazwiskach.
-- U¿yj podzapytania.

SELECT L.nazwisko, L.specjalnosc
FROM Lekarze L
WHERE L.specjalnosc IN (SELECT L1.specjalnosc
						FROM Lekarze L1
						WHERE L1.nazwisko = 'Stefanowicz'
							  AND L1.id_lekarza != L.id_lekarza)
ORDER BY L.nazwisko;

-- Pytanie 5
-- Podaj nazwiska pacjentów bez umówionych wizyt. Wyniki posortuj po nazwiskach.
-- U¿yj z³¹czenia tabel oraz IS NULL.
-- Nie u¿ywaj podzapytania oraz EXISTS.

SELECT P.nazwisko
FROM Pacjenci P
	 LEFT JOIN Wizyty W
			  ON P.id_pacjenta = W.pacjent
WHERE W.pacjent IS NULL
ORDER BY P.nazwisko;

-- Pytanie 6
-- Podaj nazwiska pacjentów bez umówionych wizyt. Wyniki posortuj po nazwiskach.
-- U¿yj podzapytania.
-- Nie u¿ywaj z³¹czenia tabel z IS NULL oraz EXISTS.

SELECT P.nazwisko
FROM Pacjenci P
WHERE P.id_pacjenta NOT IN (SELECT W.pacjent
							FROM Wizyty W)
ORDER BY P.nazwisko;

-- Pytanie 7
-- Podaj nazwiska pacjentów bez umówionych wizyt. Wyniki posortuj po nazwiskach.
-- U¿yj EXISTS.
-- Nie u¿ywaj z³¹czenia tabel i IS NULL.

SELECT P.nazwisko
FROM Pacjenci P
WHERE NOT EXISTS (SELECT *
				  FROM Wizyty W
				  WHERE P.id_pacjenta = W.pacjent)
ORDER BY P.nazwisko;

-- Pytanie 8
-- Podaj liczbê lekarzy ka¿dej specjalnoœci. Wyniki posortuj po nazwie specjalnoœci.
-- U¿yj funkcji agreguj¹cej.

SELECT specjalnosc, COUNT(*) 'ilu lekarzy'
FROM Lekarze
GROUP BY specjalnosc
ORDER BY specjalnosc;

-- Pytanie 9
-- Podaj nazwisko najm³odszego lekarza.
-- U¿yj funkcji agreguj¹cej oraz podzapytania.

SELECT L.nazwisko, L.data_urodzenia
FROM Lekarze L
WHERE L.data_urodzenia = (SELECT MAX(data_urodzenia)
						  FROM Lekarze);

-- Pytanie 10
-- Dla ka¿dej specjalnoœci podaj nazwisko najm³odszego lekarza. Wyniki posortuj po dacie urodzenia i nazwisku.
-- U¿yj funkcji agreguj¹cej i podzapytania.

SELECT nazwisko, specjalnosc, data_urodzenia
FROM Lekarze L
WHERE L.data_urodzenia IN (SELECT MAX(L1.data_urodzenia)
						   FROM Lekarze L1
						   WHERE L.specjalnosc = L1.specjalnosc)
ORDER BY L.data_urodzenia, L.nazwisko;

-- Pytanie 11
-- Podaj nazwiska lekarzy, którzy zrealizowali wiêcej ni¿ 10 wizyt. Wyniki posortuj po nazwiskach.
-- U¿yj grupowania.

SELECT nazwisko, imie, COUNT(*) 'ile wizyt'
FROM Lekarze L
	 JOIN Wizyty W
		  ON L.id_lekarza = W.lekarz
GROUP BY L.nazwisko, L.imie
HAVING COUNT(*) > 10
ORDER BY L.nazwisko;

-- Pytanie 12
-- Podaj kwotê, jak¹ Anna Gumowska wyda³a na wszystkie swoje wizyty.
-- U¿yj funkcji agreguj¹cej.

SELECT SUM(koszt) 'suma wydatków'
FROM Pacjenci P
	 JOIN Wizyty W
		  ON P.id_pacjenta = W.pacjent
			 AND P.imie = 'Anna'
			 AND P.nazwisko = 'Gumowska';

SELECT SUM(koszt) 'suma wydatków'
FROM Pacjenci P
	 JOIN Wizyty W
		  ON P.id_pacjenta = W.pacjent
WHERE P.imie = 'Anna'
	  AND P.nazwisko = 'Gumowska';

-- Pytanie 13
-- ZnajdŸ lekarza, który zrealizowa³ najwiêcej wizyt.
-- U¿yj funkcji agreguj¹cej.

SELECT L.nazwisko, L.imie, COUNT(*) 'ile wizyt'
FROM Lekarze L
	 JOIN Wizyty W
		  ON L.id_lekarza = W.lekarz
GROUP BY L.nazwisko, L.imie
HAVING COUNT(*) >= ALL (SELECT COUNT(*)
						FROM Lekarze L
							 JOIN Wizyty W
								  ON L.id_lekarza = W.lekarz
						GROUP BY L.nazwisko);

-- ZADANIA DODATKOWE
-- Pytanie 1
-- Podaj nazwiska lekarzy, dla których œrednia wieku ich pacjentów przekracza 40 lat; posortuj po œrednim wieku
-- U¿yj grupowania oraz HAVING.

SELECT L.nazwisko, AVG(DATEDIFF(year, P.data_urodzenia,GETDATE())) 'œredni wiek'
FROM Lekarze L
	 JOIN Wizyty W
		  ON L.id_lekarza = W.lekarz
	 JOIN Pacjenci P
		  ON W.pacjent = P.id_pacjenta
GROUP BY L.nazwisko
HAVING AVG(DATEDIFF(year, P.data_urodzenia,GETDATE())) > 40
ORDER BY AVG(DATEDIFF(year, P.data_urodzenia,GETDATE()));

-- Pytanie 2
-- Podaj nazwiska lekarzy, do których nigdy nie przyszed³ pacjent urodzony przed 2000 rokiem. Wyniki posortuj po nazwisku.
-- U¿yj z³¹czenia zewnêtrznego lewostronnego oraz IS NULL.
-- Nie u¿ywaj EXISTS.

SELECT L1.nazwisko
FROM Lekarze L1
WHERE L1.nazwisko NOT IN (SELECT L.nazwisko
						  FROM Lekarze L
						  JOIN Wizyty W
					    	  ON L.id_lekarza = W.lekarz
					   	  LEFT JOIN Pacjenci P
							  ON W.pacjent = P.id_pacjenta
								 AND P.pesel LIKE '0%'
						  WHERE P.id_pacjenta IS NULL)
ORDER BY L1.nazwisko

-- Pytanie 3
-- Podaj nazwiska lekarzy, do których nigdy nie przyszed³ pacjent urodzony przed 2000 rokiem. Wyniki posortuj po nazwisku.
-- U¿yj podzapytania.
-- Nie u¿ywaj IS NULL oraz EXISTS.

SELECT DISTINCT L.nazwisko
FROM Lekarze L
WHERE L.nazwisko NOT IN (SELECT L1.nazwisko
					     FROM Lekarze L1
						 JOIN Wizyty W1
							  ON W1.lekarz = L1.id_lekarza
						 JOIN Pacjenci P1
							  ON P1.id_pacjenta = W1.pacjent
						 WHERE P1.pesel NOT LIKE '0%')
ORDER BY L.nazwisko;

-- Pytanie 4

-- Pytanie 5
-- Podaj nazwisko pacjenta, który zap³aci³ najwiêcej za wizytê u Jacka Olejnika.
-- U¿yj funkcji agreguj¹cej oraz podzapytania.

SELECT P.nazwisko, W.koszt
FROM Pacjenci P
	 JOIN Wizyty W
		  ON P.id_pacjenta = W.pacjent
WHERE W.koszt = (SELECT MAX(koszt)
				 FROM Wizyty W1
					  JOIN Lekarze L
						   ON W1.lekarz = L.id_lekarza
				 WHERE L.imie = 'Jacek'
					   AND L.nazwisko = 'Olejnik');
