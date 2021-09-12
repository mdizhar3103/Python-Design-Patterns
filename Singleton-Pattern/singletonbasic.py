import sys 
print(sys.version) 
 
# singleton_classic.py
class Singleton(object):
    ans = None
 
    @staticmethod
    def instance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance
 
s1 = Singleton.instance()
s2 = Singleton.instance()
print(s1 is s2)
s1.ans = 72 
print(s1.ans == s2.ans)

