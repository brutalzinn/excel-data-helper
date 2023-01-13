# excel-data-helper" 

## This is helpfull to handle metrics with CSV.

# Context

You have a Excel with documents and you need to do a api request to handle the data. The api responds with the new data and i need to save this as csv.

# How to solve without Excel patterns
 Read a input test.csv, request a api about a especify column, read data from api response and write as test_out.csv"

The api-test has default port to 3001.
Soo, you need to configure you postman like this:

![Postman print](/docs//imgs/postman_view.png "postman print")

# Setup

1. Create a enviroment to install pip packages.
> python -m venv env
2. Install packages
> python -m pip install -r requeriments.txt
3. Run api
> python -m api-test
4. Run csv_handler
> python csv_handler.py
5. Enjoy!