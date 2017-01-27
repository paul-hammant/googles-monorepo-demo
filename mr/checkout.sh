#!/bin/sh

find . -name pom.xml -type f -delete
git checkout --
find . -name "pom-template.xml" | python mr/writepom.py
