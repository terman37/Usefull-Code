## Jupyter Lab

### venv

  - create

    ```
    conda create -n env_name python=3.7
    ```

- manage

  ```
  conda env list
  
  ```

  

### kernel

- dans base

  ```
  conda install -c conda-forge jupyterlab
  ```

- dans venv

  ```
  conda install ipykernel
  ipython kernel install --name 'env_name' --user
  ```

### defaut folder

- generate config file

  ```
  jupyter notebook –generate-config
  ```

- uncomment / modify in %user%/.jupyter/jupyter_notebook_config.py

  ```
  #c.NotebookApp.notebook_dir = ''
  ```

  

## GIT

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