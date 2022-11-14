<div>
  <h1 align="center">Compromise assessment script</h1>
  <br>
  <img align="left" alt="Invinsense logo" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/Invinsense_logo_tagline.svg" width="300px">
  <img align="right" alt="Infopercept logo" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/Infopercept_logo%202.svg" width="300px">
  <br>
</div>
<br>
<br>


## 📙 About the script
- AWS Compromise Assessment compiles the events and Indicator of Compromise (IoC) from CloudTrail Logs after an incident has occurred or appears to be compromised. It will assist in obtaining complete critical event data and making it easier for threat hunters for future forensics.



## 📖 System Prerequisites 
| Component            | README                                                                             |
| -------------------- | ---------------------------------------------------------------------------------- |
| python version > 3.6 | Must be pre-installed in computer in order to run the compromise assessment script |
| Configure AWS SDK    | Using AWS CLI you have to configure the AWS SDK                                    |
| Operating system     | Windows or Ubuntu/Linux                                                            |
| CPU                  | Core 2 CPU or more                                                                 |
| Memory               | 4 GB RAM                                                                           |


## 🚧 Features

- Scrpit will show `50000` record of cloudtrail logs by default or if you want to customize it you can give `-record_limit` argument to the command.
- Script will show cloudtrail logs according to `days` argument (`60` or `90`) in the command line default is `90` or you can give your days using `-days` command line argument.
- Script will also gives you a cloudtrail logs based on AWS services using the argument called `-service_name`.
- Script will shows the logs in the tabular format.
- Log table provide pagination functionality for traverse throught the logs.
- Log table also provide a functionality for searching a logs according to event category.
- Script will show you the `Analytic (statastical)` table.
- Script will display the `histogram` and `pie chart` according to analytic table.


## ✅ How to run the script

1. Installation of python
    - Python for Windows: https://www.digitalocean.com/community/tutorials/install-python-windows-10
    - Python for Ubuntu/Linux: https://www.makeuseof.com/install-python-ubuntu/

2. Configuration of AWS SDK
    - Install AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
    - Run the following command: `aws configure` and provide your aws credentials to setup the AWS ADK on your system.

3. Installation of required python dependency
    - Open the command prompt or terminal.
    - Go to project directory.
    - Run the following command: `pip3 install -r requirements.txt`
    - it will download all the required denpendency.

4. Run the compromise assessment script
   - There are three arguments in the command `1.days`, `2.record_limit`, and `3.service_name`
      - python3 compromise-assessment.py -days {`YOUR DAYS`} -record_limit {`YOUR RECORD LIMIT`} -service_name {`YOUR SERVICE NAME`}

## 🎦 Repository Visualization
<div align="center">
    <img alt="Report" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/report-ss.png" /><br>
    <img alt="Report" src="https://github.com/Infopercept/compromise-assessment/blob/main/templates/report-ss-2.png" />
</div>



## ⚖️ License
Licensed under the (https://www.infopercept.com/) License, Version 3.0.
Copyright 2022 Infopercept. [Copy of the license](LICENSE.txt).


## 🖥️ Website
[https://infopercept.com](https://infopercept.com)


## 🎭 Support
* [Email](mailto:sos@infopercept.com)
* [Open issue](https://github.com/Infopercept/compromise-assessment/issues)
* [Infopercept.com](https://infopercept.com/contact)


## 🤝 Contributors 

([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>  <tr>
    <td align="center"><a href="https://github.com/PrajapatiBhavik"><img src="https://avatars.githubusercontent.com/u/67953602?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bhavik Prajapati</b></sub></a><br /><a href="https://github.com/PrajapatiBhavik" title="Code">💻</a></td>
  </tr>
</table>
