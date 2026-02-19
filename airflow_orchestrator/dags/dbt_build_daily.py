from airflow.sdk import dag, task
from pendulum import datetime

DBT_PROJECT_DIR = "/opt/airflow/dbt/snowflake_pipeline"
DBT_PROFILES_DIR = "/opt/airflow/.dbt"
DBT_PROFILE = "snowflake_pipeline"
DBT_TARGET = "dev"

@dag(
    schedule="@daily",
    start_date=datetime(2026, 2, 1, tz="America/New_York"),
    catchup=False,
    tags=["dbt", "snowflake"],
)
def dbt_build_daily():

    @task.bash
    def dbt_deps():
        return f"""
        set -euo pipefail
        cd {DBT_PROJECT_DIR}
        export DBT_PROFILES_DIR={DBT_PROFILES_DIR}
        dbt deps --profiles-dir {DBT_PROFILES_DIR} --profile {DBT_PROFILE}
        """

    @task.bash
    def dbt_build():
        return f"""
        set -euo pipefail
        cd {DBT_PROJECT_DIR}
        export DBT_PROFILES_DIR={DBT_PROFILES_DIR}
        dbt build --profiles-dir {DBT_PROFILES_DIR} --profile {DBT_PROFILE} --target {DBT_TARGET}
        """

    dbt_deps() >> dbt_build()

dbt_build_daily()