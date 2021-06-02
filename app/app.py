import boto3

def handler(event, context):
    for rds_instance, start_or_stop in event.items():
        if start_or_stop in ['start', 'stop']:
            print(rds_instance + ' ' + start_or_stop)
        else:
            raise ModuleNotFoundError(start_or_stop)
    for rds_instance, start_or_stop in event.items():
        rds_set_start_or_stop(rds_instance, start_or_stop)

def rds_set_start_or_stop(rds_instance, start_or_stop):
    client = boto3.client('rds')
    if start_or_stop == 'start':
        result = client.start_db_instance(DBInstanceIdentifier = rds_instance)
    elif start_or_stop == 'stop':
        result = client.stop_db_instance(DBInstanceIdentifier = rds_instance)
    print(result)
