# Windows Command Interpreter - Alternate Data Streams (ADS)

> ### **Viewing the presence of an ADS using Command Line**
- dir /a /r c:\path\to\file\with\ads

```
C:\>dir /a /r C:\Users\Public\Desktop
Directory of C:\Users\Public\Desktop

03/01/2019  07:37    <DIR>		.
03/01/2019  07:37    <DIR>		..
03/18/2017  15:01     		174	desktop.ini
03/01/2019  07:37	 <DIR>		Folder1
02/26/2019  14:26	        24	test.txt
02/26/2019  14:27           23	test.txt:NameOfADS:$DATA
```

---

> ### **Viewing the contents of an ADS using Command Line**
- more < C:\Path\of\FileWithADS>

```
C:\>more < C:\Users\Public\Desktop\test.txt:NameOfADS
DataPutIntoAnADS
```

---

> ### **Appending content to an ADS using Command Line**
- echo “Here is my appended data” >> C:\Path\of\FileWithADS:NameOfADS

```
C:\>echo “Here is my appended data” >> C:\Users\Public\Desktop\test.txt:NameOfADS

C:\more < C:\Users\Public\Desktop\test.txt:NameOfADS
DataPutIntoAnotherADS
“Here is my appended data”
```