import constant
import argparse
import utility_functions


# Function to handle all the operation perform in the list
def drivingfunction(days, service_name, record_limit, parameter_used):
    try:
        if days != None and service_name == None:
            page_iterator = utility_functions.getdatafromcloudtrail(
                constant.cloudtrailclient, int(days), record_limit)

            if page_iterator is not None:

                logsdictionary = utility_functions.makedictobjectforreport(
                    page_iterator)

                if logsdictionary is not None:

                    tab_data = utility_functions.convertdictobjecttojson(
                        logsdictionary)

                    countdict = utility_functions.makecountdict(tab_data)
                    # parameter_used = f"compromise-assessment.py -days {days}"

                    res = utility_functions.printreport(
                        tab_data, countdict, parameter_used, constant.account_id, constant.aws_region, constant.aws_event_type)

                    utility_functions.printmsg(res)
        if days != None and service_name != None:
            if service_name == "s3":
                resource_lst = constant.S3_resource_type_lst
            elif service_name == "iam":
                resource_lst = constant.IAM_resource_type_lst
            elif service_name == "lambda":
                resource_lst = constant.lambda_resouce_type_lst

            for resource_name in resource_lst:
                if utility_functions.cloudtrailresponseforservice(constant.cloudtrailclient, resource_name, record_limit) is not None:
                    constant.logs.append(utility_functions.cloudtrailresponseforservice(
                        constant.cloudtrailclient, resource_name, record_limit))

            if constant.logs != None:
                tab_data = utility_functions.convertdictobjecttojson2(
                    constant.logs)
                countdict = utility_functions.makecountdict(tab_data)

                # parameter_used = f"compromise-assessment.py -days {days} -service_name {service_name}"

                res = utility_functions.printreport(
                    tab_data, countdict, parameter_used, constant.account_id, constant.aws_region, constant.aws_event_type)

                utility_functions.printmsg(res)
    except Exception as e:
        print(e)
        pass


try:
    # Taking default record limit 1000
    rec_lim = 1000
    # Taking all the command line arguments
    parser = argparse.ArgumentParser()

    # adding the argumets in argument parser
    parser.add_argument("-days", required=False,
                        help="days in integer so that logs fetchs from the current date to last given days.")

    parser.add_argument("-record_limit", required=False,
                        help="record_limit is the number of record you want to fetch from the cloudtrail.")

    parser.add_argument("-service_name", required=False,
                        help="service_name is the parameter used for filtering out specific service's event.")
    args = parser.parse_args()

    if args.days == None and args.record_limit == None and args.service_name == None:
        parameter_used = f"compromise-assessment.py -days 90 -record_limit {rec_lim}"
        drivingfunction(90, None, rec_lim, parameter_used)

    if args.days != None and args.record_limit != None and args.service_name != None:
        parameter_used = f"compromise-assessment.py -days {args.days} -service_name {args.service_name} -record_limit {args.record_limit}"
        drivingfunction(args.days, args.service_name.lower(),
                        args.record_limit, parameter_used)

    if args.days != None and args.record_limit == None and args.service_name == None:
        parameter_used = f"compromise-assessment.py -days {args.days} -record_limit {rec_lim}"
        drivingfunction(args.days, None, rec_lim, parameter_used)

    if args.days == None and args.record_limit != None and args.service_name == None:
        parameter_used = f"compromise-assessment.py -days 90 -record_limit {args.record_limit}"
        drivingfunction(90, None, args.record_limit, parameter_used)

    if args.days == None and args.record_limit == None and args.service_name != None:
        parameter_used = f"compromise-assessment.py -days 90 -record_limit {rec_lim} -service_name {args.service_name}"
        drivingfunction(90, args.service_name.lower(), rec_lim, parameter_used)

    if args.days != None and args.record_limit != None and args.service_name == None:
        parameter_used = f"compromise-assessment.py -days {args.days} -record_limit {args.record_limit}"
        drivingfunction(args.days, None, args.record_limit, parameter_used)

    if args.days != None and args.record_limit == None and args.service_name != None:
        parameter_used = f"compromise-assessment.py -days {args.days} -record_limit {rec_lim} -service_name {args.service_name}"
        drivingfunction(args.days, args.service_name.lower(),
                        rec_lim, parameter_used)

    if args.days == None and args.record_limit != None and args.service_name != None:
        parameter_used = f"compromise-assessment.py -days 90 -record_limit {args.record_limit} -service_name {args.service_name}"
        drivingfunction(90, args.service_name.lower(),
                        args.record_limit, parameter_used)

except constant.cloudtrailclient.exceptions.InvalidNextTokenException as e:
    print("NextToken not found", e)
except Exception as e:
    print(e)
    print("Unable to retrieve CloudTrail events for user ")
