# WMATADirectionAPI
A python program that uses the pyWMATA library to provide a RESTful route finding API for the Washington Metropolitan Area Rail Lines. 

#Example
Running 

```bash
curl localhost:80/WMATA/route/C13/A04/
```

and

``` bash
curl localhost:80/WMATA/route/King/Woodley/
```

both return: 

``` 
{
  "Start": "King Street (Start towards Fort Totten)", 
  "Transfer": "Gallery Place (Transfer towards Shady Grove)"
  "End": "Woodley Park Zoo (Exit)", 
}
```

