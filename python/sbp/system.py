#!/usr/bin/env python
# Copyright (C) 2015 Swift Navigation Inc.
# Contact: Fergus Noble <fergus@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.


"""
Standardized system messages from Swift Navigation devices.
"""

from construct import *
import json
from sbp.msg import SBP, SENDER_ID, TYPES_NP, TYPES_KEYS_NP
from sbp.utils import fmt_repr, exclude_fields, walk_json_dict, containerize,\
                      greedy_string
import numpy as np
import traceback

# Automatically generated from piksi/yaml/swiftnav/sbp/system.yaml with generate.py.
# Please do not hand edit!


SBP_MSG_STARTUP = 0xFF00
class MsgStartup(SBP):
  """SBP class for message MSG_STARTUP (0xFF00).

  You can have MSG_STARTUP inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The system start-up message is sent once on system
start-up. It notifies the host or other attached devices that
the system has started and is now ready to respond to commands
or configuration requests.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  cause : int
    Cause of startup
  startup_type : int
    Startup type
  reserved : int
    Reserved
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgStartup",
                   ULInt8('cause'),
                   ULInt8('startup_type'),
                   ULInt16('reserved'),)
  __slots__ = [
               'cause',
               'startup_type',
               'reserved',
              ]
  __zips__ = [
              ( 'u8', 'cause'),
              ( 'u8', 'startup_type'),
              ( 'u16', 'reserved'),
             ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgStartup,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgStartup, self).__init__()
      self.msg_type = SBP_MSG_STARTUP
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.cause = kwargs.pop('cause')
      self.startup_type = kwargs.pop('startup_type')
      self.reserved = kwargs.pop('reserved')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return MsgStartup.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return MsgStartup(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    try:
      self._from_binary(d)
    except:
      print traceback.print_exc()

  def __getitem__(self, item):
    return getattr(self, item)

  def _get_embedded_type(self, t):
    return globals()[t]

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgStartup._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgStartup, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_DGNSS_STATUS = 0xFF02
class MsgDgnssStatus(SBP):
  """SBP class for message MSG_DGNSS_STATUS (0xFF02).

  You can have MSG_DGNSS_STATUS inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message provides information about the receipt of Differential
corrections.  It is expected to be sent with each receipt of a complete
corrections packet.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  flags : int
    Status flags
  latency : int
    Latency of observation receipt
  num_signals : int
    Number of signals from base station
  source : string
    Corrections source string
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgDgnssStatus",
                   ULInt8('flags'),
                   ULInt16('latency'),
                   ULInt8('num_signals'),
                   greedy_string('source'),)
  __slots__ = [
               'flags',
               'latency',
               'num_signals',
               'source',
              ]
  __zips__ = [
              ( 'u8', 'flags'),
              ( 'u16', 'latency'),
              ( 'u8', 'num_signals'),
              ( 'str', 'source'),
             ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgDgnssStatus,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgDgnssStatus, self).__init__()
      self.msg_type = SBP_MSG_DGNSS_STATUS
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.flags = kwargs.pop('flags')
      self.latency = kwargs.pop('latency')
      self.num_signals = kwargs.pop('num_signals')
      self.source = kwargs.pop('source')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return MsgDgnssStatus.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return MsgDgnssStatus(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    try:
      self._from_binary(d)
    except:
      print traceback.print_exc()

  def __getitem__(self, item):
    return getattr(self, item)

  def _get_embedded_type(self, t):
    return globals()[t]

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgDgnssStatus._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgDgnssStatus, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_HEARTBEAT = 0xFFFF
class MsgHeartbeat(SBP):
  """SBP class for message MSG_HEARTBEAT (0xFFFF).

  You can have MSG_HEARTBEAT inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The heartbeat message is sent periodically to inform the host
or other attached devices that the system is running. It is
used to monitor system malfunctions. It also contains status
flags that indicate to the host the status of the system and
whether it is operating correctly. Currently, the expected
heartbeat interval is 1 sec.

The system error flag is used to indicate that an error has
occurred in the system. To determine the source of the error,
the remaining error flags should be inspected.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  flags : int
    Status flags
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgHeartbeat",
                   ULInt32('flags'),)
  __slots__ = [
               'flags',
              ]
  __zips__ = [
              ( 'u32', 'flags'),
             ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgHeartbeat,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgHeartbeat, self).__init__()
      self.msg_type = SBP_MSG_HEARTBEAT
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.flags = kwargs.pop('flags')

  def __repr__(self):
    return fmt_repr(self)

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    return MsgHeartbeat.from_json_dict(d)

  @staticmethod
  def from_json_dict(d):
    sbp = SBP.from_json_dict(d)
    return MsgHeartbeat(sbp, **d)

 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    try:
      self._from_binary(d)
    except:
      print traceback.print_exc()

  def __getitem__(self, item):
    return getattr(self, item)

  def _get_embedded_type(self, t):
    return globals()[t]

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgHeartbeat._parser.build(c)
    return self.pack()

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgHeartbeat, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    

msg_classes = {
  0xFF00: MsgStartup,
  0xFF02: MsgDgnssStatus,
  0xFFFF: MsgHeartbeat,
}