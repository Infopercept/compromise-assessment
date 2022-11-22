<div>
  <h1 align="center">AWS Compromise assessment script</h1>
  <br>
  <img align="left" alt="Invinsense logo" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/Invinsense_logo_tagline.svg" width="300px">
  <img align="right" alt="Infopercept logo" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/Infopercept_logo%202.svg" width="300px">
  <br>
</div>
<br>
<br>


## :orange_book: About the script
AWS Compromise Assessment compiles the events and Indicator of Compromise (IoC) from CloudTrail Logs after an incident has occurred or appears to be compromised. It will assist in obtaining complete critical event data and making it easier for threat hunters for future forensics.



## :book: System Prerequisites 
| Component            | README                                                                             |
| -------------------- | ---------------------------------------------------------------------------------- |
| python version > 3.6 | Must be pre-installed in computer in order to run the compromise assessment script |
| Configure AWS SDK    | Using AWS CLI you have to configure the AWS SDK                                    |
| Operating system     | Windows or Ubuntu/Linux                                                            |
| CPU                  | Core 2 CPU or more                                                                 |
| Memory               | 4 GB RAM                                                                           |


## :high_brightness: Features

- Scrpit will show `50000` record of cloudtrail logs by default or if you want to customize it you can give `-record_limit` argument to the command.
- Script will show cloudtrail logs according to `days` argument (`60` or `90`) in the command line default is `90` or you can give your days using `-days` command line argument.
- Script will also gives you a cloudtrail logs based on AWS services using the argument called `-service_name`.
- Script will shows the logs in the tabular format.
- Log table provide pagination functionality for traverse throught the logs.
- Log table also provide a functionality for searching a logs according to event category.
- Script will show you the `Analytic (statastical)` table.
- Script will display the `histogram` and `pie chart` according to analytic table.


## :white_check_mark: How to run the script

### :inbox_tray: Installation of python
Python for Windows
    
```bash
https://www.digitalocean.com/community/tutorials/install-python-windows-10
```
Python for Ubuntu/Linux
    
```bash
https://www.makeuseof.com/install-python-ubuntu/
```

### :nut_and_bolt: Configuration of AWS SDK
Install AWS CLI from the link given below
    
```bash 
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

Run the following command and provide your aws credentials to setup the AWS ADK on your system.

```bash
aws configure
```

### :syringe: Install required python dependency
Open the command prompt or terminal on your system then reach to project directory and run the following command

```bash
pip3 install -r requirements.txt
```
   
### :open_file_folder: Clone the GitHub repository
```bash
https://github.com/Infopercept/compromise-assessment
```

### :newspaper: Note
> If you are `Windows` user then use `python` for running the script.

or

> If you are `Ubunt/Linux/MacOs` user then use `python3` for runnig the script.

### :bulb: Help for script command
Type the following command

```bash
python3 compromise-assessment.py -h
```
or
```bash
python3 compromise-assessment.py --help
```
Result

<img alt="help-ss" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/compromise-assessment-help-ss.png">

### :arrow_forward: Run the compromise assessment script
- You can use this arguments to make user specific choices and arguments optionals are `days`, `record_limit`, and `service_name`.
- Commands you can use:

| Command                                                                           | Description                                                                                                                                            |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| python3 compromise-assessment.py                                                  | This command gives you the 90 days cloudtrail records as default it takes 90 days,it will take all services and it will return 5000 record by default. |
| python3 compromise-assessment.py -days 60                                         | This command gives you the 60 days cloudtrail records, it will take all services and it will return 5000 record by default.                            |
| python3 compromise-assessment.py -days 90                                         | This command gives you the 90 days cloudtrail records, it will take all services and it will return 5000 record by default.                            |
| python3 compromise-assessment.py -record_limit 1000                               | This command gives you the 90 days cloudtrail records as default, it will take all services and it will return 1000 record.                            |
| python3 compromise-assessment.py -service_name s3                                 | This command gives you the 90 days cloudtrail records as default, it will take S3 services and it will return 5000 record.                             |
| python3 compromise-assessment.py -days 60 -service_name iam                       | This command gives you the 60 days cloudtrail records, it will take IAM services and it will return 5000 record.                                       |
| python3 compromise-assessment.py -days 70 -record_limit 5000 -service_name lambda | This command gives you the 70 days cloudtrail records, it will take LAMBDA services and it will return 5000 record.                                    |



## :cinema: Repository Visualization
<div align="center">
    <img alt="Report" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/report-ss.png" /><br>
    <img alt="Report" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/report-ss-2.png" />
</div>


## :key: License
Licensed under the (https://www.infopercept.com/) License, Version 3.0.
Copyright 2022 Infopercept. [Copy of the license](LICENSE).


## :computer: Website
[https://infopercept.com](https://infopercept.com)


## :raised_hands: Support
* [Email](mailto:sos@infopercept.com)
* [Open issue](https://github.com/Infopercept/compromise-assessment/issues)
* [Infopercept.com](https://infopercept.com/contact)


## :family: Contributors 

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>  <tr>
    <td align="center"><a href="https://github.com/PrajapatiBhavik"><img src="https://avatars.githubusercontent.com/u/67953602?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bhavik Prajapati</b></sub></a><br /><a href="https://github.com/PrajapatiBhavik" title="Code">:computer:</a></td>
  </tr>
</table>

## Author

👤 **Bhavik Prajapati**

- Github: [@BhavikDevInfopercept](https://github.com/BhavikDevInfopercept)
