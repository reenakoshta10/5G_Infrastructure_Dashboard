# Dashboard: Capacity, coverage and cost of 5G infrastructure

## The Mission

On the early days of telecommunications, the majority of the clients were humans living on urban areas so the strategy of network operators was mostly focused on providing coverage in the regions with higher density of population. In today's world connectivity is different, more machines than humans will be connected and the network operators are evaluating how to rollout the new 5G infrastructure in a way that the service can be provided to all users involved (sensors, machines, people) and at the same time taking advantage of the reliable and already built 4G infrastructure.

As a Data Scientist for an international telecommunications company my role currently is to be involved on the deployment of brand new 5G networks in Europe. In order to achieve an successful allocation of resources, the company is providing a dataset with information related to capacity and coverage of 4G & 5G networks, geographical information related to demand and supply of connection (Mbps) and economic indicators.

My role is to be a data-driven advisor for the board of directors and you have the responsibility of communicating KPIs and a strategy for better allocation of resources during the construction of the new 5G infrastructure. Besides of the data analysis this information have to be easy available to all decision makers at any moment, reason why a dashboard summarizing the dataset is fundamental during the execution of this project.
## Prerequisite to run the project

Python 3 should be install in you system.  
To install python you can follow the link [Install Python](https://realpython.com/installing-python/#how-to-install-python-on-macos)

Docker should be installed in your system.  
To install python you can follow the link [Install Docker](https://docs.docker.com/engine/install/)

Heroku Cli should installed if you want to deploy your application on Heroku.  
To install python you can follow the link [Install Docker](https://docs.docker.com/engine/install/)

## Usage

### Deploy project using docker

Checkout the project and in terminal go to folder `5G_Infrastructure_Dashboard`. And follow below below steps as per your requirement.

- Deploy Application to heroku 
  * create heroku app using below command
  
    `heroku create <app-name>`
  * run below command to create docker comtainer in heroku
  
    `heroku container:push web --app <app-name>`
  * run below command to release the container.
  
    `heroku container:release web --app <app-name>`
  * open your application using `https://<app-name>.herokuapp.com` link

### Run application locally without docker

- To run application locally run `app.py` file using below command.

  `streamlit run code/app.py`
    

## Contact

Created by [Reena Koshta](https://github.com/reenakoshta10) - feel free to contact me!

## Have a nice day!
