# Problem 7
# Request Routing in a Web Server with a Trie

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None, description = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler, description)

    def insert(self, path, description):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for i in path:
            current_node.insert(i)
            current_node = current_node.children[i]
        current_node.is_handler = True
        current_node.description = description

    def find(self, match_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for i in match_path:
            if i in current_node.children:
                current_node = current_node.children[i]
            else:
                return None
        return current_node

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None, description = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.is_handler = False
        self.handler = handler
        self. description = description

    def insert(self, handler):
        # Insert the node as before
        for i in handler.split('/'):
            if i not in self.children:
                self.children[i] = RouteTrieNode()

        # The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, description):
        self.trie = RouteTrie(handler, description)

    def add_handler(self, handler, description):
        if isinstance(handler, str) is False:
            print('Please input a handler again.')
            return
        elif '/' not in [x for x in handler]:
            print('Please input a handler again.')
            return

        path_parts = self.split_path(handler)
        self.trie.insert(path_parts, description)

    def lookup(self, path):
        try:
            ans = self.trie.find(self.split_path(path)).description
        except:
            ans = None

        if path == '/':
            ans = self.trie.root.handler

        return ans


    def split_path(self, path):
        if not isinstance(path, str):
            return None

        return path.split('/')


# Test cases:

# Router and route 1:
router = Router("root handler","not found handler")
# add a router

router.add_handler("/home/about", "about handler")
# add a route

print(router.lookup("/"))
# should print 'root handler'

print(router.lookup("/home"))
# should print None

print(router.lookup("/home/about"))
# should print 'about handler'

print(router.lookup("/home/about/"))
# should print None

print(router.lookup("/home/about/me"))
# should print None

# Router and route 2:
router = Router("root handler", 'not found handler')
# add a router

router.add_handler("/home", "No handler")
# add a route

router.add_handler("/home/about/", "No handler")
# add a route

router.add_handler(None, "No handler")
# add an edge case route here. Attempting to add None as a router, should return
# a print "Please input a handler again"

router.add_handler("hello", "No handler")
# add an edge case route here. Attempting to add None as a router, should return
# a print "Please input a handler again"

print(router.lookup("/"))
# should print 'root handler'

print(router.lookup("/home"))
# should print "No handler"

# Test case 3:

router = Router("root handler", "not found handler")
# add a router
router.add_handler("/main/contact", "contact handler")
# add a route
router.add_handler("/main/about", "about handler")
# add a route
router.add_handler("/main/past clients", "past clients handler")
# add a route
router.add_handler("/main/past clients/1", "past clients: 1 handler")
# add a route
router.add_handler("/main/past clients/1/a", "past clients: 1a handler")
# add a route

# some lookups with the expected output
print(router.lookup("/"))
# should print 'root handler'
print(router.lookup("/main"))
# should print None
print(router.lookup("/main/contact"))
# should print 'contact handler'
print(router.lookup("/main/about"))
# should print 'about handler'
print(router.lookup("/main/past clients"))
# should print 'past clients handler'
print(router.lookup("/main/past clients/1"))
# should print 'past clients: 1 handler'
print(router.lookup("/main/past clients/1/a"))
# should print 'past clients: 1a handler'

# Handling unavailable links
print(router.lookup("/main/contact/"))
# should print None
print(router.lookup("/main/contact/me"))
# should print None
print(router.lookup("/main/past clients/1/a/"))
# should print None




