### How to Password-Protect a ZIP File

**This topic will cover how to password-protect a ZIP file in Kali Linux. This isn’t a secure method of protecting information, but you will need to know how to do it in order to fully understand and complete the ZIP cracking section of this course.**

![image](https://user-images.githubusercontent.com/87195021/125537629-9cfcdc1e-333a-4507-9808-e4952e0c8706.png)

Firstly, make sure you have the ZIP tool installed, and fully up-to-date. You can use the command `sudo apt-get install zip`

In the first example we will compress a text file name **text**.**txt** into a password-protected ZIP file named **Protected**.**zip**, with the password **password123**. The command I\'m using is `zip --encrypt Protected.zip text.txt.`

- **zip** – Selects the tool we want to use
- **–encrypt** – Selections the function of the tool we want to use. ‘Encrypt’ will encrypt our ZIP archive and require a password to decrypt the contents.
- **Protected.zip** – The name of the outputted ZIP file.
- **text.txt** – The file we want to compress.

![image](https://user-images.githubusercontent.com/87195021/125537751-3a3b8d4f-f483-40a3-87ae-76dd08832274.png)

Now when we try to unzip the ZIP archive, it’ll ask us for the password. If we enter it in correctly, it will extract the compressed file(s).

![image](https://user-images.githubusercontent.com/87195021/125537769-3a3c4ded-adc4-41d5-a9a5-968bf33328c9.png)

As you’ll see in the next section, these passwords can easily be attacked, allowing us to access the protected contents.

