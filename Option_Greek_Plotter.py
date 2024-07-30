from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.stats import norm

def plot_graph():
    # Retrieve values from entries
    try:
        values = [float(entry1.get()), float(entry2.get()), float(entry3.get()), 
                  float(entry4.get()), float(entry5.get()), float(entry6.get()),
                  str(combo_box1.get()), str(combo_box2.get())]
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return

    # Clear the previous plot if it exists
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Define input variables
    S0 = values[0]
    K = values[1]
    r = values[2]
    y = values[3]
    sigma = values[4]
    T = values[5]
    option_type = values[6]
    greek_type = values[7]
    
    # Create data for plotting
    X = np.linspace(max(0, min(.8*S0, .8*K)), max(1.2*S0, 1.2*K), 100)
    
    if (option_type == 'Call'):
        
        if(greek_type == 'Price'):
            Y = get_call_price(X, K, r, y, sigma, T)
            
        elif(greek_type == 'Delta'):
            Y = get_call_delta(X, K, r, y, sigma, T)
            
        elif(greek_type == 'Gamma'):
            Y = get_call_gamma(X, K, r, y, sigma, T)
            
        elif(greek_type == 'Vega'):
            Y = get_call_vega(X, K, r, y, sigma, T)
        
        elif(greek_type == 'Theta'):
            Y = get_call_theta(X, K, r, y, sigma, T)
            
        else:
            Y = get_call_rho(X, K, r, y, sigma, T)
            
    else:
        
        if(greek_type == 'Price'):
            Y = get_put_price(X, K, r, y, sigma, T)
            
        elif(greek_type == 'Delta'):
            Y = get_put_delta(X, K, r, y, sigma, T)
        
        elif(greek_type == 'Gamma'):
            Y = get_put_gamma(X, K, r, y, sigma, T)
            
        elif(greek_type == 'Vega'):
            Y = get_put_vega(X, K, r, y, sigma, T)
            
        elif(greek_type == 'Theta'):
            Y = get_put_theta(X, K, r, y, sigma, T)
            
        else:
            Y = get_put_rho(X, K, r, y, sigma, T)
        
    
    # Create plot
    title = option_type + ' Option ' + greek_type + ' vs. Stock Price'
    fig, ax = plt.subplots()
    ax.plot(X, Y)
    ax.set_title(title)
    ax.set_xlabel('Stock Price')
    ax.set_ylabel(values[6] + ' Option ' + values[7])

    # Embed the plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)


