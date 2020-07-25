## Environments

### python utils

```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

### pip

- install / upgrade

  ```bash
  sudo apt install python3-pip
  sudo apt install python3.7-venv
  
  python -m pip install --upgrade pip
  ```

### conda

  - create

    ```
    conda create -n env_name python=3.7
    ```

- manage

  ```
  conda env list
  ```

### venv

- Create

  ```
  python -m venv path_to_venv
  ```

- activate

  - win

    ```
    path_to_venv\scipts\activate.bat
    ```

  - linux

    ```
    source path_to_venv/bin/activate
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
#  http: http://proxy-tech.svc.ext.tdc
#  https: http://proxy-tech.svc.ext.tdc

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
  python -m ipykernel install --user --name=myenv
  ```

- dans venv

  ```
  pip install ipykernel ( or pip install --user ipykernel)
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

```
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

## Run bash script at startup

create a file /etc/rc.local

place script in it: (example fix sound issue on ux534ft)

```bash
#!/bin/bash

hda-verb /dev/snd/hwC0D0 0x20 0x500 0xf
hda-verb /dev/snd/hwC0D0 0x20 0x477 0x74
exit 0
```

make it executable

```bash
sudo chmod +x /etc/rc.local
```

## Install jdk on ubuntu

```bash
sudo apt install default-jre
sudo apt install default-jdk
```

