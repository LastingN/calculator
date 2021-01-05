#!/usr/bin/env bash
pytest --alluredir=results
allure generate results -o report --clean
allure open -h 127.0.0.1 -p 8803 report