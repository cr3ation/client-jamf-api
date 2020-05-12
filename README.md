# client-jamf-proxy

Intended for macOS administrators in an Jamf Pro environment.

Fetch non sensitive data about a Computer from Jamf API without autentication.
```shell
# serial=$(system_profiler SPHardwareDataType | awk '/Serial/ {print $4}')
curl 127.0.0.1:5000/computer/$serial
{
  "asset_tag": "59458", 
  "serial_number": "C02ZN353MD8F", 
  "username": "henrik.engstrom@shi******.com", 
  "ad_user": "henen62", 
  "shared_computer": "False"
}
```

## Installation

### OS X & Linux
1. Clone repository `git clone https://github.com/cr3ation/client-jamf-api/`
2. Create python3 *venv* and run `pip install -r requirements.txt` to install required modules.
3. Edit settings in `./app/config/settings_template.py` and save as `./app/config/settings.py`.
4. Run with `python3 ./app/app.py`

### Windows
No guide created. Feel free to make pull request.

### Settings
```python
# Rename settings_sample.py to settings.py
# Generate jss_credentials with:
# printf "username:password" | iconv -t ISO-8859-1 | base64 -i -

jss_server = "YOUR_JAMF_PRO_URL"            
jss_credential = "YOUR_CREDENTIALS"         

attributes = {
    "extension_attributes": [
        {
            "id": 32,                       # Extenssion attribute ID
            "name": "shared_computer",      # Name in API output
        },
        {
            "id": 11,
            "name": "Whetever..."
        }
    ]
}
```
1. Set `YOUR_JAMF_PRO_URL` to `company.jamfcloud.com`
2. Set `YOUR_CREDENTIALS` to output of `printf "username:password" | iconv -t ISO-8859-1 | base64 -i -`
3. Modify `extenssion_attributes`. Attributes is added out the web response with `name` as key

Extenssion Attribute ID is located in Jamf Pro URL.
![ExtenssionAttributes](https://github.com/cr3ation/client-jamf-api/blob/master/docs/img/extenssion_attributes_id.png)

## Usage Example
Test if server is up and running
```shell
curl 127.0.0.1:5000/hello
"Hello, World!"
```

Get data from serialnumber
```
curl 127.0.0.1:5000/computer/C02ZN353MD8F
{
  "asset_tag": "59458", 
  "serial_number": "C02ZN353MD8F", 
  "username": "henrik.engstrom@company.com", 
  "ad_user": "henen62", 
  "shared_computer": "False"
}
```

Example of use by a client machine
```
serial=$(system_profiler SPHardwareDataType | awk '/Serial/ {print $4}')
curl 127.0.0.1:5000/computer/C02ZN353MD8F > /Library/foo/bar/computer_info.json

# Set ComputerName
# Set HostName
# Set LocalHostName
# Write ad-user to settings file
...
```


## Docker
### Prerequisities
In order to run within a container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

#### Build dockerimage
```shell
docker build -t client-jamf-api:latest . 
```

#### Run container
```shell
docker run -d -p 5000:5000 client-jamf-api:latest
```

#### Environment Variables
* `jss_server` - Not yet implemented
* `jss_secret` - Not yet implemented

#### Volumes
* `/app/config` - All your settings

#### Useful File Locations (inside container)
* `/app/app.py` - Main application
* `/app/config/settings.py` - Update to add extenssion attributes

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/client-jamf-api/contributors) who 
participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
