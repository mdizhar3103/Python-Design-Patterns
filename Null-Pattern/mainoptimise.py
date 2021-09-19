from optimizedfactory import MyObjectFactory

myobj = MyObjectFactory.create_object("myclass")
myobj.do_something("something")
myobj = MyObjectFactory.create_object("myanotherclass")
myobj.do_something("something")
