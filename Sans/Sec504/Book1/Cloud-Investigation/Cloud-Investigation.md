Brief Intro

In this lab you, will continue your investigation of the Falsimentis incident, turning your focus to an evaluation of compromised AWS systems through log analysis.
Requirements for This Lab

In this lab, you will use your Slingshot Linux VM. Make sure the VM is running before continuing with this lab exercise.
Try It Yourself

Evaluate the AWS logging information in ~/labs/awslogs. Starting with the S3 logs, identify and evaluate malicious activity associated with a bucket. Use the information you collect to build threat intelligence, applying it to the information revealed in AWS API call logs to understand the origin of the compromise. Build a timeline (using pencil and paper or any other drawing tool) to map out the major compromise events.
Walkthrough
Overview

The executive leadership at Falsimentis has asked you to continue to apply your incident response analysis skills to assist them in understanding a suspected breach of AWS cloud assets.

Moritz Rawes, senior developer for Falsimentis, recently opened a ticket asking for several files to be restored from backup in an Amazon Web Services (AWS) Simple Storage Service (S3) bucket used by Falsimentis engineering: falsimentis-eng. Rawes reports that at 02:05 am UTC on 2021-08-02, he noticed that the image files for the Falsimentis AI system-on-chip (SoC) die have been replaced with what appears to be encrypted replacements.

AWS S3 bucket file listing for falsimentis-eng showing several files with .jpg.gpg filename extensions

Service desk analyst Ashlan McReath started to review the ticket 33 minutes later, confirming the presence of files with .jpg.gpg file name extensions in the s3://falsimentis-eng bucket, but also identified a ransom note from the Midnite Meerkats.

AWS S3 bucket file listing for falsimentis-eng showing a ransom note from the Midnite Meerkats

The ransom note is reproduced here.

Oops! You Have Been Pwned by the Midnite Meerkats!

We are the Midnite Meerkats, and we have control of your systems. You have 24
hours to pay us, or your files will be done. Everywhere!!!!

To pay us, fill out this form. It is in your best interest, if you ever want to
keep your files.

https://midnitemeerkats.com/payus/

Don't be too sad, you still have some time! Here is a song by some happy cats!

https://youtu.be/GSMCRD35ch4

You are asked to evaluate the logging information available to assess the incident using the following log resources:

    S3 bucket access logs
    CloudTrail API activity logs

Using the time information from Rawes' service desk ticket, we can start our timeline information as shown here.

Initial incident timeline denoting encrypted file identification

    Remember that in the electronic lab files, you can click on images to open full-size in a new tab. 

Open a Terminal

From the Slingshot Linux VM, open a terminal.
Change to Log Directory

Change to the ~/labs/awslogs directory, as shown here.

sec504@slingshot:~$ cd ~/labs/awslogs/
sec504@slingshot:~/labs/awslogs$

List Log Files

List the contents of the log files directory, as shown here.

sec504@slingshot:~/labs/awslogs$ ls
CloudTrail  s3-ai  s3-eng  vpcflowlogs  s3-cats  s3-w3

Falsimentis has collected several log files for your analysis:

    CloudTrail: CloudTrail logs, capturing all AWS API calls for successes and failures
    s3-ai: S3 logs for the falsimentis-ai bucket
    s3-cats:S3 logs for the falsimentis-cats bucket
    s3-eng: S3 logs for the falsimentis-eng bucket
    s3-w3: S3 logs for the falsimentis-w3 bucket

S3 Bucket Overview

Since the reported incident is associated with the falsimentis-eng bucket files, we can start our analysis with the associated logging information. Change to the s3-eng directory and list the files, as shown here.

sec504@slingshot:~$ cd ~/labs/awslogs/s3-eng
sec504@slingshot:~/labs/awslogs/s3-eng$ ls
2021-07-29-14-12-58-9643D3A6992B04CB
2021-07-29-14-18-58-E2B2665DDB497919
2021-07-29-14-24-46-2DE0A45E96362F96
...
2021-07-29-21-35-00-B150CC0D6633A771
2021-07-29-21-38-00-F574A331E443776A
2021-07-29-21-38-06-EA5CE2FA20B97A72
2021-07-29-21-39-45-A769FB33688D1BCA
2021-07-29-21-39-48-39F0C1A3223EB834
2021-07-29-21-40-11-EEC674779313A3F2
2021-07-29-21-42-07-1D23B1A33792AC36

