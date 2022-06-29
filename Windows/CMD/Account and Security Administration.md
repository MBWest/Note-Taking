# Account and Security Administration

| **Command** | **Description** |
|----------|-----------------|
| **Net**| 
| `Net` | Manages network shares, print jobs, and users |
| `-Accounts` | Set password and logon requirements for users |
| `-Computer` | Add or remove a computer from a domain |
| `-Config` | Show information about the configuration of the Server or Workstation service |
| `-Group` | Add, delete, and manage global groups on servers |
| `-Start` | Start a network service or list running network services |
| `-Stop` | Stop command is used to stop a network service |
| `-User` | Add, delete, and otherwise manage the users on a computer |
| **Examples** |  |
| `Net user TestUser /add` | Add a new user, "TestUser", with a blank password |
| `Net user TestUser pw /add` | Add a new user, "TestUser", with "pw" as their password |
| `Net user TestUser * /add` | Add a new user, "TestUser", and be prompted for a password |
| `Net user TestUser /delete` | Remove the "TestUser" account |
| `Net user TestUser /disable` | Disable the "TestUser" account |
| `Net user Student.dmn.adm Tr@!n3d2D3f3nd /domain` | Changes the domain account "Student.dmn.admn" password to Tr@!n3d2D3f3nd |
|` Net localgroup` | List the local group |
| `Net localgroup testgroup /add` | Add domain group "TestGroup" |
| `Net localgroup testgroup` | Display information about "TestGroup" |
| `Net localgroup testgroup testuser /as` | Adds "TestUser" to the "TestGroup" Group |
| `Net accounts` | Get User Account Policy |
| `Net accounts minpwlen:0 /maxpwage:90 /uniquepw:10` | Change the account policy to 0 password length, 90 days, 10  saved |
| `Net share` | Display all shared folders |
| `Net share C$ /users:2` | Only two users can use this share |
| `Net share IPC$ /unlimited` | An unlimited amount of users can use this share |
| `Net share C$ /delete` | Stop sharing this resource |
| `Net share "ShareName"` | Show details of Share |
| `Net share Excercise3a$=C:\Exercise3a /remark:"Exercise for Studets" /Users:5` | Share out the Exercise3a folder limiting connections to 5 and remark the Exercise for students and a share name of Exercise3a$ |
| `Net use` | Display all shared folders on a network net use |
| `Net use X: \\DC01\C$` | Mount DC01's C$ share to the X drive |
| `Net use X: /delete` | Stop using this resource |
