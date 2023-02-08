#!/bin/env python
from softioc import softioc, builder, asyncio_dispatcher

# Set the record prefix
builder.SetDeviceName("PVA-ARRAY-FORM")

# Create some records
long_string = b"A long string, a very long string, well longer than 40 chars anyway"
builder.aIn("AO", initial_value=42)
builder.aIn("AO:Hex", initial_value=42).add_info("Q:form", "Hex")
builder.aIn("AO:Bin", initial_value=42).add_info("Q:form", "Binary")
builder.aIn("AO:Exp", initial_value=42).add_info("Q:form", "Exponential")
builder.aIn("AO:Eng", initial_value=42).add_info("Q:form", "Engineering")
builder.Waveform("WF", long_string)
builder.Waveform("WF:Str", long_string).add_info("Q:form", "String")

# Boilerplate get the IOC started
builder.LoadDatabase()
softioc.iocInit(asyncio_dispatcher.AsyncioDispatcher())

# Finally leave the IOC running with an interactive shell.
softioc.interactive_ioc(globals())