def get_call_price(S0, K, r, y, sigma, T):  
    
    # Calculate d1 and d2
    d1 = (np.log(S0 / K) + (r - y + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calculate call option price
    call_price = S0 * np.exp(-y * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    
    return call_price


def get_put_price(S0, K, r, y, sigma, T):
    
    # Calculate d1 and d2
    d1 = (np.log(S0 / K) + (r - y + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calculate put option price
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * np.exp(-y * T) * norm.cdf(-d1)
    
    return put_price


def get_call_delta(S0, K, r, y, sigma, T):
    
    # Increment price change by .01
    dS = .01
    dp = get_call_price(S0 + dS, K, r, y, sigma, T) - get_call_price(S0, K, r, y, sigma, T)
    
    return(dp/dS)


def get_put_delta(S0, K, r, y, sigma, T):
    
    # Increment price change by .01
    dS = .01
    dp = get_put_price(S0 + dS, K, r, y, sigma, T) - get_put_price(S0, K, r, y, sigma, T)
    
    return(dp/dS)



def get_call_gamma(S0, K, r, y, sigma, T):
    
    # Increment price change by .01
    dS = .01
    dd = get_call_delta(S0 + dS, K, r, y, sigma, T) - get_call_delta(S0, K, r, y, sigma, T)
    
    return(dd/dS)


def get_put_gamma(S0, K, r, y, sigma, T):
      
    # Increment price change by .01
    dS = .01
    dd = get_put_delta(S0 + dS, K, r, y, sigma, T) - get_put_delta(S0, K, r, y, sigma, T)
      
    return(dd/dS)  


def get_call_vega(S0, K, r, y, sigma, T):
    
    # Increment volatility change by .001
    dsigma = .001
    dp = get_call_price(S0, K, r, y, sigma + dsigma, T) - get_call_price(S0, K, r, y, sigma, T)
    
    return(dp/dsigma)


def get_put_vega(S0, K, r, y, sigma, T):
    
    # Increment volatility change by .001
    dsigma = .001
    dp = get_put_price(S0, K, r, y, sigma + dsigma, T) - get_call_price(S0, K, r, y, sigma, T)
    
    return(dp/dsigma)


def get_call_theta(S0, K, r, y, sigma, T):
    
    # Increment volatility change by .001
    dT = .01
    dp = get_call_price(S0, K, r, y, sigma, T + dT) - get_call_price(S0, K, r, y, sigma, T)
    
    return(dp/dT)


def get_put_theta(S0, K, r, y, sigma, T):
    
    # Increment volatility change by .001
    dT = .01
    dp = get_put_price(S0, K, r, y, sigma, T + dT) - get_put_price(S0, K, r, y, sigma, T)
    
    return(dp/dT)


def get_call_rho(S0, K, r, y, sigma, T):
    
    # Increment volatility change by .001
    dr = .001
    dp = get_call_price(S0, K, r + dr, y, sigma, T) - get_call_price(S0, K, r, y, sigma, T)
    
    return(dp/dr)


def get_put_rho(S0, K, r, y, sigma, T):
    
    # Increment volatility change by .001
    dr = .001
    dp = get_put_price(S0, K, r + dr, y, sigma, T) - get_put_price(S0, K, r, y, sigma, T)
    
    return(dp/dr)


# Create main window
root = Tk()
root.title('Numeric Input Plotter')

# Frame for input fields
input_frame = Frame(root)
input_frame.pack(padx=10, pady=10)

# Create and place input fields
Label(input_frame, text="Spot Price:").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(input_frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

Label(input_frame, text="Strike Price:").grid(row=1, column=0, padx=5, pady=5)
entry2 = Entry(input_frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

Label(input_frame, text="Interest Rate:").grid(row=2, column=0, padx=5, pady=5)
entry3 = Entry(input_frame)
entry3.grid(row=2, column=1, padx=5, pady=5)

Label(input_frame, text="Yield:").grid(row=3, column=0, padx=5, pady=5)
entry4 = Entry(input_frame)
entry4.grid(row=3, column=1, padx=5, pady=5)

Label(input_frame, text="Volatility:").grid(row=4, column=0, padx=5, pady=5)
entry5 = Entry(input_frame)
entry5.grid(row=4, column=1, padx=5, pady=5)

Label(input_frame, text="Time to Maturity (Years):").grid(row=5, column=0, padx=5, pady=5)
entry6 = Entry(input_frame)
entry6.grid(row=5, column=1, padx=5, pady=5)

Label(input_frame, text="Option Type:").grid(row=6, column=0, padx=5, pady=5)
combo_box1 = ttk.Combobox(input_frame, values=["Call", "Put"])
combo_box1.grid(row=6, column=1, padx=5, pady=5)
combo_box1.current(0)  # Set the default value

Label(input_frame, text="Greek Type:").grid(row=7, column=0, padx=5, pady=5)
combo_box2 = ttk.Combobox(input_frame, values=["Price", "Delta", "Gamma", "Vega", "Theta", "Rho"])
combo_box2.grid(row=7, column=1, padx=5, pady=5)
combo_box2.current(0)  # Set the default value

# Submit button
submit_button = Button(root, text="Generate Plot", command=plot_graph)
submit_button.pack(pady=10)

# Frame for plot
plot_frame = Frame(root)
plot_frame.pack(fill=BOTH, expand=True)

# Result label
result_label = Label(root, text="")
result_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
