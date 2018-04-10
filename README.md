Echo Server Homework
==================

Your task is to build a simple "echo" server.

* The server should automatically return to any client that connects exactly what it receives (it should echo all messages).
* You will also write a python script that, when run, will send a message to the server and receive the reply, printing it to stdout.
* Finally, you’ll do all of the above in such a way that it can be tested.

Required Tasks:
---------------

* Complete the code in ``echo_server.py`` to create a server that sends back
  whatever messages it receives from a client

* Complete the code in ``echo_client.py`` to create a client function that
  can send a message and receive a reply.

* Ensure that the tests in ``tests.py`` pass.

To Try it Out:
--------------
* Open one terminal while in this folder and execute this command:

  `$ python echo_server.py`
   
* Open a second terminal in this same folder and execute this command:

  `$ python echo_client.py "This is a test message."`
  
Once all tasks are completed, the server should print out a message indicating the message that it received from the client, and the client should print out a message indicating that it received the message back from the server.

To Run the Tests:
-----------------

* Open one terminal while in this folder and execute this command:

    `$ python echo_server.py`

* Open a second terminal in this same folder and execute this command:

    `$ python tests.py`


Hints:
-----

Look at `demo_client.py` and `demo_server.py`. These demonstrate basic client/server communication as shown in class. You can play the short video `demo_client_server_behavior.mp4` to see an example how these two files can be called to work together.

To complete the assignment in `echo_server.py` and `echo_client.py`, you'll be using MOST of the same lines of code. The main difference is that the `echo_server`:

  1. Has an outer loop that accepts a connection from a client, processes a message from that client, closes the client connection, and then repeats.
  2. Has an inner loop that pulls bytes off the client connection 16 bytes at a time.
  3. Also, you're putting all of this code lives inside of a function named `server`.

One more hint: how do you know when you're done pulling 16 byte chunks off of the client connection? You're done with `recv` returns fewer than 16 bytes.


Optional Tasks:
---------------

Simple:

* Write a python function that lists the services provided by a given range of
  ports.

  * accept the lower and upper bounds as arguments
  * provide sensible defaults
  * Ensure that it only accepts valid port numbers (0-65535)

Challenging:

* The echo server as outlined will only process a connection from one client
  at a time. If a second client were to attempt a connection, it would have to
  wait until the first message was fully echoed before it could be dealt with.

  Python provides a module called `select` that allows waiting for I/O events
  in order to control flow. The `select.select` method can be used to allow
  our echo server to handle more than one incoming connection in "parallel".

  Read the documentation about the `select` module
  (http://docs.python.org/3/library/select.html) and attempt to write a second
  version of the echo server that can handle multiple client connections in
  "parallel".  You do not need to invoke threading of any kind to do this.
