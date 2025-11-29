/**
 * TypeScript Types and Generics
 * 
 * Types provide flexibility beyond interfaces and enable powerful
 * type system features like unions, intersections, and generics.
 * 
 * Key Concepts:
 * - Type aliases
 * - Union types (A | B)
 * - Intersection types (A & B)
 * - Generics (reusable type parameters)
 * - Type constraints
 * - Conditional types
 */

// Type Aliases
type ID = string | number;
type Status = "pending" | "approved" | "rejected";

// Union Types
type StringOrNumber = string | number;
type Result<T> = Success<T> | Error;

interface Success<T> {
    type: "success";
    data: T;
}

interface Error {
    type: "error";
    message: string;
}

// Intersection Types
type Person = {
    name: string;
    age: number;
};

type Employee = {
    employeeId: string;
    department: string;
};

type EmployeePerson = Person & Employee;  // Has both Person and Employee properties

// Generics - Basic
function identity<T>(arg: T): T {
    return arg;
}

// Generics - Multiple Type Parameters
function pair<T, U>(first: T, second: U): [T, U] {
    return [first, second];
}

// Generics - Constraints
interface Lengthwise {
    length: number;
}

function logLength<T extends Lengthwise>(arg: T): T {
    console.log(arg.length);
    return arg;
}

// Generic Classes
class Box<T> {
    private value: T;

    constructor(value: T) {
        this.value = value;
    }

    getValue(): T {
        return this.value;
    }

    setValue(value: T): void {
        this.value = value;
    }
}

// Generic Interfaces
interface Repository<T> {
    findById(id: string): T | null;
    save(entity: T): void;
    delete(id: string): boolean;
}

// Conditional Types
type NonNullable<T> = T extends null | undefined ? never : T;
type ArrayElementType<T> = T extends (infer U)[] ? U : never;

// Utility Types (built-in examples)
type Partial<T> = {
    [P in keyof T]?: T[P];
};

type Required<T> = {
    [P in keyof T]-?: T[P];
};

type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};

type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;

// Example Usage
const id1: ID = "user-123";
const id2: ID = 456;
const status: Status = "pending";

const result1: Result<string> = { type: "success", data: "Hello" };
const result2: Result<number> = { type: "error", message: "Not found" };

const employee: EmployeePerson = {
    name: "Alice",
    age: 30,
    employeeId: "E001",
    department: "Engineering"
};

const num = identity(42);
const str = identity("hello");
const pair1 = pair(1, "two");

const stringBox = new Box("Hello");
const numberBox = new Box(42);

export { 
    ID, Status, StringOrNumber, Result, Success, Error,
    Person, Employee, EmployeePerson,
    identity, pair, logLength,
    Box, Repository,
    NonNullable, ArrayElementType
};