S3 log files are written periodically; in practice, this can be several times a minute, each generating a unique file name, but only when there is activity to capture.

Display the contents of the first file in the log file set, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ cat 2021-07-29-14-12-58-9643D3A6992B04CB
701a23465480cca98d94a2f326ad22a9c26fec7b7a9c17ee8e10e8d50a91878e falsimentis-eng [29/Jul/2021:13:09:55 +0000] 3.238.12.183 arn:aws:iam::342082656213:user/jmerckle T7X3D7QX7X6GZ0NN REST.GET.BUCKET - "GET /?list-type=2&prefix=&delimiter=%2F&encoding-type=url HTTP/1.1" 200 - 7983 - 37 36 "-" "aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.ls" - nWH0+ldF4vxbvpaMka7kLbRAFPVRP/QL9KfZwUP/lfVT12TExikGmfIKLT3Aac13Pyr+1ww+GaA= SigV4 ECDHE-RSA-AES128-GCM-SHA256 AuthHeader falsimentis-eng.s3.us-west-1.amazonaws.com TLSv1.2 -

S3 log files follow the convention used by many Unix systems where each log entry is one line in an ASCII file, using empty space to delimit each field. This system is imperfect, since some fields use empty space within a field (such as the date and the user agent). The data elements captured in the AWS log file are, in order:

    Bucket Owner
    Bucket
    Time
    Remote IP
    Requester
    Request ID
    Operation
    Key
    Request-URI
    HTTP status
    Error Code
    Bytes Sent
    Object Size
    Total Time
    Turn-Around Time
    Referer
    User-Agent
    Version Id
    Host Id
    Signature Version
    Cipher Suite
    Authentication Type
    Host Header
    TLS version

    Additional information on each of these fields is available in the AWS guide Amazon S3 server access log format. 

S3 Bucket Log Analysis: S3Logparse

Parsing S3 log bucket data using Awk can be difficult. An alternative is to use an open source tool to summarize the data, such as S3Logparse.

S3Logparse reads from one or more S3 log files and captures basic statistics from the data. Run the s3logparse script from the command prompt with no arguments, as shown here.

ec504@slingshot:~/labs/awslogs/s3-eng$ s3logparse
s3logparse.py: Extract useful information from AWS S3 logs.
Usage: /usr/local/bin/s3logparse [useragent|toptalkers|topuploaders|topdownloaders|topfiles] <log files>

To use S3Logparse, specify a function (one of useragent, toptalkers, etc.), followed by one or more log files. Start with the useragent function, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ s3logparse useragent *
38 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.cp
38 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.sync
19 - S3Console/0.4, aws-internal/3 aws-sdk-java/1.11.1002 Linux/5.4.129-72.229.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.282-b08 java/1.8.0_282 vendor/Oracle_Corporation cfg/retry-mode/legacy
18 - S3Console/0.4, aws-internal/3 aws-sdk-java/1.11.1002 Linux/5.4.122-66.218.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.282-b08 java/1.8.0_282 vendor/Oracle_Corporation cfg/retry-mode/legacy
2 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.ls
2 - Boto3/1.18.8 Python/3.7.10 Linux/4.14.238-182.422.amzn2.x86_64 Botocore/1.21.8 Resource
1 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3api.get-bucket-versioning
1 - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36

