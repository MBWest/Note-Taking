### Steghide (Hiding & Retrieval)

When using Steghide, we will always have a cover document, and our secret document. Below are the file types we can use (note that Cover Documents can only be images or audio files due to their file structure).

![image](https://user-images.githubusercontent.com/87195021/125534258-ba41f040-c184-42ff-9120-6cd37a43a02d.png)

In this example, we\'re going to be using our cover document **laptop.jpg** and our secret document, a .ZIP archive named **secret.ZIP** which contains a text file called **1.txt**.

![image](https://user-images.githubusercontent.com/87195021/125534296-213f807e-c311-454a-a248-18babb71cddb.png)

Let’s start off by zipping the **/secret/** directory that contains **1.txt**. In the terminal, type the command `zip -r secret.zip secret`, this command will compress everything inside **secret** and output it to a file named **secret.zip.**

![image](https://user-images.githubusercontent.com/87195021/125534387-90582e99-38db-434c-be26-dcf1518f879c.png)

Now we have our cover file and secret file, let’s use Steghide to hide **secret.zip** inside of **laptop.jpg**. Here’s an explanation of the command we’re using, `steghide embed -cf laptop.jpg -ef secret.zip`.

- **steghide** – Selects the tool we want to use
- **embed** – Selects the mode we want to use (embedding files)
- **-cf laptop.jpg** – Selecting the cover file (the file we want to hide data inside)
- **-ef secret.zip** – Selecting the file we want to embed (the file we want to hide)
**When prompted for a passphrase, you may enter any password you like. This will be used to extract the data later to protect its confidentiality, meaning only the intended recipient can access it.**

![image](https://user-images.githubusercontent.com/87195021/125534556-64157e40-0c7f-483f-9b40-9368593f7254.png)

In this example, we\'ve overwritten laptop.jpg to become laptop.jpg with an embedded file. If we want to create a new `stego` file, we can use the `-sf` flag to output it to a new file. In the below screenshot we’ve used `-sf laptop2.jpg` to output to a new file.

![image](https://user-images.githubusercontent.com/87195021/125534631-632a1bf8-5a0e-4f4b-9411-55c5bf324415.png)

Now that you know how to embed files, you need to know how to extract data from steganography files. We know that **laptop2.jpg** is a stego file, and contains an embedded file, and we know the passphrase is \'**password**\'. We can use the following command to retrieve the hidden file: `steghide extract -sf laptop2.jpg`. When prompted for the passphrase, we enter it, and the tool will extract **secret.zip** and place it in the current directory.

- **steghide** – Selects the tool we want to use
- **extract** – Selects the mode we want to use (extracting files)
- **-sf laptop2.jpg** – Selects the steganography file for extraction (combination of cover file and hidden data)

![image](https://user-images.githubusercontent.com/87195021/125534748-624d808f-f7d6-4203-9017-ae64b9e2e2c6.png)