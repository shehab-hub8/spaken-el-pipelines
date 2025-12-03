
حازم السعدى
11:37 م
-- 1) (Optional) Create DB master key if not exists
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Alsaady@#01141208078';
GO

-- 2) Create database scoped credential (managed identity example)
-- For managed identity: use IDENTITY = 'Managed Identity' and DO NOT supply SECRET.
CREATE DATABASE SCOPED CREDENTIAL storage_credential
WITH IDENTITY = 'Managed Identity';
GO

-- If you prefer SAS or storage account key, use:
-- CREATE DATABASE SCOPED CREDENTIAL storage_credential
-- WITH IDENTITY = 'SHARED ACCESS SIGNATURE', SECRET = 'sv=...&sig=...';
-- GO

-- 3) Create external data source pointing to ADLS Gen2 (ABFSS) using the credential
CREATE EXTERNAL DATA SOURCE gold_data_source
WITH (
    TYPE = HADOOP,
    LOCATION = 'abfss://gold@hospitalstorge.dfs.core.windows.net/',
    CREDENTIAL = storage_credential
);
GO

-- 4) Define Parquet format
CREATE EXTERNAL FILE FORMAT ParquetFileFormat
WITH (
    FORMAT_TYPE = PARQUET
);
GO

-- 5) External tables (examples)
CREATE EXTERNAL TABLE dbo.hospital_performance_kpi (
    hospital_name VARCHAR(50),
    city VARCHAR(50),
    total_patients BIGINT,
    avg_stay_days FLOAT,         -- بدل double
    critical_cases BIGINT,
    icu_admissions BIGINT,
    last_updated DATETIME2,
    processing_date DATETIME2
)
WITH (
    LOCATION = 'hospital_performance_kpi/',
    DATA_SOURCE = gold_data_source,
    FILE_FORMAT = ParquetFileFormat
);
GO

SELECT * 
FROM dbo.hospital_performance_kpi;

DROP EXTERNAL TABLE dbo.hospital_performance_kpi;

CREATE EXTERNAL TABLE dbo.disease_geography_trends (
    governorate VARCHAR(50),
    diagnosis VARCHAR(200),
    gender VARCHAR(20),
    case_count BIGINT,
    avg_treatment_days FLOAT,   -- بدل double
    latest_case VARCHAR(200),
    last_updated TIME,          -- لو هو TIME فعلاً في الباركيت
    processing_date TIME        -- لو هو TIME فعلاً في الباركيت
)
WITH (
    LOCATION = 'disease_geography_trends/',
    DATA_SOURCE = gold_data_source,
    FILE_FORMAT = ParquetFileFormat
);
GO




SELECT * 
FROM dbo.disease_geography_trends;




CREATE EXTERNAL TABLE dbo.doctor_performance_kpi (
    doctor_full_name varchar(50),
    specialization varchar(50),
    hospital_name varchar(50),
    patients_treated BIGINT,
    critical_cases_handled BIGINT,
    avg_treatment_days FLOAT,
    last_updated DATETIME,
    processing_date DATETIME
)
WITH (
    LOCATION = 'doctor_performance_kpi/',
    DATA_SOURCE = gold_data_source,
    FILE_FORMAT = ParquetFileFormat
);
GO

-- 6) Quick test (serverless: you can also use OPENROWSET for ad hoc tests)
SELECT TOP 20 * FROM dbo.doctor_performance_kpi;
‪eqj-jfym-ybc‬‏
