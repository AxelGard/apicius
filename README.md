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
```bash
git clone git@github.com:AxelGard/apicius.git
cd apicius/
```
to then run 
```bash
sudo python3 -m apicius
```
Apicius needs sudo since it installs programs and 
those install processes needs sudo. 

## Add a program 

will add a more exnstiv totorial later but for now look at 
```bash 
cp apicius/apicius/applications/template.json apicius/apicius/applications/myapp.json
```
just copy the template file and add the install commands in the cmd value in the json file. 
As well as any other relevant information. 
> feel free to make a PR with other programs that you think should be easy to install. 

## Contribute

Feel free to make a PR if you have any changes that you think is needed. 
Senice it is still eraly and nothing is working as of know I might change a lot. 
But let me know through email or an issue if you are working on somthing. 
