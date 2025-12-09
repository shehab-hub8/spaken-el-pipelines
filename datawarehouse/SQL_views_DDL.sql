USE hospital;
GO

-- =============================================
-- KPIs VIEWS
-- =============================================

-- 1. Beds occupied total
CREATE OR ALTER VIEW dbo.vw_bed_occupancy AS
SELECT 
    p.gender,
    COUNT(CASE WHEN f.is_currently_admitted = 1 THEN f.bed_id END) * 1.0 / NULLIF(COUNT(f.bed_id), 0) * 100 AS bed_occupancy_percent
FROM dbo.fact_patient_flow_view f  -- تم التعديل
JOIN dbo.dim_patient_view p ON f.patient_sk = p.surrogate_key -- تم التعديل
GROUP BY p.gender;
GO

-- 2. Total bed turnover
CREATE OR ALTER VIEW dbo.vw_bed_turnover_rate AS
SELECT 
    p.gender,
    COUNT(DISTINCT f.fact_id) * 1.0 / NULLIF(COUNT(DISTINCT f.bed_id), 0) AS bed_turnover_rate
FROM dbo.fact_patient_flow_view f
JOIN dbo.dim_patient_view p ON f.patient_sk = p.surrogate_key
GROUP BY p.gender;
GO

-- 3. Total patients (Currently Admitted)
CREATE OR ALTER VIEW dbo.vw_patient_demographics AS
SELECT 
    p.gender,
    COUNT(CASE WHEN f.is_currently_admitted = 1 THEN f.fact_id END) AS total_patients
FROM dbo.fact_patient_flow_view f
JOIN dbo.dim_patient_view p ON f.patient_sk = p.surrogate_key
GROUP BY p.gender;
GO

-- 4. Avg treatment duration
CREATE OR ALTER VIEW dbo.vw_avg_treatment_duration AS
SELECT 
    d.department,
    p.gender,
    AVG(f.length_of_stay_hours) AS avg_treatment_duration
FROM dbo.fact_patient_flow_view f
JOIN dbo.dim_patient_view p ON f.patient_sk = p.surrogate_key
JOIN dbo.dim_department_view d ON f.department_sk = d.surrogate_key
GROUP BY d.department, p.gender;
GO

-- =============================================
-- CHARTS VIEWS
-- =============================================

-- 1. Total patients count over time
CREATE OR ALTER VIEW dbo.vw_patient_volume_trend AS
SELECT 
    f.admission_date,
    p.gender,
    COUNT(DISTINCT f.fact_id) AS patient_count
FROM dbo.fact_patient_flow_view f
JOIN dbo.dim_patient_view p ON f.patient_sk = p.surrogate_key
GROUP BY f.admission_date, p.gender;
GO

-- 2. Total patients over department
CREATE OR ALTER VIEW dbo.vw_department_inflow AS
SELECT 
    d.department,
    p.gender,
    COUNT(CASE WHEN f.is_currently_admitted = 1 THEN f.fact_id END) AS patient_count
FROM dbo.fact_patient_flow_view f
JOIN dbo.dim_patient_view p ON f.patient_sk = p.surrogate_key
JOIN dbo.dim_department_view d ON f.department_sk = d.surrogate_key
GROUP BY d.department, p.gender;
GO

-- 3. Total overstay patients count
CREATE OR ALTER VIEW dbo.vw_overstay_patients AS
SELECT 
    d.department,
    p.gender,
    COUNT(f.fact_id) AS overstay_count
FROM dbo.fact_patient_flow_view f
JOIN dbo.dim_patient_view p ON f.patient_sk = p.surrogate_key
JOIN dbo.dim_department_view d ON f.department_sk = d.surrogate_key
WHERE f.length_of_stay_hours > 50
GROUP BY d.department, p.gender;
GO


