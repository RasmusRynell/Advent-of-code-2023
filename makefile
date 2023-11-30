# Makefile

# Name of the virtual environment
VENV := venv

# Default target
all: setup

# Check if the virtual environment exists, and if not, create it
$(VENV):
	@python3 -m venv $(VENV)

# Target to set up the environment and run the script
setup: $(VENV)
	@echo "Setting up the environment and running the script"
	@. $(VENV)/bin/activate; \
	pip3 install -r requirements.txt; \
	python3 ./utils/setup.py $(problem) $(override);

# Helper target for clean-up
clean:
	@rm -rf $(VENV)
	@echo "Cleaned up the environment"

# You can pass the argument like this: make setup arg=argument1
