#!/bin/bash

if [ ! -d "./virtenv" ]; then
    virtualenv -p `which python3` virtenv

    source ./virtenv/bin/activate

    pip install beautifulsoup4
    pip install --upgrade tensorflow

    deactivate

    cd ./models/research/
    wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
    unzip protobuf.zip
    ./bin/protoc object_detection/protos/*.proto --python_out=.
    python3 setup.py sdist
    cd slim && python3 setup.py sdist
else
    echo Nothing to install
fi


