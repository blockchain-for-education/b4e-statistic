# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

from addressing.b4e_addressing import addresser
from addressing.b4e_addressing.addresser import AddressSpace
from protobuf.b4e_protobuf.actor_pb2 import ActorContainer
from protobuf.b4e_protobuf.b4e_environment_pb2 import B4EEnvironmentContainer
from protobuf.b4e_protobuf.voting_pb2 import VotingContainer
from protobuf.b4e_protobuf.class_pb2 import ClassContainer
from protobuf.b4e_protobuf.record_pb2 import RecordContainer

CONTAINERS = {
    AddressSpace.ACTOR: ActorContainer,
    AddressSpace.RECORD: RecordContainer,
    AddressSpace.CLASS: ClassContainer,
    AddressSpace.VOTING: VotingContainer,
    AddressSpace.ENVIRONMENT: B4EEnvironmentContainer
}


def deserialize_data(address, data):
    """Deserializes state data by type based on the address structure and
    returns it as a dictionary with the associated data type

    Args:
        address (str): The state address of the container
        data (str): String containing the serialized state data
    """
    data_type = addresser.get_address_type(address)

    if data_type == AddressSpace.OTHER_FAMILY:
        return []

    try:
        container = CONTAINERS[data_type]
    except KeyError:
        raise TypeError('Unknown data type: {}'.format(data_type))

    entries = _parse_proto(container, data).entries
    return data_type, [_convert_proto_to_dict(pb) for pb in entries]


def _parse_proto(proto_class, data):
    deserialized = proto_class()
    deserialized.ParseFromString(data)
    return deserialized


def _convert_proto_to_dict(proto):
    result = {}

    for field in proto.DESCRIPTOR.fields:
        key = field.name
        value = getattr(proto, key)

        if field.type == field.TYPE_MESSAGE:
            if field.label == field.LABEL_REPEATED:
                result[key] = [_convert_proto_to_dict(p) for p in value]
            else:
                result[key] = _convert_proto_to_dict(value)

        elif field.type == field.TYPE_ENUM:
            number = int(value)
            name = field.enum_type.values_by_number.get(number).name
            result[key] = name

        else:
            result[key] = value

    return result
