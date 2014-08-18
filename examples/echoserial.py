#!/usr/bin/env python


"""Simple Serial Example

This example shows how to use the ``circuits.io.Serial`` Component
to access serial data. This example simply echos back what it receives
on the serial port.

.. warning:: THis example is currently untested.
"""


from circuits.io import Serial
from circuits.io.events import write
from circuits import handler, Component, Debugger


class EchoSerial(Component):

    def init(self, port):
        Serial(port).register(self)

    @handler("read")
    def on_read(self, data):
        """Read Event Handler

        This is fired by the underlying Serial Component when there has been
        new data read from the serial port.
        """

        self.fire(write(data))


# Start and "run" the system.
# Bind to port 0.0.0.0:8000
app = EchoSerial("/dev/ttyS0")
Debugger().register(app)
app.run()
