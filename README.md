## Environments

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
  git config --global core.excludesfile %USERPROFILE%\.gitignore_global
  ```

- edit file %USERPROFILE%/.gitignore_global

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

