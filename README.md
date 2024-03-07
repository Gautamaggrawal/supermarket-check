# Supermarket Checkout System

This Python module provides functionality to run a supermarket checkout system either with a graphical user interface (GUI) or in a non-GUI mode. It utilizes the `Checkout` and `PricingRule` classes from the `checkout` module.

## Functions

1. `run_gui(pricing_rules)`
   - **Description**: Runs the supermarket checkout system with a graphical user interface (GUI).
   - **Parameters**: `pricing_rules` - A dictionary containing pricing rules for different items.
   - **Returns**: None

2. `run_non_gui(pricing_rules)`
   - **Description**: Runs the supermarket checkout system in non-GUI mode.
   - **Parameters**: `pricing_rules` - A dictionary containing pricing rules for different items.
   - **Returns**: None

3. `main()`
   - **Description**: Main entry point of the program.
   - **Parameters**: None
   - **Returns**: None

## Usage

To run the supermarket checkout system, execute the `main.py` script with the following options:

- To run in GUI mode: `python main.py gui`
- To run in non-GUI mode: `python main.py`

Ensure that the required dependencies are installed before executing the script. The GUI mode requires Tkinter to be installed, while the non-GUI mode does not have any external dependencies.

## Docker

To build the Docker image for the supermarket checkout system, run the following command:

```docker build --no-cache -t my-image .```


To run the Docker container with GUI support, use the following command:

```docker run -u=$(id -u $USER):$(id -g $USER)
-e DISPLAY=$DISPLAY
-v /tmp/.X11-unix:/tmp/.X11-unix:rw
--rm
my-image```

Ensure that X11 forwarding is enabled on your system to display the GUI.

## Testing

The functionality of the supermarket checkout system can be tested by executing the provided test cases. Run the following command:
```python test_checkout.py```


This command will run the unit tests defined in the `test_checkout.py` file to ensure that the checkout system functions correctly.

## Dependencies

- `sys`: Standard Python module for interacting with the Python interpreter.
- `checkout.Checkout` and `checkout.PricingRule`: Classes from the `checkout` module for implementing supermarket checkout functionality.
- `tkinter`: Required for running the GUI mode. Ensure Tkinter is installed in your Python environment.
- `supermarket_gui.GUI`: Class for implementing the graphical user interface. Imported from the `supermarket_gui` module.

## Notes

- Additional items and pricing rules can be added to the `pricing_rules` dictionary as needed.
- The `main.py` script can be customized or extended to suit specific requirements.
- Ensure that the Python interpreter has permission to execute the script and that all necessary files are accessible.



