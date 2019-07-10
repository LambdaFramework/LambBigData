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

You need to setup a double SSH tunnel, from local pc --> host1 --> host2 with:

```
ssh -D localhost:1122 hoh@gate.pd.infn.it
```

Pick a port number, example 1122 and change to	your username. We accessing Padova network via the PD gate. While logged into the gate, issue the next command:

```
ssh -D localhost:1234 shoh@10.64.22.135
```

After that browse ```http://10.64.22.135:8080/``` in your browser.

# Jupyter Notebook

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

## Working sparks in Jupyter notebook

### Working in Padova department of physics

You need to setup a SSH tunnel with:

```
ssh -L 1234:localhost:1234 shoh@10.64.22.135
```

Pick a port number , example 1234 and change to your username. While logged in, execute

```
jupyter notebook --no-browser --port=1234 --ip=127.0.0.1 --allow-root
```

The authentication token will be revealed as an URL, copy and paste it in your browser. To shutdown the kernal, simply issue CTRL-C to the termimal.

### Working remotely (Double ssh tunnel)

You need to setup a double SSH tunnel, from local pc --> host1 --> host2 with:

```
ssh -L 1234:localhost:1234 hoh@gate.pd.infn.it
```

Pick a port number, example 1234 and change to	your username. We accessing Padova network via the PD gate. While logged into the gate, issue the next command:

```
ssh -L 1234:localhost:1234 shoh@10.64.22.135
```

While logged inside the cluster, execute

```
jupyter notebook --no-browser --port=1234 --ip=127.0.0.1 --allow-root
```

The authentication token will be revealed as an	URL, copy and paste it in your browser. To shutdown the	kernal,	simply issue CTRL-C to the termimal.
