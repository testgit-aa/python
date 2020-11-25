


def construct_trees(nodes:list):

    """
    given the following list where the first item in the tuple is the node_id and 
    the second item is the node_id of the parent; (NODE_ID, PARENT_NODE_ID)
    
    nodes = [
                ("node1", "node1"),
                ("node2", "node1"),
                ("node3", "node8"),
                ("node4", "node2"),
                ("node5", "node1"),
                ("node6", "node7"),
                ("node7", "node7"),
                ("node8", "node9"),
                ("node9", "node6"),
                ]

    create the following nested dict:

    {
        "node1": {
                    "node2": {
                                "node4":
                                        {
                                        
                                        }
                                },
                    "node5": {},

                    },
        "node7": {
                    "node6":{
                                "node9":
                                        {
                                            "node8":{
                                                        "node3":{}
                                                    }
                                        }
                                }

                    }
 
        }

    Restrictions
    1) place_node() should be a recusive function
    
    Tips!
        - let construct_trees() run until all nodes are places, or until there are no more
        nodes to place!
        - you might need a special condition to deal with the root of trees, e.g, nodes that have themselves as parents.

    """

    def place_node():
        #FIX THIS FUCNTION
   
             
    #FIX THIS FUCNTION
    pass
        

