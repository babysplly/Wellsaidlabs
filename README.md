# Wellsaidlabs
Auto Register and Login account for https://wellsaidlabs.com/

<h3>What you might need and how to run the script</h3>
<ul>
  <li> You must have <a>Selenium</a> installed </li>
  <li> Firefox </li>
</ul>

## **Installation** 
- Install Requrements
```elm 
pip3 install -r requirements.txt
``` 
- Download Web Driver 
```elm 
wget 'https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz' -O driver.tar.gz 
``` 
- install Web Driver 
```elm 
tar -zxvf driver.tar.gz 
``` 
```elm 
sudo cp geckodriver /usr/local/bin 
``` 
## **Running🚀** 
- 1.REGISTER
```elm 
python3 register.py 
```
- 2.Login
```elm
python3 login.py
```

<h3>Read more about <a href="https:https://www.selenium.dev/documentation/webdriver/getting_started/">Selenium</a></h3>
