# ERAU Venv Workshop - SPR 2025
A workshop to teach Python virtual environments and their uses/applications in astronomy, physics, and math.

Welcome to the Virtual Environment (venv) Workshop!

Background:
  -Astronomy and Astrophysics Senior
  -Computer Science and Computational Mathematics Minor
  -First started coding 2yrs ago (learned C first)
  -No formal Python training

What this workshop will cover:
  -Purpose/uses of Python venv
  -How to initalize venv
  -How to start a venv
  -What's "contained" in a venv 
  -What a requirements file is
  -How to deactivate a venv

Let's get started!!!!

##**1. Check if Python is installed:**
First, check that you have Python installed on your computer by using the following command:

```console
  python3 -V
```

The output should say Python 3.##.## (depending on which version you have)

##**2. Go to directory where code is located:**
Now that we know we have Python installed, we can create the venv. To do this, go into the folder where the code you are working on (called a working directory) is kept using this command:

```console
  cd /your/directory/here
```

##**3. Initalize Python venv:**
Let's initalize the Python venv. Copy and paste the following command into your terminal while in your working directory:

```console
  python -m venv name_of_venv
```

You can change "name_of_venv" to pretty much whatever you'd like but everything else in the command needs to be the same for it to work. If you want to create the venv in a subfolder to the one you are currently in, you can replace "name_of_venv" with './name/of/sub/directory/name_of_venv'.

##**4. Activate venv:**
Once you have created the venv, you can then activate it using this command:

```console
  source name_of_venv/bin/activate
```

After you run this command successfully, you will have started your venv! Once there, you can begin working on your project in your venv.
Note: You will have to install dependencies into the venv before your code will work. You will only have to install packages/dependencies once for a venv.

###**(Optional) - Create and run requirements file:**
Onto the requirements file. This is a file you can have prewritten with all required dependencies for your project that will install them all at the same time. To do this, you will first need to create a 'requirements.txt' file (an example can be found in this GitHub repo). To install all dependencies at the same time, all you need to do is run this command while in your working directory:

```console
  pip install -r requirements.txt
```

Your terminal will then flood with the installation of the multiple packages.


##**5. Deactivate venv:**
To wrap up this workshop, we will close the venv to clean the environment and reduce the change of any dependency errors. To deactivate the venv you can use either commands:

```console
  deactivate
```

```console
  conda deactivate
```

Both work (assuming you have anaconda installed), but the later is prefered because the former is depreciated (outdated)


##**6. All done!**
That wraps up the workshop! I have some example Python code to run (also in this repo) using what you've learned about Python virtual environments and requirements files. If you have any questions, please feel free to reach out to me or Dr. Otani!



