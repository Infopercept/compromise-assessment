import json
from queue import Empty
import constant
from jinja2 import Environment, FileSystemLoader
import datetime
from datetime import timedelta
import re

# Function to print the HTML report


def printreport(tabledata, countdictionary, parameter_used, account_id, aws_region, aws_event_type):
    try:
        flag = False
        file_loader = FileSystemLoader("templates")
        env = Environment(loader=file_loader)
        rendered = env.get_template("table.html").render(datas=zip(
            tabledata["EventCategory"], tabledata["EventName"], tabledata["EventTime"], tabledata["ResourceName"], tabledata["ResourceType"], tabledata["sourceIPAddress"]), analysistable=countdictionary, dt=constant.currdatetime, params=parameter_used, acc_id=account_id, region=aws_region, event_type=aws_event_type)
        try:
            with open(constant.file_name, "w") as f:
                f.write(rendered)
                flag = True
            return flag
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)

# Function to filter out the specific fields from the boto3 response


def makedictobjectforreport(page_iterator):
    try:
        logsdictionary = []
        for page in page_iterator:
            for event in range(len(page["Events"])):
                page["Events"][event]["EventTime"] = str(
                    page["Events"][event]["EventTime"])
                if (page["Events"][event]["EventName"] in constant.aws_event_name) or (re.search("^Get*", page["Events"][event]["EventName"]) or re.search("^Head*", page["Events"][event]["EventName"]) or re.search("^List*", page["Events"][event]["EventName"]) or re.search("^Describe*", page["Events"][event]["EventName"])):
                    if len(page["Events"][event]["EventName"]) == 0:
                        page["Events"][event]["EventName"] = "None"

                    if page["Events"][event]["EventTime"] is None:
                        page["Events"][event]["EventTime"] = "None"
                    else:
                        page["Events"][event]["EventTime"] = str(
                            page["Events"][event]["EventTime"])

                    if len(page["Events"][event]["Resources"]) == 0:
                        res_name = "None"
                    else:
                        res_name = page["Events"][event]["Resources"][0]["ResourceName"]
                    if len(page["Events"][event]["Resources"]) == 0:
                        res_type = "None"
                    else:
                        res_type = page["Events"][event]["Resources"][0]["ResourceType"]

                    if json.loads(page["Events"][event]["CloudTrailEvent"])["sourceIPAddress"] == "":
                        json.loads(page["Events"][event]["CloudTrailEvent"])[
                            "sourceIPAddress"] = "None"

                    if json.loads(page["Events"][event]["CloudTrailEvent"])["awsRegion"] != "":
                        constant.aws_region = json.loads(
                            page["Events"][event]["CloudTrailEvent"])["awsRegion"]

                    if json.loads(page["Events"][event]["CloudTrailEvent"])["userIdentity"].get("accountId") is not None:
                        constant.account_id = json.loads(page["Events"][event]["CloudTrailEvent"])[
                            "userIdentity"].get("accountId")

                    if json.loads(page["Events"][event]["CloudTrailEvent"])["eventType"] != "":
                        constant.aws_event_type = json.loads(
                            page["Events"][event]["CloudTrailEvent"])["eventType"]

                    logsdictionary.append([{"EventName": page["Events"][event]["EventName"], "EventTime":page["Events"][event]["EventTime"], "ResourceName":res_name,
                                            "ResourceType":res_type, "sourceIPAddress":json.loads(page["Events"][event]["CloudTrailEvent"])["sourceIPAddress"]}])
        return logsdictionary
    except Exception as e:
        print(e)


# Function to fetch all the events logs from the AWS cloudetrail for a given time duration
def getdatafromcloudtrail(cloudtrailclient, days, record_limit):
    try:
        enddate = datetime.datetime.today()
        startdate = enddate - timedelta(days=int(days))
        nexttoken = ""
        paginator = cloudtrailclient.get_paginator('lookup_events')
        cloudtrailresponse0 = dict(cloudtrailclient.lookup_events(
            StartTime=startdate,
            EndTime=enddate,
        ))
        nexttoken = cloudtrailresponse0["NextToken"]
        page_iterator = paginator.paginate(
            StartTime=startdate,
            EndTime=enddate,
            PaginationConfig={
                'MaxItems': record_limit,
                'PageSize': 100,
                'StartingToken': nexttoken
            })
        return page_iterator
    except Exception as e:
        print(e)


