import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_resources():
    try:
        session = boto3.Session(profile_name='default')  
        regions = session.get_available_regions('ec2')

        resource_summary = {}
        for region in regions:
            print(f"Fetching resources in region: {region}")
            ec2 = session.client('ec2', region_name=region)
            rds = session.client('rds', region_name=region)

            # EC2 Instances
            ec2_instances = ec2.describe_instances()
            instance_ids = [instance['InstanceId'] for reservation in ec2_instances['Reservations'] for instance in reservation['Instances']]

            # RDS Instances
            rds_instances = rds.describe_db_instances()
            db_instances = [db['DBInstanceIdentifier'] for db in rds_instances['DBInstances']]

            resource_summary[region] = {
                "EC2 Instances": instance_ids,
                "RDS Instances": db_instances
            }

        for region, resources in resource_summary.items():
            print(f"\nRegion: {region}")
            for resource_type, resource_list in resources.items():
                print(f"{resource_type}: {resource_list}")

    except NoCredentialsError:
        print("AWS credentials not found.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    list_resources()
