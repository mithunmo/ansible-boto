import boto3

client = boto3.client('ec2', region_name='us-east-1')


client.run_instances(
    ImageId='ami-a4827dc9',
    KeyName='Mofilm-Stage',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    SecurityGroupIds=['sg-974596f3'],
    SubnetId='subnet-46d3036d'
)


#SecurityGroups=['quick-start-1'],

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)


#ami-a4827dc9
