-- 1. إنشاء قاعدة البيانات (لأنها غير موجودة)
CREATE DATABASE hospital;
GO

-- 2. الدخول داخل قاعدة البيانات الجديدة
USE hospital;
GO

-- 3. إنشاء مفتاح التشفير (مهم للأمان)
-- (إذا أعطى خطأ أنه موجود مسبقاً، تجاهله)
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Str0ngP@ssw0rd!';
GO

-- 4. إنشاء الاعتماد (Credential) للوصول للستوريدج
-- نستخدم Managed Identity الخاصة بالسينابس
CREATE DATABASE SCOPED CREDENTIAL storage_credential
WITH IDENTITY = 'Managed Identity';
GO

-- 5. تعريف مصدر البيانات (Data Source)
-- يشير إلى حاوية Gold
CREATE EXTERNAL DATA SOURCE gold_data_source
WITH (
    LOCATION = 'abfss://gold@hospitalstorge17.dfs.core.windows.net/',
    CREDENTIAL = storage_credential
);
GO

-- 6. إنشاء View جدول المرضى (Patient)
CREATE OR ALTER VIEW dbo.dim_patient_view
AS
SELECT *
FROM OPENROWSET(
    BULK 'gold_dim_patient/',
    DATA_SOURCE = 'gold_data_source',
    FORMAT = 'DELTA'
) 
WITH (
    patient_id VARCHAR(50),
    gender VARCHAR(10),
    age INT,
    effective_from DATETIME2,
    surrogate_key BIGINT,
    effective_to DATETIME2,
    is_current BIT
) AS [r];
GO

-- 7. إنشاء View جدول الأقسام (Department)
CREATE OR ALTER VIEW dbo.dim_department_view
AS
SELECT *
FROM OPENROWSET(
    BULK 'gold_dim_department/',
    DATA_SOURCE = 'gold_data_source',
    FORMAT = 'DELTA'
)
WITH (
    surrogate_key BIGINT,
    department NVARCHAR(200),
    hospital_id INT
) AS [r];
GO

-- 8. إنشاء View جدول الحقائق (Fact)
CREATE OR ALTER VIEW dbo.fact_patient_flow_view
AS
SELECT *
FROM OPENROWSET(
    BULK 'gold_fact/',
    DATA_SOURCE = 'gold_data_source',
    FORMAT = 'DELTA'
)
WITH (
    fact_id BIGINT,
    patient_sk BIGINT,
    department_sk BIGINT,
    admission_time DATETIME2,
    discharge_time DATETIME2,
    admission_date DATE,
    length_of_stay_hours FLOAT,
    is_currently_admitted BIT,
    bed_id INT,
    event_ingestion_time DATETIME2
) AS [r];
GO

-- 9. اختبار نهائي
SELECT TOP 10 * FROM dbo.fact_patient_flow_view;
SELECT TOP 10 * FROM dbo.dim_patient_view;
SELECT TOP 10 * FROM dbo.dim_department_view;
