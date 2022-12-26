# Apicius
Apicius is a application installer for linux, for fast setups.

**Apicius is in alpha stages of development as of now.**

![img](./doc/apicius_books.jpg)

Apicius will ask you what programs you would 
like to install and then installs them.
Apicius is post install script for linux. 
So that you can install programs and apps that you 
want to be installed. 

## Install

Apicius need python 3 to run. 

For know you need to
```batch
git clone git@github.com:AxelGard/apicius.git
cd apicius/
python3 -m apicius
```

## Add a program 

will add a more exnstiv totorial later but for now look at 
```bash 
apicius/apicius/applications/template.py
```
just copy the template file and add the install steps in the 
install method. 

## Contribute

Feel free to make a PR if you have any changes that you think is needed. 
Senice it is still eraly and nothing is working as of know I might change a lot. 
But let me know through email or an issue if you are working on somthing. 
