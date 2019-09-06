# LambdaBigData
Big Data Analytical tools for Nanoaod



# Apache Spark Web UI Monitoring

Spark master by default bind the Spark Web UI at 8080 (visible if you connected to department's network by browsing http://10.64.22.135:8080/)

## Setting up the Web UI

### Working in Padova department of physics

You need to setup a SSH tunnel with:

```
ssh -D localhost:1122 shoh@10.64.22.135
```

Pick a port number , example 1122 and change to your username. After that browse ```http://10.64.22.135:8080/``` in your browser.

### Working remotely (Double ssh tunnel)

You need to setup a double SSH tunnel, from local pc <---> ```hoh@gate.pd.infn.it``` <---> ```shoh@10.64.22.135``` with:

```
ssh -D 11223 -J hoh@gate.pd.infn.it shoh@10.64.22.135
```

Pick a port number, example ```11223``` and change to	your username. In your local PC, go to browser Network Setting, check box Manual proxy configuration, insert ```127.0.0.1``` in SOCK host, follow by insert the favourite port number. If everything in place, browsing ```http://10.64.22.135:8080/``` will guide you to SPARK WEB UI.

# Jupyter Notebook

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

## Working in Padova department of physics

```
jupyter notebook --no-browser --port=1234 --ip=127.0.0.1 --allow-root
```

The authentication token will be revealed as an URL, copy and paste it in your browser. To shutdown the kernal, simply issue CTRL-C to the termimal.

## Working remotely (Double ssh tunnel)

You need to setup a double SSH tunnel, from local pc <---> ```hoh@gate.pd.infn.it``` <---> ```shoh@10.64.22.135``` with:

```
ssh -D 11223 -J hoh@gate.pd.infn.it shoh@10.64.22.135
```

While logged inside the cluster, execute

```
jupyter notebook --no-browser --port=11223 --ip=127.0.0.1 --allow-root
```

The authentication token will be revealed as an	URL, copy and paste it in your browser. To shutdown the	kernal,	simply issue CTRL-C to the termimal.
