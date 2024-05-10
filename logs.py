from azureml.core.authentication import MsiAuthentication
from azureml.core import Workspace
from azureml.core.webservice import Webservice

msi_auth = MsiAuthentication()
# Requires the config to be downloaded first to the current working directory
ws = Workspace(subscription_id="f5091c60-1c3c-430f-8d81-d802f6bf2414",
    resource_group="aml-quickstarts-258726",
    workspace_name = "quick-starts-ws-258726", auth=msi_auth
)

# Set with the deployment name
name = "baseline-v1-baseline"

# load existing web service
service = Webservice(name=name, workspace=ws)

logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
