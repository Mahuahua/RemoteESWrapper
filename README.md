# RemoteServerWrapper
Wrapper endpoint around the remote Elastic Search (mostly). Runs on port 8049

Install the following in root
```
sudo apt install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

The following command put up the server in the background
```
nohup python wrapper.py &
```
