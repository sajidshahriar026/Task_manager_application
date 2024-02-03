*Project Requirements*  
  -- conda for python environment management  
  -- python 3.10  
  -- django 5.0.1  
  -- django environ for configuring enviroment variables in django  
  -- PostgreSQL database  
  -- psycopg2 for postgresql and django integration  


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
  ```
    pip install psycopg2    
  ```  
  
    
  *Set Up Envrironment Variables*   
   --Go to the task_manager/task_manager and create a file named .env  
   --In that file set up the environment variable as follows:  
    
  ```
    SECURITY_KEY=#your security key here 
  ```  
  ```  
    DATABASE_ENGINE=#backend for postgresql  
  ```  
  ```  
    DATABASE_NAME=#database_name  
  ```  
  ```
    DATABASE_USER=#database_user  
  ```  
  ```  
    DATABASE_PASSWORD=#password     
  ```  
  ```  
    DATABASE_HOST=localhost  
  ```
  ```  
    DATABASE_PORT=#your configured port
  ```   





