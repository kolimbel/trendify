# Scraper Module

This module is designed to scrape data from various external services, map the data to a common format, and process it for further use. The module uses Pydantic for data validation and ensures that all data adheres to the specified schema.

## Features

- Scraping data from multiple external services.
- Mapping data to a common internal format.
- Flexible data handling for different types of properties (house, apartment, land).

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.tx
```

## TODO
- [ ] logger
- [ ] external services parametrization
- [ ] external services healthcheck
- [ ] handling pagination with announcements
- [ ] handling single announcement