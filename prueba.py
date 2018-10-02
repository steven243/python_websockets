import pusher

pusher_client = pusher.Pusher(
  app_id="611990",
  key="22f110291d714ce8eaaa",
  secret="f4ab8cbd732e3e6b49d7",
  cluster="mt1",
  ssl=True
)

i = 0
while True:
    i+= 1
    pusher_client.trigger('my-channel', 'my-event', {'sl': i, 'sw': i, 'pl': i, 'pw': i})
