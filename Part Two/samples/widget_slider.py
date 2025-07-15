## This is course material for Introduction to Python Scientific Programming
## Example code: widget_slider.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# Create initial plot and values
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5; f0 = 3; delta_f = 0.1; delta_a = 0.1
s = a0 * np.sin(2 * np.pi * f0 * t)
l, = plt.plot(t, s, lw=2)       # tell pyplot to return something so that when user updates the plot, it can update the line
ax.margins(x=0)

# Create two sliders
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)       # these numbers are the position of the slider in the figure
                                                                    # relative to the entire window of the figure
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0, valstep=delta_a)

# slider update actions
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))         # update the y-data of the line object l
    fig.canvas.draw_idle()      # update an already existing figure

sfreq.on_changed(update)        # will call update function when slider only when the slider's value changes
samp.on_changed(update)         # on_changed is a method that takes a function as an argument
                                # which will be called when the slider's value changes
                                # (an event handler)

# Create a radio button
rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)       # rax is the position of where the radio button will be placed
l.set_color(radio.value_selected)
# radio button update actions
def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()

radio.on_clicked(colorfunc)     # another event handler that will call colorfunc when the radio button is clicked

plt.show()
