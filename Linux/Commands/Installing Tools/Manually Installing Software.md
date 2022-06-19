# Manually Installing Software

1. Ensure the following command is ran `apt install build-essential automake checkinstall libz-dev libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext cmake gcc curl`

2. Download git `wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.29.3.tar.gz`

3. Extract the git file `tar xfz git-2.29.3.tar.gz`

4. Change working directory to git directory `cd git-2.29.3/`

5. Configre the build enviornment `./configure`

6. Use the make utility to run the make file `make`

7. Use the install option on the make command `sudo make install`
    
8. Check that the software is installed and that the correct version is being used `git --version`