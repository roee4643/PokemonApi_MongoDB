#!/bin/bash


#Install git and clone files to the Web Server 
sudo yum update -y   # For Amazon Linux or CentOS
sudo yum install -y git
cd 
mkdir App
sudo mkdir .aws
cd App
git clone https://github.com/roee4643/PokemonApi_MongoDB

cd ..

sudo touch .aws/credentials


sudo mv App home/ec2-user/
sudo mv .aws home/ec2-user/



sudo python3 -m ensurepip --upgrade
sudo /usr/bin/python3 -m pip install --upgrade pip

sudo chown ec2-user home/ec2-user/.aws/credentials
chmod +x home/ec2-user/.aws/credentials

#pip3 install boto3

cd home/ec2-user


# Ensure the .aws directory exists
mkdir -p ~/.aws

# Write credentials to ~/.aws/credentials
#sudo tee > ~/.aws/credentials <<EOL
#[default]
#aws_access_key_id = ${AWS_ACCESS_KEY_ID}
#aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}
#aws_session_token = ${AWS_SESSION_TOKEN}
#region = us-west-2  
#EOL


#install mongodb 
sudo cat <<EOF > /etc/yum.repos.d/mongodb-org-8.0.repo
[mongodb-org-8.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/8.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-8.0.asc
EOF

sudo yum install -y mongodb-org
#sudo systemctl start mongod

# Configure MongoDB to bind to 0.0.0.0
sudo sed -i 's/127\.0\.0\.1/0.0.0.0/g' /etc/mongod.conf
#sudo systemctl stop mongod
sudo systemctl start mongod

#set and install docker 
cd home/ec2-user/App/PokemonApi_MongoDB


sudo yum install docker -y
sudo service docker start

sudo docker build -t pokemon-api .
sudo docker run -p 80:80 pokemon-api








