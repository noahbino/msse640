const TriangleType = {
    SCALENE: "scalene",
    ISOSCELES: "isosceles",
    EQUILATERAL: "equilateral"
};

function triangleType(a, b, c) {
    if (a <= 0 || b <= 0 || c <= 0) {
        throw new RangeError("Side lengths must be greater than zero")
    }

    // Triangle Inequality Rule
    if (a + b <= c || a + c <= b || b + c <= a) {
        throw new RangeError("Invalid triangle")
    }

    if (a === b && b === c) {
        return TriangleType.EQUILATERAL
    } else if (a === b || b === c || a === c) {
        return TriangleType.ISOSCELES
    } else {
        return TriangleType.SCALENE
    }
}

module.exports = { triangleType, TriangleType }