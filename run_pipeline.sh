#!/bin/bash
cd /path/to/crypto-pipeline
source venv/bin/activate
python main.py >>logs/pipeline.log 2>&1
