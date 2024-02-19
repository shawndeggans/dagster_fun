from dagster import asset

# Very simple asset that returns the number 42
@asset
def my_asset(_):
    return 42

@asset
def more_complex_asset(_):
    return {
        "key": "value"
    }
    
# an asset that returns a pandas dataframe with a single column of customer data
@asset
def customer_data(_):
    import pandas as pd
    return pd.DataFrame({
        "customer_id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "age": [32, 45, 28],
    })
    
# an asset that depends on customer_data to return the first customer record
# this asset knows to look for the customer_data asset because it is passed as an argument
@asset
def first_customer(customer_data):
    return customer_data.iloc[0]