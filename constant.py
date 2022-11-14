import secrets
import datetime
import boto3

# Declare necessary variable for printing assessment Summary
account_id = None
aws_region = None
aws_event_type = None

# Declare the counter variables for preparing the analysis table
initialaccesscount = 0
reconcount = 0
credentialaccesscount = 0
privilegeesclationcount = 0
dataexflitrationcount = 0
persistencecount = 0
collectioncount = 0
othercount = 0

logs = []

# Storing current datetime
currdatetime = str(datetime.datetime.now())

# Generating the unique file names for the reportfile
file_name = f"CloudTrailsLogs{secrets.token_hex(nbytes=8)}.html"
analytics_chart_name = f"analyticsChart{secrets.token_hex(nbytes=8)}.png"

# Initiate the cloudtrail client
cloudtrailclient = boto3.client("cloudtrail")

# List of events that we gonna catch in the report
aws_event_name = ['CopyObject', 'GetAuthorizationToken', 'GetSecretValue', 'CreateSnapshot', 'UpdateFunctionConfiguration', 'AddUserToGroup', 'CreateGroup', 'AttachRolePolicy', 'PutBucketAcl', 'CreateLoginProfile', 'CreateInstance', 'CreatePolicyVersion', 'CreateRole', 'ConsoleLogin', 'GetPasswordData', 'CreateRepository', 'ModifyImageAttribute', 'CreateUser', 'CreateAccessKey', 'ModifySnapshotAttribute',
                  'GetConsoleScreenshot', 'PutBucketPolicy', 'CreateFunction', 'CreateImage', 'CreateInstanceProfile', 'GetFederationToken', 'PutGroupPolicy', 'UpdateProfile', 'StartSession', 'UpdateAssumeRolePolicy', 'GetObject', 'PutImage', 'PutRolePolicy', 'UpdateFunctionCode', 'UpdateFunction', 'PutUserPolicy', 'RestoreDBInstanceFromDBSnapshot', 'CreateKeyPair', 'GetSessionToken', 'CreatePolicy']


# aws_event_name = ["LookupEvents", "GetCallerIdentity", "GetCallerIdentity",
#                   "DescribeLaunchTemplates", "DescribeInstances", "AssumeRole", "LookupEvents"]

# Lists for the different events categories
initial_access_lst = ["ConsoleLogin", "GetFederationToken",
                      "GetSessionToken", "StartSession", "GetAuthorizationToken"]
credential_access_lst = ["GetSecretValue", "GetPasswordData"]
privilege_esclation_lst = ["CreateUser", "CreateLoginProfile", "UpdateProfile", "PutUserPolicy", "AttachUserPolicy", "AddUserToGroup", "PutGroupPolicy", "CreateGroup",
                           "CreateRole", "AssumeRole", "CreateInstanceProfile", "UpdateAssumeRolePolicy", "AttachRolePolicy", "PutRolePolicy", "CreatePolicy", "CreatePolicyVersion"]
data_exflitration_lst = ["ModifySanpshotAttribute", "ModifyImageAttribute",
                         "PutBucketPolicy", "PutBucketAcl", "RestoreDBInstanceFromDBSnapshot"]
persistence_lst = ["CreateAccessKey", "CreateInstance",
                   "CreateKeyPair", "CreateImage", "CreateRepository", "PutImage"]
collection_lst = ["CopyObject", "GetObject",
                  "GetConsoleScreenshot", "CreateSnapshot"]

# Dictionary for gethering the analysis information
tabledata = {"EventCategory": [], "EventName": [], "EventTime": [], "ResourceName": [],
             "ResourceType": [], "sourceIPAddress": []}


# List for searching or filtering for a specific service filtering
IAM_resource_type_lst = [
    "AWS::IAM::AccessKey",
    "AWS::IAM::Group",
    "AWS::IAM::InstanceProfile",
    "AWS::IAM::ManagedPolicy",
    "AWS::IAM::OIDCProvider",
    "AWS::IAM::Policy",
    "AWS::IAM::Role",
    "AWS::IAM::SAMLProvider",
    "AWS::IAM::ServerCertificate",
    "AWS::IAM::ServiceLinkedRole",
    "AWS::IAM::User",
    "AWS::IAM::UserToGroupAddition",
    "AWS::IAM::VirtualMFADevice"]

S3_resource_type_lst = [
    "AWS::S3::AccessPoint",
    "AWS::S3::Bucket",
    "AWS::S3::BucketPolicy",
    "AWS::S3::MultiRegionAccessPoint",
    "AWS::S3::MultiRegionAccessPointPolicy",
    "AWS::S3::StorageLens",
    "AWS::S3ObjectLambda::AccessPoint",
    "AWS::S3ObjectLambda::AccessPointPolicy",
    "AWS::S3Outposts::AccessPoint",
    "AWS::S3Outposts::Bucket",
    "AWS::S3Outposts::BucketPolicy",
    "AWS::S3Outposts::Endpoint"
]
lambda_resouce_type_lst = [
    "AWS::Lambda::Alias",
    "AWS::Lambda::CodeSigningConfig",
    "AWS::Lambda::EventInvokeConfig",
    "AWS::Lambda::EventSourceMapping",
    "AWS::Lambda::Function",
    "AWS::Lambda::LayerVersion",
    "AWS::Lambda::LayerVersionPermission",
    "AWS::Lambda::Permission",
    "AWS::Lambda::Url",
    "AWS::Lambda::Version"]
