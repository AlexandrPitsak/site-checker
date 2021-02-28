# Site checker  ✅

A simple site checker allows users to validate site availability and check site response text by rule(s). 
Write result to console (by default, but can be turned off) and log file (txt and json). Includes 3 log levels:

1. INFO - informs that site is available and rule(s) verification has passed if the last is/are exist.
2. ERROR - informs that site is available but rule(s) verification has not passed or response status is not OK (e.g. 'Page not found').
3. CRITICAL - informs that site is unavailable or some connection issues appear.

## Install

1. Ensure Python 3.6+ is installed (https://www.python.org/downloads/)

2. Install and run virtual environment
    - Linux/Mac 
    ```shell
    $ pip3 install -U virtualenv
    $ python3 -m virtualenv venv
    $ source venv/bin/activate
    ```
    - Windows
    ```
    pip3 install -U virtualenv
    python3 -m virtualenv venv
    venv\Scripts\activate.bat
    ```

3. Install requirements

    ```bash
    pip3 install -r requirements.txt
    ```

4. Configure application
See the `App Config` section
5. Run application
    ```
    python3 app.py
    ```

## About

#### App Config
Config file - its a YAML ext file and consist of 3 parameters:

|Name|Type|Description|
|---|:---:|---|
|interval_in_sec|int|the interval between repeatedly checks and takes parameter in seconds|
|rules_path|str|path to the YAML file(s) with rules. Should has path from app root dirictory (dir "rules" as an example dirictory)
|log_file_name|str|the name of the log file which will be created afetr the starting app

#### Site check config
Site check config - its a YAML file which has the following form:

```yaml
url: https://example.com # Required
rules: # Optional
  - rule: must_have  
    values:
      - something    
      - Please       
      - msg         
  - rule: one_of 
    values:
      - summer    
      - time       
      - msg
```

If rules were not provided site will be checked to have a 200 OK response only.
There can be several objects with the same rule and/or values.

#### Rule
A rule object should have 2 fields:
- `rule` - rule type. Can be either `must_have` or `one_of`
- `values` - an array of strings

Rule types:
|rule|description
|---|---
|one_of| At least one value of the list should be present
|must_have| Each value of the list should be present


### Reporting
After starting the app, it will create a log file and will append logs with each check iteration.
After first iteration 'latest_report.json' will be generated, and will update data with the latest check results (for vizualization on UI and etc.). 
Site URL is used as a key for holding latest report.
**Note:** if several rule files has the same URL the data in JSON report will be overriden



### Ideas for improvement

1. Increase types of searching values with:
    - regex 
    - css/xpath selectors (with browser engine)
2. Add browser engine (Seleniun, Puppeteer, Playwright, etc.)
3. Parallel processing
4. Write unit tests
5. Handling errors
    - config:
        - empty interval
        - wrong format interval
        - empty path
        - wrong path
        - empty log file name
    - rules:
        - empty file
        - incorrect rule
        - incorrect values type (not list)
        - duplicate URLs
6. Add CLI params and/or env variables support
7. Add more reporters 