Like conventional web server logs, the S3 logs capture the user agent of the client interacting with the S3 resource. Here we see several useful pieces of information about the users interacting with the S3 storage resource, including the bucket access tool (AWS command line tool, AWS web console, Boto3 (a Python client for interacting with S3 resources) and Chrome.

None of these user agents necessarily indicates an attack, but if there are unusual user agents, they may warrant further investigation. For example, if all of your S3 access is through AWS CLI, but you see several entries for Boto3 scripts, you could investigate those requests in more detail.

Next, use the toptalkers function to identify all of the unique IP endpoints interacting with the S3 logging data, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ s3logparse toptalkers *
6.16 MiB - 3.238.12.183
34.56 KiB - 96.253.26.224

    The Falsimentis team informs you that 96.253.26.224 is the endpoint used by Irvine Obbard, an AWS administrator. 

Fortunately for us as analysts, there are only two unique IP endpoints accessing the S3 bucket. Of these IP addresses, the 96.253.26.224 IP address is used by Falsimentis executive Irvine Obbard as an AWS administrator. While there is the possibility that the attack could originate from Obbard's system under the control of an attacker, we'll continue our investigation by looking at the activity from the unknown IP address.

We can update our timeline information by adding a knowledge bin, calling out the suspected IP address, as shown here.

Timeline updated to denote suspicious IP address
Extract S3 Records: Suspicious IP Address

Use the grep utility to create a single file that contains all of activity from the unknown IP address, excluding the file name information with the -h argument, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ grep -h 3.238.12.183 * > s3-eng-unknown-ip
sec504@slingshot:~/labs/awslogs/s3-eng$

    Without the -h argument, grep will prepend the file name then the matching line, separated by a colon. The original file name isn't necessary for our analysis, so we omit it here. 

Next, repeat the query using s3logparse to examine user agent information, focusing on the new s3-eng-unknown-ip log file, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ s3logparse useragent s3-eng-unknown-ip
38 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.cp
38 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.sync
2 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.ls
2 - Boto3/1.18.8 Python/3.7.10 Linux/4.14.238-182.422.amzn2.x86_64 Botocore/1.21.8 Resource
1 - aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3api.get-bucket-versioning

Here we see similar output, but the S3Console user agent is missing, attributed to Obbard's administrative use and not the activity of the attacker.
Examine File Interaction

Next, use s3logparse to identify the file access from the unknown IP address, as shown here:

sec504@slingshot:~/labs/awslogs/s3-eng$ s3logparse topfiles s3-eng-unknown-ip
4 - gse_multipart10686.jpg
3 - PHOTOS
2 - gse_multipart67095.jpg
2 - gse_multipart46332.jpg
2 - gse_multipart67068.jpg
2 - gse_multipart67118.jpg
...
1 - gse_multipart67065.jpg.gpg
1 - gse_multipart52142.jpg.gpg
1 - README-RANSOM.txt
1 - gse_multipart67112.jpg.gpg

In this output we can confirm that the source IP address 3.238.12.183 is also the endpoint that interacted with the encrypted .jpg.gpg files, and uploaded the ransom note. We can extract the date and timestamp information from the log file for the first file access, and the first encrypted file access, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ head -1 s3-eng-unknown-ip
701a23465480cca98d94a2f326ad22a9c26fec7b7a9c17ee8e10e8d50a91878e falsimentis-eng [29/Jul/2021:13:09:55 +0000] 3.238.12.183 arn:aws:iam::342082656213:user/jmerckle T7X3D7QX7X6GZ0NN REST.GET.BUCKET - "GET /?list-type=2&prefix=&delimiter=%2F&encoding-type=url HTTP/1.1" 200 - 7983 - 37 36 "-" "aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.ls" - nWH0+ldF4vxbvpaMka7kLbRAFPVRP/QL9KfZwUP/lfVT12TExikGmfIKLT3Aac13Pyr+1ww+GaA= SigV4 ECDHE-RSA-AES128-GCM-SHA256 AuthHeader falsimentis-eng.s3.us-west-1.amazonaws.com TLSv1.2 -
sec504@slingshot:~/labs/awslogs/s3-eng$ head -1 s3-eng-unknown-ip | cut -d" " -f 3-4
[29/Jul/2021:13:09:55 +0000]
sec504@slingshot:~/labs/awslogs/s3-eng$ grep jpg.gpg s3-eng-unknown-ip | head -1 | cut -d " " -f 3-4
[29/Jul/2021:19:59:35 +0000]

In the first command, we use head to look at the first line in the extracted list of S3 events for the attacker IP address. This presents us with a lot of information, so we repeat the command, piping the results through cut using a space as a delimiter -d" " and extracting fields 3-4, retrieving the date and time information. We repeat this command a second time, extracting the first access for a file ending in jpg.gpg. We can use this information to update our timeline, as shown here.

Timeline updated to add files accessed and encrypted files observed
Enumerate File Actions

Next, let's look at the actions the attacker applied to files in the falsimentis-eng bucket. The pertinent fields are columns 8 and 9, along with the timestamp in fields 3 and 4. Request these four fields with awk as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ awk '{print $3, $4, $8, $9}' s3-eng-unknown-ip
[29/Jul/2021:13:09:55 +0000] REST.GET.BUCKET -
[29/Jul/2021:13:10:29 +0000] REST.GET.BUCKET -
[29/Jul/2021:13:10:06 +0000] REST.HEAD.OBJECT gse_multipart10686.jpg
[29/Jul/2021:13:10:30 +0000] REST.GET.OBJECT gse_multipart67095.jpg
[29/Jul/2021:13:10:30 +0000] REST.GET.OBJECT gse_multipart46332.jpg
...
[29/Jul/2021:14:03:06 +0000] BATCH.DELETE.OBJECT gse_multipart10686.jpg
[29/Jul/2021:14:03:06 +0000] BATCH.DELETE.OBJECT gse_multipart10687.jpg
[29/Jul/2021:14:03:06 +0000] BATCH.DELETE.OBJECT gse_multipart12012.jpg
[29/Jul/2021:14:03:06 +0000] BATCH.DELETE.OBJECT gse_multipart22198.jpg
...
[29/Jul/2021:14:03:06 +0000] REST.GET.BUCKETVERSIONS -
[29/Jul/2021:14:03:43 +0000] REST.GET.BUCKET -
[29/Jul/2021:14:01:48 +0000] REST.GET.VERSIONING -
[29/Jul/2021:14:04:46 +0000] REST.GET.BUCKET -
...
[29/Jul/2021:19:59:36 +0000] REST.PUT.OBJECT gse_multipart67096.jpg.gpg
[29/Jul/2021:19:59:35 +0000] REST.PUT.OBJECT gse_multipart67065.jpg.gpg
[29/Jul/2021:19:59:35 +0000] REST.PUT.OBJECT gse_multipart52142.jpg.gpg
[29/Jul/2021:19:59:36 +0000] REST.PUT.OBJECT README-RANSOM.txt
[29/Jul/2021:19:59:36 +0000] REST.PUT.OBJECT gse_multipart67112.jpg.gpg

This awk command extracts the S3 operation and key (usually the bucket file name or directory) used. Examining this output we see that initial request REST.GET.BUCKET is used (identifying the bucket, possibly the result of aws s3 ls), followed by a HEAD request (testing the server response before requesting the file) and several GET requests (possibly the result of aws s3 cp s3://falsimentis-eng/* /tmp).

Reviewing this output we see a typical story of ransomware in an S3 bucket: enumerate the bucket, download the files locally, delete the files, check for S3 versioning (where prior versions of the data can be restored after deletion), then upload encrypted copies of the files and a ransom notice.
Enumerate User Actions

To finish our assessment of the S3 bucket compromise, we can identify the user associated with the bucket activity by extracting column 6 from the log data. Use the awk command shown here to uniquely identify the number of captured actions by user.

sec504@slingshot:~/labs/awslogs/s3-eng$ awk '{print $6}' s3-eng-unknown-ip | sort | uniq -c
    116 arn:aws:iam::342082656213:user/jmerckle

The log results indicate that all of the requests observed from the suspicious source IP address are requested with the jmerckle account.

    The Falsimentis team informs you that John Merckle is a supervisor for the Falsimentis service desk. 

We don't yet know if these activities were the result of malicious insider actions, or a compromised AWS account, but we can collect and review additional supporting information by reviewing the CloudTrail logs supplied by Falsimentis. We can also add additional information to our timeline, as shown here.

Timeline updated to add files deleted, username, encrypted files uploaded
AWS CloudTrail Log Data

At this point in the investigation we know that the attacker gained access to the S3 service using the jmerckle account credentials, and replaced files with an encrypted version, adding a ransom note to the bucket. We don't yet know if the jmerckle account is compromised or is the activity of a malicious insider, and if there are any other actions taken against the cloud infrastructure.

Fortunately, Falsimentis has also supplied CloudTrail logs for our analysis. Change to the ~/labs/awslogs/CloudTrail directory and list the file contents, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ cd ~/labs/awslogs/CloudTrail/
sec504@slingshot:~/labs/awslogs/CloudTrail$ ls
ap-northeast-1  ap-southeast-2  eu-west-1  us-east-1  us-west-2
ap-northeast-2  ca-central-1    eu-west-2  us-east-2
ap-southeast-1  eu-central-1    eu-west-3  us-west-1

In the top-level CloudTrail directory we see several directories for different AWS regions. CloudTrail organizes activity by region, and it is entirely possible that an attacker can perform actions outside of the regions typically used by the organization. For this exercise, we'll focus on the us-west-1 region. Change to the us-west-1 directory and list files, as shown here.

sec504@slingshot:~/labs/awslogs/CloudTrail$ cd us-west-1/
sec504@slingshot:~/labs/awslogs/CloudTrail/us-west-1$ ls
2021

CloudTrail files are often organized with multiple subdirectories for the year, month, and day. Change to the 2021/07/29 directory, matching the date for adversary S3 activity, as shown here.

sec504@slingshot:~/labs/awslogs/CloudTrail/us-west-1$ cd 2021/07/29/
sec504@slingshot:~/labs/awslogs/CloudTrail/us-west-1/2021/07/29$ ls
342082656213_CloudTrail_us-west-1_20210729T0010Z_r9OymZ19CvpzcyvG.json.gz
342082656213_CloudTrail_us-west-1_20210729T0015Z_7PyeLLPrf8oXIb3z.json.gz
342082656213_CloudTrail_us-west-1_20210729T0015Z_DuJkfENqNokVX8to.json.gz
342082656213_CloudTrail_us-west-1_20210729T0020Z_hoCpNG2hYJM6DURl.json.gz
...
342082656213_CloudTrail_us-west-1_20210729T2355Z_Qr8foJTpXVGV0Rep.json.gz
342082656213_CloudTrail_us-west-1_20210729T2355Z_ZfiiRC0kNC9QM7Sw.json.gz

Unlike the S3 logs, CloudTrail logs are gzip-compressed JSON files. We can create summary reports of the events captured in these log files using ctsummarize.
AWS CloudTrail Summarization with ctsummarize

The ctsummarize tool parses CloudTrail logs and creates several output summaries of the data, filtering the logs by a specific IP address. Written for incident responders to use when reviewing CloudTrail logs, it accelerates our ability to grasp attacker events and pertinent details following an AWS attack.

From the terminal, change to your home directory by running cd with no arguments, as shown here.

sec504@slingshot:~/labs/awslogs/s3-eng$ cd
sec504@slingshot:~$

Next, run ctsummarize with no arguments, as shown here.

sec504@slingshot:~$ ctsummarize
ctsummarize: create multiple output files from CloudTrail activity for analysis
Usage: /usr/local/bin/ctsummarize [ipaddress] 

Ctsummarize requires a target IP address and one or more compressed CloudTrail log files for analysis. Create the ctsummarize reports by specifying the attacker IP address (3.238.12.183) and the path to the CloudTrail logs on 2021-07-29 with a wildcard to include all Gzip compressed files, as shown here.

sec504@slingshot:~$ ctsummarize 3.238.12.183 labs/awslogs/CloudTrail/us-west-1/2021/07/29/*z
ctsummarize: create multiple output files from CloudTrail activity for analysis
Creating analysis extracts using attacker IP  from CloudTrail files.

Next, run ls to list the files in the current directory. Note the introduction of the ctsummarize files, as shown here.

sec504@slingshot:~$ ls
accesskeys.txt  Desktop  eventsummary.csv  eventsummary.txt  labs  useragent.txt  wiki  writeevents.json

AWS CloudTrail ctsummarize: User Agent Analysis

First, let's look at the ctsummarize output file useragent.txt. Display the contents of the file with cat, as shown here.

sec504@slingshot:~$ cat useragent.txt
      3 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/ec2.describe-instances
      1 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/iam.create-access-key
      4 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/iam.list-roles
      1 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/iam.list-user-policies
      5 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/iam.list-users
      1 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/lambda.list-functions
      1 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/logs.describe-log-groups
      1 [aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3api.get-bucket-versioning]
      2 [aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/s3.ls]
      3 aws-cli/2.2.23 Python/3.8.8 Linux/4.14.238-182.422.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off command/sts.get-caller-identity
     15 Boto3/1.18.1 Python/3.9.5 Linux/4.14.238-182.422.amzn2.x86_64 Botocore/1.21.1

Like S3 logging data, CloudTrail captures a user agent for each request, identifying the tool used by the attacker to interact with the AWS APIs. Like normal user agents, this value can be spoofed, so it should not be relied upon exclusively for analysis, but can provide valuable insight into the attacker activities.

In the useragent.txt file, we see several user agents with a count for frequency of the observed user agent. The majority of the entries are for the AWS CLI tool, the standard utility published by Amazon for interacting with AWS APIs from the command line. From this output we can gather several useful pieces of insight about the attacker:

    aws-cli/2.2.23: The attacker is using AWS CLI version 2.2.23
    Python/3.8.8: The Python interpreter used with AWS CLI is version 3.8.8
    Linux/4.14.238-182.422.amzn2.x86_64: The attacker is using a Linux platform with kernel version 4.14.238-182.422; note that the end of the kernel string indicates a custom kernel version string, revealing that the attack platform is an Amazon EC2 Linux 2 system (amzn2)
    prompt/off: The attacker is using AWS CLI is non-prompting mode (requiring arguments to be specified on the command line; the default use case)

Note that the majority of the user agent information for AWS CLI commands the same, except for the end of the user agent. The end of the AWS CLI user agent indicates the AWS CLI command and subcommand (e.g., aws ec2 describe-instances). Seeing this information we get a good idea of the commands that the attacker run against the target system, but only for AWS CLI client activity.

The final entry in the useragent.txt file is for Boto3, the Python library for interacting with AWS APIs. We can see version information here, but Boto3 does not disclose which commands were run by the attacker. For that information, we need to refer to the ctsummarize eventsummary.txt file.

    The use of Boto3 by the attacker may indicate the use of scripted and/or automated attack tools. We'll examine several of these tools as we continue the course and investigate cloud attack tools and techniques. 

AWS CloudTrail ctsummarize: Event Summary

Next, display the ctsummarize eventsummary.txt file, as shown here.

sec504@slingshot:~$ cat eventsummary.txt
EventTime UserName AccessKeyId EventName "UserAgent" "ErrorMessage"
2021-07-29T13:02:53Z jmerckle AKIAU7JNXC7K7XNL3F6J GetCallerIdentity "aws-cli/2.2.23 Pytho" "null"
2021-07-29T13:03:25Z jmerckle AKIAU7JNXC7K7XNL3F6J ListBuckets "[aws-cli/2.2.23 Pyth" "Access Denied"
2021-07-29T13:03:31Z jmerckle AKIAU7JNXC7K7XNL3F6J DescribeInstances "aws-cli/2.2.23 Pytho" "You are not authorized to perform this operation."
2021-07-29T13:03:37Z jmerckle AKIAU7JNXC7K7XNL3F6J ListFunctions20150331 "aws-cli/2.2.23 Pytho" "User: arn:aws:iam::342082656213:user/jmerckle is not authorized to perform: lambda:ListFunctions on resource: *"
2021-07-29T13:03:42Z jmerckle AKIAU7JNXC7K7XNL3F6J ListRoles "aws-cli/2.2.23 Pytho" "null"
2021-07-29T13:04:13Z jmerckle AKIAU7JNXC7K7XNL3F6J ListUsers "aws-cli/2.2.23 Pytho" "null"
2021-07-29T13:04:25Z jmerckle AKIAU7JNXC7K7XNL3F6J ListUsers "aws-cli/2.2.23 Pytho" "null"
2021-07-29T13:04:40Z jmerckle AKIAU7JNXC7K7XNL3F6J ListRoles "aws-cli/2.2.23 Pytho" "null"
2021-07-29T13:04:50Z jmerckle AKIAU7JNXC7K7XNL3F6J ListRoles "aws-cli/2.2.23 Pytho" "null"
2021-07-29T13:04:57Z jmerckle AKIAU7JNXC7K7XNL3F6J DescribeLogGroups "aws-cli/2.2.23 Pytho" "User: arn:aws:iam::342082656213:user/jmerckle is not authorized to perform: logs:DescribeLogGroups on resource: arn:aws:logs:us-west-1:342082656213:log-group::log-stream:"
2021-07-29T13:06:30Z jmerckle AKIAU7JNXC7K7XNL3F6J GetCallerIdentity "Boto3/1.18.1 Python/" "null"
2021-07-29T13:06:31Z jmerckle AKIAU7JNXC7K7XNL3F6J GetPolicy "Boto3/1.18.1 Python/" "null"
...

Unlike the user agent summary, the ctsummarize event summary preserves each unique event with a timestamp, extracting the following fields from the CloudTrail logging data:

    Event Time: The date and time for the event in UTC (Zulu time)
    User Name: The user name associated with the event
    Access Key Id: The access key used to request the event
    Event Name: The event name (API function)
    User Agent: The user agent, truncated to 20 characters
    Error Message: The error message, if present (indicating the command failed), or null if successful

    Knowledge of the cloud provider API functions is essential when performing cloud incident response. It is useful to spend some time becoming familiar with your cloud provider's functionality by reading the documentation provided. 

This information gives us the ability to further update our timeline information, as shown here.

Timeline updated to add API event detail
AWS CloudTrail ctsummarize: Write Events

While read-only access to the cloud environment can be devastating for an organization, we are also interested in write events (for AWS, those beginning with Put or Create). Ctsummarize creates an extract of the CloudTrail logging information to capture these events in an output file called writeevents.json. As a JSON file, we can display the contents using cat, or get a pretty-printed format of the data from the JQ utility.

Display the contents of the writeevents.json file, piping the output to jq, as shown here.

sec504@slingshot:~$ cat writeevents.json | jq
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDAU7JNXC7KTE2ELED2M",
    "arn": "arn:aws:iam::342082656213:user/jmerckle",
    "accountId": "342082656213",
    "accessKeyId": "AKIAU7JNXC7K7XNL3F6J",
    "userName": "jmerckle"
  },
  "eventTime": "2021-07-29T13:06:49Z",
  "eventSource": "iam.amazonaws.com",
  "eventName": "PutUserPolicy",
  "awsRegion": "us-east-1",
...

JQ can be a complex tool, but it offers us tremendous flexibility in parsing JSON data. We'll continue to leverage JQ in many of our later class material.

    You will have the chance to build your skill in reading and parsing JSON data in the Linux bootcamp at the end of our book 1 content. 

In the JSON output we see the full CloudTrail data with two records. Press the up arrow to repeat the JQ command, this time adding a short program to retrieve the event name information, as shown here.

sec504@slingshot:~$ cat writeevents.json | jq '.eventName'
"PutUserPolicy"
"CreateAccessKey"

When working with JSON data in JQ, field names are indicated with a leading .. In this output we see the two write events captured: PutUserPolicy (used to escalate privileges) and CreateAccessKey (to establish a secondary, persistent access mechanism to the jmerckle account).

Let's examine the data associated with the PutUserPolicy event in more detail. Press the up arrow again to re-run the JQ command, this time changing the program to display only records where the event name is PutUserPolicy, retrieving the policy name and policy document content. Add the -r argument to the JQ command to display the output in raw form (without quotation marks), as shown here.

sec504@slingshot:~$ cat writeevents.json | jq -r 'select(.eventName=="PutUserPolicy") | .requestParameters | .policyName, .policyDocument'
zlj9i0k83o
{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Action": "*","Resource": "*"}]}

This command breaks down as follows:

    cat writeevents.json |: Display the contents of the writeevents.json file, sending the results to a shell pipeline
    jq -r: Run JQ in raw mode, receiving the JSON data from the shell pipeline
    ': Start a JQ program in quotes
    select(.eventName=="PutUserPolicy") |: Apply a filter with JQ, retrieving records where the event name is PutUserPolicy, sending the results to a JQ pipeline
    .requestParameters |: Retrieve the JSON object requestParameters, sending just this object to another pipeline
    .policyName, .policyDocument: Retrieve the policy name and policy document fields
    ': End the JQ program

In this output we see the policy name on the first line (zlj9i0k83o), possibly a random string generated by the attacker's Boto3 script. The second line displays the contents of the policy created, granting the attacker every privilege ("Action":"*") for all AWS resources ("Resource": "*").

Using this additional information, we can expand our attack flow diagram to capture the persistence and post-exploitation steps, as shown here.

Vertical illustration of major attack steps organized by time and category

We can also finish our timeline information, as shown here.

Completed event timeline
Cleanup

Remove the temporary files generated by ctsummarize, as shown here.

sec504@slingshot:~$ ls
accesskeys.txt  Desktop  eventsummary.csv  eventsummary.txt  labs  useragent.txt  wiki  writeevents.json
sec504@slingshot:~$ rm accesskeys.txt eventsummary.* useragent.txt writeevents.json
sec504@slingshot:~$

Why This Lab Is Important

In this lab we looked at the process of conducting incident response for cloud-based assets. The investigation used information reported by Falsimentis users (the presence of ransom indicators) and logging information from AWS, specifically S3 logs and CloudTrail logs.

During the investigation we made use of open source tools including s3logparse and ctsummarize to give us insight into the logging data, as well as manual analysis to parse specific details. Using this information we can illustrate the attack and build a timeline of events to convey the tactics of the attacker and to use when moving on to the recovery phase of the engagement.