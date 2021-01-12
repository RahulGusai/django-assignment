# django-assignment

Django REST API
Django version- 3.1.5,Python version- 3.6.9
Database- MySql

How to Run:
1. Clone the Repository
2. cd django-assignment
3. python3 manage.py runserver LOCAL_IP:PORT_NO (Add LOCAL_IP under ALLOWED_HOSTS in djangorestapi/settings.py)

API Details:
AppName-post
API- /post/api
Request Format- JSON
Response Format- JSON

Tested Cases:

For Payload 1:
curl --header "Content-Type: application/json" --request POST  --data '{"database_name":"database1","data":{"table_name":"table1"}}' http://LOCAL_IP:PORT_NO/post/api

For Payload 2:
curl --header "Content-Type: application/json" --request POST  --data '{"database_name":"database1","data":{"select_list":[  {"column": "city"},{"column": "price"} ],"worksheet_id":"table1"} }' http://LOCAL_IP:PORT_NO/post/api

For Payload 3:
1. curl --header "Content-Type: application/json" --request POST  --data '{"database_name":"database1","data":{"aggregate":[  {"column": "price","type":"sum"} ], "groupby":[{"column":"city"}] , "worksheet_id":"table1"} }' http://LOCAL_IP:PORT_NO/post/api

2.curl --header "Content-Type: application/json" --request POST  --data '{"database_name":"database1","data":{"aggregate":[  {"column": "price","type":"avg"} ], "groupby":[{"column":"city"},{"column":"userid"}] , "worksheet_id":"table1"} }' http://LOCAL_IP:PORT_NO/post/api


Note: API has been tested with two databases in the database server, default database i.e. default_db and other database i.e. database1.table1 model was created for testing purposes and only synced with database1.
