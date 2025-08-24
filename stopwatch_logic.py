counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string
            label['text'] = display
            label.after(1000, count)
            counter += 1
    count()


def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


def Reset(label):
    global counter
    counter = 0
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    else:
        label['text'] = '00:00:00'
