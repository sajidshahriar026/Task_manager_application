*Project Requirements*
  -- conda for python environment management  
  -- python 3.10  
  -- django 5.0.1  
  -- django environ for configuring enviroment variables in django  


*Project Setup*
    -- download anaconda from (https://www.anaconda.com/download)  and install  
    -- open the anaconda prompt  
    -- create an environment using python3.10  
    ```
      conda create -n ENVNAME python=3.10  
    ```  
    --change to the the newly created environment    
    ```  
      conda activate ENVNAME    
    ```  
    --install django django rest framework and django-environ in that environment      
    ```  
      pip install django    
    ```    
    ```  
      pip install djangorestframework  
    ```  
    ```   
      pip install django-environ  
    ```  
    *Set Up Envrironment Variables*  
    --Go to the task_manager/task_manager and create a file named .env  
    --In that file set up the environment variable as follows:  
      ```
        SECURITY_KEY=#your security key here\n
        DATABASE_ENGINE=#backend for postgresql\n  
        DATABASE_NAME=#database_name\n  
        DATABASE_USER=#database_user\n  
        DATABASE_PASSWORD=#password\n    
        DATABASE_HOST=localhost\n  
        DATABASE_PORT=#your configured port\n  
      ```
    
    
    
    
  
