import boto3


class LocalDAO:
    def __init__(self, table_name):
        self.table_name = table_name
        self.client = boto3.client("dynamodb")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Writing back contents into file.")

    def get(self, key):
        response = self.client.get_item(
            TableName = self.table_name,
            Key = {
                's':{
                    'S': key
                }
            }
        )
        retval = response['Item']['l']['S']
        return retval

    def put(self, key, val):
        self.client.put_item(
            TableName = self.table_name,
            Item = {
                's': {'S': key},
                'l': {'S' : val}
            }
        )
