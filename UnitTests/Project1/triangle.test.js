const { triangleType, TriangleType } = require('./Triangle');

describe('Triangle Classification', () => {

    // 1. Accepts scalene triangle in all side orders
    test('returns SCALENE for all permutations of 3, 4, 5', () => {
        expect(triangleType(3, 4, 5)).toBe(TriangleType.SCALENE)
        expect(triangleType(4, 5, 3)).toBe(TriangleType.SCALENE)
        expect(triangleType(5, 3, 4)).toBe(TriangleType.SCALENE)
    });

    // 2. 
    test('returns ISOSCELES', () => {
        expect(triangleType(3, 3, 5)).toBe(TriangleType.ISOSCELES)
    })

    // 3.
    test('returns EQUILATERAL', () => {
        expect(triangleType(3, 3, 3)).toBe(TriangleType.EQUILATERAL)
    })

    // 4. Zero-length side is invalid
    test('throws RangeError for zero-length side', () => {
        expect(() => triangleType(0, 5, 5)).toThrow(RangeError)
    })

    // 5. Triangle inequality violation
    test('throws RangeError for zero-length side', () => {
        expect(() => triangleType(3, 3, 7)).toThrow(RangeError)
    })
});