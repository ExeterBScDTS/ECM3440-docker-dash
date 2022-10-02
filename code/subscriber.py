import os
from re import S
from azure.servicebus import ServiceBusClient
import json

def sb_connect(con_str, topic_name, subscription_name):
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=con_str)
    receiver = servicebus_client.get_subscription_receiver(
        topic_name=topic_name,
        subscription_name=subscription_name
    )
    return receiver

def sb_messages(receiver):
    messages = []
    received_msgs = receiver.receive_messages(max_message_count=100, max_wait_time=2)
    for msg in received_msgs:
            nmsg = json.loads(str(msg))
            # application_properties is a dictionary with byte key value pairs
            # Use .decode() to convert the values to strings
            # See https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceivedmessage?view=azure-dotnet-preview
            nmsg['device_id'] = msg.application_properties[b'iothub-connection-device-id'].decode()
            nmsg['time'] = msg.application_properties[b'iothub-enqueuedtime'].decode()
            messages.append(nmsg)
            receiver.complete_message(msg)
    return messages

if __name__ == '__main__':
    topic = os.getenv('SERVICE_BUS_TOPIC')
    sub = os.getenv('SERVICE_BUS_SUBSCRIPTION')
    connection = os.getenv('SERVICE_BUS_CONNECTION')

    receiver = sb_connect(connection, topic, sub)
    msgs = sb_messages(receiver)
    print(msgs)

    receiver.close()
    print("Receive is done.")
