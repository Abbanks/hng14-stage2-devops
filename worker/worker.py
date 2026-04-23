import redis
import time
import os
import signal

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")

def handle_sigterm(*args):
    print("Received SIGTERM, shutting down...")
    sys.exit(0)
    
signal.signal(signal.SIGTERM, handle_sigterm)

if __name__ == "__main__":
    print(f"Worker connected to Redis at {REDIS_HOST}")
    while True:
        job = r.brpop("job", timeout=5)
        if job:
            _, job_id = job
            process_job(job_id.decode('utf-8'))