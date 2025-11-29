/**
 * Functional Programming Concepts
 * 
 * Functional programming emphasizes immutability, pure functions,
 * and higher-order functions. These concepts lead to more predictable
 * and maintainable code.
 * 
 * Key Concepts:
 * - Pure functions
 * - Immutability
 * - Higher-order functions
 * - Map, Filter, Reduce
 * - Function composition
 * - Currying
 */

// Pure Functions (no side effects, same input = same output)
function add(a: number, b: number): number {
    return a + b;  // Pure: no side effects
}

// Impure function (has side effect)
let counter = 0;
function impureIncrement(): number {
    counter++;  // Side effect: modifies external state
    return counter;
}

// Immutability - Don't mutate, create new objects
interface User {
    name: string;
    age: number;
}

// Bad: Mutating
function updateAgeBad(user: User, newAge: number): void {
    user.age = newAge;  // Mutates original
}

// Good: Immutable
function updateAgeGood(user: User, newAge: number): User {
    return { ...user, age: newAge };  // Returns new object
}

// Map - Transform each element
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);  // [2, 4, 6, 8, 10]
const strings = numbers.map(n => n.toString());  // ["1", "2", "3", "4", "5"]

// Filter - Select elements that match condition
const evens = numbers.filter(n => n % 2 === 0);  // [2, 4]
const odds = numbers.filter(n => n % 2 !== 0);   // [1, 3, 5]

// Reduce - Accumulate values
const sum = numbers.reduce((acc, n) => acc + n, 0);  // 15
const product = numbers.reduce((acc, n) => acc * n, 1);  // 120
const max = numbers.reduce((acc, n) => n > acc ? n : acc, numbers[0]);  // 5

// Chaining
const result = numbers
    .filter(n => n % 2 === 0)  // [2, 4]
    .map(n => n * 2)           // [4, 8]
    .reduce((acc, n) => acc + n, 0);  // 12

// Higher-Order Functions (functions that take/return functions)
function multiplyBy(factor: number): (n: number) => number {
    return (n: number) => n * factor;
}

const double = multiplyBy(2);
const triple = multiplyBy(3);

// Function Composition
type Func<T, R> = (arg: T) => R;

function compose<T, U, V>(f: Func<U, V>, g: Func<T, U>): Func<T, V> {
    return (x: T) => f(g(x));
}

const addOne = (x: number) => x + 1;
const multiplyByTwo = (x: number) => x * 2;
const addOneThenDouble = compose(multiplyByTwo, addOne);
// addOneThenDouble(5) = multiplyByTwo(addOne(5)) = multiplyByTwo(6) = 12

// Currying (transforming multi-argument function into single-argument functions)
function addCurried(a: number): (b: number) => number {
    return (b: number) => a + b;
}

const add5 = addCurried(5);
const result1 = add5(3);  // 8

// More practical currying example
function createLogger(prefix: string): (message: string) => void {
    return (message: string) => {
        console.log(`[${prefix}] ${message}`);
    };
}

const errorLogger = createLogger("ERROR");
const infoLogger = createLogger("INFO");

// Partial Application
function multiply(a: number, b: number, c: number): number {
    return a * b * c;
}

function partialMultiply(a: number): (b: number) => (c: number) => number {
    return (b: number) => (c: number) => multiply(a, b, c);
}

const multiplyBy2And3 = partialMultiply(2)(3);
const result2 = multiplyBy2And3(4);  // 24

// Memoization (caching function results)
function memoize<T extends (...args: any[]) => any>(fn: T): T {
    const cache = new Map<string, ReturnType<T>>();
    
    return ((...args: Parameters<T>) => {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        return result;
    }) as T;
}

const expensiveFunction = (n: number): number => {
    // Simulate expensive computation
    return n * n;
};

const memoizedExpensive = memoize(expensiveFunction);

export {
    add,
    updateAgeGood,
    multiplyBy,
    compose,
    addCurried,
    createLogger,
    partialMultiply,
    memoize
};

