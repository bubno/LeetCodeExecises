from line_profiler import LineProfiler
from Ex_27_RemoveElement import Solution

sol = Solution()
NUM_OF_ITERS = 100000

def main_func():

    for i in range(NUM_OF_ITERS):
        sol.removeElement(**sol.params)
        sol.removeElementOptimal(**sol.params)


lprofiler = LineProfiler()
lprofiler.add_function(sol.removeElement)
lprofiler.add_function(sol.removeElementOptimal)
lp_wrapper = lprofiler(main_func)

lp_wrapper()
lprofiler.print_stats()

