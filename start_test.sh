#!/bin/bash
# need chmod +
sudo docker compose up;
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^alliance-it-backend-django" | cut -d' ' -f2);
sudo docker network rm alliance-it-backend_backend;
sudo rm -r dump/;