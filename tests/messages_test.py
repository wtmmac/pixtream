import unittest
import random
import string

from pixtream.peer import specs
from pixtream.peer.messages import Message

class HandShakeMessageTest(unittest.TestCase):
    def test_iomessage(self):
        peer_id = ''.join(random.choice(string.letters) for _ in range(20))

        handshake = specs.HandshakeMessage.create(peer_id)

        bytes = handshake.pack()
        new_handshake = Message.parse(bytes)

        self.assert_(new_handshake.is_valid())
        self.assertEqual(new_handshake.peer_id, peer_id)

    def test_prefix(self):
        peer_id = ''.join(random.choice(string.letters) for _ in range(20))

        handshake = specs.HandshakeMessage.create(peer_id)

        bytes = handshake.pack()
        prefixed_bytes = handshake.pack_prefixed()

        self.assertEqual(prefixed_bytes[:4], '\x00\x00\x00.')
        self.assertEqual(prefixed_bytes[4:], bytes)

    def test_identity(self):
        peer_id = ''.join(random.choice(string.letters) for _ in range(20))

        handshake = specs.HandshakeMessage.create(peer_id)

        bytes = handshake.pack()
        new_handshake = Message.parse(bytes)

        self.assert_(isinstance(new_handshake, specs.HandshakeMessage))

if __name__ == '__main__':
    unittest.main()

