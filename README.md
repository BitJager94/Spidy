# Code Documentation - Web Scraping and URL Relational Chart

This Python script utilizes the Scrapy framework to perform web scraping and generate a URL relational chart using the NetworkX and Matplotlib libraries. The script starts by scraping a specified webpage and extracting specific elements, such as links, from it. It then builds a URL map and constructs a directed graph to represent the relationships between URLs. Finally, it displays the URL relational chart using Matplotlib.

## Requirements

To run this code, the following packages need to be installed:

- `asyncio.windows_events` (if running on Windows)
- `scrapy`
- `re`
- `colorama`
- `keyboard`
- `networkx`
- `matplotlib`

Make sure these packages are installed in your Python environment.

## Functionality

### `key_listener(event)`

This function is a keyboard event listener that listens for the 'esc' key press. When the 'esc' key is pressed, it sets the `key_pressed` variable to `True`.

### `MySpider`

This class defines the web spider for web scraping using Scrapy. It inherits from the `Spider` class provided by Scrapy. The spider starts by setting the `name` and `start_urls` attributes. It also initializes the `url_map` dictionary and the `graph` variable.

The spider includes the following methods:

#### `__init__()`

The constructor method initializes the spider. It prints a message to the console and sets up the keyboard event listener using the `keyboard.on_press()` function.

#### `parse(response)`

This method is the callback function for processing the web page response. It extracts specific elements from the webpage, such as links, and populates the `url_map` dictionary with the relationships between URLs. If the 'esc' key has not been pressed (`key_pressed == False`), it sends requests to scrape the extracted links recursively. Otherwise, it returns, indicating the end of scraping.

#### `is_valid_link(link)`

This method checks if a given link is valid by matching it against a regular expression pattern. It returns `True` if the link matches the pattern and `False` otherwise.

#### `show_chart()`

This method constructs a directed graph using the `url_map` dictionary. It adds nodes to the graph based on the keys of `url_map` and adds edges based on the values. It then uses NetworkX and Matplotlib to visualize the graph as a URL relational chart.

#### `spider_closed(spider, reason)`

This method is a signal handler that is triggered when the spider finishes. It executes the `show_chart()` method to display the URL relational chart.

## Usage

To use the script, simply run it as a Python script. The spider will start scraping the specified webpage and building the URL relational chart. Press the 'esc' key to stop the spider and display the chart.

```python
python script_name.py
```

**Note:** Make sure to have the required packages installed and update the `start_urls` attribute of the `MySpider` class with the desired webpage URL before running the script.