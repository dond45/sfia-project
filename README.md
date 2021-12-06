README file for sfia 2 project

Brief
--------------------------------------

This project was to create an application of four microservices.


 Technologies
--------------------------------------

listed below are the techonologies intended for use during the project.

IDE: visual studio code was used as the IDE thoughout the project, it allowed for seamless integration with GCP.

Jira: used for documenting the projecting and production of project.

Git: was chosen for version control, making it easy to store code in the cloud. 

Jenkins: jenkins is within the project folder but has not been deployed as of yet. the configuration can be seen in the Jenkinsfile.

Ansible: again asible within the project folders but has not be deployed as of yet, which can be accessed on port 80.

GCP:  has been used for various tasks including; docker manager, worker, and the NGINX load balancer.

Docker & Docker Swarm: docker/compose/ swarm was used in this project for containerization. swarm allowed for the connection of the virtual machines, while docker ocmpose was used to configure the deployment. dockerhub was used to store images made by the prior.

NGINX: was used to load balance across the virtual machines.


App Design
---------------------------------

this app contains 4 micro-services as described below:

frontend: the user would intect with this service directly. it is intended to post 

service2-api: This service recieves an HTTP GET reqest and pushes a random name from a list.

service3-api: This service recieves an HTTP GET reqest and pulls a random number from a list.

service4-api: This service recieves an HTTP POST request from service 1 and will randomly generate a name and a number, which then determines whether the prize is won.


Risk Assessment
--------------------------------------

there are  several risk areas, as outlined within the risk assessment.

Known Issues
the first immidate known issue lies within the fact that the application has been unable to start - this poses a severe risk and would need immidate future developement.
secondly the application would required testing before deployment.


Future Development
-------------------------------------

the applicaiton would require much further developement in all areas including integration and deployment.