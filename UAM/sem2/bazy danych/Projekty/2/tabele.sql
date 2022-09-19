/* Baza Serwis Aukcyjny */

-----Komendy gdyby trzeba bylo tworzyc cala baze danych-----

--DROP DATABASE Serwis_Aukcyjny_Kacper_Kalinowski;
--GO

--CREATE DATABASE Serwis_Aukcyjny_Kacper_Kalinowski;
--GO

--USE Serwis_Aukcyjny_Kacper_Kalinowski;
--GO

--SET LANGUAGE polski;
--GO

-----Usuwanie Poprzednio stworzonych tabel i powiazan -----

DROP TABLE IF EXISTS Posiadanie;

DROP TABLE IF EXISTS Opcja_dostawy;
DROP TABLE IF EXISTS Oferta;

DROP TABLE IF EXISTS Licytacja;
DROP TABLE IF EXISTS Przedmiot;
DROP TABLE IF EXISTS Uzytkownik;


-----Tworzenie Tabel i powiązań-----

CREATE TABLE Uzytkownik(
	login				VARCHAR(20) CONSTRAINT pk_Uzytkownik_login PRIMARY KEY,
	imie				varchar(20) NOT NULL,
	nazwisko			varchar(20) NOT NULL,
	e_mail				varchar(50) NOT NULL,
	adres_zamieszkania	varchar(60) NOT NULL,
	nr_konta			varchar(26),
	telefon				varchar(9),
	adres_dostawy		varchar(30),
	--CONSTRAINT chck_Uzytkownik_nrkonta CHECK (LENGTH(nr_konta)=26 or LENGTH(nr_konta)=0),
	CONSTRAINT chck_Uzytkownik_nrkonta CHECK (LEN(nr_konta)=26 or LEN(nr_konta)=0),
	constraint chck_Uzytkownik_telefon check (LEN(telefon)=9 or LEN(telefon)=0)
	--constraint chck_Uzytkownik_telefon check (LENGTH(telefon)=9 or LENGTH(telefon)=0)
);

CREATE TABLE Przedmiot(
	nr_przedmiotu		int CONSTRAINT pk_Przedmiot_nr PRIMARY KEY,
	nazwa				varchar(30) NOT NULL,
	kategoria			varchar(30) NOT NULL,
	cena_wyjsciowa		money NOT NULL,
	opis				varchar(80),
	cena_zakupu			money,
	wystawiajacy		varchar(20) CONSTRAINT fk_Przedmiot_wystawiajacy references Uzytkownik(Login),
	CONSTRAINT chck_Przedmiot_cena CHECK (cena_zakupu>=cena_wyjsciowa)
);

CREATE TABLE Licytacja(
	id_licytacji		int CONSTRAINT pk_Licytacja_id PRIMARY KEY,
	data_rozpoczecia	datetime NOT NULL,
	data_zakonczenia	datetime NOT NULL,
	status				varchar(20) NOT NULL,
	wygrany				varchar(20) CONSTRAINT fk_Licytacja_wygrany references Uzytkownik(Login),
	obiekt_licytacji	int CONSTRAINT fk_Licytacja_obiekt references Przedmiot(nr_przedmiotu),
	CONSTRAINT chck_Licytacja_data CHECK (data_zakonczenia > data_rozpoczecia),
	--CONSTRAINT chck_Licytacja_status CHECK (status='w trakcie' or status='zakonczona bez kupna' or status='zakonczona kupnem'),
	--Constraint chck_Licytacja_wygrany CHECK (if(status='zakonczona kupnem', wygrany=NOT NULL, wygrany=NULL)),
	CONSTRAINT chck_Licytacja_status CHECK (status IN('w trakcie','zakonczona bez kupna','zakonczona kupnem'))
);

CREATE TABLE Opcja_dostawy(
	id_opcji_dostawy	int CONSTRAINT pk_Opcja_id PRIMARY KEY,
	nazwa				varchar(20) NOT NULL,
	firma				varchar(20) NOT NULL,
	cena				money NOT NULL
);

