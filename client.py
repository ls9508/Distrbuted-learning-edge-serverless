class client:

    def __init__(self,loc,f):
        self.loc = loc
        self.func = f
        self.access = None
        self.due=0
        self.latency = 0

