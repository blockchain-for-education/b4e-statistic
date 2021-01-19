# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='voting.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cvoting.proto\"\x9a\x03\n\x06Voting\x12\x1a\n\x12\x65lector_public_key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\'\n\x0bvote_result\x18\x03 \x01(\x0e\x32\x12.Voting.VoteResult\x12\x1c\n\x14\x63lose_vote_timestamp\x18\x04 \x01(\x04\x12\"\n\x08voteType\x18\x05 \x01(\x0e\x32\x10.Voting.VoteType\x12\x1a\n\x04vote\x18\x06 \x03(\x0b\x32\x0c.Voting.Vote\x12\x11\n\ttimestamp\x18\x07 \x01(\x04\x12\x16\n\x0etransaction_id\x18\x08 \x01(\t\x1a^\n\x04Vote\x12\x19\n\x11issuer_public_key\x18\x01 \x01(\t\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x02 \x01(\x08\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x16\n\x0etransaction_id\x18\x04 \x01(\t\"&\n\x08VoteType\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0e\n\nNOT_ACTIVE\x10\x01\",\n\nVoteResult\x12\x07\n\x03WIN\x10\x00\x12\x08\n\x04LOSE\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\"+\n\x0fVotingContainer\x12\x18\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x07.Votingb\x06proto3')
)



_VOTING_VOTETYPE = _descriptor.EnumDescriptor(
  name='VoteType',
  full_name='Voting.VoteType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=343,
  serialized_end=381,
)
_sym_db.RegisterEnumDescriptor(_VOTING_VOTETYPE)

_VOTING_VOTERESULT = _descriptor.EnumDescriptor(
  name='VoteResult',
  full_name='Voting.VoteResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WIN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOSE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=383,
  serialized_end=427,
)
_sym_db.RegisterEnumDescriptor(_VOTING_VOTERESULT)


_VOTING_VOTE = _descriptor.Descriptor(
  name='Vote',
  full_name='Voting.Vote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issuer_public_key', full_name='Voting.Vote.issuer_public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accepted', full_name='Voting.Vote.accepted', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Voting.Vote.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='Voting.Vote.transaction_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=341,
)

_VOTING = _descriptor.Descriptor(
  name='Voting',
  full_name='Voting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elector_public_key', full_name='Voting.elector_public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='Voting.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vote_result', full_name='Voting.vote_result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_vote_timestamp', full_name='Voting.close_vote_timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voteType', full_name='Voting.voteType', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vote', full_name='Voting.vote', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Voting.timestamp', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='Voting.transaction_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VOTING_VOTE, ],
  enum_types=[
    _VOTING_VOTETYPE,
    _VOTING_VOTERESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=427,
)


_VOTINGCONTAINER = _descriptor.Descriptor(
  name='VotingContainer',
  full_name='VotingContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='VotingContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=472,
)

_VOTING_VOTE.containing_type = _VOTING
_VOTING.fields_by_name['vote_result'].enum_type = _VOTING_VOTERESULT
_VOTING.fields_by_name['voteType'].enum_type = _VOTING_VOTETYPE
_VOTING.fields_by_name['vote'].message_type = _VOTING_VOTE
_VOTING_VOTETYPE.containing_type = _VOTING
_VOTING_VOTERESULT.containing_type = _VOTING
_VOTINGCONTAINER.fields_by_name['entries'].message_type = _VOTING
DESCRIPTOR.message_types_by_name['Voting'] = _VOTING
DESCRIPTOR.message_types_by_name['VotingContainer'] = _VOTINGCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Voting = _reflection.GeneratedProtocolMessageType('Voting', (_message.Message,), dict(

  Vote = _reflection.GeneratedProtocolMessageType('Vote', (_message.Message,), dict(
    DESCRIPTOR = _VOTING_VOTE,
    __module__ = 'voting_pb2'
    # @@protoc_insertion_point(class_scope:Voting.Vote)
    ))
  ,
  DESCRIPTOR = _VOTING,
  __module__ = 'voting_pb2'
  # @@protoc_insertion_point(class_scope:Voting)
  ))
_sym_db.RegisterMessage(Voting)
_sym_db.RegisterMessage(Voting.Vote)

VotingContainer = _reflection.GeneratedProtocolMessageType('VotingContainer', (_message.Message,), dict(
  DESCRIPTOR = _VOTINGCONTAINER,
  __module__ = 'voting_pb2'
  # @@protoc_insertion_point(class_scope:VotingContainer)
  ))
_sym_db.RegisterMessage(VotingContainer)


# @@protoc_insertion_point(module_scope)
