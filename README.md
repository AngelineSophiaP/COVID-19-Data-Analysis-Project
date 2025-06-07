# COVID-19-Data-Analysis-Project

## Overview

This project performs an in-depth analysis of COVID-19 data using Python and Pandas. The data is sourced from a publicly available dataset that contains information about confirmed cases, deaths, and recoveries across different countries and regions. The analysis includes calculating the number of new cases, recovery rates, case fatality rates (CFR), and identifying trends over time.

## Project Objectives

* **Data Preprocessing**: Handle missing values and convert date columns to datetime format.
* **Aggregated Summary**: Summarize data by country/region, calculating confirmed cases, deaths, and recoveries.
* **Time-based Analysis**: Track daily changes in COVID-19 cases, deaths, and recoveries.
* **Key Metrics**: Calculate the Case Fatality Rate (CFR) and Recovery Rate.
* **Identifying Trends**: Find the day with the maximum number of new confirmed cases.

## Requirements

* Python 3.x
* Pandas library

You can install the necessary Python library by running the following command:

```bash
pip install pandas
```

## Dataset

The project relies on the following dataset:

* **COVID-19 Clean and Complete Dataset**: This dataset is available on Kaggle and contains detailed COVID-19 statistics across various countries and regions.

  You can access the dataset and download it from the following link:

  [COVID-19 Clean and Complete Dataset](https://www.kaggle.com/datasets/sudalairajkumar/covid19-clean-and-complete-dataset)

  After downloading the dataset, save the file as `covid_19_clean_complete.csv` and place it in the same directory as the `main.py` file before running the script.

## Results

* The top 10 countries/regions with the highest confirmed COVID-19 cases.
* The top 10 countries/regions with the highest Case Fatality Rate (CFR).
* Countries/regions with zero reported deaths.
* The date with the highest number of new confirmed cases.

## Conclusion

This project provides valuable insights into COVID-19 trends and can be extended by incorporating additional metrics, visualizations, or more recent data.

## License

This project is open-source and available under the [MIT License](LICENSE).










