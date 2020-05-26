#! /usr/bin/env python3.8

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        def _insert(path_list, curr_index, handler, node):
            path_item = path_list[curr_index]
            last_index = len(path_list) - 1

            if curr_index == last_index:
                leaf = node.insert(path_item)
                leaf.handler = handler
                return leaf

            next_node = node.insert(path_item)
            _insert(path_list, curr_index+1, handler, next_node)
        
        node = self.root
        _insert(path_list, 0, handler, node)

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        def _find(path_list, curr_index, node):
            path_item = path_list[curr_index] 
            next_node = node.children.get(path_item)
            if not next_node:
                return None
            if curr_index == len(path_list)-1:
                return next_node.handler
            return _find(path_list, curr_index+1, next_node)
        
        return _find(path_list, 0, self.root)

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path_item):
        # Insert the node as before
        new_node = RouteTrieNode()
        self.children[path_item] = new_node

        return new_node



# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, route_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_handler = route_handler
        self.not_found_handler = not_found_handler
        self.route_trie = RouteTrie()

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route_trie.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return self.route_handler

        path_list = self.split_path(path)
        found = self.route_trie.find(path_list)

        return found if found else self.not_found_handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split("/")
        route_slash = path_list[0]
        if path_list[-1] == "":
            return path_list[1:-1]
        else:
            return path_list[1:]


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root_handler", "not_found_handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about_handler")  # add a route
router.add_handler("/one/two/three/", "three_handler")


test_cases = (
    ("/", "root_handler"),
    ("/home/about", "about_handler"),
    ("/home", "not_found_handler"),
    ("/home/about", "about_handler"),
    ("/home/about/", "about_handler"),
    ("/home/about/me", "not_found_handler"),
    ("/one/two/three/", "three_handler"),
    ("/one/two/three/four/", "not_found_handler")
)

def test(test_cases, router):
    for case in test_cases:
        path, handler = case
        assert router.lookup(path) == handler

test(test_cases, router)