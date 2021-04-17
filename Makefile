

TARGET = colpad
TOOLS  = pyuic5
PHTYON = python

all: build run

build:
	$(TOOLS) $(TARGET).ui -o $(TARGET)_ui.py

run:
	$(PHTYON) -B $(TARGET).py

clean:
	@echo "clean all."

