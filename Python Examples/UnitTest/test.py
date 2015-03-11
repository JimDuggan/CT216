import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
import uuid

from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line



@gen.coroutine
def consume():
    print "hello"

def generateSquares(N):
    print "Here in the function"
    for i in range(N):
        print "here in the loop..."
        yield i ** 2


G = generateSquares(5)

# G is now a generator
print "Before we call next"

for g in G:
    print g






