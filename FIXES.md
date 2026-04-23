## Bugs found, file, line number, what it was, and how it was fixed it

1. backend/main.py, Line 8: The Redis host was hardcoded to "localhost", which would not work in a Docker environment where services communicate via service names. This was fixed by replacing it with `os.getenv("REDIS_HOST", "redis")`, allowing the application to use the environment variable `REDIS_HOST` or default to "redis" if not set.

2. backend/main.py, Line 20: The `redis.hget` method returns bytes, and there was no handling for a case where the status could be `None` (e.g., job ID not found). This was fixed by adding `.decode('utf-8')` to convert the bytes to a string and implementing an HTTPException(404) if the status is `None`.

3. worker/worker.py, Line 6: The Redis connection parameters were hardcoded, which is not ideal for different environments. This was fixed by configuring the worker to use environment variables `REDIS_HOST` and `REDIS_PORT` for flexibility.

4. worker/worker.py, Line 18: The return value of `r.brpop` was not handled correctly for decoding, which could lead to issues when processing job IDs. This was fixed by decoding the job ID correctly before passing it to the `process_job` function.

5. worker/worker.py, N/A: There was no handling for graceful shutdown, which could lead to abrupt termination of the worker and loss of in-progress jobs. This was fixed by adding signal handlers for SIGTERM and SIGINT to allow the worker to finish processing current jobs before exiting.

6. frontend/app.js, Line 6: The API URL was hardcoded to "localhost", which would not work in a Docker environment. This was fixed by replacing it with `process.env.API_URL`, allowing the frontend to use the environment variable `API_URL` for internal container-to-container communication.

7. frontend/app.js, Lines 13 and 22: There was no logging for failed API calls, which made it difficult to debug issues related to Docker networking. This was fixed by adding `console.error(err.message)` to log the error messages when API calls fail.

