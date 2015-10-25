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

    def setDirectMessageReceived(self, agent, num_id, message):
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

    def testDirectMessage(self):
        """
        Tests that direct messages can be sent.
        """
        self.client1.bind_direct_msg(self.setDirectMessageReceived)
        self.waitForNetwork()
        self.client2.send_direct_message("client1", 1, "secret message")
        self.waitForNetwork()

        self.assertEqual(self.message, "secret message")

    def testListMessage(self):
        """
        Tests that lists can be sent as direct messages (an extension 
        of the ivy protocol implemented on Python only).
        """
        self.client1.bind_direct_msg(self.setDirectMessageReceived)
        self.waitForNetwork()
        self.client2.send_direct_message("client1", 1, ["list", "message"])
        self.waitForNetwork()

        self.assertEqual(self.message, ["list", "message"])

    def tearDown(self):
        self.client1.stop()
        self.client2.stop()
        self.waitForNetwork()