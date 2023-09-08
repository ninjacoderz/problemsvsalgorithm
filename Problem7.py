class RouteTrieNode:
    def __init__(self):
        self.childrens = {}
        self.handler = None

    def insert(self, path):
        self.childrens[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path, handler):
        current_node = self.root
        for item in path:
            current_node.insert(item)
            current_node = current_node.childrens[item]
        current_node.handler = handler

    def find(self, path):
        current_node = self.root
        for item in path:
            if item not in current_node.childrens:
                return None
            current_node = current_node.childrens[item]
        return current_node.handler


class Router:
    def __init__(self, handler):
        self.router = RouteTrie(handler)
        self.error = "not found handler"

    def add_handler(self, path, handler):
        path = self.split_path(path)
        self.router.insert(path, handler)

    def lookup(self, path):
        path = self.split_path(path)
        if path is None:
            return self.error
        if len(path) == 0:
            return self.router.handler
        output = self.router.find(path)
        if output is None:
            return self.error
        return output

    def split_path(self, path):
        output = []
        items = path.split('/')
        for item in items:
            if item != '':
                output.append(item)
        return output

# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
