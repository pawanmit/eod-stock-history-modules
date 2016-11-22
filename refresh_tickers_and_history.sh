#!/bin/bash
python data-collection/db/ddl/drop-schema.py
python data-collection/db/ddl/create-schema.py
python data-collection/fetch_tickers.py
python data-collection/fetch_tickers.py