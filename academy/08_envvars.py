#!/usr/bin/python3.7

import os

stage = os.getenv("STAGE", default="DEV")

output = f"running in {stage}"

if stage.startswith("PROD"):
    output = "Be Carefull - " + output

print(output)

