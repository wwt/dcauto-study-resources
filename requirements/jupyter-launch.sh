#!/bin/bash
jupyter-lab --allow-root --ip=0.0.0.0 --no-browser --port=8888 --ServerApp.token=''
mkdocs serve
