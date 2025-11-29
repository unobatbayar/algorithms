/**
 * Async/Await and Promises
 * 
 * Asynchronous programming is crucial for handling I/O operations,
 * API calls, and non-blocking code execution.
 * 
 * Key Concepts:
 * - Promises (resolve, reject, then, catch)
 * - Async/await syntax
 * - Promise chaining
 * - Error handling
 * - Promise.all, Promise.race, Promise.allSettled
 */

// Basic Promise
function fetchUser(id: number): Promise<{ id: number; name: string }> {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id > 0) {
                resolve({ id, name: `User ${id}` });
            } else {
                reject(new Error("Invalid user ID"));
            }
        }, 1000);
    });
}

// Promise Chaining
fetchUser(1)
    .then(user => {
        console.log("User:", user);
        return fetchUser(user.id + 1);
    })
    .then(nextUser => {
        console.log("Next user:", nextUser);
    })
    .catch(error => {
        console.error("Error:", error.message);
    });

// Async/Await
async function getUserData(id: number) {
    try {
        const user = await fetchUser(id);
        console.log("User data:", user);
        return user;
    } catch (error) {
        console.error("Failed to fetch user:", error);
        throw error;
    }
}

// Multiple Async Operations
async function fetchMultipleUsers(ids: number[]) {
    // Sequential (one after another)
    const users1: any[] = [];
    for (const id of ids) {
        const user = await fetchUser(id);
        users1.push(user);
    }

    // Parallel (all at once)
    const users2 = await Promise.all(
        ids.map(id => fetchUser(id))
    );

    return users2;
}

// Promise.all - Wait for all, fail if any fails
async function fetchAllData() {
    const [users, posts, comments] = await Promise.all([
        fetchUser(1),
        fetchUser(2),
        fetchUser(3)
    ]);
    return { users, posts, comments };
}

// Promise.allSettled - Wait for all, get results even if some fail
async function fetchAllSettled() {
    const results = await Promise.allSettled([
        fetchUser(1),
        fetchUser(-1),  // This will fail
        fetchUser(3)
    ]);
    
    results.forEach((result, index) => {
        if (result.status === "fulfilled") {
            console.log(`Promise ${index} succeeded:`, result.value);
        } else {
            console.log(`Promise ${index} failed:`, result.reason);
        }
    });
}

// Promise.race - Return first resolved/rejected
async function fetchWithTimeout(url: string, timeout: number) {
    const fetchPromise = fetch(url);
    const timeoutPromise = new Promise((_, reject) =>
        setTimeout(() => reject(new Error("Timeout")), timeout)
    );

    return Promise.race([fetchPromise, timeoutPromise]);
}

// Error Handling Patterns
async function robustFetch(id: number) {
    try {
        return await fetchUser(id);
    } catch (error) {
        // Log error
        console.error("Fetch error:", error);
        // Return default or rethrow
        return { id: 0, name: "Unknown" };
    }
}

// Async Generator
async function* asyncGenerator() {
    for (let i = 1; i <= 3; i++) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        yield await fetchUser(i);
    }
}

// Using async generator
async function processAsyncGenerator() {
    for await (const user of asyncGenerator()) {
        console.log("Generated user:", user);
    }
}

export {
    fetchUser,
    getUserData,
    fetchMultipleUsers,
    fetchAllData,
    fetchAllSettled,
    fetchWithTimeout,
    robustFetch,
    asyncGenerator
};

