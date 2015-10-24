import unittest

import time

from ivy.ivy import IvyServer

class BaseTestCase(unittest.TestCase):
    def waitForNetwork(self):
        """
        Wait a small amount of time to allow local network communication
        to finish.
        """
        time.sleep(0.1)

class EndToEndTestCase(BaseTestCase):
    def setUp(self):
        self.client1 = IvyServer("client1")
        self.client2 = IvyServer("client2")

        self.client1.start()
        self.client2.start()

        self.message = None

    def setMessageReceived(self, agent, message):
        self.message = message

    def testMessageMatches(self):
        """
        Tests that the message is received by client1 when it matches
        the regex.
        """
        self.client1.bind_msg(self.setMessageReceived, "message (.*)")
        self.waitForNetwork()
        self.client2.send_msg("message value")
        self.waitForNetwork()

        self.assertEqual(self.message, "value")

    def testMessageDoesntMatch(self):
        """
        Tests that no message is sent when the regex doesn't match.
        """
        self.client1.bind_msg(self.setMessageReceived, "foo (.*)")
        self.waitForNetwork()
        self.client2.send_msg("bar value")
        self.waitForNetwork()

        self.assertEqual(self.message, None)

    def tearDown(self):
        self.client1.stop()
        self.client2.stop()
        self.waitForNetwork()