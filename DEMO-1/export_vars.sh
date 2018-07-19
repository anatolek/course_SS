#!/bin/bash

#########################################
#            APP_VM VARIABLE            #
#########################################
export PROJECT_DIR='PetClinicProject'
export APP_USER=petclinic
export APP_DIR=/home/$APP_USER/


########################################
#            DB_VM VARIABLE            #
########################################
# export DB_HOST=10.0.10.11
export DB_USER=petclinic
export DB_PASS='demka'
export DB_NAME='pc'
export DB_PORT=3306
export DB_ROOT_PASS='demka'
export DB_REMOTE_USER_HOSTS='10.0.10.%'