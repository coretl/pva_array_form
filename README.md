# pva_array_form

Some Phoebus test cases for getting display format from PVA vs setting it on the widget

## To run up the IOC

Open the directory in VSCode, and click "Open in container". Then:

    ./ioc.py

## To run up the screens

Download and unpack https://controlssoftware.sns.ornl.gov/css_phoebus

Then:

    phoebus.sh -resource test.bob

## To check the PVA structure

Open a terminal and type:

    pvget -v PVA-ARRAY-FORM:WF:String
