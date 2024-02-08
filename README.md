# country-information-catalog

a country's profile all in one. find information on a country's:
- capital city
- spoken languages
- currency (has a built-in converter to USD), 
- top restaurants and tourist spots (their name, address, website, and local number if available)

## usage

- clone this repo 

    `git clone https://github.com/gin7018/country-information-catalog.git`


- `cd` into the root folder of the repository and run the backend python api with this command
    
    `python src/api/AppController.py`


- cd into the UI sub-folder and run the web interface with this angular command
    
    ```
    cd country-catalog-ui/
    ng serve
    ``` 
    the UI should now be running on port http://localhost:4200/


- if you do not have the Angular CLI installed, run this command 
    ```
    npm install -g @angular/cli
    ``` 
    and run the previous step.


- note: some countries information may not be available at the moment


