# Real-Time Patient Flow Analytics on Azure

![Azure](https://img.shields.io/badge/Azure-Cloud-blue?logo=microsoft-azure&style=flat-square)
![PySpark](https://img.shields.io/badge/PySpark-Big%20Data-orange?logo=apache-spark&style=flat-square)
![Azure Data Factory](https://img.shields.io/badge/Azure-Data%20Factory-blue?logo=microsoft-azure&style=flat-square)
![Azure Synapse](https://img.shields.io/badge/Azure-Synapse%20Analytics-blue?logo=microsoft-azure&style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python&style=flat-square)
![Databricks](https://img.shields.io/badge/Databricks-PySpark-red?logo=databricks&style=flat-square)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-orange?logo=power-bi&style=flat-square)
![Git](https://img.shields.io/badge/Git-CI%2FCD-green?logo=git&style=flat-square)

---

## 📑 Table of Contents
- [📌 Project Overview](#-project-overview)
- [🎯 Objectives](#-objectives)
- [📂 Project Structure](#-project-structure)
- [🛠️ Tools & Technologies](#️-tools--technologies)
- [📐 Data Architecture](#-data-architecture)
- [⭐ Star Schema Design](#-star-schema-design)
- [⚙️ Step-by-Step Implementation](#️-step-by-step-implementation)
  - [1. Event Hub Setup](#1-event-hub-setup)
  - [2. Data Simulation](#2-data-simulation)
  - [3. Storage Setup](#3-storage-setup)
  - [4. Databricks Processing](#4-databricks-processing)
  - [5. Synapse SQL Pool](#5-synapse-sql-pool)
  - [6. Version Control](#6-version-control)
- [📊 Data Analytics](#-data-analytics)
- [✅ Key Outcomes](#-key-outcomes)
- [📜 License](#-license)

---

## 📌 Project Overview
This project demonstrates a **real-time data engineering pipeline** for healthcare, designed to analyze **patient flow across hospital departments** using Azure cloud services.  
The pipeline ingests streaming data, processes it in **Databricks (PySpark)**, and stores it in **Azure Synapse SQL Pool** for analytics and visualization.


## Pipeline

<img width="4719" height="2432" alt="Architecture" src="https://github.com/user-attachments/assets/cb1a1775-ab64-45d7-b45b-50ba97660e1d" />


---

## 🎯 Objectives
- Collect real-time patient data via **Azure Event Hub**.
- Process and cleanse data using **Databricks** (Bronze → Silver → Gold layers).
- Implement a **star schema** in **Synapse SQL Pool** for efficient querying.
- Enable **Version Control** with Git.

---

## 📂 Project Structure
```plaintext
real-time-patient-flow-azure/
│
├── databricks-notebooks/  # Transformation notebooks
│   ├── 01_bronze_rawdata.py
│   ├── 02_silver_cleandata.py
│   └── 03_gold_transform.py
├── simulator/             # Data simulation scripts
│   └── patient_flow_generator.py
├── sqlpool-quries/        # SQL scripts for Synapse
│   └── SQL_pool_quries.sql
├── git_commands/                  # Git Commands
└── README.md              # Project documentation
```

---

## 🛠️ Tools & Technologies
- **Azure Event Hub** – Real-time data ingestion
- **Azure Databricks** – PySpark-based ETL processing
- **Azure Data Lake Storage** – Staging raw and curated data
- **Azure Synapse SQL Pool** – Data warehouse for analytics
- **Power BI** – Dashboarding (future step)
- **Python 3.9+** – Core programming
- **Git** – Version control

---

## 📐 Data Architecture
The pipeline follows a **multi-layered architecture**:
- **Bronze Layer**: Raw JSON data from Event Hub stored in ADLS.
- **Silver Layer**: Cleaned and structured data (validated types, null handling).
- **Gold Layer**: Aggregated and transformed data ready for BI consumption.

---

## ⭐ Star Schema Design
The **Gold layer** data in Synapse follows a **star schema** for optimized analytics:
- **Fact Table**: `FactPatientFlow` (patient visits, timestamps, wait times, discharge)
- **Dimension Tables**:
  - `DimDepartment` – Department details
  - `DimPatient` – Patient demographic info
  - `DimTime` – Date and time dimension

---

## ⚙️ Step-by-Step Implementation

### **1. Event Hub Setup**
- Created **Event Hub namespace** and **patient-flow hub**.
- Configured **consumer groups** for Databricks streaming.

---

### **2. Data Simulation**
- Developed **Python script** `patient_flow_generator.py` to stream fake patient data (departments, wait time, discharge status) to Event Hub.
- [Producer Code](data_generate/patient_flow_generator.py)

---

### **3. Storage Setup**
- Configured **Azure Data Lake Storage (ADLS Gen2)**.
- Created containers for **bronze**, **silver**, and **gold** layers.

---

### **4. Databricks Processing**
- [**Notebook 1**](spark-layers/1.0-bronze.ipynb): Reads Event Hub stream into Bronze.
- [**Notebook 2**](spark-layers/2.0-silver.ipynb): Cleans and validates schema.
- [**Notebook 3** ](spark-layers/3.0-gold.ipynb): Aggregates and prepares star schema tables.

---

### **5. Synapse SQL Pool**
- Created **dedicated SQL Pool**.
- Executed schema and fact/dimension creation queries from:
  - [sqlpoolscrept](datawarehouse/sqlpoolscrept.sql)   
  - [DDL_Qureis](datawarehouse/SQL_views_DDL.sql)
  - 

---

### **6. Version Control**
- Version control with **Git**:
  

---

## 📊 Data Analytics

Once the **data pipeline** was established and a **Star Schema** implemented in Synapse SQL Pool, the next step was to build an **interactive dashboard in Power BI**.  

### **🔗 Synapse → Power BI Connection**
- Connected **Azure Synapse SQL Pool** to Power BI using a direct SQL connection.  
- Imported **FactPatientFlow** and **Dimension tables**.  
- Established relationships for **Star Schema-based reporting**.  

### **📈 Dashboard Features**
The **Healthcare Patient Flow Dashboard** provides insights into:  
- **Bed Occupancy Rate** by department and gender.  
- **Patient Flow Trends** (admissions, wait times).  
- **Department-Level KPIs** (length of stay, Total Patients).  
- **Interactive Filters & Slicers** for gender.

<img width="1282" height="724" alt="[Screenshot 2025-08-30 155951" src="[https://github.com/user-attachments/assets/cf1f84dc-c1a5-4f07-84aa-1658abb4db16](https://github.com/shehab-hub8/spaken-el-pipelines/blob/main/Power-Bi/WhatsApp%20Image%202025-12-09%20at%2014.17.31_fe33e2fc.jpg)](https://drive.google.com/file/d/147NcoUrefVEdLw-HeiPxk30x0LnXXNyb/view?usp=sharing)" />

<img width="1282" height="724" alt="[Screenshot 2025-08-30 155951" src="[https://github.com/user-attachments/assets/cf1f84dc-c1a5-4f07-84aa-1658abb4db16](https://github.com/shehab-hub8/spaken-el-pipelines/blob/main/Power-Bi/WhatsApp%20Image%202025-12-09%20at%2014.17.16_f0ec42f5.jpg)](https://drive.google.com/file/d/1i7t-Koi5Y5oO_Fg16zdLXtR9kb7KDYoI/view?usp=sharing)" />

---

## ✅ Key Outcomes
- **End-to-End Pipeline:** From **real-time ingestion → transformation → warehouse → analytics**.  
- **Scalable Architecture:** Easily adaptable for different hospital datasets.  
- **Business Insights:** Hospital admins can monitor **bed usage, patient flow, and department efficiency** in real time.  
- **Portfolio Value:** Demonstrates both **Data Engineering** and **Analytics skills** in one project.  

---

## 📜 License
This project is licensed under the **MIT License**.  
Feel free to use and adapt for learning or production.






