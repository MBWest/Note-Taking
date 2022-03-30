# Bonus - Masscan Rate Experimentation

Re-run the Masscan scan, adjusting the rate to higher values (such as --rate 100000 or higher). Repeat each scan multiple times. What is the maximum rate your system can accommodate to get reliably consistent results from Masscan? (This value will vary from system to system.)
Falsimentis Host Assessment

Visit the newly identified Falsimentis target system at https://10.200.74.2. We know this server is ostensibly named downloads.falsimentis.com from the certificate information, even though it is not present in DNS records. Spend a few minutes evaluating the server and answer several questions.

## Question: What is the hidden directory specified in the robots exclusion file?

### Click to See Hint

The robots exclusion file is robots.txt, available in the root of the web server. You can download this file to examine the contents using Firefox, or at the command line using wget or curl (with the -k option), as shown here.

    sec504@slingshot:~$ curl -k https://10.200.74.2/robots.txt

### Click to See Answer

    sec504@slingshot:~$ curl -k https://10.200.74.2/robots.txt
    # Don't allow search engine crawlers to discover hidden directory
    User-Agent: *
    Disallow: /918cd9e790b13972faa1034157a11982

**Answer**: The directory named 918cd9e790b13972faa1034157a11982 is hidden from search engine robots in the robots exclusion file.

## Question: What file is disclosed in the Falsimentis download server in the hidden directory?

### Click to See Hint

We know that the robots exclusion file is designed to prevent search engines from crawling the web server for the designated directory. Browse to that directory using Firefox or curl to see the contents of that directory.

### Click to See Answer

The robots.txt file identified the directory 918cd9e790b13972faa1034157a11982 on the web server, as shown here:

    sec504@slingshot:~$ curl -k https://10.200.74.2/robots.txt
    # Don't allow search engine crawlers to discover hidden directory
    User-Agent: *
    Disallow: /918cd9e790b13972faa1034157a11982

Since we know the site is trying to prevent web crawlers from accessing this directory, this directory might have interesting content. Request the contents of the directory to see the file list using Firefox or curl, as shown here (note that a trailing / at the end of the URL is required to obtain the directory contents).

    sec504@slingshot:~$ curl -k https://10.200.74.2/918cd9e790b13972faa1034157a11982
    <head><title>301 Moved Permanently</title></head>
    <body>
    <center><h1>301 Moved Permanently</h1></center>
    <hr><center>nginx/1.18.0</center>
    </body>
    </html>
    sec504@slingshot:~$ curl -k https://10.200.74.2/918cd9e790b13972faa1034157a11982/
    <html>
    <head><title>Index of /918cd9e790b13972faa1034157a11982/</title></head>
    <body>
    <h1>Index of /918cd9e790b13972faa1034157a11982/</h1><hr><pre><a href="../">../</a>
    <a href="Falsimentis%20Board%20Meeting%20Minutes%204Q.docx">Falsimentis Board Meeting Minutes 4Q.docx</a>          18-Apr-2021 13:14               32476
    <a href="Falsimentis%20Board%20Meeting%20Minutes%204Q.pdf">Falsimentis Board Meeting Minutes 4Q.pdf</a>           18-Apr-2021 13:14               28874
    </pre><hr></body>
    </html>

**Answer**: Two files are disclosed in the Falsimentis download server in the hidden directory: Falsimentis Board Meeting Minutes for Q4.pdf and Falsimentis Board Meeting Minutes for Q4.docx

## Question: Download the identified files. Use the Metadata in the files to identify the author, editor, application used to compose the document, and document producer.

### Click to See Hint

Use Firefox to download the two files from the Falsimentis download server hidden directory. You may optionally wish to examine the document content by opening the PDF using Firefox.

From a terminal, change to the Downloads directory. Examine the metadata associated with both the PDF and DOCX files using exiftool.

### Click to See Answer

After downloading the files, change to the Downloads directory and use exiftool to examine the document metadata, as shown here.

    sec504@slingshot:~$ cd Downloads/
    sec504@slingshot:~/Downloads$ ls
    'Falsimentis Board Meeting Minutes 4Q.docx'
    'Falsimentis Board Meeting Minutes 4Q.pdf'
    sec504@slingshot:~/Downloads$ exiftool *.docx *.pdf
    ======== Falsimentis Board Meeting Minutes 4Q.docx
    ExifTool Version Number         : 10.80
    File Name                       : Falsimentis Board Meeting Minutes 4Q.docx
    Directory                       : .
    ...
        2 image files read

Inspect the output from exiftool to identify the author, editor, application, and document producer. Optionally you can use grep to match these fields in the output of exiftool, as shown here.

    sec504@slingshot:~/Downloads$ exiftool *.docx *.pdf | grep -i -E "author|editor|application|producer"
    MIME Type                       : application/vnd.openxmlformats-officedocument.wordprocessingml.document
    Application                     : Microsoft Office Word
    Editor                          : Roseann Bycraft
    MIME Type                       : application/pdf
    Producer                        : macOS Version 11.2.3 (Build 20D91) Quartz PDFContext
    Author                          : Florina Schleicher

The grep command line can be broken down into the following components:

- **-i** - Perform case-insensitive matching
- **-E** - Treat the search term as a regular expression (regex)
- **"author|editor|application|producer"** - Match any lines matching the regular expression where | denotes an or condition (display lines containing any of the specified strings)

**Answer**: Florina Schieicher (author), Roseann/Rose Bycraft (editor), Microsoft Office word (application used to compose the document), macOS 11.2.3 (document producer).
