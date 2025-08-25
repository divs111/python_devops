import boto3

def lambda_handler(event , context):
    ec2 = boto3.client('ec2')

    # get all ebs snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # get all ec2 instances active ID

    instance_response = ec2.describe_instances(filter=[{'Name' : 'instance-state-name' , 'values' : ['running']}])
    active_instance_ids = set()

    for reservation in instance_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('volumeId')

        if not volume_id:
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached ot any volume")
        else:
            # check if volume exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=volume_id)
                if not volume_response['volume'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response9['Error']["Code"] == "InvalidVolume.NotFound":
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it's associated volume is not found")