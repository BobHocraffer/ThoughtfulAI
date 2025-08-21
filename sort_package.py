#Created using LLM, so I left in the ternary operator. Reviewed and tested with my caring human hands
def sort(width, height, length, mass):
    # Validate inputs: ensure all are numeric and non-negative
    try:
        width = float(width)
        height = float(height)
        length = float(length)
        mass = float(mass)
    except (TypeError, ValueError):
        return "REJECTED"
    
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        return "REJECTED"
    
    # Check if package is bulky
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Use ternary operator to determine stack
    return ("REJECTED" if is_bulky and is_heavy else
            "SPECIAL" if is_bulky or is_heavy else "STANDARD")

# Test cases (run with python sort_package.py to execute)
if __name__ == "__main__":
    # Test STANDARD: neither bulky nor heavy
    assert sort(10, 10, 10, 5) == "STANDARD", "Test 1 failed"
    # Test SPECIAL: bulky (large dimension)
    assert sort(150, 10, 10, 10) == "SPECIAL", "Test 2 failed"
    # Test SPECIAL: bulky (large volume)
    assert sort(100, 100, 100, 10) == "SPECIAL", "Test 3 failed"
    # Test SPECIAL: heavy
    assert sort(20, 20, 20, 20) == "SPECIAL", "Test 4 failed"
    # Test REJECTED: bulky and heavy
    assert sort(150, 10, 10, 20) == "REJECTED", "Test 5 failed"
    # Test REJECTED: bulky (large volume) and heavy
    assert sort(100, 100, 100, 20) == "REJECTED", "Test 6 failed"
    # Test REJECTED: negative dimension
    assert sort(-10, 10, 10, 5) == "REJECTED", "Test 7 failed"
    # Test REJECTED: zero mass
    assert sort(10, 10, 10, 0) == "REJECTED", "Test 8 failed"
    # Test REJECTED: non-numeric input
    assert sort("10", 10, "invalid", 5) == "REJECTED", "Test 9 failed"
    print("All tests passed!")
