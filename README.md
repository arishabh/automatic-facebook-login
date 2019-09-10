# Automatic Facebook Login for Linux
Python script that can automatically open a browser and login to your facebook and open the wall directly. You can also add it as a Startup Application so that the browser with the facebook wall opens as soon as you turn on your computer.

# Setup/To-Do/Requirements
First, you need python3 and selenium. Use the code below to download selenium. Check the python version by the following code:
```
    python --version
```
Or you can just type:
```
    python3
```
and if there is an error, then you need to download python3. 
To download selenium use the code:
```
    pip install selenium
```

To setup the script, follow these steps.

First, clone the repository by using the following code: 

```
  git clone https://github.com/arishabh/automatic-facebook-login
```

Then, go inside the directory:

```
  cd automatic-facebook-login
```

Next, you need to change the **info.txt** file and enter your username and password in place of (USERNAME) and (PASSWORD). You can use any text editor you want.

**WARNING:** Dont add any extra spaces or new line. Just add it in place of the brackets 

Lastly, search **Startup Application** and then click the **Add** button, and then select the code. This will make the code run every time you start your computer. You can add comments if you want, but it is not compulsory
```
  Startup Applications -> Add -> Select facebook.py
```

# Output
- It wil open a browser with your facebook already ogged in as soon as you turn on your computer

# Uninstall

To uninstall, go to **Startup Application** and **Remove** the Python file you had added and delete the repository by using:
```
rm -rf automatic-facebook-login
```
