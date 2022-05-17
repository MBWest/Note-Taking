# Brute-Forcing Attacks

Let\'s try our own dictionary attack, to do this we’re going to need the tool **fcrackzip**. You can check if you have the tool installed by using fcrackzip, if not you can install it using `sudo apt-get install fcrackzip`.

![image](https://user-images.githubusercontent.com/87195021/125537955-4532254d-3fb8-4845-9aa8-22d28163cdaa.png)

The command in the screenshot below might look scary at first, but we\'ll talk you through exactly what is happening. In this example, our target ZIP is **BruteForceAttack.zip** with a password of **a1bc**.

- **fcrackzip** – Selecting the tool we want to use.
- **-b** – Selecting the option for a brute-force attack.
- **BruteForceAttack.zip** – The file we want to brute-force.
- **-u** – This makes sure fcrackzip actually tries to unzip the file, without this we won\'t actually get the right password.
- **-c** – This is where we pick the characters we want to use in our dictionary attack. In this example we’re using \'a\' which represents lowercase letters, and \'1\' which represents numbers 0-9.
- **-l** – This is where we state the length of the password we want to crack. If we know the password is between 4 and 6 characters, we would use \"-l 4-6".

![image](https://user-images.githubusercontent.com/87195021/125538051-7f860a35-85f8-4a23-8261-a2ffe028cff1.png)

After a few seconds we can see that fcrackzip has identified the correct password **a1b2** and we\'re now able to successfully extract the contents of the password-protected ZIP file!

![image](https://user-images.githubusercontent.com/87195021/125538071-2a62762f-9714-4e4e-b5ef-df0c838e8968.png)

Here\'s a cheat sheet with all of the potential options that can be used with fcrackzip: http://manpages.ubuntu.com/manpages/trusty/man1/fcrackzip.1.html