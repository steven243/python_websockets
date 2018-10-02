import pusher

pusher_client = pusher.Pusher(
  app_id='612854',
  key='94ae683153c18182d415',
  secret='f3d994bfcd90e2e57875',
  cluster='mt1',
  ssl=True
)

i = 0
while True:
    i+= 1
    pusher_client.trigger('my-channel', 'my-event', {'sl': i, 'sw': i, 'pl': i, 'pw': i})
    break
