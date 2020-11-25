from demo.QAOA.qaoa import QAOAOptimizer


# this is a circular loop graph with max cut?
a = {(i, (i + 1) % 30): [[1, -1], [-1, 1]] for i in range(30)}
q = QAOAOptimizer(a, num_layers=2)
q.preprocess()
q.optimize()
