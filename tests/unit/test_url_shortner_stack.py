import aws_cdk as core
import aws_cdk.assertions as assertions

from url_shortner.url_shortner_stack import UrlShortnerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in url_shortner/url_shortner_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = UrlShortnerStack(app, "url-shortner")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
