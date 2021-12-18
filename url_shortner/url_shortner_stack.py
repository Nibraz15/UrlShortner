from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb,
    aws_lambda,
    aws_apigateway
    # aws_sqs as sqs,
)
from constructs import Construct

from waltersco_common import WaltersCoStack

class UrlShortnerStack(WaltersCoStack):

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

        self.map_waltersco_subdomain("go", api)