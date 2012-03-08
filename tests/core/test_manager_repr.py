# Module:   test_manager_repr
# Date:     23rd February 2010
# Author:   James Mills, prologic at shortcircuit dot net dot au

"""Manager Repr Tests

Test Manager's representation string.
"""

import os
from time import sleep
from threading import current_thread

import pytest

from circuits import Event, Component, BaseManager

class App(Component):

    def test(self, event, *args, **kwargs):
        pass

class Test(Event):
    pass


def test():
    id = "%s:%s" % (os.getpid(), current_thread().getName())

    m = BaseManager()
    assert repr(m) == "<BaseManager %s (queued=0) [S]>" % id

    app = App()
    app.register(m)
    s = repr(m)
    assert s == "<BaseManager %s (queued=1) [S]>" % id

    m.start()

    pytest.wait_for(m, "_running", True)

    s = repr(m)
    assert s == "<BaseManager %s (queued=0) [R]>" % id

    m.stop()

    pytest.wait_for(m, "_running", False)

    s = repr(m)
    assert s == "<BaseManager %s (queued=0) [S]>" % id
