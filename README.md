# Dinning Hall WebServer
This is a component for the Restaurant Simulation project.<br>
Kitchen component: <a href="https://github.com/dimatrubca/PR-Lab1-Kitchen">link</a>

## Usage
Create dinning-hall-image: ```docker build -t dinning-hall-image .```<br>
Create and run the container over the previously created kitchen-nw bridge network:<br> ```docker run --net kitchen-nw -p 5001:5001 --name dinning-hall-container dinning-hall-image```



! Dinning Hall container should be run after the kitchen-container
