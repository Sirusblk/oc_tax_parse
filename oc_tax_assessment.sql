DROP TABLE IF EXISTS [oc_tax_info];

CREATE TABLE [oc_tax_info]
(
	[District] VARCHAR(4) NOT NULL,
	[TaxRateArea] INT NOT NULL,
	[ParcelNumber] INT NOT NULL,
	[Zip] INT NOT NULL,
	[Zip4] INT,
	[Address01] VARCHAR(25) NOT NULL,
	[Address02] VARCHAR(25) NOT NULL,
	[Address03] VARCHAR(25) NOT NULL,
	[Address04] VARCHAR(25),
	[Address05] VARCHAR(25),
	[Address06] VARCHAR(25),
	[Num] INT NOT NULL
);
