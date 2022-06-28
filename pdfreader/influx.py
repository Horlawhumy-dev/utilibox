import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "harof.dev@gmail.com"
url = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="utilibox"

write_api = client.write_api(write_options=SYNCHRONOUS)
   
sequence = ["mem,host=host1 used_percent=23.43234543",
    "mem,host=host1 available_percent=15.856523"]
write_api.write(bucket, org, sequence)

for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="harof.dev@gmail.com", record=point)
  time.sleep(1) # separate points by 1 second

query = """from(bucket: "utilibox") |> range(start: -1h)"""
tables = client.query_api().query(query, org=org)
for table in tables:
    for record in table.records:
        print(record)

client.close()