CREATE TABLE Oferta(
	id_oferta			int constraint pk_Oferta_id PRIMARY KEY,
	kwota				money NOT NULL,
	data_zlozenia		date NOT NULL,
	godzina_zlozenia	time NOT NULL,
	skladajacy			varchar(20) CONSTRAINT fk_Oferta_skladajacy references Uzytkownik(Login),
	nr_licytacji		int CONSTRAINT fk_Oferta_nr_licytacji references Licytacja(id_licytacji)
);

CREATE TABLE Posiadanie(
	id_posiadanie		int constraint pk_Posiadanie_id PRIMARY KEY,
	id_przedmiot		int CONSTRAINT fk_Posiadanie_id_przedmiot references Przedmiot(nr_przedmiotu),
	id_dostawy			int CONSTRAINT fk_Posiadanie_id_dostawy references Opcja_dostawy(id_opcji_dostawy)
);

-----INSERT---WSTAWIANIE DANYCH-----

INSERT INTO Uzytkownik VALUES
('Zbycholud123', 'Zbyszek', 'Kotarski', 'Zbykszek257@gmail.com', 'ul. Polna 27/5 Wroclaw', '55634432897654326328328798', NULL, 'ul. Polna 27/5 Wroclaw'),
('kakcper89', 'Kacper', 'Olech', 'kakcper89@gmail.com', 'ul. Zdroje 31 Szczecin', NULL, NULL, 'ul. Zdroje 31 Szczecin'),
('Eonzix', 'Marcel', 'Firelet', 'MacFire@o2.pl', 'os. Rusa 12/31 Poznan', '99872314647572398643521865', '786453742', NULL),
('gochazm', 'Malgorzata', 'Kirke', 'gosia57843@tlen.pl', 'al. powstancow 89 Gorzow', NULL, NULL, NULL);

INSERT INTO Przedmiot VALUES
(45, 'Rower Shiman', 'Transport', 500, 'Zadbany, piekny, prawie jak nowy', NULL, 'Eonzix'),
(23, 'Pralka Amica', 'RTV&AGD', 200, NULL, 500, 'kakcper89'),
(2, 'Lampka', 'Elektornika', 20, NULL, NULL, 'gochazm'),
(99, 'Karta radeon 1000', 'Komputery', 999, 'Prawie jak nowa, byla koparka', 1500, 'Zbycholud123');

INSERT INTO Licytacja VALUES
(5, '2021-05-31 20:21:31', '2021-06-07 20:21:31', 'w trakcie', NULL, 23),
(2, '2021-05-20 21:37:38', '2021-05-28 21:37:38', 'zakonczona bez kupna', NULL, 23),
(9, '2021-05-27 14:09:02', '2021-06-12 14:09:02', 'w trakcie', NULL, 2),
(4, '2021-05-12 17:29:57', '2021-05-20 17:29:57', 'zakonczona kupnem', 'Zbycholud123', 45);

INSERT INTO Opcja_dostawy VALUES
(1, 'Kurier szybki', 'DPD', 20),
(2, 'Paczkomat', 'Inpost', 9),
(3, 'Poczta polska', 'Poczta Polska', 10),
(4, 'Dron', 'Amazon', 25);

INSERT INTO Oferta VALUES
(1, 220, '2021-05-30', '12:43:05', 'Eonzix', 5),
(2, 240, '2021-05-30', '14:15:43', 'gochazm', 5),
(5, 600, '2021-05-19', '23:55:45', 'Zbycholud123', 4),
(8, 30, '2021-05-29', '17:31:18', 'kakcper89', 9);

INSERT INTO Posiadanie VALUES
(1, 45, 2),
(2, 45, 1),
(3, 99, 4),
(4, 23, 3);


-----SELECT-----
SELECT * FROM Uzytkownik;
SELECT * FROM Przedmiot;
SELECT * FROM Licytacja;
SELECT * FROM Opcja_dostawy;
SELECT * FROM Oferta;
SELECT * FROM Posiadanie;