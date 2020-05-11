# client-jamf-proxy

Intended for macOS administrators in a Jamf Pro environment.

Let macOS clients fetch data from Jamf API without autentication – and only the data of your choosing.
```shell
SERIAL=$(system_profiler SPHardwareDataType | awk '/Serial/ {print $4}')
curl 127.0.0.1:5000/compyter/$SERIAL 
```

## Getting Started 

### Prerequisities
* Python3 – a `venv` is recommended
* pip3

### Usage

1. Rename `./app/config/settings_template.py` to `./app/config/settings.py`
2. Update `./app/config/settings.py`. Extenssion attribute ID's can be added together with name of your choosing. Extenssion attribute will be added to output.
3. `pip install -r requirements.txt`
4. `python3 ./app/app.py`


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
* `/app/config/settings.py` - Contains all settings. Update here to add extenssion attributes.

## Find Me
* [GitHub](https://github.com/cr3ation/client-jamf-api)
* [Quay.io](https://quay.io/repository/your/docker-repository)

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Versioning
I use [SemVer](http://semver.org/) for versioning. For the versions available, see the 
[tags on this repository](https://github.com/your/repository/tags). 

## Authors
* **Henrik Engström** - *Initial work* - [PurpleBooth](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/client-jamf-api/contributors) who 
participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
* Internet. Used ut a lot.
