# RemoteServerWrapper
Wrapper endpoint around the remote Elastic Search (mostly). Runs on port 8049

First time
```
sudo apt install virtualenv
virtualenv venv
```
Then install
```
pip install -r requirements.txt
```
in root:
```
source venv/bin/activate
nohup python wrapper.py &
```
