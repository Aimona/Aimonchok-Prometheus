# Prometheus and Graphana demonstration

## Deployment

Create an ubuntu ec2 instance and [install docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04) on it.

Then install docker compose by running:

`sudo apt install docker-compose -y`

Upload this project to the instance by your preferred method (e.g. SCP or some visual implementation of SCP).

In the project's root directory run:

`docker-compose up -d`

Ensure that all three containers are running by executing:

`docker ps`

Make sure that you allowed access to port 3000 in your instance's security group in order to access Grafana (also port 80 if you would like to have direct access to Prometheus too).

Now you can access Grafana at `ec2 instance's ip:3000` and if you allowed public access to port 80, Prometheus at `ec2 instance's ip`

### Importing dashboards in Grafana

Dashboards are located under the `Graphana/Dashboards` directory. Visit the endpoint of Grafana, open the hamburger menu on the left side, then click on `Dashboards`. Click on `New` then `Import`. Copy the content of the dashboard .json file you want to import, then paste it to the `Import via panel json` box, then click `Load`. Now the dashboard should have been imported.

## Stopping the containers

In order to stop the containers, you can use the `docker-compose stop` command.

If you would like to delete the containers, you can use `docker-compose down`.

If you would like to delete the containers and their volumes too, use `docker-compose down -v`.

> ⚠ Note that this will result in removing all of your persistent data.

<!-- ### Grafana configuration

In order to import the saved Grafana dashboard, you need to modify the UID of the datasource in your .json files.

To find your datasource's UID, go to `ec2 instance's ip:3000/api/datasources/` -->