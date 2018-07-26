import boto3

ec2 = boto3.resource("ec2")
# i-05a6357eab1ad30ad


new_instance = ec2.create_instances(
    ImageId = 'ami-8eecc9e2',
    InstanceType = 't2.micro',
    MinCount=1,
    MaxCount=1,
    Keyname='4LINUX',
    SecurityGroupIds=['sg-5901a520']
)
print(new_instance)


# matar_instance = ec2.instances.filter(InstanceIds=['i-05a6357eab1ad30ad']).terminate()
# reiniciar_instance = ec2.instances.filter(InstanceIds=['i-05a6357eab1ad30ad']).reboot()
# start_instance = ec2.instances.filter(InstanceIds=['i-05a6357eab1ad30ad']).start()
# stop_instance = ec2.instances.filter(InstanceIds=['i-05a6357eab1ad30ad']).stop()

# instances = ec2.instances.all()
# for c in instances:
#     print(c.instance_id)
#     print(c.instance_type)

# security_group = ec2.SecurityGroup('sg-0b31cf3dcb17ded4d')
# security_group.authorize_ingress(
#     FromPort = 80,
#     ToPort = 80,
#     CidrIp='0.0.0.0/0',
#     IpProtocol = 'tcp'
# )

# security_group.revoke_ingress(
#     FromPort = 80,
#     ToPort = 80,
#     CidrIp='0.0.0.0/0',
#     IpProtocol = 'tcp'
# )

# security_group.delete()


# security_group = ec2.create_security_group(GroupName='GrupoScript',Description='Criado por script.')
# print(security_group)

# security_groups = ec2.security_groups.all()
# for group in security_groups:
#     print(group.group_name, group.group_id)

