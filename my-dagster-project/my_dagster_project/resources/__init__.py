from dagster import StringSource, resource

@resource(config_schema={"my_config": StringSource})
def my_resource(context):
    return context.resource_config["my_config"]