## Node.js web application using Express.js

This application generates a random password consisting of 8 characters (letters and digits) and returns it as a response.

### Startup instructions

#### 1) [Install](https://nodejs.org/en/download/) Node.js on your system if it's not already installed.
#### 2) Clone the repository to your local machine:
```bash
git clone https://github.com/YanPetrov7/SDM-lab-3.git
```
#### 3) Move to the project directory:
```bash
cd SDM-lab-3/starter-project-nodejs
```
#### 4) Install dependencies:
```bash
npm install
```
#### 5) How to launch the application:
```bash
node index.js
```
### Run using Docker

#### 1) [Install](https://docs.docker.com/engine/install/) Docker on your system if it's not already installed.
#### 2) Start the daemon:
```bash
sudo systemctl start docker
```
#### 3) Clone the repository to your local machine:
```bash
git clone https://github.com/YanPetrov7/SDM-lab-3.git
```
#### 4) Move to the project directory:
```bash
cd SDM-lab-3/starter-project-nodejs
```
#### 5) Build the image:
```bash
docker build . -t nodejs_project
```
#### 6) Run the container:
```bash
docker run --rm -p 3000:3000 nodejs_project
```