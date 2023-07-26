import mido
msg = mido.Message('note_on', note=60)
print(msg.type)
msg.copy(channel=2)
port = mido.open_output()
port.send(msg)