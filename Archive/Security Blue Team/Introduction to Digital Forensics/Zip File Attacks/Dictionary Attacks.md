# Dictionary Attacks

Now let\'s get on to how to conduct a dictionary attack against a passworded ZIP file! We\'ll be using fcrackzip again, so we will open a terminal in the same location as our target ZIP. In this example, our target ZIP is **DictionaryAttack.zip** with the password **ummwhateva**. Here\'s the command we’ll be using.

- **fcrackzip** – Selecting the tool we want to use.
- **-D** – Selecting the option for a dictionary attack.
- **-u** – This makes sure fcrackzip actually tries to unzip the file, without this we won\'t actually get the right password.
- **-p** – Use strings as password.
- **/usr/share/wordlists/rockyou.txt** – This is the location of our wordlist, required to perform a dictionary attack.
- **DictionaryAttack.zip** – The file we want to crack.

![image](https://user-images.githubusercontent.com/87195021/125538278-e5db3c46-25a2-4038-976c-0135eac48ba4.png)

After a few seconds, fcrackzip tells us that it has found the correct password, and we can now successfully extract the contents of the file.

![image](https://user-images.githubusercontent.com/87195021/125538285-8de76a5b-b0b9-49f5-88ba-df0b996fe778.png)

![image](https://user-images.githubusercontent.com/87195021/125538312-2c1d51eb-2019-4cd0-9cba-9e559a751329.png)

Here\'s a cheat sheet with all of the potential options that can be used with fcrackzip: http://manpages.ubuntu.com/manpages/trusty/man1/fcrackzip.1.html