import aws_cdk
from constructs import Construct
from aws_cdk import aws_ecs, aws_ec2


class Traffico(Construct):

    def __init__(self, scope: Construct, id: str, *, url: str, tps: int):
        super().__init__(scope, id)

        cluster = aws_ecs.Cluster(self, 'Cluster')
        taskdef = aws_ecs.FargateTaskDefinition(self, 'PingerTask')
        taskdef.add_container('Pinger',
                              image=aws_ecs.ContainerImage.from_asset(
                                  './pinger'),
                              environment={"URL": url})
        aws_ecs.FargateService(self, 'PingerService',
                               cluster=cluster,
                               task_definition=taskdef,
                               desired_count=tps)
