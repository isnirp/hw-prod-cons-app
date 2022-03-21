## hw-prod-cons-app

producer consumer app

## why this approach

I understand a Queue is the preferred data structure for this implement. But a Queue is already thread safe and using that in this application won't capture the whole point since the producer and consumer objects are relatively simple.
I decided to use a list and ensure it was thread safe for the application.

## possible downfalls

I made some assumptions based on the requirements of the application in order to keep it simple. I assumed a producer produces a single name through the process. In situations where the producer should produce more names, the producer object and consumer object would have to be updated. Also the pop method for the list won't be the right method if the queue should take multiple names since we are interested in FIFO.

## how to run app

python dummy_app.py

you can also simply build and run the docker image

## how to run test

python test_dummy_app.py
