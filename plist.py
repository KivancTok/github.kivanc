import datetime


class Patient:
    def __init__(self, name, appt=None):
        self.name = name
        self.appt = appt  # appointment
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.prev_enqueued = None

        self.enqueued = 0

    def is_empty(self):
        return self.first is None

    def print(self):
        printval = self.first

        while printval is not None:
            print('name:', printval.name, 'appointment:', printval.appt)
            printval = printval.next

    def length(self):
        length = 0
        lenval = self.first

        while lenval is not None:
            lenval = lenval.next
            length += 1

        return length

    def enqueue_patient(self, patient):
        # YOUR CODE HERE
        if self.length() == 0:
            self.first = Patient(patient['last name'], patient['appt'])
            self.prev_enqueued = self.first

        else:
            self.last = Patient(patient['last name'], patient['appt'])
            self.prev_enqueued.next = self.last
            self.prev_enqueued = self.last

    def sort(self):
        # YOUR CODE HERE
        patients = []
        pat = self.first

        while pat is not None:
            patients.append(pat)
            pat = pat.next

        patients.sort(key=lambda x: x.appt)

        self.first = None
        self.last = None

        for i in [{'last name': p.name, 'appt': p.appt} for p in patients]:
            self.enqueue_patient(i)

    def insert_correct_pos(self, patient):
        self.enqueue_patient(patient)
        self.sort()


def create_queue(patients):
    queue = Queue()
    for patient in patients:
        queue.enqueue_patient(patient)

    return queue
