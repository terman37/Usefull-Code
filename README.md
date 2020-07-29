## Python

### Linux - Python specific version

- download from python Gzipped tarball https://www.python.org/downloads/source/ or 

  ```bash
  wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz
  ```

- uncompress

  ```bash
  sudo tar xzf Python-3.7.8.tgz
  ```

- compile (make alt install to keep existing configsudo)

  ```bash
  cd /usr/src
  cd Python-3.7.8
  sudosudo ./configure --enable-optimizations
  sudo make altinstall
  ```

- check

  ```bash
  python3.7 -V
  ```

- check install path

  ```bash
  which python3
  which python3.7
  ```

## Environments

### pip

- install / upgrade

  ```bash
  sudo apt install python3-pip
  sudo apt install python3-venv
  
  python3 -m pip install --upgrade pip
  ```

### Conda

  - create

    ```bash
    conda create -n env_name python=3.7
    ```

- manage

  ```bash
  conda env list
  ```

### venv

- Create

  ```bash
  python3 -m venv path_to_venv
  ```

- activate

  - win

    ```bash
    path_to_venv\scipts\activate.bat
    ```

  - linux

    ```bash
    source path_to_venv/bin/activate
    ```

- desactivate

  ```bash
  deactivate
  ```

## Jupyter Lab

### proxy

- create .condarc

```
conda config
```

- set

```
conda config --set proxy_servers.https https://address:port
```

- or add in .condarc in %USERPROFILE%

```
channels:
  - defaults

show_channel_urls: true
allow_other_channels: true

# proxy_servers:
http: https://address:port
https: https://address:port

ssl_verify: false
```

### Install

- conda

  ```
  conda install -c conda-forge jupyterlab
  ```

- pip

  ```
  pip install jupyter-lab
  ```

### Kernel

- conda

  ```
  conda install ipykernel
  ```
  
- pip

  ```
  pip install ipykernel
  ```
  
- add kernel

  ```
  python -m ipykernel install --user --name=myenv
  ```

- kernel list

  ```
  jupyter kernelspec list
  ```

- uninstall

  ```
  jupyter kernelspec uninstall myenv
  ```

### defaut folder

- generate config file

  ```
  jupyter notebook –generate-config
  ```

- uncomment / modify in %USERPROFILE%/.jupyter/jupyter_notebook_config.py

  ```
  #c.NotebookApp.notebook_dir = ''
  ```

### default web browser

- modifiy jupyter_notebook_config.py

  ```
  c.NotebookApp.browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
  ```

## GIT

### gitignore global

- create file

  %USERPROFILE%/.gitignore_global
  
- run

  ```
  git config --global core.excludesfile C:/users/ajourdan/.gitignore_global
  ```

- edit the file .gitignore_global

### proxy

- set

  ```
  git config --global --add http.proxy http:``//isp-ceg.emea.cegedim.grp:3128
  ```

- Verify with following line that the variable has been set

  ```
  git config --global --get http.proxy
  ```

- unset

  ```
  # To remove the config
  git config --global --unset http.proxy
  ```

### Python script to clone private repo

- can be used to run private repo from collab for example

  ```python
  import os
  from getpass import getpass
  import urllib
  
  user = 'user'
  password = getpass('Password: ')
  password = urllib.parse.quote(password) # your password is converted into url format
  repo_name = 'repo name'
  
  cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(user, password, repo_name)
  
  os.system(cmd_string)
  cmd_string, password = "", "" # removing the password from the variable
  ```



## Packaging

### install / check

```
pip install setuptools wheel
python -m pip install --user --upgrade setuptools wheel
```

### Folder structure

<img src="folder_structure.png" alt="folder_structure" style="zoom: 80%;" />

### Setup.py example

```python
import setuptools

setuptools.setup(
    name="ML00",
    version="0.0.6",
    author="AJO",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=['numpy >= 1.18']
)
```

### To build

- Wheel

  ```
  python setup.py bdist_wheel
  ```

- direct install (from setup.py folder)

  ```
  pip install .
  ```

## Docker

### Build / run

- from Dockerfile directory run: (**do not forget the dot at the end**)

  ```bash
  docker build --tag myappimage:v0 .
  ```

- Check images installed

  ```bash
  docker images
  ```

- Run it: (bind port 80 to 8000 in container)

  ```bash
  docker run -d -p 80:8000 myappimage:v0
  ```

- clean docker images/volumes... (all but the ones running)

  ```
  docker system prune -a
  ```


### Docker File

- Example

  ```dockerfile
  # with slim buster 371 Mo :-)
  FROM python:3.7.7-slim-buster
  
  # Working directory in image
  WORKDIR /My_API
  # Copy from local current dir to image workdir
  COPY . .
  # Change workdir (relative)
  WORKDIR flask_app
  # Run install of PIP modules
  RUN pip install --no-cache-dir -r requirements.txt
  # Open port
  EXPOSE 8000
  
  # Cmd to be run at startup
  CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgi:server"]
  ```



## Python

### Defaults packages

```bash
pip install matplotlib
pip install pandas
pip install scipy
pip install scikit-learn
```

## Pentaho

change JVM memory in spoon.bat

```
if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms1024m" "-Xmx4096m" "-XX:MaxPermSize=256m"
```

## Other Linux

### Run bash script at startup

create a file /etc/rc.local

place script in it:

```bash
#!/bin/bash

echo "hello world"

exit 0
```

make it executable

```bash
sudo chmod +x /etc/rc.local
```

### Install jdk on ubuntu

```bash
sudo apt install default-jre
sudo apt install default-jdk
```

## Other Windows

### Windows terminal

- modify **windows_terminal_settings.json** (check file with enabled cmd / cmd in venv / bash / wsl )