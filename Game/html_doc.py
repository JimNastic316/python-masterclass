#8:00 sect 317
class Tag():

    def __init__(self, name, contents):
        self-start_tag = '<{}'.format(name)
        self.end_tag = '</{}>'.format(name)
        se;f.contenst = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

