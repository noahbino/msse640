const { triangleType, TriangleType } = require('./Triangle');

describe('Triangle Classification', () => {

    // 1. Valid Scalene Triangle
    test('returns SCALENE for 3, 4, 5', () => {
        expect(triangleType(3, 4, 5)).toBe(TriangleType.SCALENE);
    });

    // 2. Accepts scalene triangle in all side orders
    test('returns SCALENE for all permutations of 3, 4, 5', () => {
        expect(triangleType(3, 4, 5)).toBe(TriangleType.SCALENE);
        expect(triangleType(4, 5, 3)).toBe(TriangleType.SCALENE);
        expect(triangleType(5, 3, 4)).toBe(TriangleType.SCALENE);
    });

    // 3. Zero-length side is invalid
    test('throws RangeError for zero-length side', () => {
        expect(() => triangleType(0, 5, 5)).toThrow(RangeError);
    });

});