# ML Server quickstart

An example to run a machine learning model in an azureml inference server http docker container

## Create an environment
To create an environment use the commands below
```
$ virtualenv myenv
$ source myenv/bin/activate
```

## Installing dependencies
```
$ pip install -r requirements.txt
```

## Running the APP
```
$ docker build --tag server-quickstart .
$ docker run server-quickstart:latest
```

## Utility Commands
To check lib versions

```
$ pip list
```