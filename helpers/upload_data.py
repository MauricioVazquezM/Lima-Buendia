import OpenBlender
import pandas as pd


df = pd.read_csv("./MC.csv")


action = "API_createDataset"
parameters = {
    "token": "62b47d30951629676b191007Tw8bQFGOM2UySjtTPs0JigwQMAJU89",
    "id_user": "62b47d30951629676b191007",
    "name": "Media Cloud Data",
    "description": "Data from media cloud",
    "visibility": "private",
    "tags": ["headlines", "MediaCloud"],
    "insert_observations": "on",
    "dataframe": df.to_json(),
}
response = OpenBlender.call(action, parameters)
response
