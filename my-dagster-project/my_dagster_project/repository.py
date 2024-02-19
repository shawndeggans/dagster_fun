from dagster import (
    load_assets_from_package_module, 
    repository,
    define_asset_job,
    ScheduleDefinition,
    with_resources,
)
from my_dagster_project import assets
from my_dagster_project.resources import my_resource

# the star means we're running all the projects
daily_asset_job = define_asset_job(name="daily_asset_job", selection="*")
daily_schedule = ScheduleDefinition(
    job=daily_asset_job,
    cron_schedule="@daily",
)

@repository
def my_dagster_project():
    return [
        daily_asset_job,
        daily_schedule,
        with_resources(load_assets_from_package_module(assets), {"my_resource": my_resource.configured({"my_config": {}})})
    ]