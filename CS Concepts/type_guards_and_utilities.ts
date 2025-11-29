/**
 * Type Guards and Utility Types
 * 
 * Type guards help narrow types at runtime, and utility types
 * provide powerful type transformations.
 */

// Type Guards
interface Fish {
    swim(): void;
}

interface Bird {
    fly(): void;
}

// Type predicate (type guard)
function isFish(animal: Fish | Bird): animal is Fish {
    return (animal as Fish).swim !== undefined;
}

function move(animal: Fish | Bird): void {
    if (isFish(animal)) {
        animal.swim();  // TypeScript knows this is Fish
    } else {
        animal.fly();   // TypeScript knows this is Bird
    }
}

// typeof type guard
function padLeft(value: string | number): string {
    if (typeof value === "number") {
        return value.toString().padStart(10);
    }
    return value.padStart(10);
}

// instanceof type guard
class Dog {
    bark(): void {
        console.log("Woof!");
    }
}

class Cat {
    meow(): void {
        console.log("Meow!");
    }
}

function makeSound(animal: Dog | Cat): void {
    if (animal instanceof Dog) {
        animal.bark();
    } else {
        animal.meow();
    }
}

// in operator type guard
interface Car {
    drive(): void;
}

interface Boat {
    sail(): void;
}

function operate(vehicle: Car | Boat): void {
    if ("drive" in vehicle) {
        vehicle.drive();
    } else {
        vehicle.sail();
    }
}

// Utility Types Examples
interface User {
    id: number;
    name: string;
    email: string;
    age: number;
}

// Partial - makes all properties optional
type PartialUser = Partial<User>;
// { id?: number; name?: string; email?: string; age?: number; }

// Required - makes all properties required
type RequiredUser = Required<PartialUser>;

// Pick - select specific properties
type UserPreview = Pick<User, "id" | "name">;
// { id: number; name: string; }

// Omit - exclude specific properties
type UserWithoutEmail = Omit<User, "email">;
// { id: number; name: string; age: number; }

// Readonly - makes all properties readonly
type ReadonlyUser = Readonly<User>;

// Record - create object type with specific keys and values
type UserRoles = Record<string, "admin" | "user" | "guest">;
// { [key: string]: "admin" | "user" | "guest" }

// Exclude - exclude types from union
type NonNullable<T> = Exclude<T, null | undefined>;

// Extract - extract types from union
type StringOrNumber = string | number;
type OnlyString = Extract<StringOrNumber, string>;  // string

// NonNullable - exclude null and undefined
type UserId = number | null | undefined;
type ValidUserId = NonNullable<UserId>;  // number

// ReturnType - get return type of function
function getUser(): User {
    return { id: 1, name: "John", email: "john@example.com", age: 30 };
}
type UserReturnType = ReturnType<typeof getUser>;  // User

// Parameters - get parameters type of function
function createUser(id: number, name: string): User {
    return { id, name, email: "", age: 0 };
}
type CreateUserParams = Parameters<typeof createUser>;  // [number, string]

// InstanceType - get instance type of constructor
class UserService {
    constructor(public name: string) {}
}
type UserServiceInstance = InstanceType<typeof UserService>;  // UserService

// Custom Utility Types
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

type Nullable<T> = T | null;
type Optional<T> = T | undefined;

export {
    isFish,
    move,
    padLeft,
    makeSound,
    operate,
    PartialUser,
    RequiredUser,
    UserPreview,
    UserWithoutEmail,
    ReadonlyUser,
    UserRoles,
    NonNullable,
    OnlyString,
    ValidUserId,
    UserReturnType,
    CreateUserParams,
    UserServiceInstance,
    DeepPartial,
    DeepReadonly,
    Nullable,
    Optional
};

