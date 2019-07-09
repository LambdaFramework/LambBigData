# LambdaBigData
Big Data Analytical tools for Nanoaod

## Setup to use jupyter notebook over cluster
### One layer tunnel

```
ssh -D localhost:1122 shoh@10.64.22.135
```

### Two layer tunnel

```
ssh -D localhost:1122 hoh@gate.pd.infn.it
ssh -L 1122:localhost:1122 shoh@10.64.22.135
```

Setup the proxy configuration in your favorite browser

![Alt text](https://github.com/LambdaFramework/LambBigData/blob/dev/browser.png)

## Bon
