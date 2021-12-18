#!/usr/bin/env python3

from url_shortner.traffica import Traffico

#from cdk_watchful import Watchful

from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb,
    aws_lambda,
    aws_apigateway,
    App,
    Duration
    # aws_sqs as sqs,
)
from constructs import Construct

class UrlShortnerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        table = aws_dynamodb.Table(self, "mapping-table",
                                   partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING))

        function = aws_lambda.Function(self, "backend",
                                       runtime=aws_lambda.Runtime.PYTHON_3_7,
                                       handler="handler.main",
                                       code=aws_lambda.Code.from_asset("./lambda"))

        table.grant_read_write_data(function)
        function.add_environment("TABLE_NAME", table.table_name)

        api = aws_apigateway.LambdaRestApi(self, "api", handler=function)

        #wf = Watchful(self, 'monitoring', alarm_email='deedat95@gmail.com')
        #wf.watch_scope(self)




class TrafficStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Traffico(self, 'TestTraffic', 
        url='https://8jhhdmzpwf.execute-api.us-east-1.amazonaws.com/prod/7d3a74ec', 
        tps= 10)

app = App()
UrlShortnerStack(app, "urlshort-app")
TrafficStack(app, "test-traffic")
app.synth()
