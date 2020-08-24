#!/usr/bin/env bash
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"matthew@matt-matters.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\