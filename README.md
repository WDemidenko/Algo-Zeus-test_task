# Test task for Algo-Zeus

## Installation
1. Clone the repository:
```shell
git clone https://github.com/WDemidenko/Algo-Zeus-test_task.git
```

2. Create and activate a virtual environment, install requirements
```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
3. Start the Flask server:
```shell
flask run
```

## Usage

### Candlestick carts
http://localhost:5000/candlestick

When you visit this url in your web browser, you can view candlestick charts for picked symbols and intervals
![img.png](candlestick.png)

### Pie chart

http://localhost:5000/piechart

At this url you can see a pie chart of market caps for 10 coins
![img.png](piechart.png)

### Saving data
Data is saved in a .csv file at root directory of project, with name in this format: {symbol}-{interval}.csv

Suggested format of saving data in a relational database
![img.png](database.png)
