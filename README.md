# Option Greek Plotter

This Python application provides a graphical user interface (GUI) for plotting various option Greeks (e.g., Price, Delta, Gamma, Vega, Theta, Rho) for both call and put options. It uses Tkinter for the GUI and Matplotlib for plotting. The application allows users to input option parameters and visualize the relationship between stock price and the selected Greek.

## Features

- Input fields for spot price, strike price, interest rate, yield, volatility, and time to maturity.
- Dropdown menus for selecting option type (Call or Put) and Greek type (Price, Delta, Gamma, Vega, Theta, Rho).
- Generates and displays a plot based on the selected option type and Greek.

## Parameter Guide
* Spot Price: Current price of the underlying asset.
* Strike Price: Strike price of the option.
* Interest Rate: Risk-free interest rate (as a decimal).
* Yield: Dividend yield (as a decimal).
* Volatility: Volatility of the underlying asset (as a decimal).
* Time to Maturity (Years): Time to expiration of the option.

## Relevant Libraries
* numpy
* scipy
* matplotlib
* tkinter
