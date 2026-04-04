# Docker Hello World App

## Build the image
docker build -t my-hello-app .

## Run the container
docker run -d -p 8080:8080 --name hello-container my-hello-app

## Test the app
Open browser and go to: http://localhost:8080
Expected output: Hello, World! Docker is working!

## Check running container
docker ps

## Stop the container
docker stop hello-container