def cloudtrailresponseforservice(cloudtrailclient, servicename, record_limit):
    try:
        logsdictionary = []
        enddate = datetime.datetime.today()
        startdate = enddate - timedelta(days=60)
        nexttoken = ""
        paginator = cloudtrailclient.get_paginator('lookup_events')
        cloudtrailresponse0 = dict(cloudtrailclient.lookup_events(
            LookupAttributes=[
                {
                    'AttributeKey': 'ResourceType',
                    'AttributeValue': servicename
                },
            ],
            StartTime=startdate,
            EndTime=enddate,
        ))
        nexttoken = cloudtrailresponse0["NextToken"]
        if nexttoken is not None:
            page_iterator = paginator.paginate(
                LookupAttributes=[
                    {
                        'AttributeKey': 'ResourceType',
                        'AttributeValue': servicename
                    },
                ],
                StartTime=startdate,
                EndTime=enddate,
                PaginationConfig={
                    'MaxItems': record_limit,
                    'PageSize': 10,
                    'StartingToken': nexttoken
                })
            if page_iterator is not Empty:
                for page in page_iterator:
                    for event in range(len(page["Events"])):
                        page["Events"][event]["EventTime"] = str(
                            page["Events"][event]["EventTime"])
                        if page["Events"][event]["EventName"] in constant.aws_event_name or re.search("^Get*", page["Events"][event]["EventName"]) or re.search("^Head*", page["Events"][event]["EventName"]) or re.search("^List*", page["Events"][event]["EventName"]) or re.search("^Describe*", page["Events"][event]["EventName"]):
                            if len(page["Events"][event]["EventName"]) == 0:
                                page["Events"][event]["EventName"] = "None"

                            if page["Events"][event]["EventTime"] is None:
                                page["Events"][event]["EventTime"] = "None"
                            else:
                                page["Events"][event]["EventTime"] = str(
                                    page["Events"][event]["EventTime"])

                            if len(page["Events"][event]["Resources"]) == 0:
                                res_name = "None"
                            else:
                                res_name = page["Events"][event]["Resources"][0]["ResourceName"]
                            if len(page["Events"][event]["Resources"]) == 0:
                                res_type = "None"
                            else:
                                res_type = page["Events"][event]["Resources"][0]["ResourceType"]

                            if json.loads(page["Events"][event]["CloudTrailEvent"])["sourceIPAddress"] == "":
                                json.loads(page["Events"][event]["CloudTrailEvent"])[
                                    "sourceIPAddress"] = "None"

                            if json.loads(page["Events"][event]["CloudTrailEvent"])["awsRegion"] != "":
                                constant.aws_region = json.loads(
                                    page["Events"][event]["CloudTrailEvent"])["awsRegion"]

                            if json.loads(page["Events"][event]["CloudTrailEvent"])["userIdentity"].get("accountId") is not None:
                                constant.account_id = json.loads(page["Events"][event]["CloudTrailEvent"])[
                                    "userIdentity"].get("accountId")

                            if json.loads(page["Events"][event]["CloudTrailEvent"])["eventType"] != "":
                                constant.aws_event_type = json.loads(
                                    page["Events"][event]["CloudTrailEvent"])["eventType"]

                            logsdictionary.append([{"EventName": page["Events"][event]["EventName"], "EventTime":page["Events"][event]["EventTime"], "ResourceName":res_name,
                                                    "ResourceType":res_type, "sourceIPAddress":json.loads(page["Events"][event]["CloudTrailEvent"])["sourceIPAddress"]}])
            return logsdictionary
    except Exception as e:
        print(e)
        pass

# Function to convert list object to dictionary for preprocessing


def convertdictobjecttojson(logsdictionary):
    try:
        for event in logsdictionary:
            if event[0]["EventName"] in constant.initial_access_lst:
                constant.tabledata["EventCategory"].append("Initial Access")
            elif event[0]["EventName"] in constant.aws_event_name and re.search("^Get*", event[0]["EventName"]) or re.search("^Head*", event[0]["EventName"]) or re.search("^List*", event[0]["EventName"]) or re.search("^Describe*", event[0]["EventName"]):
                constant.tabledata["EventCategory"].append("Recon")
            elif event[0]["EventName"] in constant.credential_access_lst:
                constant.tabledata["EventCategory"].append("Credential Access")
            elif event[0]["EventName"] in constant.privilege_esclation_lst:
                constant.tabledata["EventCategory"].append(
                    "Privilege Esclation")
            elif event[0]["EventName"] in constant.data_exflitration_lst:
                constant.tabledata["EventCategory"].append("Data Exflitration")
            elif event[0]["EventName"] in constant.persistence_lst:
                constant.tabledata["EventCategory"].append("Persistence")
            elif event[0]["EventName"] in constant.collection_lst:
                constant.tabledata["EventCategory"].append("Collection")
            else:
                constant.tabledata["EventCategory"].append("Others")

            constant.tabledata["EventName"].append(event[0]["EventName"])
            constant.tabledata["EventTime"].append(event[0]["EventTime"])
            constant.tabledata["ResourceName"].append(event[0]["ResourceName"])
            constant.tabledata["ResourceType"].append(event[0]["ResourceType"])
            constant.tabledata["sourceIPAddress"].append(
                event[0]["sourceIPAddress"])
        return constant.tabledata
    except Exception as e:
        print(e)


