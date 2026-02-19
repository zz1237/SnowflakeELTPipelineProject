## Overview
This project implements an ELT pipeline using Snowflake as the data warehouse, dbt for transformation and modeling, and Airflow for orchestration.
Data is sourced from Snowflake DWH, transformed through dbt models, and materialized into fact and dimension tables following a star schema design. Airflow manages scheduling, dependencies, and execution reliability.

## Tech Stack
- Warehous: Snowflake
- Transformation: dbt
- Orchestration: Airflow
- Language: SQL (Jinja)
- Configuration: Python (uv)
- Version Control: Git/Github

## Data Architechture
- Layered modeling: Raw → Staging → Mart
- Star schema with fact and dimension tables
- Reusable dbt macros for surrogate keys & transformations
- Data quality enforcement with generic and singular tests
- Airflow DAG orchestrating dbt runs and tests
