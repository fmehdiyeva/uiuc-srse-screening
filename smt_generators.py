from z3 import Int, Solver, sat

def generate_small_int():
    x = Int('x')
    s = Solver()
    s.add(x >= 0, x <= 10)
    if s.check() == sat:
        return s.model()[x]
    return None


def generate_timestamp():
    ts = Int('ts')
    s = Solver()
    s.add(ts >= -11676096000, ts <= 253402300799000)
    if s.check() == sat:
        return s.model()[ts]
    return None


def generate_range_bounds():
    lower, upper = Int('lower'), Int('upper')
    s = Solver()

    s.add(lower >= -1000, lower <= 1000)
    s.add(upper >= -1000, upper <= 1000)
  
    s.add(lower < upper)
    
    if s.check() == sat:
        m = s.model()
        return m[lower], m[upper]
    return None

if __name__ == "__main__":
    print(f"SMT Small Int: {generate_small_int()}")
    print(f"SMT Timestamp: {generate_timestamp()}")
    print(f"SMT Range Bounds (lower, upper): {generate_range_bounds()}")