# Function to convert list object to dictionary for preprocessing
def convertdictobjecttojson2(logsdictionary):
    try:
        for event in logsdictionary:
            for e in event:
                if e[0]["EventName"] in constant.initial_access_lst:
                    constant.tabledata["EventCategory"].append(
                        "Initial Access")
                if e[0]["EventName"] not in constant.initial_access_lst and e[0]["EventName"] not in constant.credential_access_lst and e[0]["EventName"] not in constant.privilege_esclation_lst and e[0]["EventName"] not in constant.data_exflitration_lst and e[0]["EventName"] not in constant.persistence_lst and e[0]["EventName"] not in constant.collection_lst:
                    constant.tabledata["EventCategory"].append("Others")
                elif e[0]["EventName"] in constant.aws_event_name or re.search("^Get*", e[0]["EventName"]) or re.search("^Head*", e[0]["EventName"]) or re.search("^List*", e[0]["EventName"]) or re.search("^Describe*", e[0]["EventName"]):
                    constant.tabledata["EventCategory"].append("Recon")
                elif e[0]["EventName"] in constant.credential_access_lst:
                    constant.tabledata["EventCategory"].append(
                        "Credential Access")
                elif e[0]["EventName"] in constant.privilege_esclation_lst:
                    constant.tabledata["EventCategory"].append(
                        "Privilege Esclation")
                elif e[0]["EventName"] in constant.data_exflitration_lst:
                    constant.tabledata["EventCategory"].append(
                        "Data Exflitration")
                elif e[0]["EventName"] in constant.persistence_lst:
                    constant.tabledata["EventCategory"].append("Persistence")
                elif e[0]["EventName"] in constant.collection_lst:
                    constant.tabledata["EventCategory"].append("Collection")

                constant.tabledata["EventName"].append(e[0]["EventName"])
                constant.tabledata["EventTime"].append(e[0]["EventTime"])
                constant.tabledata["ResourceName"].append(e[0]["ResourceName"])
                constant.tabledata["ResourceType"].append(e[0]["ResourceType"])
                constant.tabledata["sourceIPAddress"].append(
                    e[0]["sourceIPAddress"])
        return constant.tabledata
    except Exception as e:
        print(e)

# Function to make analytics dictionary for generating the analytics table and chart

def makecountdict(tabledata):
    try:
        for data in tabledata["EventName"]:
            if data in constant.initial_access_lst:
                constant.initialaccesscount += 1
            elif data not in constant.initial_access_lst and data not in constant.credential_access_lst and data not in constant.privilege_esclation_lst and data not in constant.data_exflitration_lst and data not in constant.persistence_lst and data not in constant.collection_lst:
                if re.search("^Get*", data):
                    constant.reconcount += 1
                if re.search("^Head*", data):
                    constant.reconcount += 1
                if re.search("^List*", data):
                    constant.reconcount += 1
                if re.search("^Describe*", data):
                    constant.reconcount += 1
            elif data in constant.credential_access_lst:
                constant.credentialaccesscount += 1
            elif data in constant.privilege_esclation_lst:
                constant.privilegeesclationcount += 1
            elif data in constant.data_exflitration_lst:
                constant.dataexflitrationcount += 1
            elif data in constant.persistence_lst:
                constant.persistencecount += 1
            elif data in constant.collection_lst:
                constant.collectioncount += 1
            else:
                constant.othercount += 1

        countdictionary = {'InitialAccess': constant.initialaccesscount, 'Recon': constant.reconcount, 'CredentialAccess': constant.credentialaccesscount, 'PrivilegeEsclation': constant.privilegeesclationcount,
                           'DataExfiltration': constant.dataexflitrationcount, 'Persistence': constant.persistencecount, 'Collection': constant.collectioncount, 'Others': constant.othercount}

        return countdictionary
    except Exception as e:
        print(e)

# Function to print the success and not success message once the report has been generated


def printmsg(flag):
    if flag:
        print("-------------------------------")
        print("Report Generated Successfully")
        print("-------------------------------")
    else:
        print("-----------------------------------")
        print("Report Not Generated Successfully")
        print("-----------------------------------")
