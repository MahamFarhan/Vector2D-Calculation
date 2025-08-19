from vector2d import Vector2D
def main():
    x1 = float(input("Enter x for first vector: "))
    y1 = float(input("Enter y for first vector: "))
    vector1 = Vector2D(x1, y1)

    # Take input for second vector
    x2 = float(input("Enter x for second vector: "))
    y2 = float(input("Enter y for second vector: "))
    vector2 = Vector2D(x2, y2)

    print("\n--- Results ---")
    print("v1 =", vector1)
    print("v2 =", vector2)

    print("\nAddition and Subtraction:")
    print("v1 + v2 =", vector1 + vector2)
    print("v1 - v2 =", vector1 - vector2)

    print("\nDot Product and Magnitude:")
    print("Dot product =", vector1.dot(vector2))
    print("Magnitude of v1 =", vector1.magnitude())
    print("Magnitude of v2 =", vector2.magnitude())

    # Scalar multiplication
    scalar = float(input("\nEnter a scalar to multiply with vector1: "))
    print("\nScalar multiplication:")
    print("vector1 * scalar =", vector1 * scalar)
    
    print("\nString Representations:")
    print("str(vector1) =", str(vector1))
    print("repr(vector1) =", repr(vector1))


if __name__ == "__main__":
    main()